#!/usr/bin/env python3
"""
RACI Matrix Generator
Generates a RACI matrix from a project kickoff transcript using Claude AI.

Usage:
    python app.py <transcript_file> [-o output_file] [-s system_prompt_file] [-m model]

Examples:
    python app.py transcript.txt
    python app.py transcript.txt -o raci_output.txt
    python app.py transcript.txt -s custom_prompt.txt -o raci_output.txt
"""

import argparse
import json
import sys
import anthropic

DEFAULT_SYSTEM_PROMPT = """You are an expert project manager specializing in RACI matrix creation.
Your job is to analyze project meeting transcripts and extract a precise, structured RACI matrix.

RACI Definitions:
- R (Responsible): The person who performs the work to complete the task.
- A (Accountable): The ONE person ultimately answerable for the task's outcome. There must be exactly ONE Accountable per task — never two.
- C (Consulted): People whose expertise or input is sought before decisions or actions are taken (two-way communication).
- I (Informed): People kept informed of progress or decisions after the fact (one-way communication).

Rules:
1. Each task must have exactly ONE (A) Accountable. If the transcript assigns two people as Accountable, choose the more senior stakeholder or the one with final decision authority.
2. A person can be both Responsible and another role is unusual — only assign R if they do the hands-on work.
3. Every stakeholder must have an assignment for every task — no blanks allowed. If a stakeholder's role for a task was not explicitly stated or agreed upon in the transcript, you MUST assign "TBD". Do NOT infer, guess, or assume roles — only use R, A, C, or I when the transcript clearly states it.
4. Extract the project name from the transcript.

Return ONLY a valid JSON object — no markdown, no explanation — with this exact structure:
{
  "project": "Project name from transcript",
  "stakeholders": ["Name1 (Role)", "Name2 (Role)", ...],
  "tasks": [
    {
      "task": "Task name",
      "assignments": {
        "Name1 (Role)": "R",
        "Name2 (Role)": "A",
        "Name3 (Role)": "C",
        "Name4 (Role)": "I"
      }
    }
  ]
}

Use "Name (Role)" format for stakeholders exactly as they appear in the transcript (e.g., "Sandra (Project Manager)").
"""


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a RACI matrix from a project kickoff transcript using Claude AI"
    )
    parser.add_argument(
        "transcript",
        help="Path to the transcript text file"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: print to terminal)"
    )
    parser.add_argument(
        "-s", "--system-prompt",
        help="Path to a custom system prompt file (overrides the built-in prompt)"
    )
    parser.add_argument(
        "-m", "--model",
        default="claude-opus-4-6",
        help="Claude model to use (default: claude-opus-4-6)"
    )
    return parser.parse_args()


def load_file(path, label="file"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {label} '{path}' not found.", file=sys.stderr)
        sys.exit(1)


def extract_raci_json(transcript, system_prompt, model):
    """Call the Claude API and return the parsed RACI JSON data."""
    client = anthropic.Anthropic()

    print(f"Calling {model}...", file=sys.stderr)

    with client.messages.stream(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": (
                    "Please analyze the following project meeting transcript "
                    "and generate a RACI matrix as a JSON object:\n\n"
                    f"{transcript}"
                )
            }
        ]
    ) as stream:
        response = stream.get_final_message()

    raw = next((b.text for b in response.content if b.type == "text"), "")

    # Strip markdown code fences if present
    if "```json" in raw:
        start = raw.find("```json") + 7
        end = raw.find("```", start)
        raw = raw[start:end].strip()
    elif "```" in raw:
        start = raw.find("```") + 3
        end = raw.find("```", start)
        raw = raw[start:end].strip()

    try:
        return json.loads(raw.strip())
    except json.JSONDecodeError as e:
        print(f"Error: Could not parse API response as JSON.\nDetails: {e}", file=sys.stderr)
        print(f"Raw response:\n{raw}", file=sys.stderr)
        sys.exit(1)


def format_raci_table(raci_data):
    """Render the RACI data as a formatted plain-text table."""
    project = raci_data.get("project", "Unknown Project")
    stakeholders = raci_data.get("stakeholders", [])
    tasks = raci_data.get("tasks", [])

    if not stakeholders or not tasks:
        return "No RACI data found in response."

    # Column widths
    task_col_w = max(len("Task"), max(len(t["task"]) for t in tasks))
    stake_col_w = max(max(len(s) for s in stakeholders), 3)

    total_width = task_col_w + 3 + (stake_col_w + 3) * len(stakeholders)

    lines = []
    lines.append("")
    lines.append(f"  RACI MATRIX: {project}")
    lines.append("  " + "=" * (total_width - 2))
    lines.append("")

    # Header row
    header = f"  {'Task':<{task_col_w}} | " + " | ".join(
        f"{s:^{stake_col_w}}" for s in stakeholders
    )
    separator = "  " + "-" * (len(header) - 2)
    lines.append(header)
    lines.append(separator)

    # Task rows
    for task_item in tasks:
        task_name = task_item["task"]
        assignments = task_item.get("assignments", {})
        row = f"  {task_name:<{task_col_w}} | " + " | ".join(
            f"{assignments.get(s, 'TBD'):^{stake_col_w}}" for s in stakeholders
        )
        lines.append(row)

    lines.append(separator)
    lines.append("")
    lines.append("  Legend:  R = Responsible  |  A = Accountable  |  C = Consulted  |  I = Informed")
    lines.append("  Note: Each task should have exactly one Accountable (A).")
    lines.append("")

    return "\n".join(lines)


def main():
    args = parse_args()

    transcript = load_file(args.transcript, label="transcript file")

    system_prompt = (
        load_file(args.system_prompt, label="system prompt file")
        if args.system_prompt
        else DEFAULT_SYSTEM_PROMPT
    )

    print("Analyzing transcript...", file=sys.stderr)

    raci_data = extract_raci_json(transcript, system_prompt, args.model)
    output = format_raci_table(raci_data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"RACI matrix saved to '{args.output}'", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()

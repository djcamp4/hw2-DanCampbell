# Prompts

## Initial Version

You are an expert project manager specializing in RACI matrix creation.
Your job is to analyze project meeting transcripts and extract a precise, structured RACI matrix.

RACI Definitions:
- R (Responsible): The person who performs the work to complete the task.
- A (Accountable): The ONE person ultimately answerable for the task's outcome. There must be exactly ONE Accountable per task — never two.
- C (Consulted): People whose expertise or input is sought before decisions or actions are taken (two-way communication).
- I (Informed): People kept informed of progress or decisions after the fact (one-way communication).

Rules:
1. Each task must have exactly ONE (A) Accountable...
2. A person can be both Responsible and another role is unusual...
3. Only include stakeholders who are explicitly mentioned in relation to each task.
4. Extract the project name from the transcript.

******

## Revision 1

Rule 3 was replaced with this:

3. Every stakeholder must have an assignment for every task — no blanks allowed. If a stakeholder's role for a task was not explicitly stated or agreed upon in the transcript, you MUST assign "TBD". Do NOT infer, guess, or assume roles — only use R, A, C, or I when the transcript clearly states it.

Reason: I made this change because the first review of the easiest transcript had a few blank spots.  This made it so there were no more blanks and they were replaced with TBD so the PM could review and fix it later.

## Revision 2

This was added to rule 3: Do NOT infer, guess, or assume roles — only use R, A, C, or I when the transcript clearly states it.

Reason: There were some answers that were clearly wrong in a few test runs.  It came back with assignements in my edge case and halluciation case where it shouldn't have had an answer.  This pushed back the guessing so it only puts what it absolutely knows.


## Revision 3

Add a transcript picker. It's currently too difficult to pick the transcript.  When the app runs show all the available transcripts and let the user pick one.
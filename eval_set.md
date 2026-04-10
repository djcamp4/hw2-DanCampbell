# Evaluation Set

Transcript 1: Normal Case

What it should do:  Create a RASCI Matrix from the provided transcript that shows stakeholders, tasks, and assignments.

Project: Employee Self-Service HR Portal
Attendees: Sandra (Project Manager), Dev (Lead Developer), Priya (HR Director), Tom (IT Security), Lisa (CFO)

Sandra: Alright everyone, thanks for joining. Today we're kicking off the HR Self-Service Portal project. The goal is to let employees manage their own PTO, payroll info, and benefits online. Let's walk through the five main tasks and figure out who owns what.
Sandra: First task — requirements gathering. Dev, I'd say you and Priya should be closely involved here.
Priya: Agreed. HR knows what employees need. I'd say I'm responsible for gathering the business requirements, and Dev should be consulted so he understands the technical constraints early.
Dev: Works for me. And Sandra, I'd assume you're accountable overall?
Sandra: Yes, I'll be accountable for this one. Tom, Lisa — we'll keep you informed as requirements come in.
Tom: Fine by me, though flag me early if anything touches employee data. I'll want to weigh in.
Sandra: Good point. Tom, we'll move you to Consulted on requirements then. Lisa, Informed still okay?
Lisa: Perfectly fine.

Sandra: Task two — UI/UX design.
Dev: That's my team's domain. We're Responsible. Priya, we'll need your input on the user flows — employees are your people, you know how they think.
Priya: Happy to be Consulted. Just don't make it complicated — our staff aren't all tech savvy.
Sandra: I'll stay Accountable. Tom and Lisa, Informed?
Tom: Yes, no concerns there.
Lisa: Informed works.

Sandra: Task three — security and compliance review. Tom, this one's yours.
Tom: Absolutely, I'm Responsible. This portal will touch payroll and personal data, so GDPR and SOC2 compliance need to be airtight. Priya, I'll need HR policy documents from you.
Priya: Consider yourself Consulted then, and I'll make sure you get everything you need.
Tom: And I'd say Sandra is Accountable, Dev should be Consulted since he'll need to implement whatever I flag.
Dev: Agreed.
Lisa: I'll want to be Consulted on this one actually — anything touching compliance has financial and legal implications.
Sandra: Good call. Lisa moves to Consulted. I'll stay Accountable.

Sandra: Task four — development and build.
Dev: That's squarely on my team. We're Responsible. Sandra, you're Accountable?
Sandra: Yes. Priya, we'll keep you Informed on progress. Tom, Consulted in case security issues come up mid-build?
Tom: Yes, please loop me in if anything looks off.
Lisa: Informed is fine for me here.

Sandra: Last one — user acceptance testing, or UAT.
Priya: HR should run this. Our staff will be the end users, so we're best placed to test it. I'll be Responsible.
Dev: And I need to be Consulted — any bugs found need to come straight to me.
Sandra: I'll be Accountable. Tom, Consulted in case security issues surface during testing?
Tom: Yes.
Lisa: Informed.
*****

Transcript 2: Normal Case

What it should do:  Create a RASCI Matrix from the provided transcript that shows stakeholders, tasks, and assignments.

Project: Cloud Migration of On-Premise Servers
Attendees: Marcus (Project Manager), Jen (Infrastructure Lead), Carlos (CTO), Aisha (Finance Manager), Ray (IT Security)

Marcus: Welcome everyone. We're migrating our on-premise servers to AWS. This is a big one — downtime risk is real, so let's be very clear about ownership. Five tasks to cover.

Marcus: Task one — infrastructure assessment. Jen, I'd assume this is your team?
Jen: Yes, we're Responsible. We'll audit everything currently on-prem — servers, storage, dependencies. Carlos, I'd want you Consulted. Some of these architectural decisions will need your sign-off directionally.
Carlos: Agreed. And I'll be Accountable on this task — infrastructure strategy is ultimately my call.
Marcus: I'll stay Informed then, and Aisha — Informed for you too at this stage?
Aisha: Yes, though flag me if the assessment uncovers cost surprises.
Ray: I'd like to be Consulted — I need to know what data lives where before we move anything.

Marcus: Task two — cloud architecture design.
Carlos: This is a joint effort. Jen is Responsible for the design work, I'll be Accountable.
Jen: I'd want Ray Consulted early — security architecture needs to be baked in, not bolted on.
Ray: Strongly agree.
Aisha: I'll need to be Consulted here too. Cloud architecture choices have direct cost implications — reserved instances, storage tiers, that kind of thing.
Marcus: Informed for me on this one then.

Marcus: Task three — data migration.
Jen: My team again — Responsible. This is the riskiest task. We're talking about moving live data.
Ray: I need to be Consulted throughout. Encryption in transit, access controls, audit logs — all of that needs oversight.
Carlos: I'm Accountable. Marcus, Informed?
Marcus: Yes. Aisha?
Aisha: Informed is fine.

Marcus: Task four — testing and validation post-migration.
Jen: Responsible again. We'll run performance tests, failover tests, and make sure everything behaves as expected.
Marcus: I'll be Accountable here — this is a project delivery milestone.
Carlos: Consulted — I want visibility on test results before we declare success.
Ray: Consulted — security validation is part of this.
Aisha: Informed.

Marcus: Final task — cutover and go-live.
Jen: Responsible for executing the cutover.
Carlos: I'm Accountable — I'll be the one authorizing the final switch.
Ray: Consulted — I need to be on call during cutover in case security issues arise.
Aisha: Informed. Though please tell me when it's done — I'll need to start tracking cloud spend from day one.
Marcus: I'll be Consulted — I want to be in the room when this happens.

******

Transcript 3: Normal Case

What it should do:  Create a RASCI Matrix from the provided transcript that shows stakeholders, tasks, and assignments.

Project: Company-Wide Multi-Factor Authentication Rollout
Attendees: Natalie (IT Project Manager), Greg (IT Security Lead), Diana (HR Manager), Felix (Help Desk Manager), Olivier (COO)

Natalie: Good morning. Today we kick off our MFA rollout. Every employee will need to use multi-factor authentication to access company systems. Security-driven project, but it touches everyone. Five tasks.

Natalie: Task one — vendor selection for the MFA platform.
Greg: Security is driving this. I'm Responsible for evaluating vendors — we're looking at Okta, Duo, and Microsoft Authenticator. Olivier, you'll be Accountable since this is a company-wide commitment.
Olivier: Agreed. Natalie, where do you sit?
Natalie: Consulted — I want to make sure whatever we pick can be rolled out practically. Felix, your help desk will be supporting users, so Consulted for you too.
Felix: Yes please — some of these platforms create a nightmare for support tickets if they're not user-friendly.
Diana: Informed for me.

Natalie: Task two — policy and compliance documentation.
Greg: I'll write the security policy. Responsible.
Diana: HR needs to be Consulted — this policy affects all employees and needs to align with our acceptable use policy.
Olivier: I'm Accountable. This is a governance document.
Natalie: Consulted for me, Informed for Felix?
Felix: Yes that's fine.

Natalie: Task three — technical implementation.
Greg: My team is Responsible. We'll configure the MFA platform, integrate it with Active Directory, and set up the enrollment flows.
Natalie: I'm Accountable here from a project delivery standpoint.
Felix: I need to be Consulted — I need to understand the enrollment flow so my team can support users.
Olivier: Informed.
Diana: Informed.

Natalie: Task four — employee communications and training.
Diana: This is HR's responsibility. We'll draft the communications and run training sessions. Responsible.
Natalie: Accountable — it's a project milestone.
Greg: Consulted — the technical accuracy of training materials needs my review.
Felix: Consulted — help desk needs to preview training so we know what questions are coming.
Olivier: Informed.

Natalie: Last task — rollout and support.
Felix: Help desk is Responsible. We'll manage the enrollment period, handle lockouts, and support users.
Natalie: I'm Accountable.
Greg: Consulted — anything that looks like a security incident comes to me immediately.
Diana: Informed — I'll want numbers on adoption rate by department.
Olivier: Informed.

****
Transcript 4: Edge Case

What it should do:  Create a RASCI Matrix from the provided transcript.  However, this transcript has 2 people assigned to a task and this is not allowed by the rules, but it is often the case in ambiguous kickoff meetings.  Hopefully it assigns both, or neither, so that it can be reviewed later.

Project: Business Intelligence Dashboard Implementation
Attendees: Paula (Project Manager), Ravi (Data Engineer), Simone (Head of Sales), Derek (CFO), Yuki (IT Manager)

Paula: Thanks for coming. We're building a company-wide BI dashboard so leadership can see sales, finance, and ops data in one place. Five tasks. Let's figure out ownership.

Paula: Task one — data source mapping.
Ravi: I'll be Responsible. I need to catalogue every data source we're pulling from — Salesforce, the ERP, the data warehouse.
Simone: Consulted for sales data — I know where the skeletons are in our Salesforce setup.
Derek: Consulted for finance data — same reason.
Paula: I'll be Accountable. Yuki, Informed?
Yuki: Yes, though flag me if any data sources require new infrastructure.

Paula: Task two — dashboard design and requirements.
Simone: Sales should drive this. We're the primary users. Responsible.
Derek: Finance co-owns this — Responsible alongside Simone?
Paula: Let's keep one Responsible per task. Simone, you lead it, Derek you're Consulted.
Derek: Fair.
Ravi: I need to be Consulted — I can tell you what's actually feasible from the data we have.
Paula: I'll be Accountable. Yuki, Informed.

Paula: Task three — data pipeline development.
Ravi: Fully my team. Responsible. This is the ETL work — extract, transform, load.
Yuki: I need to be Consulted — pipelines run on infrastructure I manage.
Paula: Accountable. Simone and Derek, Informed during this phase.
Simone: Fine, as long as we see progress demos.
Paula: We'll schedule those.

Paula: Task four — dashboard build and visualization.
Ravi: Still my team — Responsible. We'll be building in Tableau.
Simone: Consulted — I want to review visualizations as they're built, not at the end.
Derek: Same — Consulted.
Paula: And I'll be Accountable on this one as well. Yuki, Informed.
Derek: Actually Paula, I'd like to be Accountable for this task. The dashboard is ultimately a financial reporting tool. If the numbers look wrong to our board, that falls on Finance — not IT project management.
Paula: I appreciate that Derek, but from a delivery standpoint, Accountable should sit with the project manager. That's how we've structured every other task here.
Derek: I understand the logic, but this one's different. The outputs of this task are going directly to the executive team. I need to be the one signing off on it, not just being Consulted.
Simone: I'd actually agree with Derek on this one. The dashboard is a business tool, not an IT deliverable. Having Finance be Accountable makes it clear the business owns the outcome.
Paula: I hear you both, but if Derek is Accountable and something goes wrong with the build timeline or a technical decision, who does Ravi escalate to?
Derek: Me. I'm fine with that.
Paula: (pausing) Okay — I don't think we're going to resolve this right now and I don't want it to derail the rest of the meeting. Let's leave a flag on task four and keep moving. Derek, can we find 20 minutes after this to work it out?
Derek: Sure.
Paula: Good. Moving on.

Paula: Task five — UAT and stakeholder sign-off.
Simone: Sales will test this rigorously. Responsible.
Derek: Finance too — joint Responsible since we're the two primary stakeholder groups?
Paula: In this case yes. I'll be Accountable. Ravi, Consulted for bug fixing. Yuki, Informed.
Ravi: Works for me.

****

Transcript 5: Set to Fail/hallucinate

What it should do:  There are no clear assignments in this conversation.  They're discussed but not clear.  I assume it will have ot make up the data to complete the requirements for the matrix.

Project: Mobile Device Management (MDM) Implementation
Attendees: Henry (IT Project Manager), Cara (IT Systems Admin), Brendan (Legal Counsel), Fatima (HR Director), Liam (CEO)

Henry: Morning everyone. We're implementing an MDM solution to manage all company-owned mobile devices — iPhones, iPads, and laptops. This lets IT remotely wipe, configure, and secure devices. Five tasks to get through. Let's figure out who owns what.

Henry: Task one — policy and legal review. Brendan, I'd assume this starts with Legal?
Brendan: Broadly yes, though I want to be careful about how much my team takes on right now. We're stretched thin with the acquisition paperwork. I can be involved but I'm not sure I can fully own it.
Fatima: HR has done policy work before. I'm happy to take a first pass at a draft.
Brendan: That works, though anything with legal implications needs to come back through me before it goes anywhere.
Henry: So Fatima drafts and Brendan reviews?
Brendan: More or less. Though "drafts" is a strong word — I'd want Legal to at least frame the structure.
Fatima: I thought you just said you were stretched?
Brendan: I am, but I don't want HR writing legal policy without a legal framework to work from.
Liam: Can we just say both teams are jointly responsible?
Henry: The RACI framework really works best with one Responsible owner per task — otherwise accountability gets murky.
Liam: Right, right. Well sort it out between you two. What's next?
Henry: (making a note) I'll put a flag on task one and we'll come back to it. Task two — vendor and platform selection.

Henry: Task two — vendor and platform selection. Cara, this feels like IT territory?
Cara: Definitely. I've already been looking at Jamf and Intune. I can run the evaluation.
Henry: Great, so you're Responsible and I'm Accountable?
Cara: Actually Henry, shouldn't you be Responsible here too? You have vendor relationships I don't have access to.
Henry: I can help, but I was thinking I'd stay at the project management level across all tasks rather than getting into the weeds on any one of them.
Cara: Fair, but this one specifically — the vendor conversations are going to need someone with budget authority in the room.
Henry: That would be Liam or Derek, not me really.
Liam: I don't need to be in vendor meetings. That's what IT is for.
Brendan: Someone needs to review the contracts. Vendor agreements for MDM platforms can be tricky — data processing clauses, liability terms.
Cara: So Legal is involved too?
Brendan: I'd say Consulted at minimum. Possibly more depending on what the contracts look like.
Henry: Okay so we have Cara doing the evaluation, Henry possibly co-owning, Brendan on contracts, and Liam... Informed?
Liam: I'd like to be Consulted actually. This is a significant platform decision.
Henry: Noted. I'll flag this one too and we'll firm it up. Task three.

Henry: Task three — technical configuration and setup. Cara, your team again?
Cara: In theory yes. But I want to flag that my team is currently two people including me, and we're already managing the server refresh project. I'm not saying no, I'm just saying capacity is a real concern.
Henry: Do you need additional resource?
Cara: Probably. I've been meaning to raise that. Could we bring in a contractor?
Henry: That's a conversation for after this meeting — budget implications. But for the purposes of the RACI, who's Responsible?
Cara: I guess me, conditionally.
Henry: Conditionally isn't really how a RACI works.
Cara: Then provisionally me, pending the resource conversation.
Fatima: Could any of this be outsourced to the MDM vendor themselves? Some of them offer implementation services.
Cara: Some do, yes. That might actually be worth exploring.
Brendan: If we're outsourcing configuration, that changes the legal picture again — data access by a third party.
Henry: Okay, so task three is also flagged. Task four.

Henry: Task four — employee communication and consent. Fatima, HR typically runs this kind of thing.
Fatima: Agreed, and I'm happy to be involved. But I want to push back a little on HR being fully Responsible here. The reason employees are receiving this communication is a technical and legal decision. If staff push back — and some will, especially about the remote wipe capability — I don't want HR to be the ones defending a decision we didn't make.
Brendan: That's a fair point. The messaging around remote wipe in particular needs to be very precise. If we overcommunicate the capability we'll get panic. If we undercommunicate it we'll have legal exposure.
Henry: So who writes the communication?
Fatima: HR can write it, but it needs sign-off from Legal before it goes out.
Brendan: Agreed. And frankly someone from IT should review it too — I don't want Legal or HR accidentally misrepresenting what the system can and can't do.
Cara: Happy to review.
Liam: I may want to put a personal note in from me as CEO. Given the sensitivity.
Henry: That's great Liam, but for the RACI — who's Responsible for producing and sending the communication?
Fatima: HR will coordinate it.
Brendan: With Legal review.
Cara: And IT review.
Henry: So everyone is involved and nobody is specifically Responsible.
Fatima: We're all Responsible.
Henry: (sighing quietly) That's not quite how it works but let's keep going. Task five.

Henry: Task five — device enrollment and go-live. This is the actual rollout — getting every device enrolled in the MDM platform.
Cara: IT should run this.
Henry: Great — Responsible?
Cara: Yes, assuming the resource question from task three is sorted. If I'm doing configuration and rollout with two people I'll need to phase it very carefully.
Henry: Understood. And Accountable — I was going to take that.
Liam: I'd actually like to be Accountable for go-live. This is a company-wide change that touches every employee. If something goes wrong I want it to be clear that it has executive ownership.
Henry: I appreciate that Liam, but operationally it's cleaner if the project manager is Accountable for delivery milestones.
Liam: I'm not trying to step on your toes Henry. I just think for something this visible, having the CEO be Accountable sends the right signal internally.
Henry: What does Accountable mean to you in this context?
Liam: That I'm the one answering for it if it goes sideways.
Henry: And to me it means you're the decision-maker on day-to-day escalations during rollout. Are you available for that?
Liam: (pausing) Maybe not day-to-day, no.
Henry: That's what I thought. So perhaps you're Consulted and I'm Accountable?
Liam: I'm comfortable with that framing but I want it noted that I have executive oversight.
Brendan: What does that mean in RACI terms?
Liam: I don't know, that's why I'm asking you all.
Fatima: Could we add an "E for Executive Oversight" column?
Henry: That's not a standard RACI column.
Fatima: Maybe it should be.
Henry: (long pause) Let me just write down what we have and we'll sort the rest offline.
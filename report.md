# Report

Business Use Case: 
This app is useful for any business with a PMO that's following PMP guidelines (Project Management Professionals) when executing their projects.  A RASCI matrix is necessary to properly track who is responsible for a project's tasks.  This is a time consuming task, and one that's often neglected due to its tedious nature.  This app will make the process quicker, and help with PM compliance, resulting in better outcomes for the business's projects.

Why Claude?: I used Claude to build the app because I purchased a subscription for this course.  Additionally, I've heard from my professors that it is the strongest coding assistant.  It also happens to be the coding assistant that I've spent the most time with, so I felt I had the best chance of using it to make a useful application. I did try to use Google AI studio, but I was struggling to figure out the interface.  It didn't seem as powerful or interactive as Claude Code.  So, after a few attempts I went back to Claude and finished the assignment.

Baseline vs Final Design: The initial app worked, but it had a few issues.  First, it had empty assignments.  It also seemed to make some guesses for assignments on my "hallucination evaluation set" that were not supported by the text. 

My first revision forced it to always make an assignment, and if it didn't know to put TBD so that a PM could later fill in the information after reviewing the text.  My next modification was to push back on the guessing because my "hallucination evaluation set" (where I made sure the prompt had no clear assignments) came back completely filled out with answers other than TBD.  So I reinforced that it should not guess if it doesn't know the answer and after that I had far more TBD's but at least I could trust the results. And my final edit was strictly a user interface change where it wouldn't require a complicated prompt to pull the text file and run the application.

In the final design it has no blank fields, it has TBD when it's unclear, and it has fewer unsubstantiated guesses.

I think this app still has a ways to go.  But I do think it has some use.  It provides the structure of a RACI matrix and it assigns some initial values that can then be completed by a PM.  It's not as accurate as I would like, but with the final revision and the more conservative answers, it at least doesn't have incorrect or made-up assignments.  In the end, it provides a good start for a human (PM) to build upon and I can see it being useful--as long as those using it realize that it's just an initial draft and it requires work to make the matrix of a quality for a customer-facing presentation.

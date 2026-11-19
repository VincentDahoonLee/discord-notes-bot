# Homework 9
### &emsp; Software Engineering and Technical Projects

## Section 1
### Section 1.1

- "What problem are you trying to solve?
One thing I struggle with is keeping track of things - photos, videos, assignments, and some random one off thoughts I might want to keep.

### Section 1.2

- "What are you going to build?" <br>

As someone who spends a lot of time on Discord, I wish to make a discord bot that can be a sort of "thought dump", assignment reminder, and something I can connect to other features for the future all in one place. As a more "barebones" setup, I might make it a reminder that sends me a notification, and a page I can access that will hold things I might need to remember.<br><br>
-daily "Keeping Up!" texts (maybe hourly or 2/3 times a day if needed)<br>
-notifications in other spots

## Section 2
### Section 2.1 - Eisenhower Matrix

|                 |Urgent|Not Urgent|
|---              |---   |---|
|**Important**    |&bull; Working Discord Bot that has commands, buttons, and can send messages at predetermined times. <br> &bull; A way to add an alarm/reminder <br> &bull; A sort of thought dump, maybe like audio/text logs?| &bull; Any way to automate such a process with a database/json file or something <br> &bull; A way to import/export and maybe calendar integration <br> &bull; a randomize feature! of the thought dump
|**Not Important**|&bull; host on AWS <br> &bull; have 100% uptime|&bull; gaming / game feature that keeps me ingaged <br> &bull;
|                 |     |
|                 |     |

### Section 2.2 - Tech Stack

- What language are you writing in?

Python or Java, more likely python because of its ease of use and good documentation.

- What libraries, packages, or external tools do you need? If you're writing Bash, which commands or utilities will you rely on (curl, grep, jq, cron, etc.)? If you're writing Java, which external libraries (if any) do you need?

discord.py most likely, using async and other things

- How will you store data? For an MVP, a plain text / JSON / CSV file is often enough, so there's no need to jump to a full database.

prob a json file but things online talk about like sql and mongodb idk ---- I plan on using my PC to host the bot, so to store data (the )

- If you're pulling data from an external source, what is it and how will you access it? (See the APIs & External Data Sources post on Ed.)

discord.py is the standard for Discord bots, and so I will most likely use that for my own bot.


### Section 2.3 - Chunked Build Plan

- With your MVP scoped out and your tech stack picked, plan the actual build. Break the work into bite-sized milestones, where each chunk should roughly correspond to one meaningful Git commit.

For my discord bot, my steps would look something like this:

- Set up github repo & environment
- Get a token and keep them safe with environment variables
- Get the bot to login and say "Hello" when prompted
- Get the bot to say "Hello" at a set time
- Get the bot to store a reminder 
- Use the "app feature" to say something
- Use the "app" feature to store a message
- Store chunks of data like a notes app

### 2.4 - System Diagram

- The diagram must contain, at minimum: every major component or step in your MVP, labeled arrows showing how data or control flows between them, and a clearly marked starting point (the program's entry point or the first step of the workflow). A grader should be able to read the diagram cold, without looking at your README or code, and reconstruct what the project does and how its pieces fit together.

![Notes app](./Architecure%20Diagram.png)

## Section 3

### Section 3.1 - Github setup and README



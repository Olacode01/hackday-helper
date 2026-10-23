# Hack Day Ideas: 10 starting points per category

Stuck on what to build? Pick an idea, shrink it until you can finish it by 14:30, then make it yours.
These are starting points, not finished projects. **Your team's own work is what gets judged.**

**Difficulty:** 🟢 easy (good for beginners) · 🟡 medium · 🔴 stretch

## Before you start

1. **Declare your starting point.** In your README, add a short section called "What we started from" and list any template, tutorial or idea you used, and what your team built yourselves.
2. **Make it work first.** A small project that runs beats a big one that doesn't.
3. **No private data.** Don't put other people's personal details into any AI tool.
4. **Not advice.** Anything about health, money or law is for learning only. Add a clear note in your README.
5. **Check the AI's answers.** Models make mistakes. Show how your project handles that.

Starter code: `ask.py` in this repo calls Gemma 4 through the Gemini API in about 50 lines.

---

## 1. Best Use of Gemma 4 (via the Gemini API)

Gemma 4 is an open model that works with text and images. Use it through the Gemini API, name the model in your README, and show the API call in your code or demo.
Start here: mlh.link/gemma-quickstart · mlh.link/gemma-docs · mlh.link/gemma-beginnerguide

| # | Idea | What it does | How to start | Level |
|---|------|--------------|--------------|-------|
| 1 | Homework explainer | Take a photo of a problem and get a step-by-step explanation | Send the image plus a prompt asking for steps, not just the answer | 🟡 |
| 2 | Notes to quiz | Paste lecture notes and get quiz questions with answers | Prompt for 5 questions in a fixed format, then show them one at a time | 🟢 |
| 3 | Event or campus FAQ bot | Answers questions using facts you give it | Copy `ask.py` and swap in your own facts | 🟢 |
| 4 | Image describer | Describes photos in plain language for people who can't see them | Send an image, ask for a short, clear description | 🟡 |
| 5 | CV feedback buddy | Gives friendly, specific tips on a CV or cover letter | Paste the text, ask for three strengths and three fixes | 🟢 |
| 6 | Slide-photo flashcards | Photograph a slide or whiteboard and get flashcards | Send the image, ask for question-and-answer pairs | 🟡 |
| 7 | Letter or form simplifier | Turns a confusing letter into plain English and a "what to do next" list | Photo in, summary out. Add a clear "not advice" note | 🟡 |
| 8 | Receipt reader | Reads a receipt photo and totals the spending by category | Ask for the output as structured JSON, then add it up | 🟡 |
| 9 | Language practice partner | Chats with you in a language you're learning and corrects gently | Use a system-style prompt that sets the role. Test the quality in your language | 🟡 |
| 10 | Menu or label explainer | Explains ingredients or a menu in plain words for people with dietary needs | Photo in, list out. Add a "check with the label" warning | 🔴 |

---

## 2. Best Open-Source AI Project (MLH + DEV)

Open-source or open-weight AI must be an important part of how your project works. Your repo must be **public with an open-source licence** (such as MIT or Apache-2.0), and your README must **name the model and link its licence or terms**.
Learn more: mlh.com/opensource-ai · Agent Skills standard: agentskills.io

| # | Idea | What it does | How to start | Level |
|---|------|--------------|--------------|-------|
| 1 | Beginner repo explainer (agent skill) | Teaches an AI agent how to explain any repo to a beginner | Write a skill folder that follows the Agent Skills standard | 🟢 |
| 2 | Commit and README helper (agent skill) | Helps an agent write clear commit messages and READMEs | Write the instructions and a few examples as a skill | 🟢 |
| 3 | Study timetable skill | An agent skill that builds a weekly study plan from deadlines | Define the inputs and output format in the skill's instructions | 🟢 |
| 4 | Local chat app | A simple chat app running an open-weight small model on your own laptop | Pick a model of 10B parameters or fewer and a local runner | 🟡 |
| 5 | Good first issue finder | Finds beginner-friendly open issues and summarises them | Use the GitHub API plus a model to summarise each issue | 🟡 |
| 6 | Side-by-side model compare | Ask two open models the same question and compare the answers | Call both models, show the answers next to each other | 🟡 |
| 7 | Beginner PR reviewer | Comments on a code diff in kind, plain language | Feed a diff to a model, ask for three friendly suggestions | 🟡 |
| 8 | Private study buddy | A study helper that keeps all notes on your own device | Local model plus a folder of notes as context | 🟡 |
| 9 | Tiny agent harness | A small loop that lets a model use tools such as a calculator or file reader | Write the loop yourself: model, tool call, result, repeat | 🔴 |
| 10 | Improve an open-source harness | Add a real feature, fix or tests to an existing open-source agent harness | Fork a project, pick a small issue and make meaningful changes | 🔴 |

---

## 3. Best Project Built with ElevenLabs

Use any ElevenLabs product: speech, transcription, music, sound effects, dubbing, voices or agents. Name the product in your README and show it working in your demo.
Start here: the ElevenLabs Hacker Guide and docs at elevenlabs.io/docs. Look at their "best projects of 2025" list in the guide for inspiration.

| # | Idea | What it does | How to start | Level |
|---|------|--------------|--------------|-------|
| 1 | Read-aloud tool | Turns pasted text or an article into spoken audio | Call the text-to-speech API and play the result | 🟢 |
| 2 | Soundscape maker | Generates sound effects or music for a mood you type in | Use the sound-effects or music endpoint | 🟢 |
| 3 | Lecture transcriber | Turns a recording into text and a short summary | Speech-to-text, then summarise the text | 🟡 |
| 4 | Bedtime story voice | Writes a short story, adds a voice and sound effects | Generate the text, then speech, then effects | 🟡 |
| 5 | Pronunciation coach | Listens to you say a word and gives feedback | Speech-to-text and compare with the target word | 🟡 |
| 6 | Quick clip dubber | Translates a short clip into another language | Use the dubbing endpoint on a short audio file | 🟡 |
| 7 | Voice guide for forms or menus | Reads a form or menu aloud and answers questions about it | Combine text-to-speech with a model that answers questions | 🟡 |
| 8 | Podcast helper | Turns an episode transcript into show notes and a spoken intro | Transcribe, summarise, then voice the intro | 🟡 |
| 9 | Voice FAQ agent | A voice assistant that answers questions about an event | Build an agent on the ElevenLabs Agents platform with your own facts | 🟡 |
| 10 | Voice language buddy | Chats out loud in a language you're learning | Agents platform plus a clear role prompt | 🔴 |

---

## Combine categories (stretch)

A project can qualify for more than one category if it truly uses each technology. For example:

- **Photo to voice:** Gemma 4 describes a photo, ElevenLabs reads the description aloud. 🔴
- **Open-source study agent:** an open-weight model answers questions about your notes, and ElevenLabs speaks the answers. 🔴

---

## Ready to submit? Checklist

- [ ] Public GitHub repo with an open-source licence file
- [ ] README says what the project does, in plain words
- [ ] README names every AI model or tool used, with links
- [ ] README has a "What we started from" section
- [ ] A working demo, or a short screen recording
- [ ] Submitted on the MLH page before the deadline

Good luck, and have fun building!

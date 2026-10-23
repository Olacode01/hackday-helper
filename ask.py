"""Ask Gemma 4 about the CTRL + Chat Hack Day.

A tiny starter project: it sends a question, plus some event facts, to a
Gemma 4 model through the Gemini API and prints the answer.

Run:  python ask.py
"""
import os
import sys
import time

from google import genai

# Gemma 4 models available through the Gemini API (see Google's Gemma docs).
# If the first one keeps failing, the helper tries the next one.
MODELS = ["gemma-4-26b-a4b-it", "gemma-4-31b-it"]
MODEL = MODELS[0]
TRIES_PER_MODEL = 2  # Google sometimes returns a temporary 500 error

# Edit this to teach the helper about your own event.
EVENT_FACTS = """
- Event: CTRL + Chat Hack Day, part of Hacktoberfest 2026, with Major League Hacking.
- Date: Saturday 24 October 2026, 10:00am to 4:00pm.
- Venue: Luton Central Library, Luton.
- Free to attend, for students aged 18 and over.
- Teams build projects with open-source or open-weight AI.
- Submissions are made on the MLH platform before the deadline.
- Hacktoberfest is a month-long October celebration of open-source software, run by DigitalOcean and Major League Hacking, where people make contributions to open-source projects.
"""


def ask(client: genai.Client, question: str) -> str:
    prompt = (
        "You are a friendly helper for a student hackathon.\n"
        f"Facts about the event:\n{EVENT_FACTS}\n"
        "Answer the question briefly, using only the facts above. "
        "If the answer is not in the facts, say you don't know.\n\n"
        f"Question: {question}"
    )
    last_error = None
    for model in MODELS:
        for attempt in range(TRIES_PER_MODEL):
            try:
                response = client.models.generate_content(model=model, contents=prompt)
                return response.text
            except Exception as err:  # temporary errors are common, so retry
                last_error = err
                time.sleep(2 * (attempt + 1))
    raise last_error


def main() -> None:
    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("Set GEMINI_API_KEY first. See the README for how to get a key.")

    client = genai.Client()  # reads GEMINI_API_KEY from the environment
    print(f"Ask me about the Hack Day (model: {MODEL}). Type 'quit' to stop.")
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"quit", "exit", ""}:
            break
        try:
            print("Gemma:", ask(client, question))
        except Exception as err:  # keep the demo friendly if the network drops
            print("Something went wrong:", err)


if __name__ == "__main__":
    main()

# Hack Day Helper (starter project)

A tiny command-line helper that answers questions about the CTRL + Chat Hack Day
using **Gemma 4**, an open-weights model from Google, called through the
**Gemini API**. It is a starter example for beginners at the Luton Hack Day
(Hacktoberfest 2026, with Major League Hacking). Copy it and make it your own.

## AI used

- **Model:** Gemma 4, `gemma-4-26b-a4b-it` (you can also try `gemma-4-31b-it`)
- **Access:** the Gemini API, using the `google-genai` Python package
- **Model terms:** see the official Gemma pages at https://ai.google.dev/gemma
  and add the exact licence link here before you submit your own version.

## Quick start

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Install and run:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export GEMINI_API_KEY="your-api-key"   # Windows PowerShell: $env:GEMINI_API_KEY="your-api-key"
python ask.py
```

3. Ask something like "When does it start?" or "Who can come?".

## Make it yours

- Change `EVENT_FACTS` in `ask.py` to teach it about your own project.
- Need ideas? See [`IDEAS.md`](IDEAS.md) for 10 starting points in each prize category.
- Try the other model ID, or add an image to the request (Gemma 4 can read images too).
- Turn it into a web app, a Discord bot or a voice assistant.

## Notes

- Never commit your API key. The `.gitignore` already ignores a `.env` file.
- This is a teaching example. It only uses the facts in the prompt and can be wrong.

## Licence

MIT. See `LICENSE`.

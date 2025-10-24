# Bank IDs — IBAN Workshop (Python 3.13)

Tiny, clean codebase for a 30-minute Copilot **.prompt.md** workshop.  
Focus: simple **IBAN** utilities only. No I/O, no external deps.

## What’s inside
- `src/bankids/iban_core.py` → has docstrings & a few unit tests (as examples).
- `src/bankids/iban_build.py` → no docstrings & no tests (you add them).
- `src/bankids/iban_parse.py` → no docstrings & no tests (you add them).
- `src/bankids/types.py` → tiny dataclasses.
- Empty prompt directory: `.github/prompts/` (you'll add prompt files here).

---

## Quick start (from zero)

> These steps assume you just installed VS Code and don’t have Python yet.

1) **Install VS Code & set up GitHub Copilot**
   - Open VS Code.
   - Look for the Copilot icon in the Status Bar → **Set up Copilot**.
   - Sign in with GitHub and finish the setup wizard.

2) **Create a virtual environment & install deps**
   ```bash
   # macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install -U pip
   pip install -e .[test]

   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -U pip
   pip install -e .[test]
   ```

5) **Open the folder in VS Code**
   - VS Code → **File → Open Folder…** → pick the project folder.

6) **Enable & use prompt files (.prompt.md)**
   - Ensure the folder `.github/prompts/` exists (it’s already in this repo).
   - Create one or more prompt files in that folder (e.g., `docstrings.prompt.md`, `tests.prompt.md`).  
     Paste the prompt content provided by your workshop lead.
   - Open the **Chat** sidebar in VS Code.
   - To run a prompt file:
     - In the Chat input, type `/` and pick your prompt by name, then follow the prompt; or
     - Use Command Palette: **Chat: Run Prompt** and select your prompt file.

---

## Try it (2 minutes)
1. Open `src/bankids/iban_parse.py`, select all, run your **docstrings** prompt, and accept the patch.
2. Run your **tests** prompt for the same module and commit the new test file.
3. (Optional) Run tests:
   ```bash
   pytest -q
   ```

That's it—have fun!

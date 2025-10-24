# Bank IDs — IBAN Workshop (Python 3.13)

Tiny, clean codebase for a 30-minute Copilot **.prompt.md** workshop.  

## What’s inside
- `src/bankids/iban_core.py` → has docstrings & a few unit tests (as examples).
- `src/bankids/iban_build.py` → no docstrings & no tests (you add them).
- `src/bankids/iban_parse.py` → no docstrings & no tests (you add them).
- `src/bankids/types.py` → tiny dataclasses.
- Empty prompt directory: `.github/prompts/` (you'll add prompt files here).

---

## Quick start (from zero)

> These steps assume you just installed VS Code.

1) **Install VS Code & set up GitHub Copilot**
   - Open VS Code.
   - Look for the Copilot icon in the Status Bar → **Set up Copilot**.
   - Sign in with GitHub and finish the setup wizard.


2) **Choose your track & write the prompt**
   - **Unit tests track:** Inspect `tests/` (and `iban_core.py`) to infer the conventions used to write the tests.  
     Edit `.github/prompts/unit-tests.prompt.md` to include and capture those rules so that newly AI generated tests will follow the same conventions.
   - **Docstrings track:** Inspect docstrings in `src/bankids/iban_core.py` to infer the conventions used to write the docstrings. 
     Edit `.github/prompts/docstrings.prompt.md` to include and capture those rules so that newly AI generated docstrings will follow the same conventions.

3) **Run your prompt on a target file**
   - Target modules: `src/bankids/iban_parse.py` or `src/bankids/iban_build.py`.
   - Open Chat: **View → Chat** (macOS **⌃⌘I**, Win/Linux **Ctrl+Alt+I**).
   - In Chat type `/`, pick **docstrings** or **unit-tests**, then type what you want to change and send.
   - Review and accept the patch.

---

That's it—have fun!

**(Optional) Create a virtual environment & install deps**
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



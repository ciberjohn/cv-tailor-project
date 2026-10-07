# CV Tailor

**English** | [Português (Portugal)](pt-PT/README.pt-PT.md)

Drop-in project instructions for Claude, ChatGPT, Mistral Vibe, Gemini, Copilot or any local agent. Upload one CV, paste a job advert, get a tailored CV in `.docx` and PDF that does not read like a machine wrote it.

The Portuguese version is a full duplicate, not a summary: instructions, rule set, checker mode (`--lang pt`), templates and generated documents, written in European Portuguese.

## The problem this solves

Ask a chatbot to improve your CV and you get three things by default: invented achievements, a wall of adjectives, and a PDF that an applicant tracking system cannot parse. The person then walks into an interview carrying claims they cannot defend.

This project sets the rules first. Every bullet has to come from evidence you already gave it, every file has to come out as a real file, and every sentence has to survive a written anti-slop check.

## How it works

1. Upload your current CV once. The assistant builds a **Career Inventory**: roles, dates, scope, results, tools, qualifications, languages, plus the parts of your CV that are weak and the questions it needs answered.
2. Paste a full job advert. The assistant maps your evidence against the requirements, reports what matches, what only partly matches and what is missing, then rewrites the CV against that advert.
3. It runs the anti-slop pass and exports two files: a `.docx` you can edit and a PDF you can send.

Nothing is invented. The rewrite changes emphasis, order, wording and length. If the evidence is not there, you get a question instead of a guess.

## Commands

| Command | Result |
|---|---|
| `/setup` | Career Inventory, issues in the current CV, up to eight questions |
| `/cv` + advert | Tailored CV, match report, gap list, `.docx` and PDF |
| `/cover` + advert | Cover letter under the same rules |
| `/check` | Anti-slop and ATS pass on any draft you paste back |

## Quick start

**Claude Project or ChatGPT Project**: put `PROJECT-INSTRUCTIONS.md` in the project instructions, upload everything in `attachments/` plus your CV as project files. Then run `/setup`.

**Custom GPT**: `PROJECT-INSTRUCTIONS.md` in the instructions box, `attachments/` as knowledge files.

**Mistral Vibe**: Vibe Chat and Vibe Work take document uploads and run a code interpreter, so the files work as they are. Vibe Code reads `AGENTS.md`, so put the instructions there and the attachments under `.vibe/skills/`.

**Agentic CLIs** (Claude Code, Codex, Cursor, Vibe Code): `PROJECT-INSTRUCTIONS.md` copied to `AGENTS.md` or `CLAUDE.md` in your working folder, attachments beside it.

**Small instruction box** (ChatGPT's custom instruction fields, Gemini Gems, Copilot): paste Appendix C of `PROJECT-INSTRUCTIONS.md`. It is under 1,500 characters, which fits the smallest box on the market.

Then send:

> `/setup` Here is my current CV. Build the Career Inventory, tell me what is weak, and ask me what you need.

## What is in this repo

| File | Purpose |
|---|---|
| `PROJECT-INSTRUCTIONS.md` | The instructions. Also built as `PROJECT-INSTRUCTIONS.pdf` and `.docx` |
| `PROMPT-PACK.md` | Nine copy-paste prompts for anyone who just wants to open a chat: no project, no files, no commands |
| `attachments/anti-slop-rules.md` | The writing rules, standalone, for any platform |
| `attachments/banned-words.md` | The full banned vocabulary, phrases and openers, with research sources |
| `attachments/no_slop_check.py` | Runs the check on a draft and exits non-zero on violations |
| `attachments/md2docx.py` | Markdown to `.docx` with nothing but the Python standard library |
| `attachments/cv-print-template.html` | A4 CV template, print-ready, single column |
| `attachments/cover-letter-print-template.html` | A4 cover letter template |
| `pt-PT/` | The whole project in European Portuguese: instructions, rule set, templates, generated PDF and DOCX |

## The three rules that do the work

**Truth.** Three levels of edit permission. Wording, ordering and emphasis are free. A display title can carry a truthful qualifier. Numbers, dates, qualifications, tools and scope need your confirmation first. An advert keyword you cannot defend goes in the gap list, not the CV. Hidden keyword tricks fail anyway: parsers strip them and recruiters read them as fraud.

**Machine legibility.** Single column, standard section names, contact details in the body rather than a header, dates as `Mon YYYY`, one font between 10.5 and 12pt, no tables, text boxes, icons, photos or graphics. Two pages maximum, with a defined cut order when it runs over. Language and dialect mirror the advert, US, UK, Portuguese or whatever the posting uses, spelling and date formats included; when the advert is unclear, the user's language wins.

**Voice.** The anti-slop rule set bans the vocabulary and the sentence shapes that make text read as machine-written: the rule of three, three sentences of the same length in a row, parataxis, passive constructions, hedging, and the em dash habit. On a CV it also bans `results-driven`, `team player`, `passionate about`, `responsible for` and the rest of the genre. Specifics replace all of it: numbers, tool names, outcomes.

## Export for real

The instructions carry three export paths so the answer matches what the platform can actually do.

- **Code execution available** (Claude with analysis, ChatGPT with the code tool, Mistral Vibe, a local agent): `python3 md2docx.py cv.md "Firstname-Lastname-Role-Company.docx"` for Word, and `weasyprint`, headless Chrome or LibreOffice for the PDF.
- **File output, no shell** (canvas, artifacts): fill in `cv-print-template.html`, then print to PDF from the browser, or open the same file in Word and save as `.docx`.
- **Text only**: one fenced markdown block, pasted into Word or Google Docs and exported by hand.

`md2docx.py` needs no packages and no network, which is why it works in sandboxes that block installs. It writes a genuine Office Open XML file: paragraphs, headings, bullets, tables and monospaced code, all from plain markdown.

## A note on honesty in the tool

An assistant that says "I have created your PDF" while producing nothing has wasted your time. The instructions forbid that claim: if the platform cannot make a file, it says so and points at the export path that fits. Every file in this repo was produced and opened by the tools it describes.

## Credits

The anti-slop rule set comes from the `ciberjohn-no-slop` skill, which merges the [anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) directive by Jalaaldeen (MIT) with an in-house detection checklist.

Detection research behind the rules: Cheng et al. 2025 (*Advances in Simulation*), Russell, Karpinska & Iyyer 2025 (ACL), Juzek & Ward 2025, Kobak, González-Márquez, Horvát & Lause (*Science Advances* 11:eadt3813, 2025), and Wikipedia's "Signs of AI writing" field guide.

MIT licence. Take it, change it, ship it.

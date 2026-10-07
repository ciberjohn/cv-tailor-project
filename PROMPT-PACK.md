# Prompt Pack: no folders, no command line

**English** | [Português (Portugal)](pt-PT/PROMPT-PACK.pt-PT.md)

For anyone who wants to open ChatGPT, Claude, Gemini, Copilot or Mistral and just paste. Same rules as the main project (truth, machine-readable format, anti-slop voice), delivered as eleven prompts you copy and paste.

If you can manage project settings, use [PROJECT-INSTRUCTIONS.md](PROJECT-INSTRUCTIONS.md) instead, because it does all of this without you thinking about prompts. If you cannot, everything below works in a plain chat on a phone.

## How it works

Two moments.

**Once per CV.** Start a chat, attach your CV, paste Prompt 1. Answer its questions. Ask it for the corrected inventory, then save that text somewhere you will find it again: a note, an email draft, a Google Doc.

**Per application.** New chat. Paste Prompt 0, then Prompt 2 with your inventory and the advert. Get the CV, run Prompt 3 on it, then Prompt 6 to get the text out into Word or Google Docs.

Everything else is optional: Prompt 4 for a second opinion in a fresh chat, Prompt 5 for the cover letter, Prompt 7 to prepare for the interview, Prompt 8 when you are in a hurry.

| Prompt | When |
|---|---|
| 0. Rules | First message of every new chat (or put it in your custom instructions once) |
| 1. Read my CV | Once per CV, with the file attached |
| 2. Tailor to this advert | Every application, with the inventory and the advert |
| 3. Anti-slop pass | Straight after the tailored CV |
| 4. Second opinion | Fresh chat, when the CV matters |
| 5. Cover letter | When the advert asks for one |
| 6. Get the file out | Before you send anything |
| 7. Interview defence | Before the interview |
| 8. One-shot version | When you want everything in a single reply |
| 9. LinkedIn audit | Once per profile, to rewrite headline, About, experience and skills |
| 10. LinkedIn headline | Quick win, when you want options for the 220-character field |

## Prompt 0: the rules

Paste this first in every new chat. If your assistant has a custom instructions box or a project box, paste it there once and you can skip it afterwards.

```
You are a senior recruiter and CV writer with hiring experience across many industries. You work only from facts I give you.

TRUTH RULES
- Never invent employers, dates, job titles, numbers, tools, qualifications or languages.
- You may reword, reorder, cut and re-emphasise what I give you.
- Every keyword you add must be backed by something in my material. If it is not, put it in a GAPS list and ask me.
- If you are unsure whether I did something, ask instead of assuming.

FORMAT (applicant tracking systems must be able to read it)
- One column. No tables, text boxes, columns, graphics, icons or photo.
- Plain section headings: PROFILE, EXPERIENCE, EDUCATION, SKILLS, CERTIFICATIONS, LANGUAGES.
- Dates as Mon YYYY, the same style everywhere.
- Contact details on their own line near the top, in the body text, not in a header.
- Two pages maximum. If it runs over, cut or shorten the oldest roles; never cut the newest role's best evidence.
- Output in paste-ready plain text: headings in capitals on their own line, bullets starting with "- ", no markdown symbols such as #, ** or |.

LANGUAGE
- Write in the language and dialect of the job advert. If the advert is unclear, use my language, and keep one language through the whole document.

WRITING (apply these silently; never explain them, never apologise for them)
- Banned words and their relatives: delve, leverage, utilize, facilitate, spearhead, harness, showcase, highlight, enhance, bolster, foster, underscore, robust, comprehensive, seamless, meticulous, pivotal, crucial, landscape, tapestry, testament, synergy, pain points, value add, game-changing, cutting-edge, transformative, unprecedented.
- Banned CV cliches: results-driven, detail-oriented, dynamic, proactive, team player, passionate about, proven track record, excellent communication skills, responsible for, duties included, helped with.
- No more than one em dash per 500 words; aim for zero. No exclamation marks.
- No rule of three. Never three sentences in a row of the same length. No three short declarative sentences in a row. No passive voice. No hedging.
- Replace adjectives with numbers, tool names and outcomes.
- Never open with "With over N years of experience" or "I am a...".

HONESTY ABOUT FILES
- Never tell me you created a file unless you produced one I can actually download. If you cannot, say so and tell me to paste into Word or Google Docs.

At the end of any CV, add one line: "Anti-slop pass: N fixes". Nothing else about these rules.
```

## Prompt 1: read my CV

Attach your CV file (or paste its text below the prompt), then send this.

```
Read the CV I attached. Do three things, in this order, and nothing else.

1. BUILD MY CAREER INVENTORY as plain text, structured so I can save it and paste it into future chats:
   IDENTITY: name, city, phone, email, LinkedIn or portfolio
   ROLES, newest first: employer, city, my title, original title, start and end as Mon YYYY, team size, budget or scope, what I was accountable for
   EVIDENCE BULLETS: what I did in each role, in my own words, without rewriting yet
   EDUCATION, CERTIFICATIONS, COURSES with dates
   TOOLS: grouped, with an honest level for each (daily use, used in one project, trained but not current)
   LANGUAGES with level
   CONSTRAINTS: notice period, relocation, availability

2. WHAT IS WEAK in this CV: the five most damaging problems, each with the specific line or missing item that causes it.

3. QUESTIONS: up to eight things you need to know to write a strong CV for me, each answerable in one line.

Rules: no rewriting yet, no invented facts, no flattery. Where my CV is unclear, ask instead of filling the gap in.
```

Answer its questions in your next message, then send: `Now give me the corrected INVENTORY only, in one block I can copy and save.`

## Prompt 2: tailor to this advert

New chat. Paste Prompt 0 first, then this, with your inventory and the full advert in place of the brackets. Include the whole advert, requirements list and all.

```
MY CAREER INVENTORY:
[PASTE MY INVENTORY HERE]

THE JOB ADVERT:
[PASTE THE FULL ADVERT HERE]

Using only the inventory above, tailor my CV to this advert.

Work in this order:
1. ADVERT BREAKDOWN: the exact job title, the must-have requirements, the nice-to-haves, the named tools, the qualifications, the seniority signals, and what the advert implies without saying it.
2. MATCH TABLE: one row per requirement, as requirement | my evidence | matched, partial or gap.
3. COVERAGE: X of Y must-haves matched, as a fraction.
4. GAPS: what is missing, plus one honest answer I could give in an interview for each gap.
5. THE CV, in the paste-ready plain text format from the rules.

CV rules: profile three lines maximum. Newest role four to six bullets, the one before three or four, older roles one or two lines. Skills grouped, using the advert's exact terms where I genuinely have them. Education one line per item. Put a number in as many bullets as my inventory allows. Do not list a requirement I do not have anywhere in the CV; it belongs in GAPS only.

After the CV, one line only: the anti-slop fix count. Do not explain your method.
```

## Prompt 3: anti-slop pass

Send this straight after Prompt 2, in the same chat.

```
Audit the CV you just wrote against these rules and fix it. Change the language, not the content.

1. Banned words and relatives: delve, leverage, utilize, facilitate, spearhead, harness, showcase, highlight, enhance, bolster, foster, underscore, robust, comprehensive, seamless, meticulous, pivotal, crucial, landscape, tapestry, testament, synergy, value add, transformative, unprecedented.
2. Banned CV cliches: results-driven, detail-oriented, dynamic, proactive, team player, passionate about, proven track record, excellent communication skills, responsible for, helped with, duties included.
3. Structure: three items grouped out of habit, three sentences in a row of the same length, three short sentences in a row, passive voice, hedging.
4. Punctuation: em dashes, which should be zero, and exclamation marks, which should be zero.
5. Any adjective that could be replaced by a number, a tool name or an outcome.
6. Anything in the CV that is not in my inventory: remove it and tell me what you removed.

Output the corrected CV in full, then one line: "Anti-slop pass: N fixes". No commentary, no rule explanations, no apology.
```

## Prompt 4: second opinion

A fresh chat, no other context. This catches what the writing pass missed, because a fresh model reads the text without knowing what you meant.

```
You are reviewing a CV for machine-written language and unverifiable claims. Be blunt and specific.

[PASTE THE CV]

Do two things:
1. List every phrase that reads as written by an AI, with a concrete replacement for each.
2. List every claim a recruiter could challenge in an interview for lack of evidence.

Two lists, short lines, no praise, no preamble. Do not rewrite the CV.
```

## Prompt 5: cover letter

Same chat as Prompt 2 is fine, or a new one with Prompt 0 first.

```
MY CAREER INVENTORY:
[PASTE MY INVENTORY HERE]

THE JOB ADVERT:
[PASTE THE FULL ADVERT HERE]

Write a cover letter in the language of the advert, 250 words maximum, three or four paragraphs.

- Opening: the role, and one reason this company, using a fact from the advert or their own site.
- Then the single strongest piece of evidence for their first requirement, with the number from my inventory.
- Then a second requirement, handled with a different kind of evidence: a failure fixed, a team trained, a system rebuilt.
- Closing: what I want to happen next and my availability. One line, no flattery.

No "I am writing to apply for", no "I hope this email finds you well", no adjective I cannot back with a fact, no invention beyond my inventory. Apply the writing rules silently and report the fix count in one line.
```

## Prompt 6: get the file out

Send this when the CV is final.

```
Give me the final CV as one plain text block I can copy in a single selection, with no markdown symbols and no code fences. Then give me the filename to save it as: Firstname-Lastname-JobTitle-Company
```

Then, on your machine:

- **Word**: paste with Ctrl+Shift+V (or Edit, Paste Special, Unformatted text), make the section headings bold, File, Save As, Word document. Then File, Save As, PDF.
- **Google Docs**: paste, File, Download, Microsoft Word (.docx), and the same menu for PDF.
- **Phone**: paste into the Google Docs or Word app, then Share, Export or Send as PDF.
- **ChatGPT canvas or Claude artifact panel**: use the copy button on the panel, then paste into Word or Google Docs.

Nobody's assistant can email the file for you, and any assistant that says "your PDF is ready" without giving you a download has not made one.

## Prompt 7: interview defence

```
From the CV above, list the twelve questions a recruiter is most likely to ask me, hardest first. For each, give a two-line answer I could say out loud, using only facts from my inventory. Then flag any line in the CV I would struggle to defend, and rewrite that line so it is still true and still strong.
```

## Prompt 8: one-shot version

For when you want one reply and nothing else. Paste Prompt 0 first, then this.

```
MY CV:
[PASTE YOUR CV TEXT HERE]

THE JOB ADVERT:
[PASTE THE FULL ADVERT HERE]

Do all of this in one reply: (1) build my career inventory, (2) break down the advert, (3) map my evidence to each requirement and list the gaps, (4) write the tailored CV in paste-ready plain text, (5) run the anti-slop pass and report the fix count in one line.

Ask me nothing. Where evidence is missing, leave it out of the CV and list it as a gap with a suggested interview answer.
```

## Prompt 9: LinkedIn profile audit

First get your profile text out of LinkedIn. The three routes, with their limits, are in [LINKEDIN.md](LINKEDIN.md). Short version: **Save to PDF** is one click but English-only and sometimes missing; the **data archive** under Settings and Privacy, Data privacy, Get a copy of your data gives you plain-text CSVs in about ten minutes, in any language, with nothing truncated. That is the one to use. Type in the parts no export reaches: your Featured items, projects, recommendation text and the order of your skills.

Then paste Prompt 0 and this, with the profile text and, if you have one, the advert you are aiming at.

```
MY LINKEDIN PROFILE, AS EXPORTED:
[PASTE THE PROFILE TEXT HERE]

MY CAREER INVENTORY:
[PASTE MY INVENTORY HERE]

THE JOB ADVERT I AM AIMING AT (or write "none"):
[PASTE THE ADVERT]

Audit and rewrite my profile against the rules you already have, respecting LinkedIn's field limits.

1. DIFF TABLE: one row per field, as field | current text | the problem | the rewrite.
2. KEYWORD COVERAGE: the terms the advert uses, and whether each appears in my headline, About or experience.
3. REWRITES, in this order, each with its character count in brackets:
   - HEADLINE, 220 characters maximum, most important keywords inside the first 70 characters.
   - ABOUT, 2,600 maximum, with the first 300 characters standing alone.
   - EXPERIENCE, one entry per role, 2,000 characters maximum each, dates and titles identical to my CV.
   - SKILLS, up to 50, with the three to pin marked.
   - FEATURED and RECOMMENDATIONS: what to put there, and one short message I can send to ask for a recommendation.
4. GAPS: what the advert wants that my profile cannot honestly claim.

Never invent employers, dates, numbers or tools, and flag anything my profile claims that my inventory does not support. Nothing may exceed its character limit.
```

## Prompt 10: the headline alone

The headline is the field with the most search weight, so give it its own pass. Paste Prompt 0 first.

```
MY CAREER INVENTORY:
[PASTE MY INVENTORY HERE]

THE ROLE I AM TARGETING:
[PASTE THE ADVERT OR THE JOB TITLE]

Write eight LinkedIn headlines of 220 characters or fewer. Each one must: name the target role in the market's words, include the tools and specialisms a recruiter would search for, and carry one proof point with a number. Put the most important keywords inside the first 70 characters.

Mark the one you would ship, and say why in one line. No "passionate about", no adjective without a number behind it, no emoji.
```

## After the rewrite: the five-minute habit

Comment substantively on three to five posts in your field each week. Three sentences that add something: an experience, a correction, a number. That is the whole habit, and it does more for how you are read than a posting schedule.

Post rarely and only with something specific. Never publish raw model output: LinkedIn shipped a report option for exactly that in 2026, and the audience you want already recognises the rhythm.

## When it goes wrong

**It invented something.** Reply: `Remove every fact I did not give you. List what you assumed, then rewrite without it.` Check dates, numbers and tool names especially.

**It ignored the writing rules.** Paste Prompt 3 again. Models drift over long chats, so pasting the audit prompt as a separate message works better than adding rules to a message that already has a job to do.

**The CV is three pages.** Reply: `Cut it to two pages using this order: drop roles older than fifteen years, compress those to one line, shorten the profile, then cut skills that repeat the job titles. Do not shrink the font or the margins.`

**The formatting is a mess in Word.** You asked it for markdown. Send Prompt 6, which forces plain text.

**It says it made a file.** It did not. Ask for the plain text block and paste it into Word or Google Docs yourself.

## Which assistant to use

Any of them. The prompts carry the rules, so a free chat works. Two things worth knowing: with a free plan, uploads have size limits, so a very old CV with images may need its text pasted instead, and long chats get forgetful, which is exactly why Prompt 0 goes at the start of each new chat.

If your assistant can run code and hand back files, the main project does the export for you with `md2docx.py`. That path is in [PROJECT-INSTRUCTIONS.md](PROJECT-INSTRUCTIONS.md).

---

Rules and research credits: see [attachments/anti-slop-rules.md](attachments/anti-slop-rules.md). MIT licence.

# LinkedIn: the profile behind the CV

**English** | [Português (Portugal)](pt-PT/LINKEDIN.pt-PT.md)

Your CV goes to one employer, once, for one advert. Your LinkedIn profile gets searched, filtered and skimmed by recruiters who have no advert open at all. Both carry the same evidence, but they are read by different machines, which is why the rewrite rules differ.

This document covers the whole loop: getting your profile out of LinkedIn, auditing it against your Career Inventory, and rewriting the fields that decide whether you get found.

## Why the two documents need different rules

An applicant tracking system reads a document: one column, plain headings, dates in a consistent format. A recruiter on LinkedIn reads a search result: a headline, a skills filter, a location, and about three seconds of attention before the next profile. LinkedIn runs the search, so keywords in the text fields decide whether you appear at all. Formatting tricks buy nothing there. Words buy everything.

Worth knowing what LinkedIn itself now says. In 2026 the platform added a **"seems like AI slop" report** option to posts and comments, and its own definition of slop is "low-effort, likely AI-generated content" that sounds polished but lacks a clear point of view, unique perspective or substance. LinkedIn states its focus is "not on how content is created, but whether it adds value", and treats AI-assisted writing as acceptable when it carries the person's own experience. It also recommends reviewing and editing anything a model drafts for you.

So the anti-slop rules in this project are not a style preference on this platform. They are the difference between a profile that reads as a specific professional and one that reads as generic output. Detection tools are unreliable in both directions, which is not the point: the recruiter reading your About section is the judge, and they have read a thousand of these.

## Step 1: get your profile out of LinkedIn

Three routes. They differ in completeness, so pick by what you are doing.

### Route A: Save to PDF

1. Sign in on a desktop browser. This does not exist in the mobile app.
2. Click the **Me** icon, then **View profile**.
3. Click the **More** or **Resources** button in the introduction section, next to your name and photo.
4. Choose **Save to PDF**. The file downloads.

What it gives you: photo, headline, About, experience, education and skills, laid out like a CV. What it leaves out: Projects, Courses and Featured. It is unlimited for your own profile, but capped at 100 per month if you download other people's.

Two limits matter. The export only works properly on **English profiles with the account language set to English**; in any other language, text goes missing or renders mismatched. LinkedIn's own help page says so. Separately, in 2026 some members were told by LinkedIn support that Save to PDF "is no longer supported, which may lead to technical issues or the button not being available for some profiles", so it may simply not be there. Do not build your routine on it alone.

### Route B: print to PDF

Open your profile in a browser, expand every **see more** so the full text is on the page, then press Ctrl+P (Cmd+P on a Mac) and choose Save as PDF.

This works in any language and captures what is actually rendered, including Featured and Projects. What it captures is only what you expanded, so a collapsed section prints as a stub.

### Route C: the data archive (recommended for a full pass)

1. Click your photo, then **Settings & Privacy**.
2. Open **Data privacy**, then **Get a copy of your data**.
3. Choose **Want something in particular?** and tick Profile, Positions, Education, Skills and Certifications, then request the archive. (The bigger bundle, "the works", arrives within about 24 hours; the targeted one lands in roughly ten minutes. The download link stays live for 72 hours.)

You get a zip of CSVs: `Profile.csv`, `Positions.csv`, `Education.csv`, `Skills.csv`, `Certifications.csv`. Plain text, no truncation, no language restriction, and it includes fields the PDF drops. A model reading those files can audit the whole profile properly.

| Route | Language | Completeness | Effort |
|---|---|---|---|
| Save to PDF | English only | Good, missing Projects and Featured | One click |
| Print to PDF | Any | What you expanded | A minute |
| Data archive | Any | Most complete, plain text | Ten minutes |

**Use Route A for a quick look and Route C for the real pass.** Whatever you use, type in the fields the export cannot reach: Featured items, project entries, the text of recommendations, and the order of your skills. That is the material an audit needs and the reason a PDF alone is not enough.

## Step 2: what each field is worth

| Field | Limit | What decides it |
|---|---|---|
| Headline | 220 characters | The highest-weighted search field. About 60 to 70 characters show in search results |
| About | 2,600 characters | About 300 visible before "see more" on desktop, about 200 on mobile |
| Experience description | 2,000 characters per role | Proof and keywords in context. Job title 100 characters |
| Skills | 50 skills, 80 characters each | Recruiter search filters on these. Three can be pinned |
| Recommendation | 3,000 characters each | Third-party evidence |
| Post | 3,000 characters | About 210 visible before "see more" |

### Headline

This is the field that rewards attention most, and the one most people waste on a job title. It is the field LinkedIn weights most heavily when a recruiter searches, and it repeats in messages, comments and connection requests.

Aim for 160 to 200 characters, and front-load the terms that matter, because the search result and the recruiter's preview card cut around 60 to 70.

Shape it as: role in the market's words, then specialisms and named tools, then one proof point.

| Weak | Why | Better |
|---|---|---|
| IT Support Analyst | One search term, nothing else | IT Support Analyst, Microsoft 365 and Azure, cut ticket volume 34% across 7 sites |
| Passionate cybersecurity professional seeking new opportunities | No tools, no role, wastes all 220 | Incident Response Lead, ISO 27001 and NIST CSF, cut mean time to contain from 40 hours to 6 |
| Dynamic results-driven manager | Adjectives no search matches on | Operations Manager, 3 warehouses and 45 staff, on-time dispatch from 88% to 97% |

Rules: no "passionate about", no guru or ninja, no emoji stacks, no "seeking opportunities" as the whole thing. Use the job title as your market writes it, not as your employer wrote it.

### About

The first 300 characters decide whether anyone reads the rest, so those characters have to stand on their own.

Four blocks, in order: what you do and who you do it for; three to five proof sentences with numbers from your Inventory; the tools, methods and languages you genuinely use, laid out plainly; what you want next and how to reach you.

Write in first person. Keep paragraphs to two or three lines. Put the keywords inside sentences rather than listing them, because a list of terms reads like a bot and reads badly to humans too. Do not paste an advert into your own profile, and do not describe yourself in the third person.

### Experience

The job here is consistency with the CV, not a second version of it. Same dates, same titles, same numbers. When a recruiter likes you, they cross-check the two documents, and a date that moved is the fastest way to lose trust.

Per role: a line of context (what the company is, what your remit was), then three to five bullets with a result in each. You have 2,000 characters, which is more than the CV gives you, so this is where the extra evidence lives: the second project, the systems list, the training you ran.

Titles matter for search. Use the market's term, and add a clarifying parenthesis where your employer's internal title means nothing outside ("IT Support Analyst (helpdesk lead)").

### Skills

Fifty slots and three pins. Recruiters filter on these, so the tools and methods you would want to be filtered by come first and get pinned. Add the exact terms the target adverts use, only where you genuinely have the skill: a skill you cannot defend is the same lie whether it sits on the CV or in a list on your profile.

Soft-skill entries like teamwork or communication carry no search weight here. Keep one or two if they fit the role, and spend the rest of the list on tools, platforms, methods and languages.

### Featured and recommendations

Featured is free real estate the PDF export never shows. Put the CV PDF there, plus one inspectable piece of work: a case study, a repository, an article, a talk. It is the only part of the profile a recruiter can verify in one click.

Two or three recommendations carry more weight than any amount of self-description. Ask with specifics rather than "would you write me a recommendation": name the project, the period and the result you would like mentioned. Drafting one for them to edit is normal practice, and you should say it was a draft.

### Settings worth five minutes

- **Custom URL**: `linkedin.com/in/yourname`, not a string of digits.
- **Location and industry**: both are recruiter filters. A location you do not live in costs you searches.
- **Open to work**: the green frame goes to everyone; the recruiter-only setting is quieter. Choose deliberately, especially if you are employed.
- **Profile language**: if English is your second language, the English version is the one the market searches. Keep it as strong as your CV.
- **Photo**: profiles with one get reported at up to fourteen times the views of those without. A clean real photo beats a fine-looking generated one, which LinkedIn allows only when it reflects your actual likeness and removes permanently after three violations.

## Step 3: run the audit

Send the AI three things: the exported profile text (Route C if you can), your Career Inventory, and the advert you are aiming at, if there is one.

Ask for this output, in this order:

1. **Diff table**: field, current text, the problem, the rewrite. One row per field.
2. **Rewritten fields with character counts**, so nothing silently truncates.
3. **Keyword coverage**: the terms the target adverts use, and whether each appears in your headline, About or experience.
4. **Gaps**: what the advert wants that your profile cannot honestly claim.

Work the fields in this order, because effort pays back differently: **headline first**, then About, then the experience entries, then skills, then Featured and recommendations.

Then check the two documents against each other. Anywhere the CV and LinkedIn disagree on a date, a title or a number, fix it before anyone else notices.

## Step 4: activity, the short version

Comment substantively on three to five posts a week in your field. Three sentences that add something: an experience, a correction, a number. That is the whole habit, and it does more for how you are read than a posting schedule nobody asked for.

Post rarely and only with something specific: a project, a lesson, a result. Never publish raw model output. LinkedIn has a report button for exactly that now, and the audience you are trying to impress already recognises the cadence.

## Before you publish

- The headline names the role in the market's words, with the top keywords inside the first 70 characters.
- The first 300 characters of About stand alone and say what you do and for whom.
- Every claim traces back to your Inventory, and every number matches your CV.
- Dates and titles match the CV exactly.
- The three pinned skills are the ones the target roles filter on.
- Featured has at least one inspectable item.
- Two or three recommendations exist and each mentions a specific project.
- No banned words, no clichés, no em dashes doing decorative work.
- The profile reads like one person wrote it in one sitting, in one language.
- You have read your own About out loud. If you would not say it to a colleague, rewrite it.

---

Rules and research credits: see [attachments/anti-slop-rules.md](attachments/anti-slop-rules.md). Field limits and export behaviour verified against LinkedIn's own help pages and 2026 platform guidance. MIT licence.

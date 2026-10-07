# Anti-Slop Writing Rules (standalone)

Paste this file into any AI project as knowledge, or keep it in the project folder. It is the
rule set the resume work must obey. It comes from a longer internal spec, trimmed to what a CV,
a cover letter or a profile summary needs.

If the assistant has code execution, run `no_slop_check.py` on the finished draft before
exporting. If it cannot run code, walk the self-check list at the bottom of this file by hand and
report which items you fixed.

---

## 1. The point

Language models default to the most probable phrasing, which is why AI text all sounds the same.
The fix is not to sprinkle in slang. It is to cut the statistical fingerprints, then write with
specifics: real numbers, real tools, real names, real outcomes.

## 2. Vocabulary to cut

Replace, never keep.

| Banned | Use instead |
|---|---|
| delve, deep dive | went through, read, examined |
| leverage (verb) | use, with |
| utilize | use |
| commence | start |
| facilitate | ran, set up, chaired |
| spearhead | led, started |
| harness | put to work, used |
| showcase, highlight | showed, shipped, gave |
| enhance | improved, raised, cut |
| bolster | strengthened, backed |
| foster | built, encouraged, taught |
| underscore | shows, proves |
| showcase | showed |
| robust | reliable, tested |
| comprehensive | full, complete (or name the parts) |
| seamless | smooth, no manual steps |
| meticulous | careful, exacting |
| pivotal, crucial | say why it mattered, with a number |
| landscape, tapestry, interplay, multifaceted | name the actual thing |
| testament ("a testament to") | say what it proved |
| cutting-edge, groundbreaking, game-changing, transformative | name the version, the date, the result |
| synergy, pain points, value add, thought leader | plain words for the same idea |
| moving forward, touch base, circle back, rest assured | delete |
| "it goes without saying" | delete |
| "in order to" | to |
| "utilize" | use |

Statistically overused filler from the same studies: insights, findings, potential (as a noun),
particularly, additionally, notably, across (as filler), within (as filler), exhibited, rich,
fast-paced, embark on a journey.

Software and frameworks are exempt from the ban: Django REST Framework, Ruby on Rails and the
World Economic Forum's Global Risks Report are proper names, not slop. Use the name, keep the
capital letters.

## 3. Phrases to cut

Every one of these is filler. Replace it with nothing, or with the fact it was hiding.

| Banned phrase | What to do |
|---|---|
| In today's [anything] | delete, start with the fact |
| In an era of | delete |
| It's worth noting / it's important to note | delete, state the thing |
| Let's dive in / delve into | delete |
| At its core | delete |
| In the realm of / in the context of | in, for |
| When it comes to | for, with, about |
| A testament to | proved, showed |
| Not just X, but Y | state Y once |
| This is where X comes in | delete, name the action |
| Whether you're a X or a Y | delete |
| At the end of the day | delete |
| The bottom line is | delete |
| Here's the thing / here's the deal / here's what matters | delete |
| What this means is | delete |
| In a nutshell | delete |
| Buckle up | delete |
| Take it to the next level | name the change |
| Unlock the power of / empower / elevate your / supercharge your / streamline your | name the action and its result |
| Bridge the gap / move the needle | name the number |
| In conclusion / in summary / overall, | delete, stop when the point is made |
| Firstly, secondly, thirdly | order the points, or use one sentence |
| I hope this helps | delete |
| As per my last email | delete |
| Please don't hesitate to reach out | say what you want to happen |
| Not only X but also Y | state both plainly |
| In order to | to |
| It has been described as / experts say | name the source or cut the claim |

## 4. Openers to cut

| Banned opener | Instead |
|---|---|
| Certainly, / Absolutely, / Sure, | the answer itself |
| Great question! / That's a great point! | delete |
| I'd be happy to | delete, do the thing |
| As an AI / As a language model | delete |
| Moreover, / Furthermore, / Additionally, | start with the subject |
| Interestingly, / Notably, / Importantly, / Indeed, | delete |
| With over N years of experience | the result that makes the number irrelevant |
| One of the most [adjective] | the specific thing |
| By [verb]ing (as a sentence opener) | the subject and the verb |

The last three matter most on a CV. "With over fifteen years of experience in..." is the most
common opening line in AI-written resumes. It tells the reader nothing.

## 5. Structure and rhythm

- No rule of three. Models group things in threes by default. Use two, four, one or five items.
- No three consecutive sentences of the same length. This is the single most measurable AI
  signal. Vary hard: one short sentence next to a long one.
- No parataxis. Three short declarative sentences in a row reads like a machine. Connect the
  thoughts with conjunctions, semicolons or subordinate clauses.
- No hedging seesaw. State the claim; give a counterpoint one sentence at most.
- No passive voice. "The migration was completed by me" becomes "I migrated".
- No para ending in a transition. Let some paragraphs stop dead.
- No identical paragraph shape. Topic sentence, explanation, example, transition, repeated eight
  times, is a template.
- Bullets: uneven lengths, five to seven maximum in a row. If a point fits in a sentence, write a
  sentence.

## 6. Punctuation

- Em dash: one per 500 words at most. Best count on a CV is zero. Use a comma, a colon, a
  semicolon or a new sentence. In a heading line, separate the role, the company and the dates
  with commas or a pipe.
- Exclamation marks: one per 1,000 words at most. On a CV, none.
- Ellipsis: only when something genuinely trails off. Once per document at most.
- Semicolons: use them where they fit. People who write well use them; models under-use them.
- Oxford comma: omitted by default in UK English. Add it only to prevent ambiguity.

## 7. CV-specific bans

Never write: "results-driven professional", "detail-oriented", "dynamic self-starter", "team
player", "passionate about", "proven track record", "excellent communication skills", "think
outside the box", "responsible for", "duties included", "helped with", "worked on", "various
tasks", "wide range of", "strong work ethic".

Replace them with the action and its result:

| Slop | Real |
|---|---|
| Responsible for the helpdesk | Ran a 3-person helpdesk handling 400 tickets a month |
| Helped with the cloud migration | Moved 60 servers to Azure over 9 months, no unplanned downtime |
| Excellent communication skills | Trained 120 staff on phishing triage; report rate went from 8% to 41% |
| Passionate about security | Rebuilt the escalation path after the 2024 ransomware hit |

## 8. Honesty

Never invent a number, a date, an employer, a tool or a qualification. If the evidence is not in
the source material, the correct output is a gap, not a guess. Say what is missing and let the
person fill it.

## 9. Self-check before export

1. Any banned word or phrase left? Replace it.
2. Three sentences in a row the same length? Break the rhythm.
3. Three short declarative sentences in a row? Join them.
4. Items grouped in threes by default? Change the count.
5. Hedging instead of committing? Commit.
6. More than one em dash in 500 words? Cut.
7. Passive construction? Make it active.
8. Every paragraph ending in a transition? Cut some.
9. Any invented fact? Remove it, or flag it as a question for the user.
10. Could this CV belong to any candidate? Add something only this person could write.
11. Does it read like a language model wrote it? Rewrite until the answer is no.
12. Did the assistant mention these rules, or apologise for them? Delete that text. Rules are
    applied silently.

Report the result as one line, for example: "Anti-slop pass: 6 fixes (3 banned words, 2 em dashes,
1 passive line)." Do not paste the rule list back at the user.

---

Adapted from the `ciberjohn-no-slop` skill by João Silva, which merges the anti-ai-slop-writing
directive by Jalaaldeen (MIT) with the medium-story detection checklist. Detection research:
Cheng et al. 2025 (Advances in Simulation); Russell, Karpinska & Iyyer 2025 (ACL); Juzek & Ward
2025; Kobak, González-Márquez, Horvát & Lause, Science Advances 11:eadt3813 (2025); Wikipedia,
"Signs of AI writing"; ETBI Digital Library. MIT licence.

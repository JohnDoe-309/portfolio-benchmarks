# What 226 personal sites taught me

Read alongside [README.md](README.md), which lists every site. This file is the argument.

A caution on the counts below: they come from the annotations in `data/sites.json`, written while
reading each site once. They describe what was visible and worth recording, not an exhaustive audit.
Treat them as strong signal, not as a survey.

---

## 1. The craft and the ask almost never appear on the same site

This is the finding that surprised me most, and it holds across all four groups.

The 66 sites in the "top portfolios" group contain the best work on the open web — playable physics
simulations, WebGL scenes that load in under a second, typefaces the rest of us use every day. A
reader arrives impressed and then finds nothing to do. Contact is an email address in a footer, or a
row of social icons, or nothing at all. One award-winning developer's FAQ says plainly that he is
unavailable.

The 51 freelance and fractional sites are the mirror image. They ask constantly — 11 lead with a
calendar, 38 publish a number, some repeat the call to action four times on one page — and almost
none of them can hold your attention for ten seconds. Stock photography, a logo wall, three
paragraphs of "we partner with ambitious teams".

Nobody does both. A site that has the craft of the first group and the sales mechanics of the second
is an open position, and it costs nothing to take it but the discipline to do both jobs at once.

## 2. Proof comes in five grades, and most sites reach for the weakest one

Ranked by how hard it is for a stranger to dispute:

1. **The artifact itself.** tldraw's creator ships a live canvas. reveal.js's author lists
   inspectable experiments. Bartosz Ciechanowski publishes one playable simulation a year. Nothing
   is claimed, so nothing can be doubted.
2. **Dependency.** "3,000+ repositories depend on FastEmbed." Someone else's build breaks without
   your work. Unfakeable, and rare outside open source.
3. **A number with its measurement attached.** Gibson Biddle publishes an NPS *with its sample size*
   (69, n=49). One of the very few self-reported figures on any of these sites that a reader can
   evaluate rather than swallow.
4. **Named third parties.** Client logos, testimonials with a title and an employer. Weaker than it
   looks: readers assume cherry-picking, and several sites here have a wall of logos with no
   outcome attached to any of them.
5. **Audience size.** Follower and subscriber counts. Nine of the 51 operator sites lean on this,
   and it proves distribution, not competence.

The gap between grade 3 and grades 4–5 is where most credibility is lost. "We drove real business
results" is grade 5 wearing grade 3's clothes.

## 3. What the sellers do that the admired sites don't

Across the 51 freelance and fractional sites:

| Mechanic | Sites doing it |
|---|---|
| Publish a price or a rate card | 38 |
| Explicitly decline to publish a price | 18 |
| Offer a guarantee or risk reversal | 18 |
| Signal availability or capacity | 17 |
| Use a calendar as the primary call to action | 11 |

The guarantees are the interesting part, because the specific ones read as confidence and the vague
ones read as marketing. Three that land, in ascending order of nerve: "if we can't identify three
quick wins that save your team a combined five hours a week, you don't pay"; "if you don't regain ten
hours a month in ninety days, we keep working free"; and an audit that costs nothing unless it finds
losses larger than its own fee. Each names a threshold the buyer can check. Compare with "48% of AI
projects fail — ours don't", which commits to nothing.

Availability is the cheapest mechanic nobody uses. A green or red dot for open-to-work. "Booking two
to three weeks out." "One VIP day a week, currently six to eight weeks out." It costs one line, it
creates urgency without a countdown timer, and it makes the person feel like a real practitioner with
a real calendar rather than a landing page.

## 4. The BITS and IIT finding: an empty lane

Of 58 BITS and IIT alumni sites, **four** carry any signal of availability, consulting or hiring.
Four. One publishes workshops, one offers office hours, one puts a calendar link in the intro, one
routes speak / advise / project. The remaining 54 are pure identity pages.

Most are research or engineering templates: publication list, thumbnails, a scholar link. They are
competent and nearly identical — the same layout recurs across a dozen domains, which makes any
deviation from it disproportionately memorable. The most common flaw is a stale fact: a bio that
still says "PhD student" years after founding a company, or "prefinal year student" years into a
senior job.

A sweep of roughly 975 GitHub profiles with BITS in the bio turned up almost nothing verifiable in
the way of BITS-alumni *founders, PMs or investors* with a real personal site — not a LinkedIn, not a
Linktree. The IIT side has more founders, but they sell a company, not themselves. The strongest example found anywhere
in that group is a separate **proof-of-work ledger**: a page listing, per company, what shipped and
what moved, in reverse-chronological order with press links. It's the single most copyable idea in
this whole corpus, and it ends without an ask, which is the group's defining weakness.

For an operator selling work, the competitive set here is not "other BITS engineers". It's empty.

## 5. Length runs inversely to the strength of the ask

Among the public retrospectives, the ~1,200-word pieces close with a booking link. The 4,500-word
teardown closes with a share button. The most credible document of the lot — a consultant publishing
an actual client deliverable, with permission — has no call to action anywhere.

The writing that proves the most converts the least, because the people who write that well are
usually not trying to sell. That's an arbitrage for anyone willing to do both.

## 6. Small things that were quietly effective

- **Counted inventory above the fold.** "111 blogs, 673 notes, 268 videos, 7 projects." Volume
  becomes a number, and a number is checkable.
- **Work and lab kept separate**, so experiments don't dilute client work.
- **A FAQ that states timelines and how pricing is structured** — it answers the questions that
  otherwise cost a discovery call.
- **A "Working With Me" block** that routes speak / advise / project, so the visitor self-selects.
- **Naming the buying moment** rather than the service: "when repeated fixes have failed".
- **Trigger-based positioning beats capability lists.** "One senior operator, start to finish" tells
  a buyer more than six service labels.
- **Status-tagging your own work** — Shipped, Exhibited, Prototype, Seedling — is free honesty, and
  it makes the finished things look more finished.

## 7. Anti-patterns, with the receipts

- **The JS-only portfolio.** Six of the craft sites render fewer than a hundred words without
  JavaScript; one has nineteen words of HTML. Beautiful, invisible to a link preview, and hostile to
  anyone on a bad connection.
- **Award walls.** Six sites lead with award counts. Two awards read as excellence; seventy-seven
  read as a hobby.
- **Employer logos presented as client logos.** The one place a portfolio tips from selective into
  misleading.
- **Manufactured scarcity.** A countdown timer on a consulting page reads as a funnel, not an
  operator. A real calendar constraint reads as an operator.
- **Testimonials about feelings.** "Insightful", "a joy to work with", "brought clarity". Nine
  operator sites rely on these. None of them is checkable, and readers discount them.
- **The bio that never updates.** One site still describes its owner as a "prefinal year student"
  years into a senior engineering job. Nothing destroys trust in a page faster than a stale fact.

## 8. What this changed on siddansh.vercel.app

Applied so far: the ask moved above the fold; the call to action repeats in the sticky nav; the
strongest case file opens expanded; a five-question FAQ handles objections before the call; case
files became linkable with prev/next and a per-case ask; two case files now admit what's still open;
scroll depth, sections seen and every CTA click are recorded.

Still open, in order of expected effect: a calendar as the primary call to action; an identity that
resolves (LinkedIn, and a GitHub handle that reads as a name); a published price floor on the audit
with a specific guarantee attached; two or three named references; and the proof-of-work ledger.

## 9. The pricing question, since it keeps coming up

Publishing a price cuts inbound volume and raises inbound quality, with pipeline roughly flat.
HockeyStack Labs, across 80 B2B SaaS companies and 31M unique visitors: form submissions 2.8% with
transparent pricing versus 4.6% without, but submission-to-pipeline 17.50% versus 10.31%. Bounce was
*higher* on the transparent pages, which contradicts the most-repeated claim in this space.

Every source specific to solo consultants is anecdote with no numbers. So the honest argument for
publishing a floor isn't that it earns more — it's that it stops you spending your scarcest input,
your own hours, on calls that were never going to close.

Sources: [HockeyStack](https://www.hockeystack.com/lab-blog-posts/state-of-pricing-demo-case-study-pages) ·
[NN/g on scrolling and attention](https://www.nngroup.com/articles/scrolling-and-attention/) ·
[NN/g on testimonials](https://www.nngroup.com/articles/about-us-information-on-websites/) ·
[Chartbeat via Time](https://time.com/12933/what-you-think-you-know-about-the-web-is-wrong/)

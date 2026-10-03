# Gleason and Kochen–Specker

**Caltech Mathathon 2026** · Calvin Sabastian Tanzil · Physics, Institut Teknologi Bandung (ITB)

Why are quantum probabilities forced to follow the Born rule, and why is the smallest
Kochen–Specker set in three dimensions still unknown?

## The problem

**Gleason (1957).** Treat each quantum yes/no question as a direction, and ask for probabilities
that add up to 1 over every orthonormal basis. In dimension three or more, the only way to do this
is the Born rule. In dimension two it fails. Gleason's original proof is famously hard; an elementary
proof came later (Cooke, Keane and Moran), and Busch's version for generalized measurements is short
and works even in dimension two.

**Kochen–Specker (1967).** Ask the same question with hidden 0/1 answers instead of probabilities,
and it becomes a coloring puzzle: color directions in ℝ³ so that every orthogonal triple has exactly
one 1 and no orthogonal pair has two. Gleason's theorem already rules out coloring the whole sphere.
Kochen and Specker found 117 directions that cannot be colored; Peres cut this to 33, and Conway and
Kochen to 31.

**The Free Will Theorem (Conway and Kochen, 2006 and 2009).** The best-known use of a
Kochen–Specker set. Two entangled spin-1 particles are measured along Peres's 33 directions. If the
experimenters choose their measurements freely, the particles' answers cannot be functions of the
past, because such a function would color the 33 directions. Critics reply that this is not new for
deterministic models and not correct for stochastic ones. We treat it as a theorem about the
coloring obstruction, played by two particles, and leave the question of free will open.

**What is still open.** Nobody knows the smallest uncolorable set in three dimensions.

- Smallest known: 31 directions (Conway–Kochen).
- Best lower bound: 24, from two independent SAT-solver searches. The earlier bounds were 18 and 22,
  also by computer. The certificates for the 23-vector case alone fill 40.3 TiB.
- A probabilistic method that does not search over graphs currently gives 10.
- Trandafir and Cabello argue the answer is 31, under an assumption about the set's structure.

The lower bound exists only as machine search, like the four color theorem. We want to understand
how Gleason's analysis turns into Kochen–Specker's finite puzzle, and what a human-readable argument
behind the computer bounds could look like.

Every fact above is sourced in [CLAIMS.md](CLAIMS.md).

## Status: pre-event setup

The Mathathon runs **13–15 November 2026**: 40 hours of learning, a presentation, then two months to
develop an alternative proof or exposition. Until the organizers confirm what preparation is allowed,
this repository contains **setup only**: the plan, the reading list, the claims ledger, the AI-use log
and a tool check. Nothing here attempts the problem yet. The commit history records exactly what was
prepared before the event.

## Layout

| Path | What it holds |
| --- | --- |
| [PLAN.md](PLAN.md) | The 40-hour plan, exercises, and the two-month options |
| [REFERENCES.md](REFERENCES.md) | Reading list with links, checked 29–30 September 2026 |
| [CLAIMS.md](CLAIMS.md) | Every factual claim we make, with its source or the script that checks it |
| [ai-log/](ai-log/) | LLM chat histories and what each was used for |
| [notes/](notes/) | Notes from the 40-hour sprint, one file per block |
| [src/](src/) | Code written during the event (coloring checker, embeddability tests) |
| [explainer/](explainer/) | The final explainer and interactive coloring game |
| [scripts/check_env.py](scripts/check_env.py) | Confirms the tools install and run |

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_env.py
```

The check confirms that NumPy, NetworkX, PySAT, Z3 and CVXPY import, and that the SAT solver
settles two abstract toy instances of the coloring rules (one colorable, one not). The toy
instances are not sets of vectors and say nothing about the problem itself.

## How we use AI

The Mathathon asks participants to disclose and justify all LLM use and to keep chat histories in the
repository. We follow three rules:

1. Every AI conversation is exported into [ai-log/](ai-log/) with a one-line note on what it was for.
2. No claim enters the explainer until a source we opened, or a script in this repository, backs it.
   [CLAIMS.md](CLAIMS.md) records which.
3. Computer-assisted results are labeled as such, with the code that produced them.

## License

MIT. See [LICENSE](LICENSE).

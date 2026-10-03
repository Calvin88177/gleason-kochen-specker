# Plan

The 40 hours end with a talk and a live demo: a coloring puzzle that cannot be solved, why Gleason's
theorem forces that, and why the smallest such puzzle in three dimensions (somewhere from 24 to 31
directions) is still unknown.

Two tracks run in parallel: **Track 1 (analysis)** follows Gleason's theorem and its consequences;
**Track 2 (puzzles)** follows the Kochen–Specker sets and the computer search.

## Hour 40: the talk and demo

The organizers have not announced a presentation format, so we plan for 10–15 minutes.

1. **The puzzle.** State the coloring rule and let the room try a small set of directions.
2. **The demo.** A SAT solver shows the 31-direction set cannot be colored; beside it, a valid
   coloring of every direction in dimension 2.
3. **Why it must fail.** Gleason's probabilities are continuous, so a 0/1 assignment on the connected
   sphere would be constant, and neither constant works. Compactness then yields a finite uncolorable
   set, with no bound on its size.
4. **The frontier.** 24 ≤ minimum ≤ 31. The 24 exists only as a machine search; the probabilistic
   method reaches 10.
5. **Our two months.** The direction chosen at hour 34.

## The 40 hours

| Hours | Track 1 (analysis) | Track 2 (puzzles) |
| --- | --- | --- |
| 0–4 | **A · Together:** frame functions, the coloring rule, why dimension 2 can be colored | (same) |
| 4–12 | **B · Gleason's proof:** Cooke–Keane–Moran; Bell's 1966 lemma on nearby directions | **B · Kochen–Specker as puzzles:** parity proof, magic square, Peres's 33 set; a PySAT checker for any set of directions |
| 12 | *Sync 1: each explains their block to the other* | |
| 12–20 | **C · From Gleason to a finite set:** continuity, connectedness, compactness; Busch's proof for POVMs | **C · Lower bounds by hand:** the probabilistic bound of 10; history of the bounds 18, 22, 24 |
| 20 | *Sync 2: where does the human proof stop and the machine start?* | |
| 20–28 | **D · Structure and realizability:** no 4-cycles, triangles, minimum degree 3; can an orthogonality graph be drawn? (Z3) | **D · Rerun the search, small sizes:** SAT encoding of the Li–Bright–Ganesh rules; check the 31-set, dropping one vector at a time |
| 28 | *Sync 3: compare what the search and the lemmas showed* | |
| 28–34 | **E · Together:** independence number vs Lovász theta, the KCBS pentagon, Yu–Oh's 13 rays; choose the two-month direction | (same) |
| 34–40 | **F · Together:** build the slides and the coloring demo, then one full dry run | (same) |

## Exercises by hand

The letter is the block; the track leads.

- [ ] **(A, both)** Color every direction in ℝ² so each orthogonal pair has exactly one 1, then do the
      same on the Bloch sphere for ℂ². This is why hidden values exist in dimension 2.
- [ ] **(B, Track 2)** Cabello's 18 vectors in ℝ⁴ form 9 bases, each vector in exactly two. Show no
      coloring exists by counting the 1s two ways.
- [ ] **(B, Track 2)** The Mermin–Peres square: show no ±1 assignment satisfies all six row and column
      constraints.
- [ ] **(B, Track 1)** Assume Gleason. Show there is no 0/1 assignment on the sphere in ℝ³: a continuous
      0/1 function on a connected set is constant, and neither constant sums to 1.
- [ ] **(C, Track 1)** Compactness: if every finite set of directions could be colored, so could the
      whole sphere. Conclude that a finite uncolorable set exists, with no bound on its size.
- [ ] **(C, Track 1)** Busch's version in dimension 2: why additivity over generalized measurements
      already forces the Born rule.
- [ ] **(C, Track 2)** Rework the probabilistic bound of 10 on paper, and find where it loses the most.
- [ ] **(D, Track 1)** In ℝ³, orthogonality graphs have no 4-cycles, and two orthogonal triples share at
      most one direction.
- [ ] **(D, Track 1)** In a smallest uncolorable set, every direction lies in an orthogonal triple and is
      orthogonal to at least three others.
- [ ] **(B–D, Track 2)** Build a PySAT checker, prove the 31-set uncolorable, then test whether removing
      any one direction makes it colorable. Coordinates: Peres's book or Kernaghan (2026).
- [ ] **(E, Track 2)** Compute α(C₅) = 2 and ϑ(C₅) = √5 numerically, and explain what the gap means for
      the KCBS test.

## Two months: the options

We pick one main direction at hour 34.

| Direction | What we would submit | Main risk |
| --- | --- | --- |
| A readable bound above 10 | A proof, checkable by hand, that every uncolorable set in ℝ³ has more than 10 directions | Gains may be small; any clean gain is new |
| Gleason → compactness → Kochen–Specker → the gap | The explainer: what each step keeps and what it loses | Must add something the existing reviews lack |
| The coloring game | A web page where the reader tries to color the 31-set, or Cabello's symmetric 33-set, and always fails | Low; its value is clarity |
| A certified check | A Lean proof, through a checked SAT certificate, that the 31-set cannot be colored | Tooling time |
| Moonshot: 30 or fewer | A search with Axplorer or SAT; a hit would refute the conjecture that 31 is the minimum | Most likely finds nothing |

## Before 13 November

- [ ] Ask the organizers: can a second teammate join, do the 40 hours happen at the event and may we
      read beforehand, and should we name our problem now.
- [ ] Update the application in the portal with the new problem.
- [ ] Install the tools and run `python scripts/check_env.py`.
- [ ] Split the reading list and agree on the notes format in [notes/](notes/).

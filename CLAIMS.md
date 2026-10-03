# Claims ledger

Every factual claim in this repository, with how it is backed. **Source** means a page we opened.
**Script** means code in this repository that checks it. Anything not in this table is not yet a claim.

Last checked: 3 October 2026.

| # | Claim | Backed by | Status |
| --- | --- | --- | --- |
| 1 | In dimension ≥ 3, probability measures on closed subspaces of a Hilbert space are given by the Born rule (Gleason) | Source: [Wikipedia: Gleason's theorem](https://en.wikipedia.org/wiki/Gleason%27s_theorem). Primary, not yet read: [Gleason 1957](http://www.iumj.indiana.edu/IUMJ/FULLTEXT/1957/6/56050) | Checked (secondary) |
| 2 | The POVM (generalized-measurement) version also applies in dimension 2 | Source: [Wikipedia: Gleason's theorem](https://en.wikipedia.org/wiki/Gleason%27s_theorem). Primary, not yet read: [Busch 2003](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.91.120403) | Checked (secondary) |
| 3 | An elementary proof of Gleason's theorem exists (Cooke, Keane, Moran 1985) | Library record: [Semantic Scholar](https://www.semanticscholar.org/paper/An-elementary-proof-of-Gleason%27s-theorem-Cooke-Keane/8b69582aa2c05db853ddf7d9beba9b1f94b6b4d1) | Not yet read |
| 4 | Kochen–Specker follows from Gleason plus logical compactness | Source: [Hrushovski & Pitowsky](https://arxiv.org/abs/quant-ph/0307139) abstract | Checked |
| 5 | The smallest known Kochen–Specker set in three dimensions has 31 vectors (Conway–Kochen, about 1990) | Source: [Li, Bright, Ganesh (IJCAI 2024)](https://www.ijcai.org/proceedings/2024/0210.pdf); [Kernaghan 2026](https://arxiv.org/abs/2603.16988) | Checked |
| 6 | Every Kochen–Specker set in three dimensions has at least 24 vectors, for both real and complex vectors | Source: [Li, Bright, Ganesh](https://www.ijcai.org/proceedings/2024/0210.pdf) | Checked |
| 7 | The bound of 24 was obtained independently by Kirchweger, Peitl and Szeider | Source: [Li, Bright, Ganesh](https://www.ijcai.org/proceedings/2024/0210.pdf); [Kernaghan 2026](https://arxiv.org/abs/2603.16988) | Checked |
| 8 | Earlier lower bounds: 18 (Arends, Ouaknine, Wampler) and 22 (Uijlen, Westerbaan, about 300 CPU cores for three months) | Source: [Li, Bright, Ganesh](https://www.ijcai.org/proceedings/2024/0210.pdf) | Checked |
| 9 | The DRAT certificates for order 23 total 40.3 TiB, checked for all orders up to 23 | Source: [Li, Bright, Ganesh](https://www.ijcai.org/proceedings/2024/0210.pdf) | Checked |
| 10 | The search pipeline uses the constraints: no 4-cycle, minimum degree 3, every vertex in a triangle, not 010-colorable; embeddability checked with Z3 | Source: [Li, Bright, Ganesh](https://www.ijcai.org/proceedings/2024/0210.pdf) | Checked |
| 11 | A probabilistic method gives a lower bound of 10, independent of graph structure | Source: [Williams & Constantin](https://arxiv.org/abs/2403.05230) abstract | Checked |
| 12 | Trandafir and Cabello argue the minimum is 31, assuming the minimal set is rigid and contains the minimal state-independent contextuality set | Source: [Trandafir & Cabello](https://arxiv.org/abs/2501.11640) | Checked |
| 13 | A March 2026 paper calls the 24–31 gap one of the central open problems in Kochen–Specker theory | Source: [Kernaghan 2026](https://arxiv.org/abs/2603.16988) | Checked |
| 14 | The smallest three-dimensional Kochen–Specker set containing the complete 25-ray state-independent contextuality set is Schütte's 33-ray set (exhaustive search) | Source: [Li, Bright, Trandafir, Cabello, Ganesh 2026](https://arxiv.org/abs/2604.19947) abstract | Checked |
| 15 | Cabello's symmetric 33-vector set in ℂ³ uses 14 bases (Conway–Kochen 31 uses 17; Peres 33 uses 16) | Source: [Cabello 2025](https://arxiv.org/abs/2508.07335) | Checked |
| 16 | The Kochen–Specker theorem fails in dimension 2 (every direction can be colored) | To be proved by hand: exercise A in [PLAN.md](PLAN.md) | Open |
| 17 | Our tools install and a SAT solver settles abstract toy instances of the coloring rules | Script: [scripts/check_env.py](scripts/check_env.py) | Checked |
| 18 | The Free Will Theorem (Conway and Kochen; Foundations of Physics 2006, Notices of the AMS 2009): from the axioms SPIN, TWIN and MIN, if experimenters can freely choose their measurement directions, a particle's response is not determined by the previous history of the universe | Source: [Conway & Kochen 2009](https://arxiv.org/abs/0807.3286); [Wikipedia: Free will theorem](https://en.wikipedia.org/wiki/Free_will_theorem) | Checked |
| 19 | Its proof uses Peres's 33 directions and shows that no "101 function" on them exists (the Kochen–Specker obstruction) | Source: [Conway & Kochen 2009](https://arxiv.org/abs/0807.3286) | Checked |
| 20 | Critique: for stochastic models the conclusion is not correct, and for deterministic models it is not new | Source: [Goldstein, Tausk, Tumulka, Zanghì 2010](https://arxiv.org/abs/0905.4641) abstract | Checked |
| 21 | Two-player games that entangled players always win and classical players cannot are equivalent to Kochen–Specker contradictions | Source: [Renner & Wolf 2004](https://crypto.ethz.ch/publications/RenWol04d.html) abstract | Checked |

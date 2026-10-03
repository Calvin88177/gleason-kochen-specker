# Code

Written during the event, not before. Planned pieces:

| Piece | Block | What it does |
| --- | --- | --- |
| Coloring checker | B | Takes a set of directions, builds the orthogonality graph (pairs and bases), and asks a SAT solver whether a 010-coloring exists |
| Structure tests | D | Checks the Li–Bright–Ganesh constraints on a graph: no 4-cycle, minimum degree 3, every vertex in a triangle |
| Embeddability | D | Asks Z3 whether an orthogonality graph can be realized by vectors in ℝ³ |
| Lovász theta | E | Computes ϑ of an exclusivity graph with CVXPY |

Every result produced here gets a line in [CLAIMS.md](../CLAIMS.md) pointing to the script.

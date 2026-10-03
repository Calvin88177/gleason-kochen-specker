"""Pre-event environment check.

Confirms that the tools import, and that a SAT solver settles two abstract toy instances of the
coloring rules used for Kochen-Specker sets:

    every basis (a set of mutually orthogonal elements) contains exactly one 1,
    no orthogonal pair contains two 1s.

The toy instances are abstract constraint systems, not sets of real vectors, and say nothing about
the problem itself.
"""
import importlib
import sys
from itertools import combinations

TOOLS = {"numpy": "numpy", "networkx": "networkx", "pysat": "python-sat", "z3": "z3-solver", "cvxpy": "cvxpy"}


def check_imports():
    ok = True
    for module, package in TOOLS.items():
        try:
            m = importlib.import_module(module)
            version = getattr(m, "__version__", None) or getattr(m, "get_version_string", lambda: "?")()
            print(f"  ok    {package:12s} {version}")
        except Exception as exc:  # report every missing tool, not just the first
            print(f"  MISSING {package:10s} ({exc.__class__.__name__}: {exc})")
            ok = False
    return ok


def coloring_clauses(bases, pairs):
    """CNF for the coloring rules. Elements are 0..n-1; variable i+1 means 'element i gets a 1'."""
    clauses = []
    for basis in bases:
        clauses.append([i + 1 for i in basis])                              # at least one 1
        clauses += [[-(a + 1), -(b + 1)] for a, b in combinations(basis, 2)]  # at most one 1
    clauses += [[-(a + 1), -(b + 1)] for a, b in pairs]
    return clauses


def colorable(bases, pairs):
    from pysat.solvers import Solver

    with Solver(name="glucose4", bootstrap_with=coloring_clauses(bases, pairs)) as solver:
        return solver.solve()


def check_solver():
    # Two bases sharing one element: colorable (give the shared element the 1).
    sat = colorable(bases=[(0, 1, 2), (2, 3, 4)], pairs=[])
    # Three two-element bases in a cycle: each element lies in exactly two bases and there is an odd
    # number of bases, so counting the 1s two ways gives a contradiction. Not colorable.
    unsat = not colorable(bases=[(0, 1), (1, 2), (2, 0)], pairs=[])
    print(f"  {'ok' if sat else 'FAIL':5s} toy instance 1 is colorable")
    print(f"  {'ok' if unsat else 'FAIL':5s} toy instance 2 is not colorable (parity)")
    return sat and unsat


if __name__ == "__main__":
    print(f"Python {sys.version.split()[0]}")
    print("Tools:")
    imports_ok = check_imports()
    print("SAT solver:")
    solver_ok = imports_ok and check_solver()
    print("All checks passed." if imports_ok and solver_ok else "Some checks failed; see above.")
    sys.exit(0 if imports_ok and solver_ok else 1)

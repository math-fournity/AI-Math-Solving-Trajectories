"""sep3d.py — exact rational separation toolkit for 3D lattice configurations.

Core question (Q): decide whether conv(A) ∩ conv(B) = ∅ for finite lattice sets,
with A = lattice points of a candidate tetrahedron, B = the rest.

Rigorous protocol — float LP only PROPOSES, both outcomes get independent exact
certificates (so a buggy LP or simplex can never fabricate an answer):
  YES side: proposed dir → exact Fraction copy → rescale so
            min_{a,b} <dir, a-b> >= 1, verify every pair exactly.
  NO  side: exact phase-1 simplex (Bland, Fractions) proves infeasibility;
            duals pi extracted from the tableau are verified exactly:
                pi >= 0,  Σ_i pi_i (a_i - b_i) = 0,  Σ_i pi_i > 0.
Any certificate failure raises AssertionError (never silent).
"""
from fractions import Fraction
import itertools

# ---------------------------------------------------------------- linear algebra

def dot(u, v):
    return sum(x * y for x, y in zip(u, v))

def sub(u, v):
    return tuple(x - y for x, y in zip(u, v))

def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

# ---------------------------------------------------------------- exact simplex

def _pivot_loop(T, basis, cost, ncols):
    """Bland-rule simplex on tableau T (rows m+1 incl. implicit obj tracked separately).
    Returns optimal objective value (sum c_B x_B)."""
    while True:
        m = len(T)
        cb = [cost[basis[i]] for i in range(m)]
        enter = -1
        for j in range(ncols):                      # reduced cost < 0, lowest index
            rc = cost[j] - sum(cb[i] * T[i][j] for i in range(m))
            if rc < 0:
                enter = j
                break
        if enter < 0:
            return sum(cb[i] * T[i][ncols] for i in range(m))
        leave, best = -1, None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][ncols] / T[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best, leave = ratio, i
        if leave < 0:
            raise AssertionError("unbounded in phase where bounded expected")
        p = T[leave][enter]
        T[leave] = [x / p for x in T[leave]]
        for i in range(len(T)):
            if i != leave and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [x - f * y for x, y in zip(T[i], T[leave])]
        basis[leave] = enter

def _row0(T, basis, cost, ncols):
    m = len(T)
    cb = [cost[basis[i]] for i in range(m)]
    return [cost[j] - sum(cb[i] * T[i][j] for i in range(m)) for j in range(ncols)]

def feasibility_lp(diffs, rhs=1):
    """Decide ∃ dir ∈ R^3 : <dir, diff_i> >= rhs for all i.
    Returns ('yes', dir_rationals) or ('no', farkas_pi).  Exact throughout."""
    k = len(diffs)
    # variables: d+ (3), d- (3), t (k surplus), art (k)
    n = 6 + 2 * k
    A, b = [], []
    for i, v in enumerate(diffs):
        row = [Fraction(x) for x in v] + [Fraction(-x) for x in v]
        row += [Fraction(0)] * k                 # room for t
        row[6 + i] = Fraction(-1)
        row += [Fraction(0)] * k                 # room for artificials
        row[6 + k + i] = Fraction(1)
        A.append(row)
        b.append(Fraction(rhs))
    # ---- phase 1
    cost1 = [Fraction(0)] * (6 + k) + [Fraction(1)] * k
    T = [A[i][:] + [b[i]] for i in range(k)]
    for i in range(k):
        T[i] = A[i][:] + [b[i]]
        T[i][6 + k + i] = Fraction(1)
    basis = [6 + k + i for i in range(k)]
    ncols1 = 6 + 2 * k
    obj1 = _pivot_loop(T, basis, cost1, ncols1)
    if obj1 > 0:
        pi = [Fraction(1) - r for r in _row0(T, basis, cost1, ncols1)[6 + k:]]
        return "no", tuple(pi)
    # ---- phase 2 (drop artificial columns; clean rows with basic artificials)
    k_keep = 6 + k
    T2rows = [r[:k_keep] + [r[-1]] for r in T]
    rows, basis2 = [], []
    for i, bc in enumerate(basis):
        if bc < k_keep:
            rows.append(T2rows[i]); basis2.append(bc)
        else:
            # artificial still basic; obj1 = 0 ⇒ its value (rhs) is 0.
            pivoted = False
            for j in range(k_keep):
                if T2rows[i][j] != 0:
                    p = T2rows[i][j]
                    newr = [x / p for x in T2rows[i]]
                    for r2 in range(len(rows)):
                        f = rows[r2][j]
                        if f != 0:
                            rows[r2] = [x - f * y for x, y in zip(rows[r2], newr)]
                    rows.append(newr); basis2.append(j)
                    pivoted = True
                    break
            if not pivoted:
                assert all(x == 0 for x in T2rows[i]), "inconsistent row with basic artificial"
    T2 = rows
    cost2 = [Fraction(0)] * k_keep
    obj2 = _pivot_loop(T2, basis2, cost2, k_keep)
    assert obj2 == 0
    x = [Fraction(0)] * k_keep
    for i, bc in enumerate(basis2):
        x[bc] = T2[i][-1]
    d = (x[0] - x[3], x[1] - x[4], x[2] - x[5])
    gaps = [dot(d, v) for v in diffs]
    mn = min(gaps)
    if mn > 0:
        d = tuple(z / mn for z in d)
        assert min(dot(d, v) for v in diffs) >= 1
        return "yes", d
    raise AssertionError("phase-2 claims feasible but min gap = %s" % mn)

def separator_exists_exact(Apts, Bpts):
    """conv(A) ∩ conv(B) = ∅ ?  Certified both ways.
    Returns (True, dir) or (False, farkas_pi)."""
    diffs = [sub(a, b) for a in Apts for b in Bpts]
    if not Apts or not Bpts:
        return True, None                          # vacuous side ⇒ separable
    import numpy as np
    from scipy.optimize import linprog
    Mf = np.array([[float(x) for x in v] for v in diffs])
    res = linprog(c=[0.0, 0.0, 0.0], A_ub=-Mf, b_ub=[-1.0] * len(diffs),
                  bounds=[(None, None)] * 3, method="highs")
    if res.status == 0:
        d = tuple(Fraction(float(z)) for z in res.x)
        gaps = [dot(d, v) for v in diffs]
        mn = min(gaps)
        if mn > 0:
            d = tuple(z / mn for z in d)
            assert min(dot(d, v) for v in diffs) >= 1, "exact verify failed"
            return True, d
    elif res.status != 2:
        pass                                       # numerical trouble → exact path
    verdict, cert = feasibility_lp(diffs)
    if verdict == "yes":
        return True, cert
    pi = cert
    k = len(diffs)
    assert all(y >= 0 for y in pi), "farkas negative"
    for j in range(3):
        s = sum((pi[i] * diffs[i][j] for i in range(k)), Fraction(0))
        assert s == 0, f"farkas combination coord {j} = {s}"
    assert sum(pi) > 0, "farkas degenerate"
    return False, tuple(pi)

# ---------------------------------------------------------------- lattice geometry

def lattice_points_in_tetra(tetra, pts):
    """Exact barycentric membership.  Returns list, or None if degenerate."""
    p0, p1, p2, p3 = tetra
    M = [[p1[j] - p0[j] for j in range(3)],
         [p2[j] - p0[j] for j in range(3)],
         [p3[j] - p0[j] for j in range(3)]]
    D = det3(M)
    if D == 0:
        return None
    inside = []
    for q in pts:
        rx, ry, rz = (q[0] - p0[0], q[1] - p0[1], q[2] - p0[2])
        l1 = det3([[rx, M[1][0], M[2][0]], [ry, M[1][1], M[2][1]], [rz, M[1][2], M[2][2]]]) / D
        l2 = det3([[M[0][0], rx, M[2][0]], [M[0][1], ry, M[2][1]], [M[0][2], rz, M[2][2]]]) / D
        l3 = det3([[M[0][0], M[1][0], rx], [M[0][1], M[1][1], ry], [M[0][2], M[1][2], rz]]) / D
        if l1 >= 0 and l2 >= 0 and l3 >= 0 and l1 + l2 + l3 <= 1:
            inside.append(q)
    return inside

def hull_planes(pts):
    """Outward supporting planes {(nv, dd)} with nv·x <= dd ∀x ∈ pts."""
    from math import gcd
    def prim(v):
        g = 0
        for x in v:
            g = gcd(g, abs(x))
        return tuple(x // g for x in v) if g else tuple(v)
    planes = {}
    np_ = len(pts)
    for i in range(np_):
        for j in range(i + 1, np_):
            for k2 in range(j + 1, np_):
                u = sub(pts[j], pts[i]); w = sub(pts[k2], pts[i])
                nv = (u[1] * w[2] - u[2] * w[1],
                      u[2] * w[0] - u[0] * w[2],
                      u[0] * w[1] - u[1] * w[0])
                if nv == (0, 0, 0):
                    continue
                dd = dot(nv, pts[i])
                if all(dot(nv, p) <= dd for p in pts):
                    planes[(prim(nv), dd)] = (nv, dd)
                elif all(dot(nv, p) >= dd for p in pts):
                    nn = (-nv[0], -nv[1], -nv[2])
                    planes[(prim(nn), -dd)] = (nn, -dd)
    return list(planes.values())

def close_config(S):
    """Lattice closure: grid points of bounding box inside conv(S), S included."""
    pts = sorted(set(S))
    lo = [min(p[i] for p in pts) for i in range(3)]
    hi = [max(p[i] for p in pts) for i in range(3)]
    planes = hull_planes(pts)
    L = set()
    for x in range(lo[0], hi[0] + 1):
        for y in range(lo[1], hi[1] + 1):
            for z in range(lo[2], hi[2] + 1):
                q = (x, y, z)
                if all(dot(nv, q) <= dd for nv, dd in planes):
                    L.add(q)
    return frozenset(L)

# ---------------------------------------------------------------- master oracle

def config_is_yes(L, sample=None, seed=12345, max_checks=None):
    """Does L admit a full-dim lattice tetrahedron whose lattice points are
    strictly separable from the rest (conv vs conv)?  Early exit on first hit."""
    pts = sorted(L)
    n = len(pts)
    tetras = list(itertools.combinations(range(n), 4))
    if sample is not None and len(tetras) > sample:
        import random
        tetras = random.Random(seed).sample(tetras, sample)
    checked = 0
    for (i, j, k2, l) in tetras:
        tet = (pts[i], pts[j], pts[k2], pts[l])
        Alist = lattice_points_in_tetra(tet, pts)
        if Alist is None:
            continue
        Aset = set(Alist)
        Blist = [p for p in pts if p not in Aset]
        if not Blist:
            return True, {"tetra": tet, "cert": "trivial", "checked": checked}
        ok, cert = separator_exists_exact(sorted(Aset), Blist)
        checked += 1
        if ok:
            return True, {"tetra": tet, "cert": cert, "checked": checked}
        if max_checks is not None and checked >= max_checks:
            return None, {"timeout": checked}
    return False, {"all_failed": checked}

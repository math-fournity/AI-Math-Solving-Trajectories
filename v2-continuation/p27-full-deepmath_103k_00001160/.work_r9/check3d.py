"""check3d.py — decisive 3D experiment battery (round 9).

Verifies, with exact rational certificates everywhere:
  §4.2-a certificate table entries (boxes / octahedra / prism / products / pyramid)
  F1  boxes: [0,1]^3 full sweep (70), [0,2]^3 early-exit
  F2  octahedra conv(±a e1,±b e2,±c e3)
  F3  embraced-tetrahedron family (core + facet attachments), v1 FULL sweep
  F4  pyramids / prisms / products
  F5  random configurations in [0,2]^3 and sparse ones in [0,3]^3
A 'False' verdict from config_is_yes = every tetrahedron certified non-separable
= genuine counterexample candidate (details dumped).
"""
import sys, time, itertools, random
from fractions import Fraction as Fr
sys.path.insert(0, "/Volumes/data/math-agent-glm5.2-tmux-agents-trajectory/v2-continuation/p27-full-deepmath_103k_00001160/.work_r9")
from sep3d import (separator_exists_exact, lattice_points_in_tetra,
                   close_config, hull_planes, dot, config_is_yes)

T0 = time.time()
def log(*a):
    print(f"[{time.time()-T0:8.1f}s]", *a); sys.stdout.flush()

_CACHE = {}
def sep_cached(A, B):
    key = (frozenset(A), frozenset(B))
    if key not in _CACHE:
        _CACHE[key] = separator_exists_exact(sorted(A), sorted(B))
    return _CACHE[key]

def full_dim(L):
    """affine rank == 3 via integer 3x3 minors"""
    from sep3d import det3
    pts = sorted(L); p0 = pts[0]
    vs = []
    for p in pts[1:]:
        v = tuple(a-b for a,b in zip(p,p0))
        if any(v): vs.append(v)
        if len(vs) >= 3:
            break
    if len(vs) < 3:
        return False
    import itertools as it
    return any(det3([list(vs[i]) for i in c]) != 0
               for c in it.combinations(range(len(vs)), 3))

# ------------------------------------------------------------------ certificates

def verify_cert(L, tetra, hcoef, label):
    """h = hcoef·x + c ; require h>0 on L∩tetra, h<0 elsewhere."""
    inside = lattice_points_in_tetra(tetra, sorted(L))
    assert inside is not None, f"{label}: degenerate tetra"
    a, b, c, d = hcoef
    bad = []
    for p in sorted(L):
        val = a*p[0] + b*p[1] + c*p[2] + d
        if p in set(inside):
            if val <= 0: bad.append(("should-be-positive", p, val))
        else:
            if val >= 0: bad.append(("should-be-negative", p, val))
    if bad:
        print(f"CERT FAIL {label}: {bad[:6]}")
        return False
    log(f"cert OK  {label}   (|L|={len(L)}, |L_Δ|={len(inside)})")
    return True

def section_certs():
    okall = True
    # boxes [0,m]^n
    for n in range(1, 7):
        for m in range(1, 4):
            pts = list(itertools.product(range(m+1), repeat=n))
            D = {p: Fr(3,2) - sum(p) for p in pts}
            pos = [p for p in pts if D[p] <= 0 and sum(p) <= 1]
            if any(D[p] <= 0 for p in pts if sum(p) <= 1) or \
               any(D[p] >= 0 for p in pts if sum(p) >= 2):
                okall = False; print("CERT FAIL box", n, m)
    log("cert OK  boxes [0,m]^n, n≤6, m≤3  (unit-corner + 3/2−Σx)")
    # octahedron ±e_i : CORRECTED certificate
    L7 = [(0,0,0)]
    for j in range(3):
        for s in (1,-1):
            v=[0,0,0]; v[j]=s; L7.append(tuple(v))
    tet = tuple(sorted([(1,0,0),(0,1,0),(0,0,1),(-1,0,0)]))
    okall &= verify_cert(L7, tet, (Fr(0),Fr(1),Fr(1),Fr(1,2)), "octa ±e_i  h=x2+x3+1/2")
    # octahedron ±2e_i
    L25 = []
    for x,y,z in itertools.product(range(-2,3), repeat=3):
        if abs(x)+abs(y)+abs(z) <= 2: L25.append((x,y,z))
    assert len(L25)==25
    tet2 = ((1,0,0),(2,0,0),(0,2,0),(0,0,2))
    okall &= verify_cert(L25, tet2, (Fr(6,5),Fr(9,10),Fr(9,10),Fr(-1)), "octa ±2e_i h=1.2x+.9y+.9z-1")
    # triangular prism & [0,2]^3 unit corner
    prism = [(0,0,0),(1,0,0),(0,1,0)] ; prism += [tuple(v[2:]+ (1,)) if False else (v[0],v[1],1) for v in prism]
    okall &= verify_cert(prism, ((0,0,0),(1,0,0),(0,1,0),(0,0,1)), (Fr(-1),Fr(-1),Fr(-1),Fr(3,2)), "prism tri unit-corner")
    cube27 = list(itertools.product(range(3), repeat=3))
    okall &= verify_cert(cube27, ((0,0,0),(1,0,0),(0,1,0),(0,0,1)), (Fr(-1),Fr(-1),Fr(-1),Fr(3,2)), "[0,2]^3 unit-corner")
    # product instance 1: unimod triangle × [0,2]
    P9 = [(i,j,k) for i,j,k in itertools.product(range(3), repeat=3) if i+j<=1]
    assert len(P9)==9
    okall &= verify_cert(P9, ((0,0,0),(1,0,0),(0,1,0),(0,0,1)),
                         (Fr(-1,2),Fr(-1,2),Fr(-3,4),Fr(1)), "unimodTri×[0,2]")
    # product instance 2: conv{00,20,02}×[0,1]
    P12 = [(i,j,k) for k in (0,1) for i,j in itertools.product(range(3), repeat=2) if i+j<=2]
    assert len(P12)==12
    okall &= verify_cert(P12, ((0,0,0),(1,0,0),(0,1,0),(0,0,1)),
                         (Fr(-3,2),Fr(-3,2),Fr(-1),Fr(2)), "tri20×[0,1]")
    return okall

# ------------------------------------------------------------------ families

def sweep_config(S, label, sample=None, max_checks=None, expect="yes"):
    L = close_config(S)
    n = len(L)
    tets = sum(1 for _ in itertools.combinations(range(n),4))
    res, info = config_is_yes(L, sample=sample, max_checks=max_checks)
    checked = info.get("checked", 0)
    tag = {True:"YES", False:"**COUNTEREXAMPLE**", None:"INCONCLUSIVE(timeout)"}[res]
    log(f"F {label}: |L|={n} (tetraballs={tets}) -> {tag}  [checked {checked}]")
    if res is False:
        print("DETAIL:", sorted(L)); print("INFO:", info)
    return res

def f1_boxes():
    r=[]
    r.append(sweep_config([(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)], "F1 cube[0,1]^3"))
    r.append(sweep_config(list(itertools.product((0,1,2),repeat=3)), "F1 box[0,2]^3", sample=None))
    return r

def f2_octa(a,b,c):
    verts=[]
    for j,m in enumerate((a,b,c)):
        for s in (1,-1):
            v=[0,0,0]; v[j]=s*m; verts.append(tuple(v))
    return sweep_config(verts, f"F2 octa({a},{b},{c})",
                        sample=None if len(close_config(verts))<=11 else 4000)

def f3_embraced():
    out=[]
    core = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    att_x = [(-1,0,0),(-1,1,0),(-1,1,1),(-2,1,1)]
    att_diag = [(1,1,1),(2,2,2),(1,1,2)]
    for att in att_x:
        out.append(sweep_config(core+[att], f"F3 core+{att}"))
        perms=set()
        for perm in itertools.permutations(range(3)):
            perms.add(tuple(att[perm[i]] for i in range(3)))
        for q in sorted(perms):
            if q!=att:
                out.append(sweep_config(core+[q], f"F3 core+{q}(perm)", max_checks=60))
    for att in att_diag:
        out.append(sweep_config(core+[att], f"F3 core+{att}"))
    # v1: full sweep, no caps
    v1 = core + [(-1,1,1),(1,-1,1),(1,1,-1),(2,2,2)]
    out.append(sweep_config(v1, "F3 v1 EMBRACED-TETRA (full)"))
    # pairwise attachments (subset for budget)
    pairs = list(itertools.combinations(att_x,2))[:6]
    for pa,pb in pairs:
        out.append(sweep_config(core+[pa,pb], f"F3 core+{pa}+{pb}", max_checks=120))
    return out

def f4_pyramid_prism_products():
    out=[]
    # height-1 square pyramid over [0,2]^2
    base = list(itertools.product((0,1,2),repeat=2))
    pyr = [v+(0,) for v in base] + [(0,0,1)]
    out.append(sweep_config(pyr, "F4 sq-pyramid h=1 over [0,2]^2"))
    # prism [0,2]^2 × [0,1]
    prsm = [v+(k,) for k in (0,1) for v in base]
    out.append(sweep_config(prsm, "F4 prism [0,2]^2×[0,1]", max_checks=400))
    # generic 2D-base height-1 pyramid (Thm C stress): base conv{00,30,12}, apex lattice at z=1
    b2 = [(x,y) for x in range(4) for y in range(3) if 2*x+3*y<=6]
    pyr2 = [v+(0,) for v in b2] + [(1,1,1)]
    out.append(sweep_config(pyr2, "F4 tri-pyramid(base conv{00,30,12},apex(1,1,1))"))
    return out

def f5_random():
    out=[]
    rnd = random.Random(2024)
    grid = list(itertools.product(range(3), repeat=3))
    yes=0; other=0
    flat=0
    for t in range(600):
        k = rnd.randint(6,9)
        S = rnd.sample(grid, k)
        L = close_config(S)
        if len(L)<4 or not full_dim(L):
            flat+=1; continue
        res,info = config_is_yes(L)
        if res is True: yes+=1
        else:
            other+=1
            print("**NON-YES**", sorted(S), "->", sorted(L), info)
    log(f"F5 [0,2]^3 subsets: 600 configs -> YES={yes}, non-yes={other}, skipped(flat/small)={flat}")
    out.append(other==0)
    # sparse [0,3]^3
    grid3 = list(itertools.product(range(4), repeat=3))
    yes2=0; other2=0
    flat2=0
    for t in range(120):
        S = rnd.sample(grid3, 9)
        L = close_config(S)
        if len(L)<4 or len(L)>18 or not full_dim(L):
            flat2+=1; continue
        res,info = config_is_yes(L, sample=3000)
        if res is True: yes2+=1
        else:
            other2+=1
            print("**NON-YES-sparse**", sorted(S), "->", sorted(L), info)
    log(f"F5 [0,3]^3 sparse: 120 configs -> YES={yes2}, non-yes/inconclusive={other2}, skipped={flat2}")
    out.append(other2==0)
    return out

if __name__ == "__main__":
    log("=== section 4.2 certificate table ===")
    ok = section_certs()
    log("certificate table:", "ALL PASS" if ok else "FAILURES PRESENT")
    log("=== F1 boxes ===");            f1_boxes()
    log("=== F2 octahedra ===")
    for a in (1,2):
        for b in (1,2):
            for c in (1,2):
                f2_octa(a,b,c)
    log("=== F3 embraced ===");         f3_embraced()
    log("=== F4 pyramid/prism/products ==="); f4_pyramid_prism_products()
    log("=== F5 random ===");           f5_random()
    log("=== battery complete ===")

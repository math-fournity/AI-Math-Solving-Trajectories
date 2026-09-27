Let me start by reading the analysis notes file to understand the problem state.Let me understand the situation:

1. This is round 9 of a multi-round AI relay solving a math problem.
2. The analysis notes say rounds 1, 3, 5, 7 were solver rounds that all died on budget with zero files written.
3. Round 8 (observer) has digested everything into 分析笔记.md.
4. My job: continue the proof from the frontier.

Key tasks per the notes (Section 4):
1. **First action: Write proof.md to disk immediately** following the §2.6 plan structure. Content is all in the notes + round 6 notes §2.1. Then write enum2d.py and check3d.py per specs in 2.4/2.5. **Save each file immediately after completing it**.
2. **Second action: Run decisive experiments**. Cheap items first: F1 m=1 (70 checks), F3 v1 member (495 FM checks), F5 random family.
3. **Theory closure (parallel)**: attack the weighted-sum criterion adversarial point for D≥3 cones; possibly enumerate D=2,3 primitive triples for 3-point cone experiments.

The problem statement (from Section 1):

Given a convex lattice polytope $P \subset \mathbb{R}^n$, question: does there always exist a full-dimensional lattice simplex $\Delta \subseteq P$ and a linear (affine) polynomial $h$ such that $h>0$ on all lattice points of $\Delta$, and $h<0$ on all lattice points of $P\setminus\Delta$. Equivalent form (Q): there exists a full-dimensional lattice simplex $\Delta$ such that $\mathrm{conv}(L_\Delta) \cap \mathrm{conv}(L \setminus L_\Delta) = \varnothing$, where $L_\Delta = \Delta \cap L$.

Wait, I need to be careful about the exact problem. Let me re-read.

"给定凸格点多面体 $P \subset \mathbb{R}^n$，问：是否总存在满维格单纯形 $\Delta \subseteq P$ 和一次多项式 $h$，使 $h>0$ 于 $\Delta$ 的所有整点、$h<0$ 于 $P\setminus\Delta$ 的所有整点。等价形式（Q）：存在满维格单纯形 $\Delta$ 使 $\mathrm{conv}(L_\Delta) \cap \mathrm{conv}\big(L\setminus L_\Delta\big) = \varnothing$，$L_\Delta=\Delta\cap L$。"

So: Given a convex lattice polytope P, is it always true that there exists a full-dimensional lattice simplex Δ ⊆ P and an affine function h with h > 0 on all integer points of Δ and h < 0 on all integer points of P \ Δ?

The answer status:
- n=1: always YES (proven round 1)
- n=2: always YES (proven, transcription-level text in round 6 notes §2.1)
- n≥3: open (no counterexample found; all verified families are YES)

The boxed answer (honest version): "$n=1,2$ 恒 YES（已证）；$n\ge3$ 开放（未找到反例，已验证族均 YES）"

So the final deliverable is a proof.md containing:
- §0: problem statement + Lemma 0 (separable ⟺ island-simplex, with equivalence proof)
- §1: Thm A (2D always YES — transcribe from round 6 notes §2.1)
- §2: Thm B/C/D + computational verification section + boxed answer
- Computational verification section: run the code and fill in results

Important: I need to read round 6 notes §2.1 for the 2D proof. Where is it? The notes say "誊写级文本在轮6笔记第2.1节". The round 6 observer notes should be in `../.work_r6/rounds/round6/` or similar. Let me check the directory structure.

Actually the notes say: "各轮原始流不在 `rounds/roundN/` 下，而在兄弟目录 `../.work_rN/rounds/roundN/{thoughts.jsonl,thinking.md,meta.json}`；`rounds/roundN/` 只存观察者交接笔记。"

So observer handoff notes are in `rounds/roundN/` (relative to... hmm, the working directory?). Let me look at the current directory structure first.

My plan:
1. Look at the working directory to find files (round 6 notes).
2. Read round 6 notes §2.1 (the 2D proof transcription).
3. Write proof.md immediately (following §2.6 plan).
4. Write enum2d.py and check3d.py, run them.
5. Fill in computational verification results in proof.md.
6. Also work on the theory frontier: weighted-sum criterion for D≥3 deep singular corners — enumerate D=2,3 primitive triples, do 3-point cone experiments.
7. Write 工作笔记.md as I go (append after each reasoning block).

Let me start by exploring the directory.Let me look at the round 6 notes (observer handoff notes) which contain the 2D proof transcription in §2.1.Now I have the complete picture. Let me set up a task list and start working.

Plan (per Section 4 of round 8 notes):
1. **First action: Write proof.md immediately** following §2.6 plan:
   - §0: problem statement + Lemma 0 (separable ⟺ island-simplex with equivalence proof)
   - §1: Thm A (n=1 YES + 2D always YES — transcribe from round 6 notes §2.1, plus n=1 prefix segment argument from round 1)
   - §2: Thm B/C/D + computational verification section + boxed answer
2. Write enum2d.py and check3d.py per specs in 2.4/2.5. Save each file immediately.
3. Run decisive experiments: F1 m=1 (70 checks), F3 v1 member (495 FM checks), F5 random family.
4. Theory: attack weighted-sum criterion for D≥3 cones; enumerate D=2,3 primitive triples for 3-point cone experiments.
5. Append to 工作笔记.md after each reasoning block.
6. Fill in computational verification results into proof.md.

I need the n=1 proof too. From the notes: "n=1 恒 YES | 已证（轮次1） | 前缀段论证". I don't have the exact text but I can reconstruct: For P = [a,b] interval with lattice points L = {integers in [a,b]}. Take Δ = [m, m+1] where... hmm wait, full-dimensional lattice simplex in 1D is a segment [u,v] containing at least 2 lattice points? Actually "满维格单纯形" in 1D means an interval with nonempty interior containing lattice points. The condition h>0 on lattice points of Δ, h<0 on lattice points of P\Δ.

Prefix segment argument: take Δ = [min, min+1]? Hmm, let me think. Actually let me reconstruct: P ⊂ R, convex lattice polytope = closed interval with integer endpoints. L = Z ∩ P. We want Δ ⊆ P a "full-dimensional lattice simplex" (non-degenerate segment containing ≥2 lattice points), and affine h (= ax+b) with h>0 on L_Δ and h<0 on L\L_Δ.

Simple construction: Let L = {k, k+1, ..., K}. Take Δ = [K-1, K] (the last two points). Then L_Δ = {K-1, K}, complement = {k,...,K-2}. h(x) = x - (K-1) + ε... wait need h>0 at both K-1 and K, h<0 elsewhere. h(x) = x-(K-3/2): at K-1: 3/2>0, at K: 5/2 >0; at x ≤ K-2: ≤ -1/2 <0. Yes! So Δ=[K-1,K], h(x)=x-K+3/2. Works for |L|≥2. If |L|=1... P is a single point? A convex lattice polytope that's full-dim... in R^1 a polytope is an interval [a,b]; if it contains only one lattice point, e.g., [0.5, 0.7]? Hmm, but lattice polytope usually means vertices are lattice points! Wait — 凸格点多面体 = convex lattice polytope, which standardly means vertices ∈ Z^n. If vertices are lattice points then [a,b] with integer endpoints has |L| = b-a+1 ≥ 2. OK so n=1 always works trivially.

Hmm wait, actually there's subtlety about what "格点多面体" means here — vertices are lattice points presumably (round notes say "P=conv(L)" in the 2D proof step 1: "首先注意 $P=\mathrm{conv}(L)$（顶点是格点）"). Good.

But wait — in higher dimensions, if P is not full-dimensional itself? E.g., P lies in a hyperplane. The problem says "满维格单纯形 Δ ⊆ P" — requires full-dimensional simplex inside P, so P must be full-dimensional for YES. Presumably the problem assumes P is full-dimensional, or answer is NO for lower-dim P. The rounds have treated P as full-dimensional implicitly. I'll state the assumption in proof.md: assume P is n-dimensional (else no full-dimensional simplex exists and the property fails vacuously/trivially NO). Actually let me be careful: the question asks "是否总存在" — does there ALWAYS exist. If P is contained in a hyperplane, there's no full-dim simplex inside P, so such P would be a counterexample. But that's degenerate; the intended problem surely assumes P full-dimensional. Round 1 "退化低维单纯形使问题平凡为真，故必须满维" — degenerate simplices make it trivially true, hence must require full-dimensional. I'll note the assumption: P full-dimensional convex lattice polytope.

Also the equivalence Lemma 0: existence of (Δ, h) ⟺ conv(L_Δ) ∩ conv(L \ L_Δ) = ∅.

Proof direction 1: Given h with h>0 on L_Δ, h≤0... wait h<0 on L\L_Δ. Since h is affine, h>0 on conv(L_Δ) and h<0 on conv(L\L_Δ), so the two convex hulls are separated by the hyperplane {h=0}, hence disjoint.

Direction 2: Suppose conv(A) ∩ conv(B) = ∅ where A = L_Δ, B = L\A, both finite sets. By the strict separation theorem for disjoint compact convex sets, there's an affine function h with h>0 on conv(A), h<0 on conv(B). 

So Lemma 0 holds. Note this makes the property purely combinatorial-geometric on the point set L: it depends only on whether some simplex-lattice-point-set can be strictly separated.

Now Thm B: boxes [0,m]^n all dims. Δ = unit corner simplex conv(0,e1,...,en), h = 3/2 − Σx_i. Check: L_Δ = {0, e1,...,en} (unit simplex is unimodular, contains exactly those lattice points). h(0)=3/2>0, h(e_i)=1/2>0. Any other lattice point in box has Σx_i ≥ 2, h ≤ −1/2 < 0. And all these points are in P. ✓.

Thm C: height-1 pyramid. Base B ⊆ {z=0} lattice polytope (dimension n−1) with winning pair (τ, g) — τ simplex in base, g affine cert. P = conv((B×{0}) ∪ {(a,1)}) with apex lattice point at height exactly 1. Then P is YES.

Wait — careful: apex (a,1) where a is a lattice point in z=0 plane. The lattice layers intersecting P: z=0 layer and z=1 layer. Points at z=1: only those in P∩{z=1} = {(a,1)}? Is that right? P = conv(B×{0} ∪ {(a,1)}). Cross-section at height z=t is conv((B×{0}) ∪ {(a,1)}) ∩ {z=t} = conv(((1−t)(B×{1}) ... hmm, standard: cross-section at t ∈ [0,1] equals conv( ((1−t)·B + t·a) × {t} )? Let me verify: point of P at height t is (1−s)(b,0)+s(a,1) = ((1−s)b + sa, s), so s=t, giving ((1−t)b + ta, t), b ∈ B. At t=1: just (a,1). ✓. So z=1 layer contains exactly {(a,1)}. 

Take Δ = conv((τ×{0}) ∪ {(a,1)}) — full-dim simplex (apex off the base plane, τ full-dim in base). L_Δ = L_τ ∪ {(a,1)}.

Certificate: h = g̃ + εz where g̃ any affine extension of g (g defined on z=0 plane; extend affinely, e.g., g̃(x,z) = g(x)). On L_τ: h = g > 0 ✓. On (a,1): h = g(a) + ε > ? Need g(a) + ε > 0. Hmm — the notes say "apex 得 μh(a)>0". But is g(a)>0 guaranteed?? Not necessarily! a might be a foreign point of the base pair, i.e., g(a)<0 possibly!

Hmm wait. Let me re-read the note: "证书 $h=\tilde g+\varepsilon z$（$\tilde g$ 为 $g$ 的任意仿射延拓，$\varepsilon>0$ 小）：$\tau$ 内点得 $\nu g>0$，apex 得 $\mu h(a)>0$；帽外点 $z=0$ 上由 $g<0$，$z$ 无其他取值。"

So they need g(a) + ε > 0 at apex AND g < 0 at foreign points of base. If a is a foreign point of the base configuration with g(a) very negative, we need ε > −g(a), but then foreign points with z=0 get h=g̃<0 fine (ε doesn't matter since they're at z=0!). Wait — foreign base points have z=0, so h = g̃ + 0 = g̃ < 0 regardless of ε. And apex gets g(a)+ε. So choose ε > max(0, −g(a)) — small enough? There's no upper constraint from base points since they don't see z... but wait, are there other points at intermediate heights? No—only layers z=0,1 exist. Points of P∩L: L_B × {0} plus possibly (a,1) only at top. So:

- L_Δ = (L_τ × {0}) ∪ {(a,1)}
- Foreign: (L_B \ L_τ) × {0}

h = g̃ + εz with ε > max(0, −g(a)):
- On L_τ×{0}: h = g > 0 ✓
- Apex: h(a,1) = g(a) + ε > 0 ✓
- Foreign: h = g̃(b,0) = g(b) < 0 ✓

No upper bound on ε needed! Great, so Thm C is clean and unconditional given the base pair (τ,g). Actually even simpler: could also use ε large. Fine.

Hmm wait, one more check: are ALL lattice points of P captured by (L_B×{0}) ∪ {(a,1)}? P∩{z=0} = B (since cross-section at t=0 is B). P∩{z=1} = {(a,1)}. Yes since P ⊆ {0 ≤ z ≤ 1}. ✓

Thm C for 3D: base is 2D polygon, 2D always YES unconditionally → all height-1 pyramids over 2D lattice polygons are YES. For n≥4 conditional on IH(n−1).

Thm D: product Q×[0,m]. Base Q ⊆ R^{n−1} with winning pair (τ,g), τ = conv(u,v,w) (for 2D base). P = Q×[0,m]. Layers z=0..m.

Construction for m=1 ("tent"): Δ = conv((u,0),(v,0),(w,0),(u,1)), h = g + ε(1−z), ε < m₀ where m₀ := min over foreign base points of (−g) = −max_{foreign} g > 0. Checks:
- L_Δ: lattice points of tent. Tent cross-sections: at height t∈[0,1]: conv((1−t)τ + t·u) — scaled copy of τ anchored at u. Hmm, does the tent contain extra lattice points beyond its 4 vertices? Possibly! E.g. if τ contains interior lattice points or the scaled sections hit lattice points. Hmm. The notes say "$\Delta\cap L=\{...\}$"... actually the notes say for the tent "帐篷 $\Delta=\mathrm{conv}((u,0),(v,0),(w,0),(u,1))$，证书 $h=g+\varepsilon(1-z)$".

Hold on — do we need L_Δ to be exactly the vertices? No! We need h>0 on ALL lattice points OF Δ, whatever they are. The certificate must be positive on every lattice point inside Δ. So let me redo: any lattice point p=(x,t) in tent: h(p) = g(x) + ε(1−t). Problem: x ∈ section conv((1−t)τ + tu). Is g(x) possibly negative there? g>0 on L_τ but g could be negative elsewhere in τ (e.g., interior lattice points of τ with negative g!). Hmm wait, but actually g>0 on all of conv(L_τ)? No — g>0 on the lattice points L_τ; as an affine function, g>0 on conv(L_τ) iff g>0 at all vertices, which holds! Affine function attains min over a polytope at vertices. g>0 at u,v,w ⟹ g>0 on τ. ✓ So for x in the section at height t: x = (1−t)y + t·u with y∈τ ⟹ g(x) = (1−t)g(y) + t·g(u) > 0. So h(p) = g(x) + ε(1−t) > 0 automatically. ✓ All lattice points in the tent are positive. 

Foreign points (x,t) ∉ Δ: need h < 0. If x ∉ Q's lattice... x is lattice point of Q (base lattice). Cases:
- x ∈ L_Q \ L_τ (foreign base): g(x) < 0. h = g(x) + ε(1−t) ≤ g(x) + ε < 0 iff ε < −g(x) for all foreign x, i.e., ε < m₀ = min_{foreign}(−g).
- x ∈ L_τ but (x,t) ∉ tent: possible? The tent at height t contains section S_t = conv((1−t)τ + tu). Is L_τ × {t} ⊆ tent for all t? Point (y,t) with y∈τ: y ∈ S_t iff y = (1−t)z + t·u for some z ∈ τ iff y ∈ (1−t)τ + tu =: S_t. S_t is τ shrunk toward u. y near the opposite face (vw side) won't be in S_t. E.g., y=w: w ∈ S_t iff w = (1−t)z + tu, i.e., z = (w − tu)/(1−t); for t>0 this needs z outside... z = ((1-t)w + t(w−u))/(1−t)... hmm let me just compute: w − tu = w − t·u; divide by (1−t): coefficients: w coefficient 1/(1−t) > 1 when t>0, so z ∉ τ for t ∈ (0,1]. So (w,t) ∉ tent for t>0. Then h(w,t) = g(w) + ε(1−t) > 0 — VIOLATION! (w,t) is a lattice point NOT in Δ but h>0 there.

Hmm!! That breaks the naive tent for ANY m ≥ 1 whenever (w,1) ∈ P — which it is since P = Q×[0,m] includes the whole product. Wait but the notes say m=1 case was proven with this tent... Did I misread the geometry?

Let me recompute. Tent Δ = conv((u,0),(v,0),(w,0),(u,1)). At height t, section = conv of ((1−t)(u,v,w at 0) + t(u,1))... cross-section of a simplex at height t: barycentric combos with apex weight t: (1−t)·conv{(u,0),(v,0),(w,0)} + t·(u,1) = ((1−t)conv{u,v,w} + tu) × {t}. Yes S_t = (1−t)τ + tu.

Point (w,1) (top layer): in tent only if w = tu + (1−t)z, t=1 ⟹ w=u false. So (w,1) ∉ Δ. h(w,1) = g(w) + ε·0 = g(w) > 0. VIOLATION confirmed.

So the m=1 tent as described FAILS?! Unless... the certificate is different. Hmm, wait — maybe I should re-read: "两层情形 $m=1$：帐篷 $\Delta=\mathrm{conv}((u,0),(v,0),(w,0),(u,1))$，证书 $h=g+\varepsilon(1-z)$，取 $\varepsilon< m_0$（$-m_0=\max_{\text{foreign}}g<0$）。多层 $m\ge2$ 的障碍：$(u,2)$ 拿到 $g(u)+\varepsilon>0$。"

The stated obstacle for m≥2 was (u,2): h(u,2) = g(u) + ε(1−2) = g(u) − ε. With ε < m₀ and g(u)>0... g(u) − ε could still be positive if ε < g(u). To make (u,2) negative need ε > g(u). Combined with ε < m₀: feasible iff m₀ > g(u)... but ALSO my discovered obstruction (w,1): h(w,1) = g(w) needs to be < 0 — impossible since g(w) > 0 fixed!! Unless (w,1) IS in the tent... it's not.

Hmm wait, unless the tent uses apex over u and the certificate is different, like h = g + μ(z−1)? Then (w,1): g(w) + 0 = g(w) > 0 still violation. Hmm.

So Thm D's m=1 tent seems broken as transcribed?? Unless the winning pair (τ, g) has additional structure. Hmm hold on — maybe I'm wrong that all of L_τ × {t} must satisfy h<0. They're foreign only if not in Δ. (w,1): w ∈ L_τ ⊆ L_Q, so (w,1) ∈ P∩L, and (w,1) ∉ Δ. It's a genuine foreign point requiring h<0. g(w)>0 kills it.

Unless the tent is oriented differently... What if instead the apex sits above u and we use h = g − δ·(distance-ish)... any affine h = α∘g-part... h is affine: h(x,t) = ℓ(x) + βt + c. Constraints:
- On L_τ×{0}: >0 (all lattice points of base τ at level 0 are in Δ)
- (u,1) ∈ Δ: >0
- Other tent lattice points: >0
- (w,t) for t=1..m: <0. In particular (w,1): ℓ(w) + β + c < 0 while ℓ(w) + c > 0 (from level 0). So β < 0.
- Similarly (v,1): β<0 consistent.
- (u,2) (if m≥2): ℓ(u) + 2β + c < 0, with ℓ(u)+c>0 ⟹ 2β < −(ℓ(u)+c) < −β... fine β<0 helps.
- Foreign base points x: ℓ(x) + c < 0.

So general solution shape: h = g + β(z − s) form... Let me parametrize h = g + βz + c'. Conditions:
1. g(y) + c' > 0 for y ∈ L_τ (at z=0).
2. (u,1): g(u) + β + c' > 0.
3. (w,t), t≥1: g(w) + βt + c' < 0. At t=1: g(w) + β + c' < 0. Combined with 2: g(w) < g(u) needed?? g(w) + β + c' < 0 < g(u) + β + c' ⟹ g(w) < g(u). Interesting!
4. Similarly v: g(v) < g(u).
5. (u,t) t≥2 (m≥2): g(u) + βt + c' < 0.

With scaling trick: replace g by g/K. Set c' = something. Let me think of h = g/K + β(z−1):
- Level 0: g(y)/K − β > 0 ∀y∈L_τ ⟹ β < min_{L_τ} g/K.
- (u,1): g(u)/K > 0 ✓.
- (w,t), (v,t), t≥1: g(w)/K + β(t−1) < 0 ⟸ β < −g(w)/K etc. (β<0 suffices).
- Foreign base x: g(x)/K − β < 0 ⟹ β > max_foreign g/K = −m₀/K.
- Interior tent points: positive automatically? Tent lattice point (x,t): x ∈ S_t ⟹ g(x)/K > 0, plus −β(1−t)... h = g/K + βt − β = g(x)/K + β(t−1). For t=1: g(x)/K>0 ✓. t=0: covered by condition 1 (x∈L_τ). 0<t<1 no lattice points (integer layers only). ✓
- (u,t), t≥2: g(u)/K + β(t−1) < 0 ⟸ β < −g(u)/K (worst t=2).

Feasible window: max(−m₀/K, ...) < β < min(min_{L_τ} g/K, −max(g(u),g(w),g(v))/K, ...). As K→∞, left side → 0⁻, right side → 0⁻ but strictly ordered? Right side is min of negatives /K — all terms are strictly negative divided by K; left side −m₀/K. Window nonempty iff −m₀ < min(min_{L_τ} g, −g(u), −g(w), −g(v))·(1/K scaling same) — scaling doesn't help if window is empty at the ratio level!! Window in original units: −m₀ < β' where β' ranges over (−m₀, min(min_{L_τ}g, −max_{τ vertices}g)). Since min_{L_τ} g ≤ min over vertices, and −max vertex g < 0 < min_{L_τ} g... wait min_{L_τ} g is the MIN over all lattice points of τ including interior ones, which is ≤ each vertex value but could be much smaller (still positive though? g>0 on all of conv(L_τ) ⟹ min_{L_τ} g > 0). So right side = min(positive number, negative number) = −max(g(u),g(v),g(w)) < 0. Window: −m₀ < β' < −max_v g. Nonempty iff m₀ > max_v g, i.e., **the worst foreign point is less bad than the worst vertex value**. Scaling does NOT change this comparison (both sides scale by 1/K)! 

Hmm!! So the claim "把 g 换成 g/K 后窗口必非空" is WRONG under my analysis?? Scaling divides BOTH sides of the inequality by K. −m₀/K < β < −M/K where M = max vertex g: multiply by K: −m₀ < βK < −M — same condition. Scaling doesn't open the window!

Wait, wait. Let me re-read the note once more: "可行窗口 $-m_0<\mu<\min\big(-\max_{L_\tau}g,\ \min_{L_\tau}g\big)$，即需 $m_0>\max_{L_\tau}g$". Hmm: "−max_{L_τ} g" — max over L_τ of g. And min_{L_τ} g. So window: −m₀ < μ < min(−max_{L_τ} g, min_{L_τ} g). Since max_{L_τ} g ≥ min_{L_τ} g > 0, −max_{L_τ}g < min_{L_τ} g... so window top = −max_{L_τ}g. Condition: m₀ > max_{L_τ} g. Same as mine (with max over all L_τ rather than vertices — slightly stronger).

Then: "把 $g$ 换成 $g/K$（符号不变）后 $\max_{L_\tau}g/K$ 任意小，窗口必非空" — they claim after scaling, max g/K becomes arbitrarily small, so window becomes nonempty. But −m₀ also scales to −m₀/K! The window is (−m₀/K, −max_{L_τ}(g)/K) — empty iff −m₀/K ≥ −max g/K iff m₀ ≤ max g. SCALING PRESERVES EMPTINESS. The observer's transcription says "轮7借此证出乘积定理", claiming scaling fixes it — but mathematically scaling cannot fix an empty window of the form (−a/K, −b/K) with a ≤ b.

Hmm, but maybe the actual round-7 reasoning had a different certificate family where scaling DOES help — e.g., if the window is (−m₀, μ_max) with μ_max independent of scaling... Like h = g + μ(z−1): conditions give window (−m₀, min(min_{L_τ}g, −max_{L_τ}g))... hmm same issue.

OR maybe the tent geometry differs: maybe the correct tent avoids the (w,1)-type violation because the tent's top layer section covers MORE of τ... Impossible — a simplex with one apex at height 1 has top-layer section = single point.

Alternatively the product theorem might use a DIFFERENT Δ: e.g., prismatoid or split across layers. OR maybe the theorem is true but needs a smarter proof. Let me think about whether Q×[0,m] YES is even plausible for arbitrary 2D Q.

Hmm, wait. Actually, hold on. Let me reconsider. Maybe the certificate isn't required to be positive on ALL lattice points of Δ — yes it is ("h>0 于 Δ 的所有整点"). And foreign points include (w,1) etc.

OK here's the thing: I've found a potential FLAW in Thm D's transcribed proof. The scaling argument as transcribed is invalid (scaling cancels). This is exactly the kind of thing I should verify computationally and either fix or downgrade. Let me think harder about whether Q×[0,m] is still provable by another route.

Alternative approach for products: induction on m using Thm C-like stacking? Or: reduce to base winning pair with STRONGER properties. Actually here's a cleaner idea: strengthen the base pair requirement. Define "strong pair": (τ,g) with g>0 on L_τ, g<0 on foreign, AND max_{vertices} ... hmm.

Actually, alternative: use the FULL-DIMENSIONAL trick — treat Q×[0,m] directly with its own corner: if Q contains a unit square [0,1]^2 translated... not every polygon contains a unimodular square... but every lattice polygon with ≥3 lattice points contains... hmm, Pick's theorem: area = I + B/2 − 1 ≥ ... a lattice polygon with exactly 3 lattice points is unimodular triangle. Does every 2D lattice polygon contain a unimodular triangle (empty lattice triangle)? Yes! Triangulate the polygon into empty triangles (standard: triangulation using all lattice points as vertices gives empty cells). So Q always contains an empty lattice triangle τ₀. But "empty" isn't enough for separation in the product...

Let me test the simplest product: Q = unimodular triangle conv{0,e1,e2}, P = Q×[0,m]. Lattice points: (i,j,k), i,j≥0, i+j≤1, k∈[0,m]. That's 3(m+1) points. Is P YES for m=2? Points: k=0: {00,10,01}; k=1: same 3; k=2: same 3. Total 9 points in R³. Want simplex + separating affine h.

Try Δ = conv((0,0,0),(1,0,0),(0,1,0),(0,0,2))? That's a simplex (tetrahedron). Its lattice points: vertices + ? Segment from (0,0,0) to (0,0,2) contains (0,0,1)! So L_Δ = {(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,0,2)}. Certificate: want h>0 on those 5, h<0 on other 4: (1,0,1),(0,1,1),(1,0,2),(0,1,2). Try h = a(x+y) + bz + c: 
- (0,0,0): c>0
- (1,0,0),(0,1,0): a+c>0
- (0,0,1): b+c>0
- (0,0,2): 2b+c>0
- (1,0,1),(0,1,1): a+b+c<0
- (1,0,2),(0,1,2): a+2b+c<0
From c>0, a+c>0, b+c>0: try c=1, b=−2, then 2b+c=−3<0 ✗. Try c=1, b=−0.75, a=−0.75: a+b+c=−0.5<0 ✓, a+2b+c=1−1.5−0.75... a+2b+c = −0.75−1.5+1 = −1.25<0 ✓, 2b+c = −0.5 <0 ✗ (need (0,0,2)>0: 2b+c = −1.5+1 <0 ✗). Conflict: need 2b+c>0 and a+b+c<0 with a+c>0 ⟹ a > −c ⟹ a+b+c > b ⟹ b < 0; 2b+c>0 ⟹ b > −c/2. And a+b+c<0 ⟹ a < −b−c. Need −c < −b−c ⟹ b>0. Contradiction with b<0. So this Δ fails; LP would find others. Let me think structurally: is Q×[0,2] (9 pts) separable? 

Points: three columns C_k = {(0,0,k),(1,0,k),(0,1,k)}, k=0,1,2. Equivalent (Q): find subset A = L_Δ (lattice points of some tetrahedron in P) with conv(A) ∩ conv(complement) = ∅.

Tetrahedra in P: 4 points among 9 forming a tetrahedron within the prism Q×[0,2] (a triangular prism). Hmm, brute force C(9,4)=126 — I'll do this computationally later. But intuitively: the point set is "two triangles stacked"; conv(A) vs conv(B) separation... 

Actually WAIT. Maybe I'm overcomplicating. Let me reconsider: perhaps pick Δ = conv((0,0,0),(1,0,0),(0,1,0),(0,0,1)) (unit corner tetrahedron, unimodular, L_Δ = 4 vertices). Complement: (1,0,1),(0,1,1),(0,0,2),(1,0,2),(0,1,2). Separation: conv(4 pts) vs conv(5 pts) disjoint? The unit corner tetra touches (1,0,1)? Distance... (1,0,1) is outside (tetra has x+y+z≤1). Conv(complement) contains (1,0,0)?? No wait complement excludes (1,0,0). conv{(1,0,1),(0,1,1),(0,0,2),(1,0,2),(0,1,2)}: does it intersect the unit tetra? Lowest z in complement-conv is 1 (points at z=1: (1,0,1),(0,1,1); segment between them: x+y=1, z=1). Unit tetra has x+y+z ≤ 1, z≥0: intersection with z≥1 plane: only point (0,0,1). Is (0,0,1) ∈ conv(complement)? Complement points all have x+y ≥ 1 except (0,0,2) which has z=2. Point (0,0,1): x+y=0 forces combo weights on x,y-bearing points zero ⟹ (0,0,1) = t(0,0,2)+(1−t)(something with x+y≥1)... any convex combo giving x=y=0 uses only (0,0,2), giving z=2≠1. So no intersection! DISJOINT. So Q×[0,2] with Q=unimodular is YES via unit corner + separation. 

Certificate: h with h>0 on {000,100,010,001}, h<0 on rest. By symmetry in x,y: h = a(x+y) + bz + c, c>0, a+c>0, b+c>0, a+b+c<0 (violators (1,0,1),(0,1,1)), a+2b+c<0 ((1,0,2),(0,1,2)), 2b+c<0 ((0,0,2)). Take c=1, a=0: need b+1>0, b+1<0 contradiction. Take c=1, a=−0.5: a+c=0.5>0 ✓; need b+1>0 ⟹ b>−1; a+b+c = b+0.5<0 ⟹ b<−0.5; 2b+1<0 ⟹ b<−0.5; a+2b+c = 2b+0.5<0 ⟹ b<−0.25. So b ∈ (−1, −0.5): b=−0.75. Check: h = −0.5(x+y) −0.75z + 1: 000:1>0✓; 100: 0.5>0✓; 010 ✓; 001: 0.25>0✓; 101: −0.5−0.75+1=−0.25<0✓; 011 ✓; 002: −0.5<0✓; 102: −0.5−1.5+1=−1<0✓; 012 ✓. ALL PASS. So Q×[0,2] YES.

Interesting — so the product theorem conclusion holds at least here, but via a different mechanism than the transcribed tent (my Δ was the corner tetra, not the tent). The transcribed Thm D proof is flawed (scaling doesn't open the window), but the theorem might still be true via other constructions for specific cases. For general Q×[0,m]... hmm, hard. General Q arbitrary lattice polygon, arbitrary m.

Hmm OK. Let me now step back and prioritize per the handoff notes:

Priority 1: WRITE proof.md NOW with honest content. Include Thm B (boxes — solid), Thm C (height-1 pyramid — solid, I verified above), Thm D — PROBLEMATIC as transcribed. Options: (a) omit Thm D, (b) include with corrected scope: prove it for the cases where the window condition m₀ > max_{L_τ} g genuinely holds, and note the scaling claim is void. Hmm wait, but actually let me double-check the window derivation once more, because maybe the intended certificate was h = g + ε(1−z) with ε SMALL for m=1, and the (w,1) problem doesn't arise because... (w,1) has h = g(w) > 0. Yeah no, it arises. Unless the tent apex is chosen ABOVE a vertex u such that the opposite edge vw's endpoints... no, g(w)>0 regardless.

Hmm, hmm. Wait — maybe I have the roles reversed: maybe the tent is inverted: apex at BOTTOM and base at top? Δ = conv((u,0),(v,1),(w,1),(u,1))? Top face = τ at z=1... Let me not rabbit-hole; the cleanest path: I'll re-derive the product theorem properly myself, or restrict claims. Actually you know what — let me reconsider the whole picture. The REAL question is the final boxed answer: "n=1,2 恒 YES（已证）；n≥3 开放". The theorems B/C/D are supporting evidence for "hard to find counterexamples". If Thm D is shaky, I can either fix or drop it; Thm C is solid; Thm B solid.

Let me now also double-check Thm C once more since it goes in the proof file. Done above — solid, with ε > −g(a) allowed (no upper bound needed since foreign points sit at z=0 where ε vanishes). Also need: Δ = conv(τ×{0} ∪ {(a,1)}) has no OTHER lattice points with h ≤ 0 — all its lattice points get h>0? Lattice points of Δ: Δ ⊆ P, so Δ∩L ⊆ P∩L = (L_B×{0}) ∪ {(a,1)}. Those in Δ∩{z=0}: Δ∩{z=0} = τ (cross-section at t: (1−t)τ + t·a... wait apex is (a,1), section at height t is conv((1−t)(τ) + t·a)×{t}; at t=0: τ). So Δ∩{z=0}∩L = L_τ: h=g>0 ✓. At t=1: apex: h=g(a)+ε>0 ✓. Intermediate layers: none. ✓✓ Thm C fully verified. Also full-dim: τ is (n−1)-dim, apex off the plane ✓.

And I should double check the claim "P∩{z=1}={(a,1)}": P = conv(B×{0} ∪ {(a,1)}), points at height exactly 1: (1−s)(b,0)+s(a,1) has z=s=1 ⟹ pure apex. ✓. And P∩{z=0} = B×{0}: z=0 forces s=0 ⟹ (b,0). ✓.

Thm C gives: EVERY height-1 pyramid over a 2D lattice polygon is YES (3D case unconditional). Nice.

Now Priority 2: write enum2d.py & check3d.py and RUN them. This is the decisive experiment. Per specs:

enum2d.py: enumerate subsets S of [0,3]^2 grid (16 points), close under hull (add grid points inside conv(S)), dedupe, for each config L apply the 2D THEOREM CONSTRUCTION (leaf triangle + collinear patch) — but wait, the 2D theorem is already proven, so enumeration serves as VERIFICATION of the theorem's engine. Honestly, the more valuable target is 3D. But the notes specify enum2d as designed; it double-checks the 2D proof engine. Cost: 65536 subsets × work each. Might be slow in Python with Fractions but each config is cheap (find boundary vertex a, empty corner check, construct, single separation check via exact rational arithmetic — no LP needed per the design: "Fraction 精确验证分离" using explicit candidate h). Actually the design says verify the specific constructed candidate works. That's O(|L|) per config after finding the leaf triangle. Should be fast enough. But honestly — the 2D theorem is proven by hand; enumerating 65536 configs to confirm is nice-to-have. Priority to 3D.

check3d.py: the F1–F5 families. Most important per notes: F1 m=1 ([0,1]^3, 70 tetras — trivial), F3 v1 环抱四面体 (12 points, C(12,4)=495 FM checks), F5 random families. This needs an exact separation solver: given finite point sets A (inside candidates) — actually the real question: does THERE EXIST a tetrahedron (any 4-subset spanning a tetrahedron contained in P... careful: Δ must be ⊆ P; vertices must be lattice points of P; and L_Δ = all lattice points in Δ; need conv(L_Δ) ∩ conv(L\L_Δ) = ∅.

Exact approach per config: enumerate all 4-subsets T of L that form a full-dim simplex contained in P (need containment test — for convex hull of lattice points, tetra ⊆ P iff all 4 vertices ∈ P and... tetra = conv of 4 points of P ⊆ P by convexity! YES — any 4 points of P span a simplex inside P. So containment is FREE.) Compute A = L ∩ Δ exactly (lattice point in tetrahedron test via barycentric coords with Fractions), B = L \ A, then test conv(A) ∩ conv(B) = ∅ exactly. 

Testing conv(A) ∩ conv(B) = ∅ for finite point sets: solve feasibility of: λ≥0 on A, μ≥0 on B, Σλ=Σμ=1, Σλa − Σμb = 0. This is an LP feasibility. Exact LP via Fraction-based Fourier–Motzkin elimination on... variables = |A|+|B| points — too many for FM. Better: separation via LP duality — conv(A)∩conv(B) ≠ ∅ ⟺ for all directions... ⟺ max min ⟨dir, a⟩ ... Standard: conv(A) ∩ conv(B) = ∅ ⟺ ∃ dir and γ: ⟨dir,a⟩ > γ ∀a∈A, ⟨dir,b⟩ < γ ∀b∈B (strict hyperplane separation, since compact). So disjointness ⟺ ∃ dir: min_A ⟨dir,a⟩ > max_B ⟨dir,b⟩, i.e., min_{a}⟨dir,a⟩ − max_b⟨dir,b⟩ > 0. This is an LP in dim 3 (+1 offset): maximize t s.t. ⟨dir,a⟩ − t ≥ 0 ∀a∈A... wait: want min_A − max_B > 0: introduce γ: ⟨dir,a⟩ ≥ γ ∀a, ⟨dir,b⟩ ≤ γ ∀b, and maximize (min gap)... maximize nothing — just FEASIBILITY of ⟨dir,a⟩ − ⟨dir,b'⟩ ≥ 1 (normalize) ∀ a∈A,b'∈B: ∃ dir ∈ R³ with ⟨dir, a−b'⟩ ≥ 1 for all pairs. THAT'S the FM reduction already in the notes! ("∃dir: ⟨dir,a−b⟩≥2 ∀(a,b)∈A×B" — with ≥2 coming from integrality rounding: if some real dir works with gap > 0, scale it; integer lattice: gaps ⟨dir, a−b⟩ are... hmm, dir real, differences integral vectors; strict > 0 gap can be normalized to ≥ 1 by scaling; the "≥2" version comes from wanting h ≥ 1 / ≤ −1 with h having... whatever, ≥1 normalization suffices for pure separation.)

So: disjointness test = ∃ dir ∈ R³: min_{a∈A,b∈B} ⟨dir, a−b⟩ ≥ 1. This is a small LP (3 vars, |A|·|B| constraints — up to ~50–200 constraints typically). Solve with Fraction-based simplex or FM on 3 variables. FM on 3 vars with N constraints: eliminate x → pairs... N could be ~100–500; FM blowup manageable if we're careful, but simpler: implement exact simplex LP (Fraction, Bland). Risky to code from scratch quickly but doable. Alternative: scipy float LP prefilter + exact verification of the found dir (verify min gap > 0 with Fractions) + for "infeasible" claims use Farkas certificate from float solver, verified exactly. That's robust: float LP (scipy linprog HiGHS) proposes dir*; exact check min_{pairs} ⟨dir*, a−b⟩ ≥ 1−tiny... then rescale dir* exactly to rationals and verify gap ≥ 1 after scaling. If float says infeasible, extract dual/Farkas: y ≥ 0 with Σ y_{ab}(a−b) = 0 and Σ y_{ab} > 0... Farkas: system ⟨dir, d_i⟩ ≥ 1 infeasible ⟺ ∃ y ≥ 0: Σy_i d_i = 0, Σ y_i > 0. Verify exactly: Σ y_i d_i = 0 with rational y. Both verifications are cheap exact arithmetic. 

That's the plan: float LP propose, exact verify either dir (YES-side) or Farkas certificate (NO-side). Bulletproof.

For enumerating: per config, iterate over 4-subsets (early exit on first success — most configs YES early). Only when ALL 4-subsets fail do we declare counterexample, with each failure backed by exact Farkas.

Cost estimate F3-v1: 12 points, C(12,4)=495 tetras, each ≤ C(|A|,?)… A sizes vary; pairs |A|×|B| ≤ 12²=144 constraints, 3-var LP — milliseconds each with scipy. Totally feasible. F5 random: similar.

F2 octahedra ±a e_i: |L|=25 for a=b=c=2: C(25,4)=12650 tetras × LP — heavier but sampling per notes. Actually with fast float-LP + exact verify and early exit, full sweep might run in minutes. Let's see.

Also F4: pyramids/prisms/products — structural candidates.

AND the theory frontier (weighted-sum criterion, deep corners D≥3): small enumeration of primitive triples with D=2,3 and testing whether SOME cut plane + simplex separates within the cone-restricted setting... Actually the cleaner sub-question: the "corner kill" analysis is about local obstructions; global counterexample search is F5. Given limited budget, priority: proof.md FIRST, then check3d.py core + run F1/F3/F5, then report.

One more theory piece to nail down before writing proof.md — the n=1 argument (trivial, reconstructed above), Lemma 0 (done above), and decide final stance on Thm D. Let me think again about Thm D…

Honest resolution for Thm D: The transcribed proof is broken (scaling cancels; moreover the tent admits the (w,1) violation making even the m=1 case fail under that certificate). BUT maybe I misread and the tent is meant differently... Let me recheck by considering the possibility apex over u with certificate h = g + ε(1−z), and the claim "h>0 on Δ's lattice points, h<0 elsewhere" — foreign (w,1): g(w) + 0 > 0. Broken, period, for m≥1. UNLESS the winning pair is required to satisfy g(w) ≤ 0 for... no, g>0 on all of L_τ.

Hmm, actually WAIT. What if the tent is Δ = conv((u,0),(v,0),(w,0),(a,1)) where a is chosen OUTSIDE τ but... no. Or the certificate h = g + ε(z − c)... any affine h = ℓ + βz: (w,t) t≥1 needs ℓ(w)+βt<0 ∀t≥1 ⟹ β<0 and ℓ(w)+β<0 ⟹ ℓ(w) < −β; level-0 needs ℓ(w)>0 (w ∈ L_τ at z=0 in Δ). So need −β > ℓ(w) > 0. (u,1) ∈ Δ needs ℓ(u) + β > 0 ⟹ β > −ℓ(u). So −ℓ(u) < β < −ℓ(w) ⟹ REQUIRES ℓ(u) > ℓ(w). Similarly (v,1)... wait is (v,1) foreign? Yes (not in tent). Need ℓ(v)+β<0 ⟹ β < −ℓ(v) ⟹ ℓ(u) > max(ℓ(w),ℓ(v))... and (u,2) for m≥2: ℓ(u)+2β<0 ⟹ β < −ℓ(u)/2, combined with β > −ℓ(u): fine (−ℓ(u) < −ℓ(u)/2). So necessary & sufficient-ish: exists affine ℓ (≈ scaled g + const? no — ℓ is the z=0 part of h, must be >0 on L_τ and <0 on foreign L_Q — i.e., ℓ IS a winning certificate g for the base!) with ℓ(u) > max(ℓ(v), ℓ(w)) and window −m₀ < β < min(−ℓ(v), −ℓ(w), −ℓ(u)/2 (if m≥2), min_{L_τ}ℓ (level-0 all positive: β<0 doesn't affect z=0)... wait level-0 condition: ℓ(y) > 0 for y ∈ L_τ — automatic from winning pair, no β involvement. Tent interior points (x,t): ℓ(x) + βt > 0; x ∈ S_t ⟹ ℓ(x) > 0 (convexity, ℓ>0 on τ... ℓ>0 at vertices of τ ⟹ ℓ>0 on τ ⟹ on S_t) and βt ≥ β... for t∈(0,1): no lattice points. Fine.)

So corrected Thm D: Q×[0,m] YES if base winning pair (τ=conv(u,v,w), g) can be chosen with g(u) > max(g(v),g(w)) and window −m₀ < β < −max(g(v),g(w)) [and β < −g(u)/2 if m ≥ 2] nonempty, i.e., **m₀ > max(g(v), g(w))** for m=1; **m₀ > max(g(v),g(w), g(u)/2)** for m≥2 — where m₀ = −max_{foreign} g. NOTE: scaling g→g/K preserves all comparisons (both sides scale). So the TRUE criterion: exists winning pair whose "second-highest vertex value" is dominated by the least-negative foreign value. NOT automatic. The round-7 claim "窗口必非空" via scaling is definitively WRONG.

Can we always rescale/re-pick to satisfy it? Consider translating... adding constant to g: g' = g + c changes m₀ → m₀ − c and vertex values +c: condition m₀ − c > max(second-highest...) hmm: m₀' = −max_foreign(g+c) = m₀ − c; need m₀ − c > max_v g + c − max... let me define M₁ = max vertex g, M₂ = second max vertex g, m₀ = −max foreign g (>0 since foreign all <0). Condition (m≥2): m₀ − c > max(M₂ + c, (M₁+c)/2). Optimize over c: decreasing c helps LHS? No: smaller c → larger m₀−c? m₀−c increases as c decreases. RHS: M₂+c decreases, (M₁+c)/2 decreases. So DECREASING c helps BOTH sides! But constraint: g+c > 0 on L_τ ⟹ c > −min_{L_τ} g. Take c → −min_{L_τ}g⁺: then min vertex value → 0⁺. New M₂' = M₂ − min_g... Define vertex values sorted a ≥ b ≥ d > 0 (d = min). Condition: (m₀ + d... c = −d + tiny) LHS: m₀ + d; RHS: max(b − d, (a−d)/2)... wait M₂+c = b − d, (M₁+c)/2 = (a−d)/2. Hmm, so condition: m₀ + d > max(b−d, (a−d)/2) — STILL not automatic! E.g., foreign barely negative (m₀ = 0.1) and vertices strongly positive (a=b=d... say unimodular τ with g values 1, 1, 1 at vertices, foreign max −0.1: condition: 0.1 + 1 = 1.1 > max(0, 0) = 0 ✓ fine. Try g vertices (100, 100, 1), foreign −0.1: m₀+d = 1.1, RHS: max(99, 49.5) = 99 ✗. Can't fix by scaling (all scale together). Different pair? Maybe. So Thm D as "unconditional given any winning pair" is FALSE-as-stated; the correct statement is conditional on the refined criterion. Whether EVERY lattice polygon Q admits a pair satisfying the refined criterion: unknown/open — plausibly yes via choosing τ cleverly, but I can't prove it now.

DECISION for proof.md: present Thm D in corrected conditional form (with the honest derivation above — it's a nice fix!), explicitly noting the earlier scaling claim was erroneous and why. This is exactly the kind of audit contribution expected. Actually hmm, wait — let me reconsider whether the tent could be replaced by something else making products unconditionally YES given base pair. Alternative: use TWO tents / different apex choice per layer... For m=1: need β-window (−m₀, −max(g(v),g(w))) with the freedom of WHICH vertex gets the apex: choose apex over the MAX vertex: condition m₀ > second-max vertex value (after optimal constant shift c→−min: m₀ + min_v > max(other two − min_v...)). Hmm anyway: conditional it is.

Hmm, actually hold on, one more idea for rescuing unconditional products: DON'T keep all of L_τ×{0} in Δ. E.g., Δ = corner-type tetra conv((u,0),(v,0),(w,0),(u,1)) was the tent. What about Δ = conv((u,0),(v,0),(w,1),(u',1))-type skew tetras, or Δ using points from multiple layers like my successful manual example (corner tetra with long vertical edge: conv(000,100,010,002) for the Q=unimodular, m=2 case — which worked with h = −0.5(x+y) −0.75z + 1!). Notice MY working example had NEGATIVE coefficients on x+y — i.e., ℓ = −(x+y)·0.5 + 1: on base layer, ℓ > 0 on L_τ={00,10,01}: ℓ(00)=1, ℓ(10)=0.5, ℓ(01)=0.5 >0 ✓; foreign at z=0: none! (Q=unimodular has only 3 lattice points, all in τ). m₀ = +∞ effectively (no foreign base points) — that's why it worked despite "bad" vertex ordering. So products over bases WITH FOREIGN POINTS are where the criterion bites. E.g., Q = [0,2]-triangle conv{0, 2e1, 2e2}? L_Q = {0,(1,0),(2,0),(0,1),(1,1),(2,1)...} hmm conv{00,20,02}: lattice pts: 00,10,20,01,11,21? No: x,y≥0, x+y≤2: 00,10,20,01,02,11. 6 points. Q×[0,m]: does YES hold? Try m=1: P = tri-prism, 12 points. Corner attempt: Δ = conv(000,100,010,001) unit corner: L_Δ = 4 pts. Foreign: 9 pts incl (1,1,0)... h = a x + b y + c z + d: >0 on 000(d>0), 100, 010, 001; <0 on 110,101,011,200,020,002,111? wait is (1,1,1) in P? x+y≤2, z≤1: yes. etc. Symmetry x↔y: h = a(x+y) + cz + d: d>0; a+d>0; c+d>0; violators: (1,1,0):2a+d<0; (2,0,0):2a+d<0 (same); (0,2,0): same; (1,0,1): a+c+d<0; (0,0,2)∉P (m=1). (0,0,1): c+d>0 ✓already; (1,1,1): 2a+c+d<0; (2,0,1),(0,2,1): 2a+c+d<0 same; (0,0,1) done. So need: d>0, a>−d, c>−d, 2a+d<0, a+c+d<0, 2a+c+d<0. From 2a+d<0: a<−d/2; combined a>−d ok window (−d, −d/2). c>−d and a+c+d<0 ⟹ c<−a−d; with a∈(−d,−d/2): −a−d ∈ (−d/2, 0); need c>−d AND c < −a−d AND 2a+c+d<0 ⟹ c < −2a−d; take a=−0.75d: −a−d = −0.25d; −2a−d = 0.5d; need c ∈ (−d, min(−0.25d, 0.5d)) = (−d, −0.25d): c = −0.5d: checks: c+d = 0.5d > 0 ✓; a+c+d = −0.75−0.5+1 = −0.25d < 0 ✓; 2a+c+d = −1.5−0.5+1 = −1d < 0 ✓. WORKS with d=2: h = −1.5x −1.5y − z + 2. Verify all 12 points of Q×[0,1], Q=conv{00,20,02}: pts: (0,0,0):2>0✓ (in Δ); (1,0,0): 0.5>0✓ (in Δ); (0,1,0): ✓; (0,0,1): 1>0 ✓ (in Δ); (2,0,0): −1<0✓; (0,2,0): −1✓; (1,1,0): −1✓; (2,0,1): −2✓; (0,2,1): −2✓; (1,1,1): −2✓; (1,0,1): −0.5<0✓ — wait (1,0,1) must be FOREIGN: is (1,0,1) in Δ=conv{000,100,010,001}? x+y+z≤1: 1+0+1=2>1 no ✓ foreign correctly negative. (0,1,1): −0.5 ✓. ALL GOOD. So tri(Q=[0,2]-triangle)×[0,1] YES.

Fine — products seem robust empirically; the general unconditional proof remains open. I'll state Thm D' (corrected conditional criterion) in proof.md.

Now, ANOTHER important audit item: the claimed equivalence (Q) and Lemma 0 — done. The 2D proof — let me AUDIT it myself carefully now, since it's the centerpiece:

Step 3 (切锥论证): claim: L-points strictly on a-side of line ℓ = aff(b,c): only a. Setup: T = conv(a,b,c) is a leaf triangle of a triangulation of P (using ALL lattice points as vertices? — "以 L 全体为顶点的三角剖分" yes). ab, ac are boundary edges of P (leaf triangle has exactly one internal edge bc). a is a genuine vertex of P.

Claim: if p ∈ L ∩ H⁺ (strict side), p ≠ a ⟹ contradiction. Since P convex and both a,p ∈ P: [a,p] ⊆ P. Direction: p ∈ H⁺ means h(p) > 0 where h = signed distance from ℓ, h(a) > 0, h(b)=h(c)=0. Tangent cone at a: generated by rays a→b and a→c (boundary edges at vertex a — valid since P is 2D and ab, ac are THE two edges at a... careful: a is a vertex of P; its two incident boundary edges are along ab and ac? The triangulation edges ab, ac lie ON ∂P — yes since they're boundary edges of the triangulation and triangulation boundary = P boundary. Two distinct boundary edges at a ⟹ they ARE the two edges at a (a 2D polygon vertex has exactly 2 edges). Hence tangent cone T_aP = pos{b−a, c−a} (convex position assumed — angle < π). Now p ∈ P, p ≠ a: vector p−a ∈ T_aP? For convex set, p−a ∈ T_aP (tangent cone contains all directions from a into P — yes, tangent cone of convex set at a contains {p−a : p ∈ C}). So p−a = u(b−a) + v(c−a), u,v ≥ 0. Apply h: h(p) = u·0 + v·0 + ... h affine: h(p) = h(a) + u(h(b)−h(a)) + v(h(c)−h(a)) = h(a)(1−u−v). p ∈ H⁺: h(p) > 0 ⟹ 1−u−v > 0 ⟹ u+v < 1 ⟹ p = a + u(b−a) + v(c−a) with u,v ≥ 0, u+v<1 ⟹ p ∈ T = conv(a,b,c). T is a triangulation cell: T ∩ L = {a, b, c} (cells have no lattice points besides own vertices BECAUSE triangulation uses all of L as vertices — any lattice point in T would be a vertex of the triangulation lying in the cell, but cells meet only at shared faces; a lattice point strictly inside T or on edge bc... on edge bc: bc is an edge of the triangulation; triangulation vertices on edge bc would subdivide it — since ALL lattice points are triangulation vertices, if a lattice point q lay on segment bc, q would be a triangulation vertex on segment bc, contradicting bc being a single edge. ✓). So p ∈ {a,b,c}; p ∈ H⁺ excludes b,c (h=0); p=a excluded by assumption. CONTRADICTION. ∎ Lemma solid.

Step 4 (collinear patch): if L ∩ ℓ ⊋ {b,c}, take extreme points u,v of the segment L∩ℓ (they're lattice points, [b,c] ⊆ [u,v]); Δ = conv(a,u,v). Recheck step 5 with u,v: (i) L∩Δ: points with ĥ ≥ 0 where ĥ := the height function wrt ℓ (positive at a): Δ = {a + t(w−a)...}: any point of Δ is ta + (1−t)w', w' ∈ [u,v]; ĥ = t·ĥ(a) ≥ 0. Conversely lattice pts of P with ĥ ≥ 0: by lemma only a (on ĥ>0 side) plus L∩ℓ points — but wait, the lemma was for T = conv(a,b,c); generalizing: any p ∈ L ∩ H⁺: same tangent-cone argument applies INDEPENDENTLY of T! The lemma's proof only used: ab, ac boundary edges, tangency, and p ∈ T ⟹ p ∈ {a,b,c} — the last step used T empty. With Δ = conv(a,u,v) ⊇ T: p ∈ Δ doesn't immediately give contradiction... but we don't need it: we need to SHOW Δ∩L = {a} ∪ (L∩ℓ). Direct: ⊇ clear (a, u, v and everything on segment uv... wait L∩ℓ ⊆ [u,v] ⊆ ℓ ∩ Δ ✓, plus a). ⊆: q ∈ Δ ∩ L: if q = a or q ∈ [u,v]: fine. Else q has ĥ(q) > 0 (strictly between... any point of Δ not in ℓ∪{a} has ĥ ∈ (0, ĥ(a)): q ∈ H⁺ ∩ L ⟹ by lemma q ∈ T ∩ ... lemma gives q ∈ conv(a,b,c) ∩ L = {a,b,c} ⟹ q ∈ {a} ∪ ... b,c ∈ ℓ ⊆ [u,v]. So indeed Δ ∩ L = {a} ∪ (L∩ℓ). ✓ 
(ii) Δ ⊆ P ✓ (vertices in P). (iii) full-dim: a ∉ ℓ ✓. (iv) separation: ĥ' = ĥ + ε, ε = ½ min_{z ∈ L∖Δ}(−ĥ(z))... need min > 0: foreign z with ĥ(z) ≥ 0: z ∈ P, ĥ ≥ 0: z ∈ H⁺ ⟹ z = a ∈ Δ, or z ∈ L∩ℓ ⊆ Δ. So all foreign have ĥ < 0, finite set ⟹ ε > 0 well-defined. ✓✓ 2D proof CONFIRMED SOLID.

Edge case |L| = 3: Δ = P itself; need h > 0 on all 3, h < 0 on ∅ — vacuous; any h positive at the 3 non-collinear points exists ✓. |L| ≤ 2: P not full-dim, excluded by hypothesis.

Also n=1 (reconstructed): P = [p,q], integers p<q. Δ = [q−1, q] ⊆ P, L_Δ = {q−1,q}, h(x) = x − q + 3/2: h(q−1) = 1/2 > 0, h(q) = 3/2 > 0; foreign x ≤ q−2: h ≤ −1/2 < 0. ✓ (Need q−1 ≥ p i.e. |L| ≥ 2 ✓ since vertices are lattice points p<q.)

Lemma 0 equivalence — one more precision: (⟸) given disjoint convs, strict separation theorem: ∃ affine h strictly separating two disjoint compact convex sets: h > 0 on conv(A), < 0 on conv(B) — standard (distance realized, supporting hyperplane midway). ✓ (⟹) immediate. Also note: the equivalence shows the property depends ONLY on the finite set L (not on P) — worth stating: "P is YES ⟺ the finite point set L = P∩Zⁿ admits a subset A which is the lattice-point set of some lattice simplex Δ ⊆ P with conv-separation." Hmm — careful: the property involves Δ's identity via L_Δ; two different Δ could share same L_Δ. Fine.

NOW — also should I double check Thm B: boxes [0,m]^n, m ≥ 1 integer... wait, actually boxes with integer vertices: [0,m]^n. Unit corner simplex conv(0,e₁..eₙ) ⊆ box ✓ unimodular ⟹ L_Δ = {0,e_i} ✓ h = 3/2 − Σx_i > 0 at those (3/2, 1/2) ✓; foreign lattice point in box: some xᵢ ≥ ... any lattice pt ≠ those has Σx ≥ 2 ⟹ h ≤ −1/2 ✓. Solid. General boxes ∏[aᵢ,bᵢ]: translate/scale — translation preserves lattice structure ✓.

Alright. Also the F3 v1 example (环抱四面体 v1): conv(0, e1,e2,e3, (−1,1,1), (1,−1,1), (1,1,−1), (2,2,2)) — will verify computationally.

Let me also reconsider the DEEP CORNER frontier briefly to see if I can crack it analytically today... The setup: simple vertex a, primitive edge directions w₁,w₂,w₃, cone Λ of lattice points in cone-coordinates. Weighted-sum criterion with σ = conv(a, a+tᵢwᵢ): separation achievable IF min{Σαᵢ/tᵢ : α ∈ Λ∖{0, t₁e₁,t₂e₂,t₃e₃}} > 1. Adversarial: D = |det| ≥ 3, (w₁+w₂+w₃)/D integral ⟹ (1/D,1/D,1/D) ∈ Λ, weight 3/D ≤ 1. Question: can another construction save it? This is genuinely hard; leave as open with computational probe if time permits (enumerate D=2,3 triples; but note: for a GLOBAL counterexample you'd need ALL corners deep AND wrap-around killing everything else — F5 random search won't produce that; targeted construction would be needed. Out of scope for this round's remaining budget; document honestly.)

PLAN OF ACTION (writing first!):
1. 工作笔记.md initial entry (plan + audits found: Thm D flaw).
2. proof.md full write (§0–§2 + verification placeholders), SAVE.
3. sep3d.py (exact separation library: lattice-point-in-tetra via Fractions, float LP propose + exact verify both directions).
4. check3d.py (F1, F3-v1, F2 sample, F4 samples, F5 random). Run. Record results.
5. Update proof.md verification section + boxed answer. Final save.
6. Keep appending 工作笔记.md throughout.

Budget discipline: files first. GO.

Actually — one consideration on scope of "形式化验证" requirement: I must verify with computation the KEY branches: (a) 2D theorem engine spot-check via enum (small version — maybe [0,2]^2 grid 9 points, 512 subsets, full check) rather than 65536 if time tight — actually 65536 × cheap check in optimized Python ≈ maybe 1–4 minutes; try full but fall back gracefully. Hmm, the closure step (hull(S)) requires computing hull per subset — 65536 hulls... each tiny (16 pts). Python maybe 30–60 µs each with numpy... more like 1ms with Fractions-free integer hull code → ~65s. OK try. Actually simpler: iterate subsets, compute integer hull closure via cross-product tests; skip supersets... dedupe via frozenset. Fine.

(b) 3D: F1 m=1 full 70; F3 v1 full 495; F5 random 300+100; F2 octahedra: full for ±e_i (7pts, C(7,4)=35), ±√... a=b=c=1 only 35; (1,1,2): pts = 6+1+1=8? ±e₁,±e₂,±2e₃: 8 points, C(8,4)=70; (2,2,2): 25 pts C(25,4)=12650 — heavy; do structured-candidate + sample per notes. (c) certificates from table: verify numerically-exactly each row of the certificate list (octahedra certs, box certs). (d) Thm C instance: random height-1 pyramids. (e) Thm D' criterion demo: the two worked examples.

Let me write everything now. Start with 工作笔记.md.

Note re language: the user-facing notes have been in Chinese; I'll continue in Chinese for consistency.

Let me draft proof.md content carefully.

---

# proof.md draft

# 格点多面体的可分离单纯形问题：当前进展与部分结果

## §0 问题与基本等价

**问题（P）**：设 P ⊂ Rⁿ 为满维凸格点多面体（顶点均为整点），L = P ∩ Zⁿ。是否总存在满维格单纯形 Δ ⊆ P 与仿射函数 h：Rⁿ → R，使得 h > 0 于 Δ 的所有整点、h < 0 于 P∖Δ 的所有整点？

记 L_Δ = Δ ∩ L。

**引理 0（分离形式等价）**: 存在 (Δ,h) 如上 ⟺ 存在满维格单纯形 Δ ⊆ P 使 conv(L_Δ) ∩ conv(L ∖ L_Δ) = ∅。

证：(⟹) h 仿射，h>0 于 L_Δ ⟹ h>0 于 conv(L_Δ)；同理 <0；两张开半平面不交。(⟸) A := L_Δ, B := L∖A 为两个有限不交集，其凸包为紧凸不交集；由两个紧凸集的严格分离定理（取实现距离的中垂超平面方向），存在仿射 h 严格分离二者。∎

推论：性质只依赖有限点集 L（与 P 的具体形状无关，只要 P = conv(L)）；且判据是纯组合几何的。

注记：若允许退化（低维）单纯形则问题平凡（单点即可），故必须满维；若 P 不满维则不存在满维内接单纯形，本文按题意设 P 满维。

## §1 低维情形：n=1,2 恒 YES

### 1.1 n=1

P = [p,q]，p<q 整数。取 Δ=[q−1,q]，h(x)=x−q+3/2。验证：h(q−1)=½>0, h(q)=3/2>0；其余整点 x≤q−2 有 h(x)≤−½<0。∎

### 1.2 n=2 定理 A

[Transcribe the round-6 §2.1 proof — I verified every step above.]

## §2 高维正面结果与边界

### 2.1 定理 B 盒子
### 2.2 定理 C 高度1金字塔
### 2.3 命题 D'（乘积的修正判据）+ 对原 Thm D 证明的勘误
### 2.4 计算验证
### 2.5 boxed 答案

---

For §2.3, write the corrected analysis: necessary-and-sufficient window for tent-family certificates, the refutation of the scaling claim, and the conditional criterion. Also mention my manual YES instances (Q unimodular ×[0,2]; Q=[0,2]-tri ×[0,1]) as computed certificates.

Boxed answer: $\boxed{\text{n=1,2: 恒 YES（已证）；n}\ge3\text{: 开放——未找到反例，所有已验证族均 YES}}$

Now the code. Design sep3d core:

```python
from fractions import Fraction
import itertools, random
from functools import reduce

def hull_closure(S, grid): # add grid points inside conv(S)
    # iterate: a grid point g is in conv(S) iff ... use exact LP? Simpler: incremental —
    # For 16-point grids, do: repeat: for each g not in S: test g in conv(S) via solving LP feasibility with Fractions... expensive.
```

Hmm, hull closure for enum2d over 65536 subsets: testing "point in conv(S)" for each of ≤16 points per iteration — LP feasibility each... too slow pure-Python-Fraction? Feasibility in 2D: point p ∈ conv(S) ⟺ p not strictly separable ⟺ for the polygon hull... Efficient way: compute convex hull of S (integer cross products, monotone chain — fast), then test p in hull polygon (O(log) or O(n) scan). Iterate until stable (each addition enlarges hull; ≤16 iterations but practically few). Monotone chain on ≤16 int points: microseconds. Total ~65536 × few hundred µs ≈ 30 s. OK.

Then for each closed L: find boundary vertices of hull; for each hull vertex a with neighbor edges: get adjacent hull vertices... The theorem's construction: leaf-triangle needs a TRIANGULATION cell — equivalent check per notes: "空角" boundary vertex a: neighbors b,c on hull with conv(a,b,c)∩L={a,b,c}. Then cap lemma: points strictly on a-side of line bc only a. Then Δ = conv(a,u,v), u,v extremes of L∩line(bc)... wait in 2D L∩ℓ is collinear points; extremes = min/max along the line. Construct h and verify exactly. Early accept per config. Count successes; expect 100%.

Wait, subtle: the theorem guarantees existence via triangulation leaf; the constructive check "some empty-corner vertex passes cap+separation" should succeed for EVERY full-dim L with |L|≥3. If some config fails the constructive test, that flags a proof-engine bug (theorem says existence, construction searches all a — should find one). Good verification semantics.

For 3D separation: implement:

```python
def lattice_points_in_tetra(tetra_pts, L): # exact barycentric
    # solve x = Σλᵢvᵢ, Σλᵢ=1, λᵢ≥0 rational; check membership for each candidate lattice point via solving 3x3 linear systems with Fractions
def separated(dir_exists, A, B): # ∃dir: ⟨dir, a−b⟩ ≥ 1 ∀(a,b)
    # scipy linprog: minimize 0 s.t. A_ub dir ≤ −1 ... build matrix of (b−a) rows: ⟨b−a, dir⟩ ≤ −1
    # if status ok: exact-verify with Fraction-rounded dir (use rational approximation: dir floats → Fraction(limit denominator) → rescale so min gap ≥1 exactly)
    # if infeasible: get farkas from dual? HiGHS returns marginals; safer: verify infeasibility exactly via FM elimination on 3 vars? Could be heavy. Alternative: trust-but-verify protocol: if float-infeasible, run exact certificate search: solve Farkas system with Fraction LP... 
```

Simpler bulletproof approach for the NO side: the Farkas certificate y ≥ 0, Σy(a−b) = 0, Σy = 1 — this itself is an LP feasibility in variables y (|A||B| many). Instead: note conv(A)∩conv(B) ≠ ∅ can be decided DIRECTLY by a different exact method: iterated convex-combination... Hmm.

Cleanest exact decision: FM elimination over dir variables (3 vars + maybe γ). Constraints: for all pairs: ⟨dir, a−b⟩ ≥ 1. Variables d1,d2,d3. Eliminate d3: combine rows pairwise (sign patterns): rows count N=|A||B|. After eliminating d3: O(N²) rows; d2: O(N⁴)... N=144 → 20736 → 4×10⁸ too big. BUT with normalization tricks and pruning (remove dominated rows: row (α,β,γ) with constants — dominated if another row has ≥ coefficients and ≥ constant... prune aggressively) it might collapse. Risky.

Better: exact SIMPLEX LP implementation (Fraction, Bland's rule, standard form). Constraints ⟨dir, a−b⟩ ≥ 1 → −⟨dir, a−b⟩ + s = −1... convert: maximize 0 subject to A·dir ≥ 1. Phase-1 simplex with artificials. Sizes: ≤ 200 rows × 3 cols — trivial for simplex. Bland guarantees termination. Implementing bug-free phase-1 simplex in limited time: moderate risk but standard; I'll write it carefully with tests (compare against known cases + cross-check float scipy on random instances).

Actually — hybrid strategy minimizing risk: 
1. Float LP (scipy if available, else implement float simplex... check environment first!) proposes answer.
2. YES-proposals: exact rational verification (rescale dir to clear gap ≥ 1) — fully rigorous ACCEPT.
3. NO-proposals (float infeasible): need rigorous confirmation. Use exact phase-1 simplex ONLY here, or: derive Farkas y from float dual marginals, ROUND to rationals, verify Σy(a−b)=0 & Σy>0 exactly — if verification fails due to rounding, fall back to exact simplex. Dual of "∃dir: M dir ≥ 1" infeasibility: ∃y≥0: yᵀM = 0, yᵀ1 > 0. HiGHS gives equality multipliers; sign conventions fiddly. Plan: implement exact Fraction simplex (phase 1 only, feasibility) as the arbiter; use it ALWAYS (skip float entirely) if instance sizes are small enough — |pairs| ≤ ~150 rows, 3 vars + slacks + artificials ≈ 156 cols: simplex iterations maybe tens — each iteration O(rows×cols) = 30k Fraction ops — fine. 495 tetras × maybe 2 LPs... wait per tetra ONE feasibility LP (∃dir separator). Plus per tetra the lattice-point extraction (small). So F3-v1: 495 LPs × ~50k Fraction ops ≈ 25M Fraction ops... Python Fraction ops are ~µs each → ~30–60 s. Acceptable. F5 300 configs × avg maybe 20 tetras tried (early exit) × 50k = 300M ops... too slow?? Hmm. Optimize: presolve with FLOAT lp first (scipy likely available — check); float YES → exact verify (cheap); float NO → exact simplex confirm (rare — only for genuinely failed tetras; most configs exit early on first success). Random configs: first tetra tried often succeeds → mostly float+exact-verify. Worst case bounded. Also add caching/memoization where easy. And numpy float LP fallback: implement small float simplex myself if scipy absent — check env.

Let me check python/scipy availability first. Then write files in order: 工作笔记.md → proof.md → sep3d/check3d → run → update proof.md.

One more math item for proof.md completeness — the certificate-table entries (from round-6 §2.4): I should re-verify computationally rather than transcribe blindly (round-7 already found cert errors historically). The check3d script will verify each listed (P, Δ, h) exactly. Include: octahedron ±e_i (7 pts, h = x+y+z+½ — wait must check ALL lattice points of P: P = conv(±e₁,±e₂,±e₃); lattice points: origin ± e_i = 7 points. Δ = conv(e₁,e₂,e₃,−e₁): contains 0 (midpoint of e₁,−e₁) → L_Δ = {±e₁, e₂, e₃, 0} (5 pts). h = x₁+x₂+x₃+½: at e₁: 1.5; −e₁: −0.5 <0 ✗!!! WAIT. h(−e₁) = −1 + ½ = −½ < 0 but −e₁ ∈ L_Δ needs POSITIVE. Hmm?! Table says h = x₁+x₂+x₃+½ on Δ = conv(e₁,e₂,e₃,−e₁)... h(−e₁) = −0.5 < 0. BROKEN?? Let me recompute: −e₁ = (−1,0,0): h = −1 + 0 + 0 + 0.5 = −0.5 < 0. Indeed broken! Unless Δ is different... maybe Δ = conv(e₁, e₂, e₃, −e₂)? same issue symmetric. Hmm, maybe the intended Δ = conv(e₁,e₂,e₃, −e₁−e₂−e₃)? Not a lattice point of P. OR the octahedron case: is it even YES? Let me think: 7 points: 0, ±e₁,±e₂,±e₃. Find tetra Δ with L_Δ separable from rest by affine h. Try Δ = conv(e₁, e₂, e₃, −e₁): L_Δ = {e₁,e₂,e₃,−e₁, 0} (0 = midpoint(e₁,−e₁) ✓ inside). Foreign: {−e₂, −e₃}. Separation: need h>0 on 5 pts, h<0 on −e₂,−e₃. Try h = x₁+x₂+x₃+½: −e₂: −0.5<0 ✓; −e₃ ✓; e₁ 1.5 ✓; e₂ 1.5 ✓; e₃ 1.5 ✓; −e₁: −0.5 ✗ FAIL (−e₁ ∈ L_Δ). Try h = x₂+x₃+½: e₁: ½>0 ✓ (e₁ ∈ L_Δ); −e₁: ½ > 0 ✓; e₂ 1.5 ✓; e₃ 1.5 ✓; 0: 0.5 ✓; −e₂: −0.5 ✓; −e₃: −0.5 ✓. ALL PASS!! So correct cert: h = x₂+x₃+½ with L_Δ = {±e₁, e₂, e₃, 0}. The round-6 table cert (x+y+z+½) is WRONG (fails at −e₁) — ANOTHER transcription error caught. My audit instinct was right: verify everything computationally. I'll put corrected certs in proof.md (verified by code).

Similarly ±2e_i octahedron cert h = 1.2x₁+0.9x₂+0.9x₃−1 with Δ = conv(e₁,2e₁,2e₂,2e₃): L_Δ: lattice pts in tetra: e₁, 2e₁, 2e₂, 2e₃ + ? segment e₁–2e₁: no interior lattice pts; faces: conv(e₁,2e₁,2e₂): contains (1,1,0)? barycentric: (1,1,0) = λ(e₁)+μ(2e₁)+ν(2e₂): z: ν·0... (1,1,0) = (λ+2μ, 2ν, 0), λ+μ+ν=1: 2ν=1 ⟹ ν=½; λ+2μ=1; λ=1−μ−½ = ½−μ; ½−μ+2μ = 1 ⟹ μ=½, λ=0: so (1,1,0) = ½(2e₁)+½(2e₂) ∈ face! So L_Δ ⊇ {e₁,2e₁,2e₂,2e₃,(1,1,0)}; similarly (1,0,1) = ½(2e₁)+½(2e₃) ✓ in; (0,1,1) in face conv(2e₂,2e₃,?)... face conv(e₁,2e₂,2e₃): (0,1,1) = λe₁+μ2e₂+ν2e₃, x: λ=0 ⟹ (0,1,1)=(2μ,2ν): μ=ν=½, sum=1 ✓ in. Also interior: (1,1,1)? = combination: solve λe₁+μ2e₁+ν2e₂+ρ2e₃ = (1,1,1), λ+μ+ν+ρ=1: 2ν=1,2ρ=1,λ+2μ=1: ν=ρ=½ ⟹ λ+μ=0 ⟹ λ=μ=0, λ+2μ=0≠1 ✗ not in. Interior (1,1,1) NOT in Δ. Face conv(2e₁,2e₂,2e₃): x+y+z=2 plane: lattice pts there within: (2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1) all in that face ✓ counted. So L_Δ = {e₁,2e₁,2e₂,2e₃,(1,1,0),(1,0,1),(0,1,1)} — 7 pts ✓ matches table's "7 个 L_Δ 点". Cert h = 1.2x+0.9y+0.9z−1: e₁: 0.2>0 ✓; 2e₁: 1.4 ✓; 2e₂: 0.8 ✓; 2e₃ ✓; (1,1,0): 0.1 > 0 ✓; (1,0,1) ✓; (0,1,1): 0.8 ✓. Foreign (rest of 25): (0,0,0): −1 ✓; ±... e₂: −0.1 < 0 ✓; e₃ ✓; −e_i: negative ✓; −2e_i ✓; (2,0,0): 1.4... wait 2e₁ ∈ L_Δ ✓ positive needed ✓; (0,2,0) ∈ ✓; (1,1,1): 1.2+0.9+0.9−1 = 2.0 > 0 ✗!!! (1,1,1) is a lattice point of P (interior of octahedron conv(±2eᵢ)? |x|+|y|+|z| ≤ 2: 3 > 2 — NO, (1,1,1) NOT in P!). Phew. Octahedron L_∞ ball: points with |x|+|y|+|z| ≤ 2: 25 points: all (x,y,z) ∈ Z³ with L₁ norm ≤ 2. (1,1,1) norm 3 excluded ✓. Foreign norms: 0:(0,0,0); norm1: 6 pts ±e_i; norm2: 18 pts: (±2,0,0)×6, (±1,±1,0)-type ×12. Check h = 1.2x+0.9y+0.9z−1 on norm-2 foreigners: (2,0,0)→wait (2,0,0)=2e₁ ∈ L_Δ! Right, it's in Δ. Foreign norm2: (−2,0,0): −3.4 ✓; (0,2,0)=2e₂ ∈ Δ; (0,−2,0): −2.8 ✓; (0,0,−2) ✓; (1,1,0)∈Δ; (1,−1,0): 1.2−0.9−1 = −0.7 ✓; (−1,1,0): −1.3 ✓; (−1,−1,0): −2.2 ✓; (1,0,1)∈Δ; (1,0,−1): −0.7 ✓; (−1,0,1): −1.3 ✓; (−1,0,−1) ✓; (0,1,1)∈Δ; (0,1,−1): −0.1+... 0.9−0.9−1 = −1 ✓; (0,−1,1): −1 ✓; (0,−1,−1) ✓. Norm1: (1,0,0)=e₁∈Δ; (0,1,0): −0.1 ✓; (0,0,1): −0.1 ✓; negatives ✓. Origin: −1 ✓. ALL 25 CHECK. Cert VALID. 

So the ±2e_i cert survives audit; the ±e_i cert needs correction (h = x₂+x₃+½). Code will settle all.

Time to execute. Files:

工作笔记.md entry 1: plan + audits (Thm D scaling flaw; ±e_i cert flaw; Thm C verified solid; 2D proof re-audited solid; Lemma 0 written).

Then proof.md.

Then code. Let me be efficient. First check environment (python3, scipy/numpy availability).scipy available. Good. Now write 工作笔记.md first entry with the audit findings. Key audits I did in my head:

1. Thm C (height-1 pyramid): verified solid. Even improved: ε needs only ε > max(0, −g(a)), no upper bound.
2. Thm D (product): transcribed proof is BROKEN — two flaws: (a) tent admits (w,1)-type violation for ANY m≥1 since g(w)>0 and (w,1) ∉ Δ; (b) scaling g→g/K does NOT open the μ-window because −m₀ scales too. Corrected criterion derived: apex must be over a vertex u with strictly maximal certificate value; window condition m₀ > max(g(v),g(w)) (m=1) resp. m₀ > max(g(v),g(w),g(u)/2) (m≥2) after optimal constant shift c → −min_{L_τ}g. Conditional statement D'.
3. ±e_i octahedron cert from round-6 table: WRONG (h=x+y+z+½ fails at −e₁∈L_Δ). Corrected: Δ=conv(e₁,e₂,e₃,−e₁), L_Δ={±e₁,e₂,e₃,0}, h = x₂+x₃+½. To be machine-verified.
4. ±2e_i cert: audited by hand, survives.
5. 2D proof re-audited line by line: solid.
6. n=1 reconstructed.

Write these to 工作笔记.md now.Now write proof.md immediately. Full structure per §2.6 plan:
- §0: problem + Lemma 0
- §1: n=1 + Thm A (2D)
- §2: Thm B, C, D' (corrected) + computational verification (placeholder to fill) + boxed answer

Write it now, completely.Now write proof.md immediately. Full content per §2.6 plan:
- §0 problem + Lemma 0
- §1 Thm A (n=1, n=2)
- §2 Thm B, C, D' + erratum + computational section placeholder + boxed answer

Let me write it carefully and completely. I'll leave the computational verification section with placeholders to fill after running code.proof.md is saved (with placeholder for verification section). Now write sep3d.py — the exact separation library. Key components:

1. Exact lattice-point-in-tetrahedron test (Fraction barycentric).
2. Exact separation test: conv(A) ∩ conv(B) = ∅ via ∃dir: ⟨dir, a−b⟩ ≥ 1 ∀pairs.
   - Float proposal via scipy linprog.
   - Exact verification: rational rescale of proposed dir.
   - NO side: Farkas certificate — from linprog duals? HiGHS provides marginals. Alternatively implement exact phase-1 simplex as arbiter. Let me implement a small exact simplex too (for the NO side), since sizes are small.

Actually simpler robust plan: implement exact Fraction simplex directly and use it always; use scipy float LP only as prefilter for speed on big instances. Let me write a clean phase-1/primal simplex in standard form:

Problem: does ∃ d ∈ R³ with M·d ≥ 1 (M has k rows)? Equivalent feasibility: minimize sum of artificials s.t. M·d + s·(-1)... Let me set up standard form: variables x = (d1,d2,d3) free → split into d⁺−d⁻? That doubles vars to 6 + slacks. Constraints: M d ≥ 1 ⟺ −M d ≤ −1 ⟺ −M d + t = −1, t ≥ 0 slack. Feasibility of {−Md + t = −1, t≥0, d free}. Phase-1 with artificial r ≥ 0: minimize r s.t. −Md + t + ... hmm need basis: add artificial a: −M d + t − a·? Standard: rows: −M_i·d + t_i − a_i = −1? Then a appears with coefficient −1... make it: M_i·d − t_i + a_i = 1 with t_i ≥ 0 (surplus), a_i ≥ 0 artificial basic. Minimize Σa_i. If min = 0 → feasible (separator exists). Else infeasible.

Sizes: k = |A|·|B| rows, cols = 3(d) + k(slack/surplus) + k(artificial). For k=144: 291 cols × 144 rows. Fraction simplex iterations ~ maybe 50–200; each pivot O(rows×cols)=42k ops → ~8M ops worst per LP. Python Fractions slow-ish but OK if not too many LPs.

Speed strategy: 
- Precompute pair difference vectors once per (A,B).
- Use scipy float first (linprog with bounds d free): if optimal value > tiny margin → propose dir, verify exactly (cheap!). If infeasible per floats → run exact simplex to confirm. If ambiguous (feasible but small margin) → exact simplex.

Exact verification detail: given float dir f ∈ R³, convert each component to Fraction(f_i).limit_denominator(10^6)? Better: use exact rational arithmetic directly on the float's exact binary value: Fraction(f_i) gives exact dyadic rational. Compute gaps g_pair = ⟨frac_dir, a−b⟩ exactly; let m = min gap > 0; then scale dir by 1/m: new min gap = 1 exactly. All exact. ✓

Farkas for NO side: when exact simplex says infeasible, extract certificate: y over pairs with Σy(a−b)=0, Σy>0. Simplex duals give this but bookkeeping is annoying. Alternative NO-side verification that's simpler to trust: after exact simplex reports infeasibility (min Σa > 0 at optimum with Bland termination), the optimality itself is the proof — Bland's rule guarantees no cycling, so the exact tableau IS the certificate (reproducible). To make it auditable, I'll dump the final objective value > 0 plus the primal/dual solution extracted from the final tableau, then verify complementary slackness / duality exactly:
- Extract y ≥ 0 from final tableau (duals for the M d ≥ 1 constraints): yᵀM = 0 and yᵀ1 = w* > 0. Verify these two identities exactly with Fractions — that's an independent, compact certificate! 

Dual derivation: primal (phase-1): min 1ᵀa s.t. M d − t + I a = 1, d free, t,a ≥ 0. Dual: max 1ᵀy s.t. Mᵀy = 0 (from free d), −y ≤ 0 (t), y ≤ 1 (a), y free sign? Careful: constraint rows equalities with rhs 1; variables d free → dual constraint Mᵀy = 0; surplus t ≥ 0 with column −1 → dual constraint −y ≤ 0 i.e. y ≥ 0; artificial a ≥ 0 column I → y ≤ 1. So dual: max 1ᵀy s.t. Mᵀy = 0, 0 ≤ y ≤ 1. Infeasibility of primal ⟺ dual optimum > 0. So Farkas-style certificate: y ∈ [0,1]^k with Σy_i(a_i − b_i) = 0 and Σ y_i > 0. Exactly what we want. Extraction from final tableau: y = c_B B^{-1} restricted appropriately — standard; I'll extract duals from the tableau row under artificial columns... Simpler implementation: solve the DUAL directly with my simplex?? The dual has k variables — worse. 

Alternative pragmatic approach: get y approximately from float LP duals (linprog marginals), round to rationals, verify exactly; if rounding fails, fall back to exact-simplex-extracted duals. Actually simplest reliable: implement exact simplex returning final tableau + basis; duals y = (row0 coefficients on artificial columns) with sign convention depending on formulation. I'll be careful and SELF-TEST the whole pipeline against brute-force cases where ground truth is known by construction (e.g., clearly separable vs clearly intersecting point sets).

Even simpler alternative for NO-side rigor without dual extraction: FM elimination on 3 variables with aggressive pruning. Rows: ⟨dir, v_i⟩ ≥ 1 for pair vectors v_i ∈ Z³. Eliminate d3: for rows with v3 > 0 and v3 < 0 combine; keep v3 = 0 rows. Resulting rows R' (≤ N²/4). Then eliminate d2 similarly, end with constraints on d1 alone: feasible iff max lower bound < min upper bound... wait after eliminating down to 1 var: constraints α d1 ≥ 1 forms: d1 ≥ 1/α (α>0) etc. Feasibility check trivial. Complexity: N=144 → after eliminating d3: up to 5184 rows; prune dominated: row (a,b,c;k) dominates (a',b',c';k') if a≥a',b≥b',c≥c', k≥k' (all constraints normalized same direction ≥). With c now gone... hmm after eliminating d3 the rows live in (d1,d2)-space: (α,β;κ): αd1+βd2 ≥ κ. Prune: remove (α,β,κ) if exists (α',β',κ') ≠ with α'≥α, β'≥β, κ'≤κ. Pruning via sort + sweep: O(R log R). Could still blow: 5184 rows → eliminate d2 → up to 6.7M combos — too many before pruning. Prune between eliminations helps but worst case still bad. Skip FM; go with exact simplex + self-tests.

Let me also think about performance for the enumeration loops:

check3d families:
- F1 m=1: cube [0,1]^3, L = 8 pts. All C(8,4)=70 tetras. Each tetra: compute A=L∩Δ (barycentric), B=complement, separation test. Early exit YES.
- F3-v1: 环抱四面体 conv{0,e1,e2,e3,(−1,1,1),(1,−1,1),(1,1,−1),(2,2,2)} — 12 points? Count listed: 0,e1,e2,e3 = 4, plus 3 negatives-ish = 7, plus (2,2,2) = 8. Hmm "L 约 12 点" — the hull closure will add grid points inside conv of these 8! E.g., (1,1,1) might be inside conv{(1,1,-1),(2,2,2),...}. Need hull-closure step like enum2d: P = conv(S), L = grid points in box ∩ P. Grid: bounding box of S: x∈[−1,2], y∈[−1,2], z∈[−1,2] → 4³=64 candidate pts; test membership in conv(S) exactly (LP or hull facets). Point-in-convex-polytope via facet halfspaces: compute convex hull facets (triples) of S, check all points on same side. Implement integer hull (monotone-chain style in 3D: enumerate all triples forming faces via support tests). |S|=8 → C(8,3)=56 triples, each test O(|S|) → trivial.
- F5 random: subsets of [0,2]^3 (27 pts) size ~8, close hull, enumerate.

Tetra containment: any 4 non-coplanar points of P give Δ ⊆ P ✓ (convexity). But ALSO must ensure Δ∩P-lattice computed right — A := L ∩ Δ where L is the config's full lattice set. Barycentric coordinates solve 3×3 system with Fractions: λ = T⁻¹(p − v₀); check λᵢ ≥ 0, Σλᵢ ≤ 1 (with Σλ = 1 automatically).

Full-dim requirement: det ≠ 0.

Also dedupe configs via frozenset.

Early-exit ordering heuristic: try tetras containing envelope vertices first ("角形单纯形优先" per notes). Simple version: shuffle but put tetras with ≥3 extreme points first. Or just natural order; fine.

Now enum2d.py: subsets of 16-pt grid [0,3]^2. Closure: hull of S ∩ grid. Hull in 2D: monotone chain with integer cross products; point-in-hull: boundary or inside via cross tests against hull edges (O(h)). For 65536 subsets: skip empty/too-small; require |closed L| ≥ 3 non-collinear. Then theorem-engine constructive search: for each hull vertex a (of closed L), neighbors b,c (hull adjacent vertices); check corner emptiness conv(a,b,c)∩L={a,b,c}... WAIT. The theorem uses triangulation leaf cells, NOT arbitrary corner triangles — §5 correction #1 of round-8 notes says exactly this: must check conv(a,b,c)∩L={a,b,c} (empty corner) which reproduces leaf-triangle vertices situation. Then cap lemma check: lattice points strictly a-side of line bc: only a. Note: with the empty-corner condition, the tangent cone argument works: ab, ac are boundary edges (a is a hull vertex, b,c its hull neighbors ⟹ segments ab, ac lie ON hull boundary ⟹ are the two edges at a). Empty corner ⟹ T∩L={a,b,c} ⟹ lemma holds ⟹ cap contains only a strictly positive side. Then Δ = conv(a,u,v) with u,v extremes of L∩line(b,c) — note line through b,c may contain other lattice points beyond b,c (collinear patch). Construct η (height fn wrt ℓ, positive at a) and h = η+ε, verify EXACTLY on all points of L: positive on L∩Δ, negative elsewhere. Also verify (Q)-style: conv(A)∩conv(B) disjoint via the explicit h (that's implied by sign conditions). Count PASS/FAIL. Expect all pass. This validates the 2D engine exhaustively over 65536 configs.

Cost: 65536 × (closure ~16 hull ops + few vertex checks) — Python maybe 60–180 s. Acceptable; run in background while doing 3D? Sequential is fine.

Optimization for enum2d: many subsets share closures; dedupe by frozenset(L) BEFORE running engine (compute closure, store unique L sets, run engine per unique L). Number of unique closed subsets of [0,3]^2 much smaller than 65536 (maybe a few thousand). 

Implementation order: sep3d.py (library: exact simplex, separation, lattice tools, hull tools) → quick self-test → check3d.py (families) → run → enum2d.py → run → update proof.md.

Let me write sep3d.py now. Careful with the exact simplex implementation.

Exact simplex (Fraction, tableau form, Bland):

Standard form: min cᵀx s.t. Ax = b, x ≥ 0. Phase 1: add artificials. Implementation plan:

```python
def simplex_solve(A, b, c):
    # min c^T x, Ax=b, x>=0, b>=0 assumed (flip rows)
    # returns (opt_value, x, status)
    m, n = A.shape conceptually (lists of lists of Fraction)
    # phase 1: append identity artificials, basis = artificials
    # pivot with Bland: entering = smallest index with reduced cost < 0; leaving = min ratio, tie -> smallest basis index
```

I'll write it carefully with plain lists. Sizes small. Bland guarantees termination.

For our LP: variables z = (d1,d2,d3, t_1..t_k, a_1..a_k); constraints: M_i·d − t_i + a_i = 1 (i=1..k) where M_i rows = (a_j − b_j) vectors... wait direction: want ⟨dir, a−b⟩ ≥ 1: M_i = a_i − b_i, constraint M_i·dir ≥ 1 ⟺ M_i·dir − t_i = 1 − ... with t ≥ 0: M_i·dir − t_i + a_i = 1. Yes.

c = 0 except artificial cost 1. Initial basis: artificials (coefficient +1, rhs 1 ≥ 0 ✓).

Phase-1 optimum 0 ⟺ feasible ⟺ separator exists ⟹ extract dir from solution. Optimum > 0 ⟺ infeasible ⟹ extract duals y for certificate.

Dual extraction from final tableau: reduced costs row (row 0) values under original columns: for constraint-attached variables... Standard result: duals y = −(row0 entries under artificial columns) when artificials formed identity... Let me define precisely: tableau row0: z + Σ_j \bar c_j x_j = \bar z... I'll derive: with initial basis artificials, row0 = cᵀ − c_BᵀB⁻¹A. At optimum, duals π = c_BᵀB⁻¹ satisfy: reduced cost of col j = c_j − πᵀA_j. Artificial col j has A_j = e_i, c_j = 1: reduced cost = 1 − π_i. Dual variable for constraint i is π_i. From final row0 entry under artificial i: rc_i = 1 − π_i ⟹ π_i = 1 − rc_i. Then verify: πᵀA = ... check π ≥ 0? At optimum for phase-1: dual feasibility: rc_j ≥ 0 ∀j. For structural columns: c_j=0: rc_j = −πᵀA_j ≥ 0. Constraint: πᵀ M-cols: for d-columns (free? NO — in my setup d is NOT split into free parts; d columns have entries M_i but d must be FREE variables, not ≥ 0!!)

PROBLEM: standard simplex needs x ≥ 0. dir is free-signed. Split d = d⁺ − d⁻ with d± ≥ 0: columns ±M_i. Then rc_{d+} = −πᵀ(+M-col) ≥ 0 and rc_{d−} = +πᵀM-col ≥ 0 ⟹ πᵀM_col = 0 ✓ exactly the dual condition Σ_i π_i (a_i−b_i) = 0. And π_i = 1 − rc_{art i}; rc_art ≥ 0 ⟹ π_i ≤ 1; π ≥ 0 needed: from t-column: rc_t = 0 − πᵀ(−e_i) = π_i ≥ 0 ✓. So certificate: π ≥ 0, πᵀ(diff matrix) = 0, Σπ = phase1 opt > 0. And Σπ = 1ᵀπ = dual obj = primal opt > 0 ✓. 

So: extract π from row0 artificial entries; verify exactly: (i) all πᵢ ≥ 0; (ii) Σ πᵢ (aⱼ − bⱼ) = 0 vector for each of 3 coords; (iii) Σπᵢ > 0. These checks are independent of simplex correctness — perfect audit chain.

Also YES-side: solution d* from tableau (basic values); exact verify min gap ≥ 1 after scaling. Independent check again. The simplex itself just needs to terminate correctly per Bland — and both outcomes get INDEPENDENTLY verified, so even a buggy simplex can't fool us (worst case: wrong "infeasible" claim would fail certificate generation; wrong "feasible" would fail exact gap verification). Bulletproof design. If verification fails → raise loudly.

Point-in-tetrahedron exact: given tetra verts p0..p3 (integer), point q integer: solve q − p0 = λ1(p1−p0)+λ2(p2−p0)+λ3(p3−p0) via Cramer with Fraction determinants; inside iff all λ ≥ 0 and λ1+λ2+λ3 ≤ 1. degenerate: det=0 → skip (not full-dim).

Hull machinery 3D: facets of S (integer points): triples (p,q,r) whose supporting plane has all other points on one side AND the triangle is "extreme" (all strictly on one side or coplanar-with-inclusion...). Simple approach: for each triple with nonzero area, compute plane orientation n·(x−p); if all other points satisfy n·(x−p) ≤ 0 or all ≥ 0 (allowing =) then it's a facet-supporting triangle... but coplanar composite faces produce redundant triangles — harmless for membership testing (union of facet triangles = boundary; interior test: point inside iff for EVERY supporting triple's plane it's within the halfspace... actually membership: p inside conv(S) iff for all facet planes, signed dist ≤ 0 (taking outward normals). Collect planes: for every triple that is a face of the hull (supporting), the plane divides; p inside iff no plane has p strictly outside on the negative side of some outward normal. Redundant coplanar triples don't hurt. So: planes = {(n, c)} collected from supporting triples (dedupe by normal direction & offset). Membership test: ∀planes: n·q ≤ c or n·q ≥ ... normalize outward: store (n, d) meaning outward n with n·x ≤ d for all x∈S; q inside iff n·q ≤ d ∀. Coplanar-boundary ok. ✓

Grid closure: L = {g ∈ bbox grid : g inside conv(S)} — includes S itself. ✓

2D analogues similar (monotone chain).

Config canonicalization: frozenset of tuples.

Family definitions (check3d):
- F1: cube unit: S = [0,1]^3 grid (8 pts) — closed already; full sweep 70.
- F3-v1: S = {0,e1,e2,e3,(−1,1,1),(1,−1,1),(1,1,−1),(2,2,2)}, close → expect ~12 pts; full sweep C(12,4)=495.
- F3 variants: parametrized per notes §2.5 table: core {0,e1,e2,e3} + one attachment per facet: x=0 face attachments {(−1,0,0),(−1,1,0),(−1,1,1),(−2,1,1)} and permutations; face x+y+z=1 attachments {(1,1,1),(2,2,2),(1,1,2)}. Generate single-attachment configs (core+1 pt = 5 pts) and maybe pairwise combos capped. Full sweeps where ≤ 12 pts.
- F2 octahedra: (a,b,c) ∈ {1,2}³: conv(±ae₁,±be₂,±ce₃): sizes 7,8,9,25... (1,1,2): 6+2 = 8 pts (lattice pts: all |x|≤...: for a=1,b=1,c=2: L₁-ball radius mix — actually octahedron conv(±e1,±e2,±2e3) lattice points: count via membership: bbox grid test. Sweep if ≤ 10 pts fully (C(10,4)=210); (2,2,2) 25 pts: structured candidates only + random sample 4000.
- F4: square pyramid apex (0,0,1) over [0,2]²: S={(0,0,0),(2,0,0),(0,2,0),(2,2,2→no apex (0,0,1))}: P=conv((0,0,0),(2,0,0),(2,2,0),(0,2,0),(0,0,1)); close: grid bbox [0,2]³ → find L (should include (1,0,0),(0,1,0),(1,1,0),(0,0,1),(1,0,... z=1 layer: cross-section at z=1 is apex only; z∈(0,1): none lattice; so L = base 9 pts + apex = 10 pts). Thm C applies (base 2D polygon YES, height 1) → expect YES; verify by sweep C(10,4)=210.
  - prism [0,2]²×[0,1]: 18 pts: C(18,4)=3060 sweeps × LP — heavy-ish but with early exit likely fast; try with cap & sampling fallback. Also Thm D'-instance certs verified separately.
- F5: random subsets of [0,2]^3 grid: 300 configs size 6–9, closed; sweep with early exit (most succeed instantly). Plus [0,3]^3 sparse: 100 configs of ~10 pts from 64-grid, closed, sweep capped.

Runtime guards: global time budget per family; report counts.

Alright — also enum2d.py as designed.

One more thing: "禁止搜索题目文本" — no web use anyway. Fine.

Write sep3d.py now.I wrote sep3d.py but it has a bug I introduced: in `separator_exists_exact`, the row construction has a weird line:

```python
row[k + i if False else 6 + i] = Fraction(-1)          # t slot
```

That's `6 + i` always — OK functionally but ugly. Also n_cols = 6 + 2k, and columns: d+ (0..2), d− (3..5), t (6..6+k−1), art (6+k..5+2k). Row: [v for v]+[−v] gives 6 entries; then zeros of length k; then set index 6+i to −1 — WAIT index 6+i is within the t block only if the row list currently has 6+k entries... Let me recount: after `[Fraction(0)] * k` the row has 6+k entries; setting row[6+i] = −1 sets t_i ✓; then append art? No — I do `row[6 + k + i] = Fraction(1)` but the row only has 6+k entries at that point! Index 6+k+i is OUT OF RANGE → IndexError. Bug! Need to extend with another k zeros before. Let me fix.

Also in `config_is_yes` there's leftover junk (`len(tetas_sample_guard(tetas))` nonsense). Clean up.

Also the simplex() phase-2 code has a weird dead line:
```python
T, basis2, obj2 = pivot(...) if False else (None, None, None)
```
and then manual loop — fine but ugly. The bigger issue: in phase-2 I truncated rows T[i][:n] + [rhs] — correct. But basis indices >= n that couldn't be pivoted out (degenerate artificial still basic at zero) — I attempt pivot on any nonzero original column; if all zero, row is all-zero → drop? If row is all zeros with rhs 0, we can just delete the row. My current code leaves basis2[i] = artificial ≥ n which then breaks cb lookup (cost2 index out of range). Need to handle: drop such rows entirely.

Let me rewrite the file more carefully and cleanly. Also self-test immediately on trivial cases.

Also one subtle thing in simplex(): Bland's rule needs consistent smallest-index entering AND smallest-index-basis tie-breaking for leaving — implemented. Termination guaranteed.

Another subtlety: phase 1 optimum > 0 → "infeasible" — duals π = 1 − rc_art. But careful: rc computed w.r.t. phase-1 cost including ALL columns; π_i = 1 − row0[n+i]. Then certificate checks are independent anyway. Good.

But wait — there's an important correctness point: when float LP says feasible with exact-verifiable direction, fine. When float says infeasible (status 2), I skip to exact LP which will confirm via Farkas. When float status==0 but exact copy fails → fall through to exact LP → should return feasible via simplex with proper gap ≥1 assertion. All paths certified. Good.

One more design check: `config_is_yes` — the case len(Aset)==n means Δ contains ALL lattice points; complement empty; h<0 vacuous; any h>0 works → YES trivially. Actually can that happen with full-dim tetra ⊇ L but conv(L) bigger than tetra? If Aset == L, then conv(L) ⊆ tetra ⊆ P = conv(L) ⟹ equality. Possible for small configs (e.g., |L|=4 non-coplanar: P itself is a tetra). Then YES trivially (Δ=P, h positive at 4 points). Keep as YES — return True with note. My current code does `continue`!! That's wrong-ish: skipping means we might end up returning False ("all-failed") even though this tetra was a winner... no wait — if some tetra covers everything, other tetras likely separate. But cleanest: treat as immediate YES (vacuous complement). Fix: return True.

Hmm wait, actually also need care: B empty → separation vacuous YES. Yes return True.

Let me rewrite sep3d.py cleanly now.There are still issues in my phase-2 basis cleanup code — that weird line:

```python
rows = [[rr[j] and 1 or 0] and rr for rr in rows]  # noop guard
```

That's nonsense leftover. And the pivot-onto-column logic is convoluted and buggy (it modifies rows while iterating and the newr reference comparison is wrong). Let me rewrite `feasibility_lp`'s phase-2 cleanup properly:

```python
    # phase 2: drop artificial columns; remove rows still carrying a basic artificial
    keep_rows = []
    keep_basis = []
    T2rows = [r[:6+k] + [r[-1]] for r in T]
    for i, bc in enumerate(basis):
        if bc < 6 + k:
            keep_rows.append(T2rows[i]); keep_basis.append(bc)
        else:
            # artificial still basic (value 0); try pivoting to an original column
            pivoted = False
            for j in range(6 + k):
                if T2rows[i][j] != 0:
                    p = T2rows[i][j]
                    newr = [x / p for x in T2rows[i]]
                    # eliminate col j from all kept rows
                    for r2 in range(len(keep_rows)):
                        f = keep_rows[r2][j]
                        if f != 0:
                            keep_rows[r2] = [x - f * y for x, y in zip(keep_rows[r2], newr)]
                    keep_rows.append(newr); keep_basis.append(j)
                    pivoted = True
                    break
            if not pivoted:
                # row must be identically zero with rhs 0 → drop
                assert all(x == 0 for x in T2rows[i]), "inconsistent system"
                continue  # but careful: we already skipped eliminating this row from kept rows — it wasn't in kept rows, fine
    ...
```

Wait, subtle: if the artificial row is dropped, kept rows don't need elimination against it (it was never in kept set). But if it pivots onto column j, kept rows need elimination. Also the rhs of newr must be 0 (artificial basic at zero level) — fine either way.

Hmm wait, actually there's an important subtlety: an artificial basic variable could be at a NONZERO level if obj1 == 0? No — if obj1 = Σ artificial values = 0 and all artificials ≥ 0, every artificial is 0. ✓ So rhs is 0 for those rows. Good.

Let me rewrite the whole feasibility_lp function cleanly. Actually, let me just rewrite sep3d.py's feasibility_lp via edit. Then run self-tests:

Test 1: separable sets: A = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)], B = [(2,0,0),(0,2,0),(0,0,2)] → expect YES.
Test 2: intersecting: A = [(0,0,0),(2,0,0)], B = [(1,0,0),(3,0,0)] → conv segments overlap at (1,0,0)… conv(A)=[0,2]×{0}, conv(B)=[1,3]×{0} — intersect → expect NO.
Test 3: touching at boundary point: A = [(0,0,0),(1,0,0)], B=[(1,0,0),(2,0,0)] share point (1,0,0) → convs intersect → NO.
Test 4: A = [(0,0,0),(1,0,0)], B = [(2,0,0)] → YES.
Test 5 (random cross-check vs scipy): random small sets, compare separator_exists_exact verdict with a float-based independent check (e.g., scipy LP on both formulations) — just consistency YES/NO.

Also test lattice_points_in_tetra: unit corner tetra vs points (0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0)→outside,(1,1,1)→outside, (0,0,... (1/2 stuff not integer. Test tetra conv(000,200,020,002): contains (1,1,0)? barycentric: (1,1,0) = λ1(2,0,0)+λ2(0,2,0)+λ3(0,0,2): 2λ1=1,2λ2=1,λ3=0, sum=1 ✓ inside (face). Contains (1,1,1): λ sum = 1/2·3 = 1.5 > 1 → outside ✓.

And close_config: cube corners 8 → 8 pts; F3-v1 S → expect the closure adds (1,1,1)? Let me think: S = {(0,0,0),(1,0,0),(0,1,0),(0,0,1),(-1,1,1),(1,-1,1),(1,1,-1),(2,2,2)}. Is (1,1,1) ∈ conv? Probably yes (mix of (2,2,2) and (0,0,0) region...). (1,1,0)? (1,0,1)? (0,1,1)? (1,0,0)∈S... (2,2,1)? etc. Code will tell.

Fix the file first.Also fix the placeholder line in feasibility_lp:

```python
    x = [Fraction(0)] * (6 + k)
```
should be k_keep. And remove the weird `d = tuple(x[0] - x[3], )` placeholder line.Small bug in my test script: `(None,None)]*3+(0.0,1.0)` — list + tuple. Fix to `+ [(0.0,1.0)]`.

Good news so far:
- All directed cases pass.
- Barycentric membership correct.
- Cube closure correct.
- F3-v1 closure = 12 points exactly as predicted ("L 约 12 点") ✓ — includes (0,0,1),(0,1,0),(1,0,0),(0,1,1),(1,0,1),(1,1,0),(1,1,1) etc.

Fix and rerun the random cross-check part.600 random trials, 0 mismatches with independent float reference, 440 YES / 160 NO — both branches exercised heavily (Farkas path used 160 times successfully). The separation oracle is trustworthy.

Now write check3d.py implementing the F1–F5 families. Design:

- F1: [0,1]^3 cube (8 pts): full sweep C(8,4)=70.
- F1b: [0,2]^3 box (27 pts): verify Thm B certificate exactly + config_is_yes early-exit.
- F2: octahedra conv(±a e1, ±b e2, ±c e3), (a,b,c) ∈ {1,2}³: compute L via closure from vertices; full sweep if C(|L|,4) ≤ ~20000 else sample 4000 + structured candidates. Also verify the table certs for ±e_i and ±2e_i.
- F3: 环抱四面体 v1: full sweep 495. Plus single-attachment family: core {0,e1,e2,e3} + one attachment per facet list; each closed config ≤ maybe 7-9 pts, full sweeps. Pairwise combos where size allows (cap).
- F4: square pyramid apex (0,0,1) over [0,2]^2 base (10 pts) full sweep 210; [0,2]²×[0,1] prism (18 pts): structured candidates + sample 3000; product certs (D'-instances) verified point-by-point.
- F5: random subsets of [0,2]^3 grid: 300 configs sizes 6–10 → close → sweep early-exit; sparse [0,3]^3: 100 configs of 10 random pts → closure |L| ≤ 16ish → sweep with cap/sample.

Certificate verification helper: given P-lattice set L, tetra verts, h coeffs (rational), check sign conditions exactly.

Also record per-family: #configs, #YES, #FAIL (with details), #skipped/timeout.

Important: a "NO" from config_is_yes means genuine counterexample candidate (all tetras certified non-separable). If that happens, dump full detail.

Time management: F5 300 configs × early exit usually first few tetras... but worst case a config where NO is real would sweep ALL C(n,4). With n≈10–14 closed configs, C(12,4)=495 LP-ish checks each involving scipy call (~1ms) + occasionally exact simplex (slow!). Exact simplex only invoked when float says infeasible — for genuinely failed tetras. If a config has many failing tetras before first success, exact LPs could pile up (each maybe 0.1–2 s in Fractions for k~100 rows... hmm risky). Mitigation: order tetras to try likely winners first? Heuristic per notes: prefer tetras containing envelope/extreme points. Simple improvement: sort candidate tetras by number of hull vertices among their 4 points descending. Hull vertex set from hull_planes supporting points... simpler: extreme = points appearing in some facet triple. Compute once per config.

Also add memo: separator_exists_exact results keyed by frozenset(A)|frozenset(B)? Different A/B pairs recur across tetras within same config (same complement sets). Cache dict on (Aset_frozen, Bset_frozen) — cheap win.

Let me also include in check3d.py the §4.2 certificate table verifications:
1. Box [0,m]^n for n=1..6, m=1..3: unit corner simplex + h=3/2−Σx: verify all lattice pts signs (enumerate lattice pts via itertools product over ranges — for n=6,m=3: 4^6=4096 pts fine).
2. ±e_i octa: corrected cert h=x2+x3+½, Δ=conv(e1,e2,e3,−e1), verify L_Δ membership via barycentric + signs on all 7 pts.
3. ±2e_i octa: cert 1.2x+0.9y+0.9z−1 as Fractions (6/5, 9/10, 9/10, −1), Δ=conv(e1,2e1,2e2,2e3), all 25 pts: lattice-in-tetra then signs.
4. [0,2]^3 + 三棱柱: unit corner certs.
5. Product instances: unimod tri ×[0,2] (9 pts) cert; conv{00,20,02}×[0,1] (12 pts) cert.
6. Thm C instance: pyramid over random 2D polygon with height 1: construct from Thm C proof: pick base polygon e.g. conv{(0,0),(3,0),(1,2)} (lattice pts: (0,0),(1,0),(2,0),(3,0),(1,1),(2,1),(1,2)) apex (2,3)... wait apex must be lattice at height 1: apex=(2,1)?? no — apex is (a,1) in R³ with a any lattice pt of plane z=0. Take apex ((1,1),1)=(1,1,1). Base winning pair: τ=conv{(0,0),(1,0),(0,1)}, g=1−x−y? g>0 on L_τ={00,10,01}: g=1−x−y gives 1,0,0 — not >0! Need strictly positive: g=2−2x−2y? At (1,0): 0 ✗. g=3−2x−2y: 3,1,1 >0 ✓ foreign: (2,0):−1,(3,0):−3,(1,1):−1,(2,1):−3,(1,2):−5 <0 ✓. So pair works. Then pyramid YES by theorem — machine-check directly too (compute L of pyramid, run config_is_yes).

That's a good spread. Write check3d.py now.

Also plan runtime guards: overall time budget printouts per family. Use sys.setrecursionlimit not needed. Let me write it.There's a leftover broken line in section_certs:

```python
    L7 = [(0,0,0)] + [(s*1 if i==j else 0) for j in range(3)] for s,i in [(1,0),(-1,0),(1,1),(-1,1),(1,2),(-1,2)]
```

This is a syntax error. I immediately redefine L7 properly on the next lines, so delete the broken line. Also in f2_octa there's a dead loop `for j,s,m in ...: pass` — remove. Let me fix both.Two issues:

1. **CERT FAIL unimodTri×[0,2]**: my hand certificate h = −½(x+y) −¾z + 1 fails at (0,0,2): h = 0 − 1.5 + 1 = −0.5 < 0. But (0,0,2) should be IN the tetra Δ = conv(000,100,010,002) — it's the apex vertex! The verify function says "should-be-negative" meaning (0,0,2) wasn't detected inside the tetra. Wait — the error says ('should-be-positive', (0,0,2), −1/2): so (0,0,2) IS in `inside` (it demands positive) and h(0,0,2) = −¾·2 + 1 = −0.5 < 0. VIOLATION of my hand cert!

Let me recompute my earlier manual check: I claimed h = −0.5(x+y) −0.75z + 1 with 002: −0.5 < 0... wait in my earlier scratch I wrote "002: −0.5<0✓" — I listed 002 as FOREIGN! But 002 is a VERTEX of Δ = conv(000,100,010,002)!! I made an arithmetic slip in my head earlier: I checked "h(001) = 0.25 > 0" and "002: −0.5" treating 002 as foreign — but it's the apex of the tetra. My earlier scratch was WRONG: with Δ = conv(000,100,010,002), L_Δ = {000,100,010,001,002} (001 on the vertical edge) and 002 needs POSITIVE. h(002) = −1.5+1 = −0.5 < 0 ✗. So my "verified" instance cert is bogus — the machine caught ME making exactly the class of error I was auditing for. Beautiful — the verification protocol works.

Is unimodTri×[0,2] still YES? Need a different Δ/cert. Let me think: 9 points: (0,0,k),(1,0,k),(0,1,k) for k=0,1,2.

Try Δ = unit corner conv(000,100,010,001): L_Δ = 4 pts. Foreign: 5 pts: (1,0,1),(0,1,1),(0,0,2),(1,0,2),(0,1,2). By x↔y symmetry h = a(x+y) + bz + c: conditions: c>0; a+c>0; b+c>0; violators: (1,0,1): a+b+c<0; (0,0,2): 2b+c<0; (1,0,2): a+2b+c<0. Try c=1, b=−0.75: 2b+c=−0.5<0 ✓; b+c=0.25>0 ✓; a+1>0 ⟹ a>−1; a+b+1<0 ⟹ a<−0.25; a+2b+1<0 ⟹ a<0.5. So a∈(−1,−0.25): a=−0.5: h=−0.5(x+y)−0.75z+1. Check: 000:1>0 ✓; 100/010: 0.5>0 ✓; 001: 0.25>0 ✓; 101: −0.5−0.75+1=−0.25<0 ✓; 011 ✓; 002: −0.5<0 ✓; 102: −0.5−1.5+1=−1<0 ✓; 012 ✓. ALL PASS. So Δ = unit corner (not the long-edge tetra) works with the SAME h I derived before. My scratch had used the right h but paired it with the wrong tetra. Fix the table: Δ = unit corner conv(000,100,010,001), same h. Machine will confirm.

2. **config_is_yes returns 2 values, not 3** — I defined it returning `(res, info)` in the rewritten sep3d.py. Fix sweep_config unpacking: `res, info = config_is_yes(...)`; checked = info.get("checked", info.get("timeout", info.get("all_failed",0))).

Let me fix both files.Very interesting results! Let me analyze:

1. Certificate table: ALL PASS (after my fix).
2. F1–F4: all YES.
3. **F5 found a NON-YES config**: S = [(0,0,0),(1,0,1),(1,1,1),(2,0,2),(2,1,2),(2,2,2)] closes to L = {(0,0,0),(0,1,0),(0,2,0),(1,0,1),(1,1,1),(1,2,1),(2,0,2),(2,1,2),(2,2,2)} — 9 points, and `{'all_failed': 0}` — WAIT, 'all_failed': 0 means ZERO tetras were checked?! That's wrong — it returned False with all_failed=0, meaning the loop never ran a single successful check... Looking at config_is_yes: for each tetra, if lattice_points_in_tetra returns None (degenerate) we `continue` — if ALL C(9,4)=126 tetras are degenerate, checked stays 0 and we return False "all_failed". 

Is that plausible? The L here is a planar-ish configuration? Points: (x,y,z) with pattern x∈{0,1,2}, z=x, y arbitrary... look: (0,0,0):z=0=x ✓; (0,1,0) ✓; (0,2,0); (1,0,1): z=1=x; (1,1,1); (1,2,1); (2,0,2); (2,1,2); (2,2,2). ALL points satisfy z = x!! The whole configuration lies in the plane x−z=0 — it's a 2D config in 3D space! P is NOT full-dimensional. close_config produced a degenerate (flat) polytope.

So this "NON-YES" is just a lower-dimensional P (violates the problem's full-dim hypothesis). My random sampler picked 6 points on a common plane by chance? S = {(0,0,0),(1,0,1),(1,1,1),(2,0,2),(2,1,2),(2,2,2)} — indeed all satisfy x=z. Probability of that from random sampling of 27 grid points... suspicious but possible (C(27,6) huge, but plane x=z contains exactly 3 pts per... grid [0,2]³ has 3 points with x=z per y-value × 3 y = 9 points; choosing all 6 from those 9: probability = C(9,6)/C(27,6) ≈ 84/296010 ≈ 2.8e-4 — unlucky-lucky. Whatever, it happened.)

Fix: in f5_random (and sweep generally), require closed L to be FULL-DIMENSIONAL (check via hull_planes nonempty / rank of point differences). Skip flat configs (they violate problem hypotheses). Also sparse family already filters len(L)>18 but not dimensionality — add dimension check there too (43 YES out of ~80: many were skipped silently due to len filter or sampled cap inconclusive... it says non-yes/inconclusive=0, fine).

Also note F5 sparse: 43 YES out of 80 attempted — rest were filtered (len(L)<4 or >18). Fine.

Add a dim check helper: full-dim iff max over coords of (max−min)... no — need affine rank of difference set = 3. Compute via integer rank of 3×3 minors: pick p0, find rank of vectors {p−p0} = 3.

Then rerun F5 with more trials (say 600) to be thorough. Also rerun sparse with dim check.

One more consideration: `config_is_yes` returning False with all_failed=0 for degenerate configs would be a false counterexample report — guard against it inside config_is_yes too: assert dimension ≥ 3 before sweeping (raise or return special value). I'll add a dim check at the top of sweep_config and skip with an explicit "FLAT" tag.

Let me patch check3d.py: add `def full_dim(L)` using det3 minors over first point; use in f5 loops + sweep_config.My edit removed the trailing newline and merged two lines. Fix line 118 area.F5 clean now: 600 configs in [0,2]³ → 292 full-dim YES, 0 non-yes (308 skipped as flat/small — high skip rate because small random subsets often close to flat or <4 points; fine). Sparse [0,3]^3: 120 → 28 full-dim YES, 0 non-yes.

Hmm, the sparse family only got 28 usable configs. Let me boost that with more trials and larger sample sizes for better coverage... Actually, wait — many skips due to len(L)>18 (9 random points in 64-grid close to big hulls). The notes wanted |L|≤14 full sweeps otherwise sample 5000. My sample=3000 cap is fine.

Let me also run a supplementary decisive experiment per the notes' priority list: **the deep-corner probe** (§4.5) — enumerate primitive triples w1,w2,w3 with D=2,3, build the corner cone configurations (as polyhedra = conv of a few lattice points along rays + maybe more points to make it a bounded P), and test whether SOME tetra separates. But careful: a "corner" alone isn't a polytope; the notes' question was whether the weighted-sum obstruction kills ALL simplex constructions in such cones. A cheap meaningful probe: take the cone C = pos{w1,w2,w3}, truncate at some height by a lattice plane (e.g., take P = conv{0, m1·w1', ...}) hmm — simplest bounded version: P = conv{0, w1+t..., }...

Simpler concrete probe of the adversarial claim: for triples like (w1,w2,w3) = ((1,0,0),(0,1,0),(1,1,D)) hmm let me think about what the adversarial condition means concretely. The condition: D = |det| ≥ 3 and (w1+w2+w3)/D ∈ Z³. Example from round-7 analysis presumably: w_i columns of some matrix with det ±D and column sum divisible by D. E.g., w1=(1,0,0), w2=(0,1,0), w3=(1,1,2): sum=(2,2,2), D=2 → (1,1,1) integral! D=2 though. For D=3: need sum/D integral. E.g., w1=(1,0,0),w2=(0,1,0),w3=(2,2,3): det=3, sum=(3,3,3) ✓ D=3 deep corner!

Probe design: P_t = conv{0, t1·w1, t2·w2, t3·w3} (tetrahedron itself!) plus possibly extra points... If P IS the tetrahedron conv(0, tw's): then L_Δ could be Δ=P itself; complement empty → trivially YES?? No wait — complement empty means separation vacuous, but hold on: if P is a simplex, Δ := P gives L_Δ = L, complement ∅, any h positive on L works → trivially YES. So single tetrahedra are always YES. The interesting case needs MORE lattice points around so the corner isn't the whole story — e.g., the cube-like arrangement where the cone sits at a vertex of a bigger P. That's exactly [0,2]^3 at origin: cone directions e_i (D=1). Deep corner version: P = {x ∈ Z³-ish region} bounded by planes through lattice points... Constructing genuine bounded polytopes where EVERY vertex is a deep corner is the actual counterexample-hunting program — too ambitious for remaining budget. 

The honest scope for §4.5 this round: verify the weighted-sum ADVERSARIAL FACT itself computationally on the example cone w=(e1,e2,(2,2,3)): confirm (a) Λ contains (1/3,1/3,1/3); (b) for all t_i choices in range 1..4, min weight ≤ 1 (criterion fails within this construction family); (c) BUT also check whether truncations of THIS cone admit OTHER separating tetras when embedded in a bounded P. Doable minimal version: P = conv{0, 4e1, 4e2, 4w3'}... hmm w3=(2,2,3) scaled: P = conv{0, 6e1, 6e2, 2·(2,2,3)}? Are those "lattice polytope"? Vertices must be lattice: yes all integral. But its other vertices... it's just a tetra again → trivially YES. To make the corner non-trivial, add the standard trick: intersect cone with box: P = conv{0, N e1, N e2, N e3-ish...} no.

Realistic minimal test embedding the deep corner: P = conv{0, (m,0,0)... } I want a polytope whose tangent cone at 0 equals pos{w1,w2,w3}. Take P = conv{0, w1, w2, w3, s} where s = w1+w2+w3 (a lattice point INSIDE the cone, making P 3D with 5 vertices, tangent cone at 0 still generated by the w's if s beyond... actually adding s inside the cone keeps 0 a vertex with the same tangent cone iff s ∈ interior of cone ✓). With w=(e1,e2,(2,2,3)), s=(3,3,3). P = conv{0,(1,0,0),(0,1,0),(2,2,3),(3,3,3)}: closure adds grid pts; sweep → does ANY tetra separate? This is a genuine 5+ point config with a deep corner at 0. If YES anyway, consistent with "deep corner doesn't kill the polytope". Also try bigger truncations: add multiple points like k·s layers.

Given budget, do: enumerate a handful of deep-corner embeddings:
- w3 ∈ {(2,2,3) [D=3], (1,1,2) [D=2], (1,2,3)?det=... det(e1,e2,(1,2,3))=3, sum=(2,3,3) not div by 3 → non-adversarial control}, truncate with s = w1+w2+w3 and with 2s, plus fill via closure.
Run sweeps. Report.

Also worth running: F2-style octahedron (2,2,2) full sweep was sampled? It says checked 6 → early exit YES. Fine.

And one more valuable exact check: the FULL brute force of cube [0,1]^3 verifying EVERY tetra classification consistency (70 checks both ways) — cheap sanity that "checked 1" early-exit isn't hiding NO-configs... Actually the real guarantee against hidden NOs: config_is_yes returns False ONLY after checking all tetras. Early exit True after 1 is fine. OK.

Also enum2d.py — the notes' spec. Given budget realities (this session already consumed a lot), prioritize: (1) deep-corner probe quick script; (2) enum2d full run (65536 subsets — estimate runtime first on a sample); (3) update proof.md + 工作笔记. Let me do the deep-corner probe + enum2d concurrently? Sequential, keep simple.

enum2d design recap: grid G = [0,3]^2 (16 pts). For each subset S ⊆ G (65536): close: L = S ∪ (G ∩ hull(S)). Dedup frozenset. Require |L| ≥ 3 non-collinear. Engine test: find hull vertex a with neighbors b,c (in closed L's hull) s.t. corner empty & cap lemma holds & constructed Δ separates exactly. Expect PASS for every valid config.

Implementation: 
- hull2d monotone chain returning CCW vertices.
- point-in-convex-polygon for closure: since hull changes as we add points... iterate: compute hull of S; add grid pts strictly inside/on; recompute; until stable.
- engine: for each hull vertex index i: a=V[i], b=V[i−1], c=V[i+1]; empty corner: no L-point in conv(a,b,c) except a,b,c; cap: no L-point strictly a-side of line bc; then u,v = extremes of L∩line(b,c) along direction; η(x) = cross(c−b, x−b)-style signed (positive at a); ε = −min over foreign η / 2... construct h = η + ε with ε = half of min foreign (−η) > 0 required... foreign η < 0 guaranteed by cap lemma (points not in Δ have η<0: those on ℓ are in [u,v] ⊆ Δ; strict side only a). Verify signs exactly over all L.
- PASS if any vertex works.

Cost: 65536 × closure(hull ~8 pts × 16 grid tests) ≈ 65536 × ~50µs–200µs ≈ 10–30 s. Plus dedup reduces engine work. Go.

Write enum2d.py now, then the deep-corner probe (can be inline script appended to 工作笔记 results), then final proof.md update.
#!/usr/bin/env sage
# -*- coding: utf-8 -*-
"""
sage_cross_check.sage —— 用 SageMath 独立复核主反例的承重事实
（与 sympy 脚本相互独立，作为第二 CAS 的交叉验证）

复核内容：
  C1  b = E11 非零、自伴、正规
  C2  σ(b) = {0,1}：det(xI−b) 的根精确落在 {0,1}
  C3  函数演算像 = 对角代数（f(b) 公式 + 到上性）
  C4  φ 保乘、保 *、等距（等距性用随机复值上的算子范数数值复核）
  C5  ψ(λ)=λE12 非零线性但不是 *-同态
  C6  方程 λE12 = diag(α,β) 只有平凡解（符号求解）
  C7  阳性对照：ψ'(λ)=λE11 时非零解存在
  C8  反例 2（λp）与反例 3（λq）同样只有平凡解
"""
import random

print("SageMath 独立交叉验证开始")

Zm = matrix(ZZ, [[0, 0], [0, 0]])
E11 = matrix(ZZ, [[1, 0], [0, 0]])
E12 = matrix(ZZ, [[0, 1], [0, 0]])
E21 = matrix(ZZ, [[0, 0], [1, 0]])
I2 = identity_matrix(ZZ, 2)

def ck(name, cond):
    assert cond, "[FAIL] " + name
    print("  [PASS] " + name)

print("[C1] b 非零自伴正规")
ck("E11 != 0", not E11.is_zero())
ck("b* == b", E11.conjugate_transpose() == E11)
ck("bb* == b*b", E11 * E11.conjugate_transpose() == E11.conjugate_transpose() * E11)

print("[C2] sigma(b) = {0,1}")
x = var('x')
detx = (x * I2 - E11).det().expand()
ck("det(xI-b) = x(x-1)", detx == x * (x - 1))
rts = [s.rhs() for s in solve(detx == 0, x)]
ck("roots = [0,1]", sorted(rts, key=lambda z: RR(z)) == [0, 1])

print("[C3] 函数演算像 = 对角代数")
f0, f1, lam, lmu, al, be = var('f0 f1 lam lmu alpha beta')
fb = f0 * (I2 - E11) + f1 * E11
ck("f(b) == diag(f(1), f(0))", fb == matrix(SR, [[f1, 0], [0, f0]]))
ck("到上: diag(a,b) = a*b + b*(I-b)",
    matrix(SR, [[al, 0], [0, be]]) == al * E11 + be * (I2 - E11))

print("[C4] phi 保乘保*且等距")
g0, g1 = var('g0 g1')
gb = g0 * (I2 - E11) + g1 * E11
ck("(fg)(b) == f(b) g(b)", fb * gb == (f0 * g0) * (I2 - E11) + (f1 * g1) * E11)
ck("conj(f)(b) == f(b)*", fb.conjugate_transpose()
    == conjugate(f0) * (I2 - E11) + conjugate(f1) * E11)
rng = random.Random(int(20260821))
ok = True
for _ in range(300):
    a0 = complex(rng.gauss(0, 1), rng.gauss(0, 1))
    a1 = complex(rng.gauss(0, 1), rng.gauss(0, 1))
    M = matrix(CDF, [[a1, 0], [0, a0]])
    _, S, _ = M.SVD()
    ok &= abs(S[0, 0] - max(abs(a0), abs(a1))) < 1e-9
ck("||f(b)||_op == ||f||_inf (300 组随机)", ok)

print("[C5] psi(lam)=lam*E12 非 *-同态")
ck("线性", lam * E12 + lmu * E12 == (lam + lmu) * E12)
ck("乘法性失败: E12^2 == 0 != E12", E12 * E12 == Zm and E12 != Zm)
ck("保*失败: E12* == E21 != E12",
    E12.conjugate_transpose() == E21 and E21 != E12)

print("[C6] 关键方程只有平凡解")
X = lam * E12
eqs = list((X - matrix(SR, [[al, 0], [0, be]])).list())
sol = solve(eqs, [lam, al, be], solution_dict=True)
ck("唯一解 lam=alpha=beta=0",
    len(sol) == 1 and sol[0][lam] == 0 and sol[0][al] == 0 and sol[0][be] == 0)

print("[C7] 阳性对照")
ck("E11 幂等且自伴 => psi' 是 *-同态", E11**2 == E11 and E11.conjugate_transpose() == E11)
ck("psi'(1) = E11 = id(b) != 0", 1 * E11 == E11 and E11 != Zm)

print("[C8] 反例 2 与反例 3")
p = (1 / 2) * matrix(QQ, [[1, 1], [1, 1]])
b2 = matrix(ZZ, [[1, 0], [0, -1]])
ck("p 投影", p**2 == p and p.conjugate_transpose() == p)
ck("psi2 保乘保*: 由 p^2=p, p*=p 推出",
    (lam * p) * (lmu * p) == lam * lmu * p
    and (lam * p).conjugate_transpose() == conjugate(lam) * p)
ck("p != 0 且 p != I", p != Zm and p != I2)
ck("b2 非零自伴正规",
    b2 != Zm and b2.conjugate_transpose() == b2
    and b2 * b2.conjugate_transpose() == b2.conjugate_transpose() * b2)
det2 = (x * I2 - b2).det().expand()
ck("det(xI-b2) = x^2-1", det2 == x**2 - 1)
rts2 = [s.rhs() for s in solve(det2 == 0, x)]
ck("roots(b2) = {1,-1}", sorted(set(RR(z) for z in rts2)) == [-1, 1])
fb2 = f1 * (I2 + b2) / 2 + f0 * (I2 - b2) / 2
ck("f(b2)==diag(f(1),f(-1))", fb2 == matrix(SR, [[f1, 0], [0, f0]]))
sol2 = solve(list((lam * p - matrix(SR, [[al, 0], [0, be]])).list()),
             [lam, al, be], solution_dict=True)
ck("lam*p=diag 唯一平凡解",
    len(sol2) == 1 and sol2[0][lam] == 0 and sol2[0][al] == 0 and sol2[0][be] == 0)

q = matrix(ZZ, [[1, 1], [0, 0]])
ck("q 幂等、不自伴", q**2 == q and q.conjugate_transpose() != q)
sol3 = solve(list((lam * q - matrix(SR, [[al, 0], [0, be]])).list()),
             [lam, al, be], solution_dict=True)
ck("lam*q=diag 唯一平凡解",
    len(sol3) == 1 and sol3[0][lam] == 0 and sol3[0][al] == 0 and sol3[0][be] == 0)

print()
print("SageMath 独立交叉验证全部通过 ✔")

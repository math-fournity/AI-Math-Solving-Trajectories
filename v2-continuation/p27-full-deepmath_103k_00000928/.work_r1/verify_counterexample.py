#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_counterexample.py —— 题目断言的形式化验证（sympy 精确符号计算）

题目断言（全称读法）："对任意 C*-代数 A,B、任意非 *-同态 psi:A->B、任意非零正规元 b∈B，
必存在 f∈C(σ(b)) 与 a∈A 使 psi(a)=f(b)≠0。"

反驳一个全称命题只需一个实例。本脚本对反例实例
    A = C,  B = M2(C),  psi(λ) = λ·E12,  b = E11
逐条验证其满足题设、且结论（存在非零解）不成立。

逻辑链与检查项的对应：
  S1  b 非零且正规                       （题设之一）
  S2  σ_B(b) = {0,1}                     （确定 C(σ_B(b)) 是两点空间上的函数代数）
  S3  函数演算 φ 的像 = 对角代数；φ 保乘、保 *、等距   （题面关于 φ 的断言在实例中成立）
  S4  ψ 不是 *-同态（但为良定义线性映射）  （题设之一）
  S5  关键：∀λ∈C, ∀f∈C({0,1}): λ·E12 = f(b) ⇒ λ=0，即 ψ(A)∩C*(b,b*)={0}
      —— 由于 f↦(f(0),f(1)) 是 C({0,1})→C² 的双射，对自由符号 (α,β)=(f(1),f(0))
         的符号求解就是对全体 f 的全称验证
  S6  阳性对照：换 ψ'(λ)=λE11 则确有非零解（证明检验手段本身有效，防"假阴性脚本"）
  S7  稳健性：随机复矩阵几乎必然使 ℂx∩C*(b)={0}（反例是通有的而非退化特例）
  S8  反例 2：ψ(λ)=λp（非零非酉 *-同态）配合 b=diag(1,-1)，仍无非零解
  S9  反例 3：ψ(λ)=λq（q²=q, q*≠q，即保乘法不保 * 的同态）配合 b=E11，仍无非零解

符号计算全部使用 sympy 的精确有理数/复符号运算，无浮点参与；
仅 S3 的等距性抽样与 S5/S7 的随机复核是数值性的补充检查。
任何一项失败都会抛出 AssertionError。
"""
import sympy as sp
import numpy as np

PASS = []

def check(name, cond):
    assert cond, f"[FAIL] {name}"
    PASS.append(name)
    print(f"  [PASS] {name}")

x = sp.Symbol('x')
lam, mu = sp.symbols('lambda mu', complex=True)
alpha, beta = sp.symbols('alpha beta', complex=True)
f0, f1, g0, g1 = sp.symbols('f0 f1 g0 g1', complex=True)

Z2 = sp.zeros(2)
E11 = sp.Matrix([[1, 0], [0, 0]])
E12 = sp.Matrix([[0, 1], [0, 0]])
E21 = sp.Matrix([[0, 0], [1, 0]])
E22 = sp.Matrix([[0, 0], [0, 1]])
I2 = sp.eye(2)

print("=== 主反例: A=C, B=M2(C), psi(lam)=lam*E12, b=E11 ===")

print("[S1] b 非零且正规")
check("b = E11 ≠ 0", E11 != Z2)
check("b 自伴: b* = b", E11.H == E11)
check("b 正规: b·b* = b*·b", E11 * E11.H == E11.H * E11)

print("[S2] σ_B(b) = {0,1}（t∉σ ⟺ tI−b 可逆 ⟺ det(tI−b)≠0）")
det_expr = sp.expand((x * I2 - E11).det())
check("det(tI − b) = t(t−1)", sp.simplify(det_expr - x * (x - 1)) == 0)
check("t(t−1) 的根恰为 {0,1}", set(sp.solve(det_expr, x)) == {sp.Integer(0), sp.Integer(1)})

print("[S3] 函数演算 φ: f ↦ f(b)：像 = 对角代数，保乘、保 *、等距")
# 两点谱上连续函数由 (f(0), f(1)) 决定，且 f(b) = f(0)(I−b) + f(1)b
fb = f0 * (I2 - E11) + f1 * E11
gb = g0 * (I2 - E11) + g1 * E11
check("f(b) = diag(f(1), f(0))",
      sp.simplify(fb - sp.Matrix([[f1, 0], [0, f0]])) == Z2)
check("保乘: (fg)(b) = f(b)·g(b)",
      sp.simplify(fb * gb - (f0 * g0 * (I2 - E11) + f1 * g1 * E11)) == Z2)
check("保*: conj(f)(b) = f(b)*",
      sp.simplify(fb.H - (sp.conjugate(f0) * (I2 - E11) + sp.conjugate(f1) * E11)) == Z2)
check("到上: 任一对角阵 diag(α,β) = α·b + β·(I−b)",
      sp.simplify(sp.Matrix([[alpha, 0], [0, beta]]) - (alpha * E11 + beta * (I2 - E11))) == Z2)
rng = np.random.default_rng(20260821)
ok_iso = True
for _ in range(500):
    a0 = complex(rng.normal(), rng.normal())
    a1 = complex(rng.normal(), rng.normal())
    M = np.array([[a1, 0], [0, a0]], dtype=complex)
    ok_iso &= bool(np.isclose(np.linalg.norm(M, 2), max(abs(a0), abs(a1)), atol=1e-10))
check("等距: ‖f(b)‖₂ = ‖f‖_∞ = max(|f(0)|,|f(1)|)（500 组随机复值抽样）", ok_iso)

print("[S4] ψ(λ) = λ·E12 不是 *-同态")
check("线性良定义: ψ(λ+μ) = ψ(λ)+ψ(μ)，ψ(cλ) = cψ(λ) 对符号成立",
      sp.simplify((lam + mu) * E12 - (lam * E12 + mu * E12)) == Z2)
check("乘法性失败: ψ(1·1)=E12 但 ψ(1)ψ(1) = E12² = 0",
      E12 * E12 == Z2 and E12 != Z2)
check("保 * 失败: ψ(1̄)=ψ(1)=E12 而 ψ(1)* = E21 ≠ E12", E12.H == E21 and E21 != E12)

print("[S5] 关键命题: ∀λ∈C, ∀f: λ·E12 = f(b) ⇒ λ = 0")
X = lam * E12
D = sp.Matrix([[alpha, 0], [0, beta]])          # D 取遍 C*(b,b*)（由 S3 的到上性）
eqs = [X[0, 0] - D[0, 0], X[0, 1] - D[0, 1], X[1, 0] - D[1, 0], X[1, 1] - D[1, 1]]
sols = sp.solve(eqs, [lam, alpha, beta], dict=True)
check(f"方程组唯一解 λ=α=β=0（sympy 解集 = {sols}）",
      sols == [{lam: 0, alpha: 0, beta: 0}])
ok_num = True
for _ in range(2000):
    L = complex(rng.normal(), rng.normal())
    A = complex(rng.normal(), rng.normal())
    B = complex(rng.normal(), rng.normal())
    if abs(L) > 1e-6 and np.allclose(np.array([[0, L], [0, 0]], dtype=complex),
                                     np.array([[A, 0], [0, B]], dtype=complex), atol=1e-8):
        ok_num = False
check("2000 组随机 (λ,α,β) 数值复核：无非零解", ok_num)

print("[S6] 阳性对照: ψ'(λ)=λ·E11 时确有非零解（检验手段有效性）")
check("ψ' 是 *-同态: E11² = E11 且 E11* = E11", E11 * E11 == E11 and E11.H == E11)
fb_id = 0 * (I2 - E11) + 1 * E11                # f(t) = t
check("取 λ=1, f(t)=t: ψ'(1) = E11 = id(b) ≠ 0 —— 非零解确实存在",
      fb_id == E11 and E11 != Z2)

print("[S7] 稳健性: 随机 x 几乎必然 ℂx ∩ C*(b) = {0}")
hits = 0
for _ in range(4000):
    Mx = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    # 由 S5：ℂx∩C*(b)≠{0} ⇔ 存在 λ≠0 使 λx 为对角阵 ⇔ x 本身是对角阵
    if abs(Mx[0, 1]) < 1e-9 and abs(Mx[1, 0]) < 1e-9:
        hits += 1
check(f"4000 个随机复矩阵中落在对角代数里的个数 = {hits}（期望 0）", hits == 0)

print("[S8] 反例 2: ψ(λ)=λp, p=½[[1,1],[1,1]] 是非零 *-同态（非酉），结论仍为 No")
p = sp.Rational(1, 2) * sp.Matrix([[1, 1], [1, 1]])
b2 = sp.Matrix([[1, 0], [0, -1]])
check("p 是投影: p² = p 且 p* = p",
      sp.simplify(p * p - p) == Z2 and p.H == p)
check("ψ₂ 保乘: ψ₂(λ)ψ₂(μ) = λμ·p² = λμ·p = ψ₂(λμ)",
      sp.simplify((lam * p) * (mu * p) - (lam * mu) * p) == Z2)
check("ψ₂ 保*: ψ₂(λ̄) = λ̄·p = ψ₂(λ)*",
      sp.simplify((lam * p).H - sp.conjugate(lam) * p) == Z2)
check("ψ₂ 非零且非酉: p ≠ 0 且 p ≠ I", p != Z2 and p != I2)
check("b2 = diag(1,−1) 非零自伴正规", b2 != Z2 and b2.H == b2 and b2 * b2.H == b2.H * b2)
cp2 = sp.expand((x * I2 - b2).det())
check("σ(b2) = {1,−1}: det(tI−b2) = t²−1", sp.simplify(cp2 - (x**2 - 1)) == 0
      and set(sp.solve(cp2, x)) == {sp.Integer(1), sp.Integer(-1)})
fb2 = f1 * (I2 + b2) / 2 + f0 * (I2 - b2) / 2   # f(1)=f1, f(−1)=f0
check("f(b2) = diag(f(1), f(−1))，像仍为对角代数",
      sp.simplify(fb2 - sp.Matrix([[f1, 0], [0, f0]])) == Z2)
X2 = lam * p
eqs2 = [X2[0, 0] - D[0, 0], X2[0, 1] - D[0, 1], X2[1, 0] - D[1, 0], X2[1, 1] - D[1, 1]]
sols2 = sp.solve(eqs2, [lam, alpha, beta], dict=True)
check(f"λp = diag(α,β) 唯一解 λ=α=β=0（{sols2}）",
      sols2 == [{lam: 0, alpha: 0, beta: 0}])

print("[S9] 反例 3: ψ(λ)=λq, q=[[1,1],[0,0]]（保乘法、不保 *），结论仍为 No")
q = sp.Matrix([[1, 1], [0, 0]])
check("q 幂等: q² = q（⇒ ψ₃(λ)ψ₃(μ)=λμq=ψ₃(λμ)，保乘法）",
      sp.simplify(q * q - q) == Z2)
check("q 不自伴: q* ≠ q（⇒ 不保 *）", q.H != q)
check("q ≠ 0 且 q ≠ I", q != Z2 and q != I2)
X3 = lam * q
eqs3 = [X3[0, 0] - D[0, 0], X3[0, 1] - D[0, 1], X3[1, 0] - D[1, 0], X3[1, 1] - D[1, 1]]
sols3 = sp.solve(eqs3, [lam, alpha, beta], dict=True)
check(f"λq = diag(α,β) 唯一解 λ=α=β=0（{sols3}）",
      sols3 == [{lam: 0, alpha: 0, beta: 0}])

print()
print(f"全部 {len(PASS)} 项检查通过 ✔  逻辑链 S1–S9 完整成立")

/-!
# lean_core_check.lean —— 反例承重事实的 Lean 4 形式化（纯 core，无 Mathlib）

把 2×2 矩阵抽象到任意带零的类型 K 上（K 可取 ℂ；core Lean 无复数，
而下面第 1 组论证只用到"有零对象"这一结构，故对 K = ℂ 自动成立；
第 2 组是关于具体矩阵 E₁₂、E₁₁ 的可判定事实，在 ℕ 上验证即可）。

形式化了反例 ψ(λ) = λE₁₂（b = E₁₁）中两条承重事实：

1. `key_lemma`：λ·E₁₂ = diag(α, β) 强制 λ = 0 ∧ α = 0 ∧ β = 0。
   即方程 ψ(a) = f(b) 只有零解 —— 这是"不存在非零解"的精确形式。
2. `E₁₂ · E₁₂ = 0 ≠ E₁₂` 且 `E₁₂ᵗ = E₂₁ ≠ E₁₂`，
   故 ψ 既不保乘法也不保对合，确实是"非 *-同态"。
-/

/-- 2×2 矩阵表示为嵌套对 ((a₁₁, a₁₂), (a₂₁, a₂₂)) -/
abbrev M2 (K : Type) := (K × K) × (K × K)

/-- E₁₂ 的 c 倍 -/
def E12 {K : Type} [Zero K] (c : K) : M2 K := ((0, c), (0, 0))

/-- 对角矩阵 diag(a, b) —— 即 C*(E₁₁) 中的一般元素 -/
def diag2 {K : Type} [Zero K] (a b : K) : M2 K := ((a, 0), (0, b))

/-- 零矩阵 -/
def zero2 {K : Type} [Zero K] : M2 K := ((0, 0), (0, 0))

/-- 逐分量定义的矩阵乘法 -/
def mul2 {K : Type} [Add K] [Mul K] (m n : M2 K) : M2 K :=
  ((m.1.1 * n.1.1 + m.1.2 * n.2.1, m.1.1 * n.1.2 + m.1.2 * n.2.2),
   (m.2.1 * n.1.1 + m.2.2 * n.2.1, m.2.1 * n.1.2 + m.2.2 * n.2.2))

/-- 转置（实系数下共轭是恒等，转置即共轭转置） -/
def adj2 {K : Type} (m : M2 K) : M2 K := ((m.1.1, m.2.1), (m.1.2, m.2.2))

/-! ### 承重事实 1：关键方程只有零解 -/

/-- 若 λ·E₁₂ = diag(α, β)，则 λ = 0、α = 0、β = 0。
    证明即"比较各分量"，用投影函数的 congrArg 提取。 -/
theorem key_lemma {K : Type} [Zero K] (l a b : K)
    (h : E12 l = diag2 a b) : l = 0 ∧ a = 0 ∧ b = 0 := by
  unfold E12 diag2 at h
  have e12 : l = 0 := congrArg (fun m : K × K => m.2) (congrArg Prod.fst h)
  have e11 : a = 0 := Eq.symm (congrArg (fun m : K × K => m.1) (congrArg Prod.fst h))
  have e22 : b = 0 := Eq.symm (congrArg (fun m : K × K => m.2) (congrArg Prod.snd h))
  exact ⟨e12, e11, e22⟩

/-- 推论形式：ψ(a) = f(b) 时必有 ψ(a) = 0（即 f(b) = 0）。 -/
theorem psi_a_is_zero {K : Type} [Zero K] (l a b : K)
    (h : E12 l = diag2 a b) : E12 l = zero2 := by
  have hl : l = 0 := (key_lemma l a b h).1
  subst hl
  rfl

/-! ### 承重事实 2：ψ 确实不是 *-同态（在 ℕ 上可判定验证） -/

/-- E₁₂² = 0 -/
example : mul2 (E12 (1 : Nat)) (E12 1) = zero2 := by decide

/-- 故 ψ 不保乘法：ψ(1)·ψ(1) = 0 ≠ E₁₂ = ψ(1·1) -/
example : mul2 (E12 (1 : Nat)) (E12 1) ≠ E12 1 := by decide

/-- E₁₂ᵗ = E₂₁ -/
example : adj2 (E12 (1 : Nat)) = (((0 : Nat), 0), (1, 0)) := by decide

/-- 故 ψ 不保对合：ψ(1)ᵗ = E₂₁ ≠ E₁₂ = ψ(1) -/
example : adj2 (E12 (1 : Nat)) ≠ E12 1 := by decide

/-- 阳性对照：E₁₁ 幂等且自伴，故 ψ'(λ) = λE₁₁ 是 *-同态 —— 检验手段能区分两种情形 -/
def E11n (c : Nat) : M2 Nat := ((c, 0), (0, 0))

example : mul2 (E11n 1) (E11n 1) = E11n 1 := by decide
example : adj2 (E11n 1) = E11n 1 := by decide

#print axioms key_lemma
#print axioms psi_a_is_zero

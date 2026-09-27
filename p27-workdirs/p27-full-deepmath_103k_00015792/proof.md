# Proof: If $\lambda_{FP}(X_1) + \lambda_{FP}(X_2) \in \mathbb{Z}$, then both $\lambda_{FP}(X_i) \in \mathbb{Z}$

## Answer

$$\boxed{\text{Yes}}$$

---

## Setup and Key Facts

Let $\alpha = \lambda_{FP}(X_1)$, $\beta = \lambda_{FP}(X_2)$, and suppose $\alpha + \beta = n \in \mathbb{Z}$.

**Fact 1 (Spectral radius of nonneg integer matrices).** For any nonneg integer matrix $A$, the spectral radius $\rho(A)$ is a nonneg real algebraic integer. Moreover, every eigenvalue $\lambda$ of $A$ satisfies $|\lambda| \le \rho(A)$.

**Fact 2 (Conjugates are eigenvalues).** If $\rho = \rho(A)$ is irrational of degree $d \ge 2$, its minimal polynomial $m_\rho(x)$ divides the characteristic polynomial $\chi_A(x)$. Hence all conjugates $\rho_1 = \rho, \rho_2, \dots, \rho_d$ are eigenvalues of $A$, and by Fact 1, $|\rho_i| \le \rho$ for all $i$.

**Definition.** A real algebraic integer $\rho > 0$ is a **weak Perron number** if every conjugate $\rho_i \ne \rho$ satisfies $|\rho_i| \le \rho$.

By Facts 1–2, the spectral radius of any nonneg integer matrix is either $0$ or a weak Perron number.

**Fact 3 (Rational algebraic integers are integers).** If $\rho$ is an algebraic integer and $\rho \in \mathbb{Q}$, then $\rho \in \mathbb{Z}$.

**Fact 4 (Conjugate structure under $x \mapsto n - x$).** If $\alpha$ has minimal polynomial $p(x)$ of degree $d$ with roots $\alpha_1 = \alpha, \alpha_2, \dots, \alpha_d$, then $\beta = n - \alpha$ has minimal polynomial $q(x) = (-1)^d p(n - x)$, also of degree $d$, with roots $n - \alpha_1, \dots, n - \alpha_d$. In particular, $\alpha$ is irrational $\iff$ $\beta$ is irrational, and they share the same degree.

---

## Proof

### Step 1: Reduction to the positive case

Since $X_1, X_2$ are non-degenerate nonneg integer matrices, $\alpha, \beta \ge 0$.

- If $\alpha = 0$: then $\beta = n \in \mathbb{Z}$. Both are integers. ✓
- If $\beta = 0$: then $\alpha = n \in \mathbb{Z}$. Both are integers. ✓

So assume $\alpha > 0$ and $\beta > 0$. Then $\alpha, \beta$ are weak Perron numbers, and $n = \alpha + \beta > \alpha$ (since $\beta > 0$), i.e., $n > \alpha$.

### Step 2: If $\alpha \in \mathbb{Z}$, done

If $\alpha$ is rational, then by Fact 3, $\alpha \in \mathbb{Z}$, and $\beta = n - \alpha \in \mathbb{Z}$.

### Step 3: $\alpha \notin \mathbb{Z}$ leads to contradiction

Suppose for contradiction that $\alpha$ is irrational, so $\alpha$ has degree $d \ge 2$ with conjugates $\alpha_1 = \alpha, \alpha_2, \dots, \alpha_d$ (all distinct, since minimal polynomials over $\mathbb{Q}$ are separable).

By Fact 4, $\beta = n - \alpha$ is also irrational of degree $d$, with conjugates $n - \alpha_1, \dots, n - \alpha_d$.

Since $\beta$ is a weak Perron number, we require:

$$|n - \alpha_i| \le n - \alpha \quad \text{for all } i = 2, \dots, d. \tag{$\star$}$$

We show $(\star)$ is **impossible** for every conjugate $\alpha_i \ne \alpha$, given $n > \alpha > 0$ and $|\alpha_i| \le \alpha$.

#### Case A: $\alpha_i$ is real

Since $|\alpha_i| \le \alpha$ and $\alpha_i \ne \alpha$:

- If $\alpha_i \ge 0$: then $\alpha_i < \alpha$, so $n - \alpha_i > n - \alpha = \beta > 0$, giving $|n - \alpha_i| > \beta$. ✗
- If $\alpha_i < 0$: then $n - \alpha_i > n > n - \alpha = \beta$, so $|n - \alpha_i| > \beta$. ✗

In both subcases, $(\star)$ fails.

#### Case B: $\alpha_i = a + bi$ with $b \ne 0$ (complex conjugate)

Condition $(\star)$ becomes:

$$(n - a)^2 + b^2 \le (n - \alpha)^2.$$

Expanding and simplifying:

$$2n(\alpha - a) \le \alpha^2 - |\alpha_i|^2. \tag{$\star\star$}$$

**Key observations:**

1. $\alpha - a > 0$: since $a = \operatorname{Re}(\alpha_i) \le |\alpha_i| \le \alpha$, and equality $a = \alpha$ would force $b = 0$ (contradiction).

2. $\alpha^2 - |\alpha_i|^2 \ge 0$: since $|\alpha_i| \le \alpha$.

**Sub-case B1: $|\alpha_i| = \alpha$.** Then $\alpha^2 - |\alpha_i|^2 = 0$, so $(\star\star)$ gives $n \le 0$, contradicting $n > \alpha > 0$.

**Sub-case B2: $|\alpha_i| < \alpha$.** From $(\star\star)$:

$$n \le \frac{\alpha^2 - |\alpha_i|^2}{2(\alpha - a)} = \frac{(\alpha - |\alpha_i|)(\alpha + |\alpha_i|)}{2(\alpha - a)}.$$

Since $a \le |\alpha_i|$ (real part $\le$ modulus), we have $\alpha - a \ge \alpha - |\alpha_i|$, so:

$$n \le \frac{\alpha + |\alpha_i|}{2} < \frac{\alpha + \alpha}{2} = \alpha.$$

But this contradicts $n > \alpha$. ✗

### Step 4: Conclusion

In every case, the weak Perron condition $(\star)$ for $\beta$ fails when $\alpha$ is irrational. Therefore $\alpha$ cannot be irrational, so $\alpha \in \mathbb{Q}$, and by Fact 3, $\alpha \in \mathbb{Z}$. Consequently $\beta = n - \alpha \in \mathbb{Z}$.

$$\boxed{\text{Yes, } \lambda_{FP}(X_1) + \lambda_{FP}(X_2) \in \mathbb{Z} \implies \lambda_{FP}(X_1), \lambda_{FP}(X_2) \in \mathbb{Z}.}$$

### PROOF COMPLETE

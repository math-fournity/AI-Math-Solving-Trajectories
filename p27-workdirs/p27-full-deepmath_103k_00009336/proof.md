# Proof: $C_N$ equals its centralizer in $\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})$

**Answer: Yes.** For any CM elliptic curve $E$ (with CM by an order $\mathcal{O}$ in an imaginary quadratic field $K$) and any integer $N\geq 1$, the image $C_N$ of $(\mathcal{O}/N\mathcal{O})^\times$ in $\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})$ equals its own centralizer.

---

## Setup and notation

Let $E/\mathbb{C}$ have CM by $\mathcal{O}\subseteq K$, so $\operatorname{End}(E)\cong\mathcal{O}$. Choose a lattice $\Lambda\subset\mathbb{C}$ with $E\cong\mathbb{C}/\Lambda$, where $\Lambda$ is a **proper** $\mathcal{O}$-ideal (this is the standard CM construction: every CM elliptic curve arises as $\mathbb{C}/\Lambda$ for a proper $\mathcal{O}$-ideal class). The CM action of $\mathcal{O}$ on $E$ is induced by multiplication on $\Lambda$.

Fix a basis of $E[N]\cong(\mathbb{Z}/N\mathbb{Z})^2$, giving $\operatorname{Aut}(E[N])\cong\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})$. Let
$$A \;:=\; \text{image of } \mathcal{O}/N\mathcal{O} \text{ in } \operatorname{End}(E[N])\cong M_2(\mathbb{Z}/N\mathbb{Z}),$$
so that $C_N = A^\times$ (the image of $(\mathcal{O}/N\mathcal{O})^\times$). We must show
$$\operatorname{Cent}_{\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})}(C_N) \;=\; C_N.$$

The proof proceeds in four steps.

---

## Step 1. $E[N]$ is a projective rank-1 module over $\mathcal{O}/N\mathcal{O}$

**Key classical fact.** For an order $\mathcal{O}$ in an imaginary quadratic field $K$, every proper $\mathcal{O}$-ideal is **invertible** (hence a projective rank-1 $\mathcal{O}$-module). This is a standard result in the ideal theory of orders in imaginary quadratic fields: a proper $\mathcal{O}$-ideal $\mathfrak{a}$ satisfies $\mathfrak{a}\cdot(\mathcal{O}:\mathfrak{a})=\mathcal{O}$, where $(\mathcal{O}:\mathfraka)=\{x\in K:x\mathfrak{a}\subseteq\mathcal{O}\}$, and properness ensures the colon ideal is again a proper $\mathcal{O}$-ideal, giving a genuine two-sided inverse.

Since $\Lambda$ is a proper $\mathcal{O}$-ideal, it is an invertible (hence projective rank-1) $\mathcal{O}$-module. Now
$$E[N] \;\cong\; \tfrac{1}{N}\Lambda/\Lambda \;\cong\; \Lambda\otimes_{\mathcal{O}} \mathcal{O}/N\mathcal{O}$$
as $\mathcal{O}/N\mathcal{O}$-modules (the isomorphism $\tfrac{1}{N}\Lambda/\Lambda\cong\Lambda\otimes_{\mathcal{O}}\mathcal{O}/N\mathcal{O}$ sends $\tfrac{\lambda}{N}\bmod\Lambda\mapsto\lambda\otimes 1$). Projectivity is preserved under base change, so:

> **$E[N]$ is a projective rank-1 module over $R:=\mathcal{O}/N\mathcal{O}$.**

In particular $E[N]$ is locally free of rank 1, hence faithful over $R$ (locally isomorphic to $R$, which is faithful over itself).

---

## Step 2. The centralizer of $A$ in $M_2(\mathbb{Z}/N\mathbb{Z})$ is $A$ itself

The centralizer of $A$ in $\operatorname{End}(E[N])\cong M_2(\mathbb{Z}/N\mathbb{Z})$ is, by definition, the ring of $\mathcal{O}/N\mathcal{O}$-linear endomorphisms of $E[N]$:
$$\operatorname{Cent}_{M_2(\mathbb{Z}/N\mathbb{Z})}(A) \;=\; \operatorname{End}_{\mathcal{O}/N\mathcal{O}}(E[N]).$$

For a locally free rank-1 module $M$ over a commutative ring $R$, there is a canonical isomorphism
$$\operatorname{End}_R(M) \;\cong\; M^*\otimes_R M \;\xrightarrow{\;\mathrm{ev}\;}\; R,$$
where $M^*=\operatorname{Hom}_R(M,R)$ and $\mathrm{ev}$ is the evaluation pairing. (Locally, $M\cong R$, $M^*\cong R$, and the evaluation is just multiplication $R\otimes R\to R$; this glues.) Applying this with $R=\mathcal{O}/N\mathcal{O}$ and $M=E[N]$:

$$\operatorname{End}_{\mathcal{O}/N\mathcal{O}}(E[N]) \;\cong\; \mathcal{O}/N\mathcal{O}.$$

Under the embedding $\mathcal{O}/N\mathcal{O}\hookrightarrow M_2(\mathbb{Z}/N\mathbb{Z})$ (which is injective by faithfulness of $E[N]$), this image is exactly $A$. Therefore:

> **$\operatorname{Cent}_{M_2(\mathbb{Z}/N\mathbb{Z})}(A) = A$.**

---

## Step 3. $C_N = A^\times$ generates $A$ as a $\mathbb{Z}/N\mathbb{Z}$-algebra

To pass from "centralizer of $A$" to "centralizer of $C_N=A^\times$", we show $A^\times$ generates $A$ as a $\mathbb{Z}/N\mathbb{Z}$-algebra. Then any element commuting with $C_N$ commutes with all of $A$, and conversely.

By the Chinese Remainder Theorem,
$$\mathcal{O}/N\mathcal{O} \;\cong\; \prod_{p^k\,\|\, N}\, \mathcal{O}/p^k\mathcal{O},$$
so it suffices to work one prime power at a time. Write $A_p$ for the image of $\mathcal{O}/p^k\mathcal{O}$.

**Structure of $\mathcal{O}/p^k\mathcal{O}$.** Since $K\otimes_{\mathbb{Q}}\mathbb{Q}_p$ is either a quadratic field extension of $\mathbb{Q}_p$ (when $p$ is **inert** or **ramified** in $K$) or $\mathbb{Q}_p\times\mathbb{Q}_p$ (when $p$ is **split**), the ring $\mathcal{O}/p^k\mathcal{O}$ is either:
- a **local ring** (inert or ramified case), or
- a **product of two local rings** (split case).

In either case it is a finite product of local rings. So we reduce to: **in a finite local $(\mathbb{Z}/p^k\mathbb{Z})$-algebra $R$ with maximal ideal $\mathfrak{m}$, the unit group $R^\times$ generates $R$ as a $\mathbb{Z}/p^k\mathbb{Z}$-algebra.**

**Proof of the local claim.** In a finite local ring $R$ with maximal ideal $\mathfrak{m}$, the units are exactly $R\setminus\mathfrak{m}$, and crucially $1+\mathfrak{m}\subseteq R^\times$ (since $x\in\mathfrak{m}\Rightarrow 1+x\notin\mathfrak{m}\Rightarrow 1+x$ is a unit). For any $x\in\mathfrak{m}$, we have $x=(1+x)-1$, and both $1+x\in R^\times$ and $1\in R^\times$. Hence every element of $\mathfrak{m}$ lies in the $\mathbb{Z}/p^k\mathbb{Z}$-subalgebra generated by $R^\times$. Together with $1$, this generates all of $R = \mathbb{Z}/p^k\mathbb{Z}\cdot 1 + \mathfrak{m}$ (as a $\mathbb{Z}/p^k\mathbb{Z}$-module, $R$ is generated by $1$ and $\mathfrak{m}$; and $\mathfrak{m}$ is generated by $R^\times$ as shown). $\square$

In the split case (product of two local rings), the same argument applies componentwise. Therefore $A_p^\times$ generates $A_p$ for each $p^k\|N$, and taking the product:

> **$C_N = A^\times$ generates $A$ as a $\mathbb{Z}/N\mathbb{Z}$-algebra.**

---

## Step 4. Conclusion: $\operatorname{Cent}_{\operatorname{GL}_2}(C_N) = C_N$

Since $C_N$ generates $A$ as a $\mathbb{Z}/N\mathbb{Z}$-algebra (Step 3), an element of $M_2(\mathbb{Z}/N\mathbb{Z})$ commutes with $C_N$ if and only if it commutes with all of $A$:
$$\operatorname{Cent}_{M_2(\mathbb{Z}/N\mathbb{Z})}(C_N) \;=\; \operatorname{Cent}_{M_2(\mathbb{Z}/N\mathbb{Z})}(A) \;=\; A$$
by Step 2. Now restrict to the centralizer inside $\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})$ (i.e., among invertible elements):
$$\operatorname{Cent}_{\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})}(C_N) \;=\; \operatorname{Cent}_{M_2(\mathbb{Z}/N\mathbb{Z})}(C_N)\;\cap\;\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z}) \;=\; A\;\cap\;\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z}) \;=\; A^\times \;=\; C_N.$$

The last equality $A\cap\operatorname{GL}_2 = A^\times$ holds because an element of $A$ (viewed as a $2\times 2$ matrix) is invertible in $M_2(\mathbb{Z}/N\mathbb{Z})$ if and only if it is a unit in $A$ (the inverse, being a polynomial in the element, lies back in the commutative subalgebra $A$).

Therefore:
$$\boxed{\,\operatorname{Cent}_{\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})}(C_N) \;=\; C_N\,}$$

That is, **$C_N$ is equal to its centralizer in $\operatorname{GL}_2(\mathbb{Z}/N\mathbb{Z})$**.

### PROOF COMPLETE

# Proof

## Answer

**Yes.** Such a norm-bounded sequence $(y_n)$ can always be found. Specifically, one can achieve $\sup_n \|y_n\|_\psi \leq 2$.

$$\boxed{\text{Yes}}$$

## Setup and Key Definitions

Let $\varphi:[0,\infty)\to[0,\infty)$ be a Young function (convex, $\varphi(0)=0$, $\lim_{t\to\infty}\varphi(t)=\infty$) with conjugate $\psi(s)=\sup_{t\geq 0}\{st-\varphi(t)\}$.

- **Luxemburg norm:** $\|x\|_{(\varphi)} = \inf\{c>0:\mathbb{E}[\varphi(|x|/c)]\leq 1\}$.
- **Orlicz (Amemiya) norm:** $\|x\|_\varphi^O = \sup\{\mathbb{E}[|xy|]:\mathbb{E}[\psi(|y|)]\leq 1\}$.

The problem uses $\|x_n\|_\varphi = 1$, which we interpret as the Luxemburg norm $\|x_n\|_{(\varphi)}=1$ (the standard convention for this notation).

## Key Theorem: Norm Duality in Orlicz Spaces

**Theorem (Luxemburg–Orlicz norm comparison).** For all $x\in L^\varphi$:
$$\|x\|_{(\varphi)} \;\leq\; \|x\|_\varphi^O \;\leq\; 2\,\|x\|_{(\varphi)}.$$

### Proof of the theorem

**Upper bound** ($\|x\|_\varphi^O \leq 2\|x\|_{(\varphi)}$): Let $k=\|x\|_{(\varphi)}$. By Young's inequality $st \leq \varphi(s)+\psi(t)$ applied with $s=|x|/k$, $t=|y|$:
$$\frac{|xy|}{k} \leq \varphi\!\left(\frac{|x|}{k}\right) + \psi(|y|).$$
Taking expectations: $\mathbb{E}[|xy|] \leq k\,\mathbb{E}[\varphi(|x|/k)] + k\,\mathbb{E}[\psi(|y|)]$.

Now, $\mathbb{E}[\varphi(|x|/k)] \leq 1$ (by MCT: for all $c>k$, $\mathbb{E}[\varphi(|x|/c)]\leq 1$; letting $c\searrow k$ gives $\mathbb{E}[\varphi(|x|/k)]\leq 1$). If $\mathbb{E}[\psi(|y|)]\leq 1$, then $\mathbb{E}[|xy|]\leq 2k$. Taking sup gives $\|x\|_\varphi^O\leq 2k$. $\checkmark$

**Lower bound** ($\|x\|_{(\varphi)} \leq \|x\|_\varphi^O$): Let $k=\|x\|_{(\varphi)}>0$. For any $0<\epsilon<k$, set $c=k-\epsilon$, so $\mathbb{E}[\varphi(|x|/c)]>1$ (since $c<k$). Define:
$$u = \frac{|x|}{c}, \qquad v = \varphi'(u) \quad\text{(right derivative)}, \qquad A = \mathbb{E}[\varphi(u)] > 1.$$

By **Young's equality** $u\,\varphi'(u) = \varphi(u)+\psi(\varphi'(u))$:
$$\mathbb{E}[uv] = A + \mathbb{E}[\psi(v)].$$

We construct $y$ with $\mathbb{E}[\psi(|y|)]\leq 1$ and $\mathbb{E}[|xy|]\geq k-\epsilon$:

- **Case 1:** $\mathbb{E}[\psi(v)]\geq 1$. Set $t=1/\mathbb{E}[\psi(v)]\leq 1$ and $y=t\,v\,\mathrm{sgn}(x)$. By convexity of $\psi$ and $\psi(0)=0$: $\psi(tv)\leq t\,\psi(v)$ for $t\leq 1$, so $\mathbb{E}[\psi(|y|)]\leq t\,\mathbb{E}[\psi(v)]=1$. $\checkmark$ Moreover:
$$\mathbb{E}[|xy|]=tc\,\mathbb{E}[uv]=tc\!\left(A+\mathbb{E}[\psi(v)]\right)=c\!\left(\frac{A}{\mathbb{E}[\psi(v)]}+1\right)\geq c = k-\epsilon.$$

- **Case 2:** $\mathbb{E}[\psi(v)]<1$. Set $y=v\,\mathrm{sgn}(x)$ (i.e., $t=1$). Then $\mathbb{E}[\psi(|y|)]=\mathbb{E}[\psi(v)]<1\leq 1$. $\checkmark$ Moreover:
$$\mathbb{E}[|xy|]=c\,\mathbb{E}[uv]=c\!\left(A+\mathbb{E}[\psi(v)]\right)>c\cdot A>c=k-\epsilon.$$

In both cases, $\mathbb{E}[|xy|]\geq k-\epsilon$ with $\mathbb{E}[\psi(|y|)]\leq 1$. Since $\epsilon>0$ is arbitrary, $\|x\|_\varphi^O\geq k=\|x\|_{(\varphi)}$. $\checkmark$

**Remark.** The Orlicz norm equals the associate norm: $\|x\|_\varphi^O = \sup\{\mathbb{E}[|xy|]:\|y\|_{(\psi)}\leq 1\}$, because $\|y\|_{(\psi)}\leq 1 \iff \mathbb{E}[\psi(|y|)]\leq 1$ (the forward direction by MCT, the reverse by evaluating at $c=1$).

## Main Proof

**Reduction to single-variable problem.** Since the $x_n$ are disjoint and we require $\mathrm{supp}(y_n)\subset\mathrm{supp}(x_n)$, the $y_n$ are also disjoint, and the conditions $\mathbb{E}[x_n y_n]=1$ are independent across $n$. Thus it suffices to show: there exists a universal constant $C$ such that for every $x\geq 0$ with $\|x\|_{(\varphi)}=1$, one can find $y\geq 0$ with $\mathrm{supp}(y)\subset\mathrm{supp}(x)$, $\mathbb{E}[xy]=1$, and $\|y\|_{(\psi)}\leq C$.

**Construction of $y$ for a single $x$.** Let $x\geq 0$ with $\|x\|_{(\varphi)}=1$. By the theorem above, $\|x\|_\varphi^O\geq 1$. Fix $\epsilon=1/2$. Then there exists $\tilde{y}\in L^\psi$ with:
$$\mathbb{E}[\psi(|\tilde{y}|)]\leq 1 \qquad\text{and}\qquad \mathbb{E}[|x\tilde{y}|]\geq 1-\epsilon=\tfrac{1}{2}.$$

Define $y_0 = |\tilde{y}|\cdot\mathbf{1}_{\mathrm{supp}(x)}$. Then:

1. **Non-negativity:** $y_0\geq 0$. $\checkmark$
2. **Support:** $\mathrm{supp}(y_0)\subset\mathrm{supp}(x)$. $\checkmark$
3. **$\psi$-norm bound:** Since $y_0\leq|\tilde{y}|$ and $\psi$ is increasing, $\mathbb{E}[\psi(y_0)]\leq\mathbb{E}[\psi(|\tilde{y}|)]\leq 1$, which gives $\|y_0\|_{(\psi)}\leq 1$. $\checkmark$
4. **Pairing:** Since $x\geq 0$ and $x=0$ off $\mathrm{supp}(x)$:
$$\mathbb{E}[x\,y_0]=\mathbb{E}\!\left[x\,|\tilde{y}|\,\mathbf{1}_{\mathrm{supp}(x)}\right]=\mathbb{E}[x\,|\tilde{y}|]=\mathbb{E}[|x\tilde{y}|]\geq\tfrac{1}{2}.\quad\checkmark$$

Now **normalize**: set $y = y_0\,/\,\mathbb{E}[x\,y_0]$. Then:
- $y\geq 0$, $\mathrm{supp}(y)\subset\mathrm{supp}(x)$. $\checkmark$
- $\mathbb{E}[xy]=1$. $\checkmark$
- By homogeneity of the Luxemburg norm:
$$\|y\|_{(\psi)}=\frac{\|y_0\|_{(\psi)}}{\mathbb{E}[x\,y_0]}\leq\frac{1}{1/2}=2.\quad\checkmark$$

**Applying to the sequence.** For each $n$, apply the above construction to $x_n$ (with $\|x_n\|_{(\varphi)}=1$) to obtain $y_n\geq 0$ with $\mathrm{supp}(y_n)\subset\mathrm{supp}(x_n)$, $\mathbb{E}[x_n y_n]=1$, and $\|y_n\|_{(\psi)}\leq 2$.

Therefore:
$$\sup_n \|y_n\|_\psi \leq 2 < \infty,$$
and $(y_n)$ is a norm-bounded sequence in $L^\psi$ satisfying all the required conditions. $\blacksquare$

## Summary

The key insight is that the Orlicz (Amemiya) norm $\|x\|_\varphi^O = \sup\{\mathbb{E}[|xy|]:\mathbb{E}[\psi(|y|)]\leq 1\}$ satisfies $\|x\|_\varphi^O \geq \|x\|_{(\varphi)}$ (the Luxemburg norm). This is a fundamental duality result in Orlicz space theory, proved here via Young's equality and a case analysis on $\mathbb{E}[\psi(\varphi'(|x|/c))]$. The lower bound $\|x\|_\varphi^O \geq 1$ when $\|x\|_{(\varphi)}=1$ guarantees the existence of a dual element with $\psi$-norm $\leq 1$ and pairing $\geq 1/2$; after restricting to $\mathrm{supp}(x)$, taking absolute values, and normalizing, we obtain $y$ with $\|y\|_\psi \leq 2$ and $\mathbb{E}[xy]=1$.

Notably, this argument works for **all** Young functions $\varphi$, without any $\Delta_2$ or $\nabla_2$ assumptions. The $\Delta_2$ condition is only needed for the isometric isomorphism $(L^\varphi)^* \cong L^\psi$, which is a stronger statement than what we need here. The associate norm duality $\|x\|_{(\varphi)} \leq \|x\|_{(\psi)'} \leq 2\|x\|_{(\varphi)}$ holds unconditionally.

### PROOF COMPLETE

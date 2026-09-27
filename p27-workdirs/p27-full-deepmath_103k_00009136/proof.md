# Proof: $CD(K,\infty)$ spaces are length spaces

## Answer

$$\boxed{\text{Yes, } (X,d) \text{ is a length space.}}$$

## Setup

Let $(X,d)$ be a complete, separable metric space, $\mu$ a nonnegative Borel measure with $\operatorname{supp}(\mu)=X$ and $\mu(B(x,r))<\infty$ for all $x\in X$, $r>0$. Suppose $(X,d,\mu)$ is a $CD(K,\infty)$ space in the sense of Sturm. We prove $(X,d)$ is a length space.

## Sturm's $CD(K,\infty)$ definition

$(X,d,\mu)$ satisfies $CD(K,\infty)$ if for every pair $\mu_0,\mu_1\in\mathcal{P}_2(X,\mu)$ (probability measures absolutely continuous w.r.t.\ $\mu$ with finite second moment), there exists a minimizing $W_2$-geodesic $(\mu_t)_{t\in[0,1]}$ in $(\mathcal{P}_2(X),W_2)$ from $\mu_0$ to $\mu_1$ such that for all $t\in[0,1]$:

$$\operatorname{Ent}(\mu_t\mid\mu)\le(1-t)\operatorname{Ent}(\mu_0\mid\mu)+t\operatorname{Ent}(\mu_1\mid\mu)-\frac{K}{2}t(1-t)W_2^2(\mu_0,\mu_1).$$

**Key property used:** The definition requires the *existence* of a $W_2$-geodesic between any two absolutely continuous measures. We use only this geodesic existence; the entropy inequality is not needed for our argument.

## Strategy

1. Use $CD(K,\infty)$ to produce $W_2$-geodesics between measures supported on small balls.
2. Extract approximate midpoints in $X$ from these Wasserstein geodesics.
3. Use completeness to promote approximate midpoints to the length property.

## Step 1: Constructing test measures

Fix $x,y\in X$ with $D:=d(x,y)>0$. For $r>0$ (with $r<D/4$), define:

$$\mu_0^r:=\frac{\mu|_{B(x,r)}}{\mu(B(x,r))},\qquad \mu_1^r:=\frac{\mu|_{B(y,r)}}{\mu(B(y,r))}.$$

These are well-defined probability measures because:
- $\mu(B(x,r))>0$: since $\operatorname{supp}(\mu)=X$, every $x\in X$ lies in the support, so every open ball has positive $\mu$-measure.
- $\mu(B(x,r))<\infty$: by hypothesis.

They are absolutely continuous w.r.t.\ $\mu$ (as normalized restrictions) and have finite second moment (supported on bounded balls). Thus $\mu_0^r,\mu_1^r\in\mathcal{P}_2(X,\mu)$.

By the $CD(K,\infty)$ condition, there exists a $W_2$-geodesic $(\mu_t^r)_{t\in[0,1]}$ from $\mu_0^r$ to $\mu_1^r$. In particular:

$$W_2(\mu_0^r,\mu_{1/2}^r)=\tfrac{1}{2}W_2(\mu_0^r,\mu_1^r),\qquad W_2(\mu_{1/2}^r,\mu_1^r)=\tfrac{1}{2}W_2(\mu_0^r,\mu_1^r).$$

## Step 2: Estimating $W_2(\mu_0^r,\mu_1^r)$

Since $\mu_0^r$ is supported on $B(x,r)$ and $\mu_1^r$ on $B(y,r)$, for any $a\in B(x,r)$, $b\in B(y,r)$:

$$D-2r\le d(a,b)\le D+2r.$$

Therefore:

$$(D-2r)^2\le W_2^2(\mu_0^r,\mu_1^r)\le (D+2r)^2,$$

and hence $W_2(\mu_0^r,\mu_1^r)\to D$ as $r\to 0$.

## Step 3: $L^2$ estimates on $\mu_{1/2}^r$

We bound $W_2(\delta_x,\mu_{1/2}^r)$ using the triangle inequality for $W_2$ (valid for all measures in $\mathcal{P}_2(X)$, including Dirac measures):

**Upper bound:**
$$W_2(\delta_x,\mu_{1/2}^r)\le W_2(\delta_x,\mu_0^r)+W_2(\mu_0^r,\mu_{1/2}^r).$$

Since $\mu_0^r$ is supported on $B(x,r)$:
$$W_2(\delta_x,\mu_0^r)=\left(\int d(x,a)^2\,d\mu_0^r(a)\right)^{1/2}\le r.$$

And $W_2(\mu_0^r,\mu_{1/2}^r)=\frac{1}{2}W_2(\mu_0^r,\mu_1^r)\le\frac{D+2r}{2}$. Therefore:

$$W_2(\delta_x,\mu_{1/2}^r)\le r+\frac{D+2r}{2}=\frac{D}{2}+2r.$$

**Lower bound:**
$$W_2(\delta_x,\mu_{1/2}^r)\ge W_2(\mu_0^r,\mu_{1/2}^r)-W_2(\mu_0^r,\delta_x)\ge\frac{D-2r}{2}-r=\frac{D}{2}-2r.$$

Since $W_2^2(\delta_x,\mu_{1/2}^r)=\int d(x,b)^2\,d\mu_{1/2}^r(b)$ (the optimal coupling with a Dirac is trivial), we obtain:

$$\left(\frac{D}{2}-2r\right)^2\le\int d(x,b)^2\,d\mu_{1/2}^r(b)\le\left(\frac{D}{2}+2r\right)^2.$$

By the identical argument with $y$:

$$\left(\frac{D}{2}-2r\right)^2\le\int d(b,y)^2\,d\mu_{1/2}^r(b)\le\left(\frac{D}{2}+2r\right)^2.$$

## Step 4: Variance vanishes — the key computation

Consider the quantity:

$$\int\left[(d(x,b)-D/2)^2+(d(b,y)-D/2)^2\right]d\mu_{1/2}^r(b).$$

Expanding:

$$=\int d(x,b)^2\,d\mu+\int d(b,y)^2\,d\mu-D\int(d(x,b)+d(b,y))\,d\mu+\frac{D^2}{2}.$$

We bound each term:
- $\int d(x,b)^2\,d\mu\le (D/2+2r)^2$ (Step 3).
- $\int d(b,y)^2\,d\mu\le (D/2+2r)^2$ (Step 3).
- $\int(d(x,b)+d(b,y))\,d\mu\ge D$ (triangle inequality: $d(x,b)+d(b,y)\ge D$ pointwise).

Therefore:

$$\int\left[(d(x,b)-D/2)^2+(d(b,y)-D/2)^2\right]d\mu_{1/2}^r(b)\le 2\left(\frac{D}{2}+2r\right)^2-D^2+\frac{D^2}{2}.$$

Expanding $2(D/2+2r)^2=2(D^2/4+2Dr+4r^2)=D^2/2+4Dr+8r^2$:

$$=D^2/2+4Dr+8r^2-D^2+D^2/2=4Dr+8r^2.$$

In particular:

$$\int(d(x,b)-D/2)^2\,d\mu_{1/2}^r(b)\le 4Dr+8r^2\xrightarrow{r\to 0}0,$$

and similarly $\int(d(b,y)-D/2)^2\,d\mu_{1/2}^r(b)\to 0$.

## Step 5: Existence of approximate midpoints

Let $\varepsilon>0$. Choose $r>0$ small enough that $4Dr+8r^2<\varepsilon^2/4$.

By Markov's inequality:

$$\mu_{1/2}^r\bigl(|d(x,b)-D/2|>\varepsilon\bigr)\le\frac{4Dr+8r^2}{\varepsilon^2}<\frac{1}{4},$$

$$\mu_{1/2}^r\bigl(|d(b,y)-D/2|>\varepsilon\bigr)<\frac{1}{4}.$$

By the union bound:

$$\mu_{1/2}^r\bigl(|d(x,b)-D/2|\le\varepsilon\text{ and }|d(b,y)-D/2|\le\varepsilon\bigr)>1-\frac{1}{2}=\frac{1}{2}>0.$$

Therefore the set $S_\varepsilon:=\{b\in X:|d(x,b)-D/2|\le\varepsilon,\;|d(b,y)-D/2|\le\varepsilon\}$ has positive $\mu_{1/2}^r$-measure, hence intersects $\operatorname{supp}(\mu_{1/2}^r)$.

Pick $z\in S_\varepsilon\cap\operatorname{supp}(\mu_{1/2}^r)$. Then:

$$|d(x,z)-D/2|\le\varepsilon,\qquad|d(z,y)-D/2|\le\varepsilon.$$

Since $\varepsilon>0$ was arbitrary, $(X,d)$ has the **approximate midpoint property**: for every $x,y\in X$ and every $\varepsilon>0$, there exists $z\in X$ with $d(x,z)\le d(x,y)/2+\varepsilon$ and $d(z,y)\le d(x,y)/2+\varepsilon$.

## Step 6: Approximate midpoints + completeness $\Longrightarrow$ length space

We show that a complete metric space with approximate midpoints is a length space.

**Construction of an approximate geodesic.** Fix $x,y\in X$ with $D=d(x,y)>0$ and $\eta>0$. We construct a continuous curve $\gamma:[0,1]\to X$ with $L(\gamma)\le D+\eta$.

Define $\gamma$ on dyadic rationals $\{k/2^n:k=0,\ldots,2^n\}$ by recursive bisection:
- $\gamma(0)=x$, $\gamma(1)=y$.
- At level $n$ (subdividing each existing segment), choose $\gamma$ at the new midpoints using the approximate midpoint property with error $\varepsilon_n:=\eta/4^n$.

**Length bound.** Let $L_n$ be the total length of the polygonal path through the $2^n+1$ dyadic points. At each level, every segment of length $\ell$ is replaced by two segments of total length $\le\ell+2\varepsilon_n$. Since there are $2^{n-1}$ segments being subdivided at level $n$:

$$L_n\le L_{n-1}+2^n\varepsilon_n.$$

Starting from $L_0=D$:

$$L_n\le D+\sum_{k=1}^n 2^k\cdot\frac{\eta}{4^k}=D+\eta\sum_{k=1}^n\frac{1}{2^k}\le D+\eta.$$

**Mesh size.** The longest segment at level $n$ has length $\le D/2^n+2\sum_{j=1}^n\varepsilon_j/2^{n-j}$. With $\varepsilon_j=\eta/4^j$:

$$2\sum_{j=1}^n\frac{\eta}{4^j\cdot 2^{n-j}}=\frac{2\eta}{2^n}\sum_{j=1}^n\left(\frac{1}{2}\right)^j\le\frac{2\eta}{2^n}.$$

So the mesh size is $\le(D+2\eta)/2^n\to 0$.

**Uniform continuity.** For dyadic rationals $s<t$ in $[0,1]$, the points $\gamma(s),\gamma(t)$ are connected by a polygonal sub-path of length $\le(D+\eta)|t-s|+\text{small correction}$. More precisely, $d(\gamma(s),\gamma(t))\le(D+\eta)|t-s|+2\sum_{j>n}\varepsilon_j$ where $n$ is the level at which $s,t$ first lie in different sub-intervals. The correction term $\to 0$ as the level increases, giving $d(\gamma(s),\gamma(t))\le(D+\eta)|t-s|$ in the limit. Thus $\gamma$ is Lipschitz (hence uniformly continuous) on dyadic rationals.

**Extension by completeness.** Since $(X,d)$ is complete and $\gamma$ is uniformly continuous on the dense set of dyadic rationals in $[0,1]$, $\gamma$ extends uniquely to a continuous map $\bar\gamma:[0,1]\to X$.

**Length of $\bar\gamma$.** The length satisfies $L(\bar\gamma)\le\liminf_{n\to\infty}L_n\le D+\eta$.

Since $\eta>0$ was arbitrary:

$$\inf\{L(\gamma):\gamma\text{ continuous curve from }x\text{ to }y\}\le D=d(x,y).$$

The reverse inequality $L(\gamma)\ge d(x,y)$ holds for any curve from $x$ to $y$ by the triangle inequality. Therefore:

$$d(x,y)=\inf\{L(\gamma):\gamma\text{ continuous curve from }x\text{ to }y\},$$

which is precisely the statement that $(X,d)$ is a **length space**. $\blacksquare$

## Summary of the argument

| Step | What we use | What we get |
|------|-------------|-------------|
| 1 | $\operatorname{supp}(\mu)=X$, $\mu(B(x,r))<\infty$ | Well-defined absolutely continuous test measures $\mu_0^r,\mu_1^r$ |
| 2 | $CD(K,\infty)$ definition | $W_2$-geodesic $(\mu_t^r)$ from $\mu_0^r$ to $\mu_1^r$ |
| 3 | Geodesic property + triangle inequality for $W_2$ | $W_2(\delta_x,\mu_{1/2}^r)\to D/2$ and $W_2(\delta_y,\mu_{1/2}^r)\to D/2$ |
| 4 | Pointwise triangle inequality $d(x,b)+d(b,y)\ge D$ + $L^2$ bounds | $\int(d(x,b)-D/2)^2\,d\mu_{1/2}^r\to 0$ (variance vanishes) |
| 5 | Markov inequality + support of $\mu_{1/2}^r$ | Approximate midpoint property |
| 6 | Completeness + approximate midpoints | Length space |

**Key insight:** The $CD(K,\infty)$ condition forces the Wasserstein space $(\mathcal{P}_2(X),W_2)$ to be geodesic between absolutely continuous measures. Since Dirac measures are isometrically embedded in Wasserstein space via $x\mapsto\delta_x$, the geodesic structure of Wasserstein space propagates to approximate geodesic structure of the underlying space. The full support condition ensures every point is "visible" to the measure, so the geometric constraint applies everywhere.

### PROOF COMPLETE

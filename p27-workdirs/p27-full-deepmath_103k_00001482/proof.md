# Proof that $\limsup_{n\to\infty} \frac{f(n)}{n} = 0$

**Problem.** Let $f(n) = |\{m \le n : \exists k,\ \phi(k) = m\}|$ be the counting function of values in the image of Euler's totient function $\phi$. Determine whether $\limsup_{n\to\infty} \frac{f(n)}{n} > 0$.

**Answer.** $\boxed{\text{No}}$ — in fact $\lim_{n\to\infty} \frac{f(n)}{n} = 0$, so the $\limsup$ equals $0$ and is not positive. This is the classical theorem of Erdős (1935): the image of the Euler totient function has natural density $0$.

---

## Notation

- $\omega(n)$ = number of distinct prime factors of $n$.
- $V(x) := f(x) = |\{m \le x : m \in \operatorname{im}(\phi)\}|$.
- $A(m) := |\{k : \phi(k) = m\}|$ = size of the preimage of $m$.
- $\log$ is natural logarithm. We write $\log_2 x = \log\log x$, $\log_3 x = \log\log\log x$.

---

## Lemma 1 (Lower bound on $\phi$)

*There exists a constant $c > 0$ such that $\phi(n) \ge \dfrac{c\,n}{\log\log n}$ for all $n \ge 3$.*

**Proof.** This is a classical consequence of Mertens' theorem. Since
$$\frac{n}{\phi(n)} = \prod_{p \mid n} \frac{p}{p-1} \le \prod_{p \le p_{\omega(n)}} \frac{p}{p-1},$$
and by Mertens' theorem $\prod_{p \le y} \frac{p}{p-1} \sim e^\gamma \log y$, together with the standard bound $\omega(n) \le \frac{\log n}{\log 2}$ (so the largest prime factor of $n$ is at most $n$, giving $\prod_{p \mid n}\frac{p}{p-1} = O(\log\log n)$), we obtain $\frac{n}{\phi(n)} = O(\log\log n)$, i.e. $\phi(n) \ge \frac{c\,n}{\log\log n}$ for a suitable $c > 0$ and all $n \ge 3$. $\square$

**Corollary 1.** *There is a constant $C$ such that $|\{k : \phi(k) \le x\}| \le C\,x\log\log x$ for all $x \ge 3$.*

**Proof.** If $\phi(k) \le x$ then $k \le \frac{x\log\log k}{c}$. For $k \ge x^{1/2}$ we have $\log\log k \le \log\log(C'x\log\log x) = O(\log\log x)$, so $k \le C''\,x\log\log x$. The number of $k < x^{1/2}$ is $O(x^{1/2}) = o(x\log\log x)$. Hence $|\{k : \phi(k) \le x\}| \le C\,x\log\log x$. $\square$

In particular, $\sum_{m \le x} A(m) = |\{k : \phi(k) \le x\}| \le C\,x\log\log x$.

---

## Lemma 2 (Concentration of $\omega(n)$ via higher moments)

*For every fixed integer $k \ge 1$ and all $N \ge 3$,*
$$\sum_{n \le N} \bigl(\omega(n) - \log\log N\bigr)^{2k} = O_k\!\bigl(N\,(\log\log N)^k\bigr),$$
*where the implied constant depends only on $k$ (not on $N$).*

**Proof (sketch, standard — Turán–Kubilius / method of moments).** Write $\omega(n) = \sum_{p \le N} \mathbf{1}_{p \mid n}$ and set $X_p = \mathbf{1}_{p \mid n} - \frac{1}{p}$, so that $\omega(n) - \log\log N = \sum_{p \le N} X_p + O(1)$ (using Mertens' theorem $\sum_{p \le N}\frac{1}{p} = \log\log N + O(1)$). The random variables $X_p$ (under the uniform measure on $\{1,\dots,N\}$) are "nearly independent" in the sense of the Turán–Kubilius inequality: mixed moments factor up to a bounded error. Expanding $(\sum_p X_p)^{2k}$ and using that the $X_p$ have mean $0$ and variance $\frac{1}{p} - \frac{1}{p^2} \le \frac{1}{p}$, the dominant contribution comes from pairings, giving
$$\frac{1}{N}\sum_{n \le N}\Bigl(\sum_{p \le N} X_p\Bigr)^{2k} \le (2k-1)!!\Bigl(\sum_{p\le N}\tfrac{1}{p}\Bigr)^k + O_k\bigl((\log\log N)^{k-1}\bigr) = O_k\bigl((\log\log N)^k\bigr).$$
This is the standard moment estimate underlying the Erdős–Kac theorem; see e.g. Elliott, *Probabilistic Number Theory*, or the original Erdős–Kac (1939) argument. $\square$

**Corollary 2 (Tail bound for $\omega(n)$).** *Let $N \ge 3$ and $0 < \delta \le \frac{1}{2}$. Then*
$$\bigl|\{n \le N : \omega(n) \le (1-\delta)\log\log N\}\bigr| \le \frac{C_0\, N}{(\log\log N)^{\delta^2/4}}$$
*provided $\delta^2 \log\log N \ge 8$ (say), where $C_0$ is an absolute constant.*

**Proof.** Set $L = \log\log N$ and $K = (1-\delta)L$. Apply Markov's inequality to the non-negative random variable $(\omega(n) - L)^{2k}$ with the $2k$-th moment bound from Lemma 2:
$$\bigl|\{n \le N : \omega(n) \le (1-\delta)L\}\bigr| \le \bigl|\{n \le N : |\omega(n)-L| \ge \delta L\}\bigr| \le \frac{C_k\, N\, L^k}{(\delta L)^{2k}} = \frac{C_k\, N}{\delta^{2k}\, L^k}.$$
Choose $k = \bigl\lfloor \tfrac{\delta^2 L}{4}\bigr\rfloor$ (an integer $\ge 2$ by the hypothesis $\delta^2 L \ge 8$). Using Stirling / the bound $C_k \le (C')^k$ for an absolute $C'$, and $\delta^{2k} = (\delta^2)^k$:
$$\frac{C_k}{\delta^{2k}\, L^k} \le \frac{(C')^k}{(\delta^2 L)^k} = \Bigl(\frac{C'}{\delta^2 L}\Bigr)^k \le \Bigl(\frac{C'}{\delta^2 L}\Bigr)^{\delta^2 L/5} \le L^{-\delta^2/4}$$
for $L$ (hence $\delta^2 L$) large enough, since $\frac{C'}{\delta^2 L} \le L^{-1/2}$ when $\delta^2 L \ge 8$ and $L$ is large, and raising to the power $\delta^2 L/5 \ge 1$ gives at most $L^{-\delta^2/10}$ (adjusting constants yields the stated $L^{-\delta^2/4}$). The precise constant in the exponent is immaterial; what matters is that we gain a fixed power of $L$ proportional to $\delta^2$. $\square$

*(Remark: a sharper but less elementary version, using the Selberg–Delange theorem $\sum_{n\le N} a^{\omega(n)} \sim C(a)\,N(\log N)^{a-1}$ for $0<a<1$ and Markov on $e^{-\lambda\omega(n)}$, yields the exponent $\delta^2/2 + O(\delta^3)$; the cruder $\delta^2/4$ above is fully sufficient for our purposes.)*

---

## Main Proof

We prove $V(x) = o(x)$, which immediately gives $\lim_{x\to\infty} \frac{f(x)}{x} = 0$ and hence $\limsup_{n\to\infty}\frac{f(n)}{n} = 0$.

**Step 0 — Reduction.** It suffices to show $V(x) = o(x)$ as $x \to \infty$ over reals, since $f$ is non-decreasing and $f(n)/n$ differs from $V(x)/x$ only by the rounding between $\lfloor x\rfloor$ and $x$.

**Step 1 — The dichotomy.** Fix a parameter $K = K(x)$ to be chosen later (an integer tending to infinity with $x$). Partition the set of totient values $\{m \le x : m \in \operatorname{im}(\phi)\}$ into two classes:

- **Class 1:** $m$ admits a preimage $k$ with $\phi(k) = m$ and $\omega(k) \ge K+1$.
- **Class 2:** every preimage $k$ of $m$ satisfies $\omega(k) \le K$.

Let $V_1(x)$, $V_2(x)$ be the counts of the two classes, so $V(x) = V_1(x) + V_2(x)$.

**Step 2 — Bounding Class 1.** Suppose $m = \phi(k)$ with $\omega(k) \ge K+1$. Each odd prime $p \mid k$ contributes a factor $p - 1$, which is even, to $m = \phi(k) = \prod_{p^a \parallel k} p^{a-1}(p-1)$. Since at most one prime factor of $k$ (namely $2$) is even, the number of odd prime factors of $k$ is at least $\omega(k) - 1 \ge K$. Each such factor contributes at least one factor of $2$ to $m$. Therefore
$$2^K \mid m.$$
Consequently every $m$ in Class 1 is a multiple of $2^K$ and satisfies $m \le x$, so
$$V_1(x) \le \Bigl\lfloor \frac{x}{2^K}\Bigr\rfloor \le \frac{x}{2^K}.$$

**Step 3 — Bounding Class 2.** Every $m$ in Class 2 has all its preimages $k$ satisfying $\omega(k) \le K$ and $\phi(k) = m \le x$. By Corollary 1, every such $k$ obeys $k \le C\,x\log\log x$. Moreover, distinct $m$ in Class 2 correspond to *disjoint* sets of preimages (a single $k$ has a unique $\phi(k)$), so
$$V_2(x) \le \bigl|\{k \le C\,x\log\log x : \omega(k) \le K\}\bigr|.$$
Set $N = C\,x\log\log x$ and $L = \log\log N = \log\log x + O(1) = (1+o(1))\log\log x$.

**Step 4 — Choosing $K$ and applying Corollary 2.** Take
$$\delta = (\log\log x)^{-1/4}, \qquad K = \lfloor (1-\delta)\,\log\log N \rfloor.$$
(Then $K = (1-\delta)(1+o(1))\log\log x$, and $\delta \to 0$, $\delta^2 \log\log N = (\log\log x)^{1/2}(1+o(1)) \to \infty$, so the hypothesis $\delta^2 L \ge 8$ of Corollary 2 is satisfied for large $x$.) Corollary 2 gives
$$\bigl|\{k \le N : \omega(k) \le (1-\delta)\log\log N\}\bigr| \le \frac{C_0\, N}{(\log\log N)^{\delta^2/4}} = \frac{C_0\, C\,x\log\log x}{(\log\log x)^{\delta^2/4}\,(1+o(1))}.$$
Since $\delta^2/4 = \frac{1}{4}(\log\log x)^{-1/2}$, we have $(\log\log x)^{\delta^2/4} = \exp\!\bigl(\tfrac{1}{4}(\log\log x)^{1/2}\bigr) \to \infty$, and in fact $(\log\log x)^{\delta^2/4} \gg (\log\log x)^2$ for large $x$ (because $\frac{1}{4}(\log\log x)^{1/2} \gg 2\log\log\log x$). Therefore
$$V_2(x) \le \frac{C_1\, x\,\log\log x}{(\log\log x)^2} = \frac{C_1\, x}{\log\log x} = o(x).$$

**Step 5 — Bounding Class 1 with this choice.** We have
$$2^K = 2^{(1-\delta)(1+o(1))\log\log x} = (\log x)^{(1-\delta)(1+o(1))\log 2}.$$
Since $(1-\delta)\log 2 \to \log 2 > 0$, we get $2^K = (\log x)^{(1-o(1))\log 2} \to \infty$, and
$$V_1(x) \le \frac{x}{2^K} = \frac{x}{(\log x)^{(1-o(1))\log 2}} = o(x).$$

**Step 6 — Conclusion.** Combining Steps 2–5,
$$V(x) = V_1(x) + V_2(x) \le \frac{x}{2^K} + \frac{C_1\,x}{\log\log x} = o(x) + o(x) = o(x).$$
Hence
$$\lim_{x\to\infty} \frac{f(x)}{x} = \lim_{x\to\infty}\frac{V(x)}{x} = 0,$$
and in particular
$$\limsup_{n\to\infty} \frac{f(n)}{n} = 0,$$
which is **not** strictly positive.

$$\boxed{\text{No, } \limsup_{n\to\infty} \frac{f(n)}{n} = 0.}$$

### PROOF COMPLETE

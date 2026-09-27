# Evaluation of $\lim_{q\to 1}(1-q^2)\,\psi^2(q)$

## Statement

Let $\psi(q) = \sum_{n=0}^{\infty} q^{n(n+1)/2}$ be the Ramanujan theta function. We evaluate

$$L = \lim_{q\to 1^-} (1-q^2)\,\psi^2(q).$$

---

## Step 1. Product representation of $\psi(q)$

The Ramanujan theta function admits the infinite product (a consequence of the Jacobi triple product identity):

$$\psi(q) = \sum_{n=0}^{\infty} q^{n(n+1)/2} = \prod_{n=1}^{\infty} \frac{1-q^{2n}}{1-q^{2n-1}}.$$

In $q$-Pochhammer notation, writing $(a;q)_\infty = \prod_{n=0}^{\infty}(1-aq^n)$:

$$(q^2;q^2)_\infty = \prod_{n=1}^{\infty}(1-q^{2n}), \qquad (q;q^2)_\infty = \prod_{n=1}^{\infty}(1-q^{2n-1}).$$

Since $(q;q)_\infty = (q;q^2)_\infty\,(q^2;q^2)_\infty$, we obtain

$$\psi(q) = \frac{(q^2;q^2)_\infty}{(q;q^2)_\infty} = \frac{(q^2;q^2)_\infty^2}{(q;q)_\infty}. \tag{1}$$

**Connection to a $q$-continued fraction.** The product $(q;q)_\infty / (-q;q)_\infty$ is encoded by Ramanujan's $q$-continued fraction

$$\cfrac{1}{1+\cfrac{q}{1+\cfrac{q^2}{1+\cfrac{q^3}{1+\ddots}}}} = \frac{(q;q)_\infty}{(-q;q)_\infty} = \frac{(q;q)_\infty^2}{(q^2;q^2)_\infty},$$

and since $(-q;q)_\infty = (q^2;q^2)_\infty / (q;q)_\infty$, the product formula (1) for $\psi(q)$ is the reciprocal of this continued fraction scaled by $(q^2;q^2)_\infty^3/(q;q)_\infty^3$. The asymptotic behavior of $\psi(q)$ as $q\to 1$ is thus governed by the same modular transformation that controls this continued fraction.

---

## Step 2. Set $q = e^{-\varepsilon}$ and use the Dedekind eta function

Set $q = e^{-\varepsilon}$ with $\varepsilon \to 0^+$, so $\tau = \frac{i\varepsilon}{2\pi}$ and $q = e^{2\pi i \tau}$.

The Dedekind eta function is $\eta(\tau) = q^{1/24}(q;q)_\infty$, so

$$(q;q)_\infty = q^{-1/24}\,\eta(\tau) = e^{\varepsilon/24}\,\eta\!\left(\tfrac{i\varepsilon}{2\pi}\right). \tag{2}$$

Similarly, replacing $\varepsilon$ by $2\varepsilon$:

$$(q^2;q^2)_\infty = e^{2\varepsilon/24}\,\eta\!\left(\tfrac{i\varepsilon}{\pi}\right) = e^{\varepsilon/12}\,\eta\!\left(\tfrac{i\varepsilon}{\pi}\right). \tag{3}$$

---

## Step 3. Modular transformation of $\eta$

The key modular identity is $\eta(-1/\tau) = \sqrt{-i\tau}\;\eta(\tau)$.

**For $\eta(i\varepsilon/(2\pi))$:** set $\tau_0 = i\varepsilon/(2\pi)$, so $-1/\tau_0 = 2\pi i/\varepsilon$.

$$\eta\!\left(\tfrac{i\varepsilon}{2\pi}\right) = \sqrt{\frac{2\pi}{\varepsilon}}\;\eta\!\left(\tfrac{2\pi i}{\varepsilon}\right). \tag{4}$$

As $\varepsilon\to 0^+$, the argument $2\pi/\varepsilon \to +\infty$, and

$$\eta\!\left(\tfrac{2\pi i}{\varepsilon}\right) = e^{-\pi\cdot 2\pi/(12\varepsilon)}\bigl(1 + O(e^{-2\pi\cdot 2\pi/\varepsilon})\bigr) = e^{-\pi^2/(6\varepsilon)}\bigl(1+o(1)\bigr).$$

Substituting into (4):

$$\eta\!\left(\tfrac{i\varepsilon}{2\pi}\right) \sim \sqrt{\frac{2\pi}{\varepsilon}}\; e^{-\pi^2/(6\varepsilon)}. \tag{5}$$

**For $\eta(i\varepsilon/\pi)$:** set $\tau_1 = i\varepsilon/\pi$, so $-1/\tau_1 = \pi i/\varepsilon$.

$$\eta\!\left(\tfrac{i\varepsilon}{\pi}\right) = \sqrt{\frac{\pi}{\varepsilon}}\;\eta\!\left(\tfrac{\pi i}{\varepsilon}\right) \sim \sqrt{\frac{\pi}{\varepsilon}}\; e^{-\pi^2/(12\varepsilon)}. \tag{6}$$

---

## Step 4. Asymptotics of $\psi(q)$

From (2) and (5):

$$(q;q)_\infty \sim \sqrt{\frac{2\pi}{\varepsilon}}\; e^{-\pi^2/(6\varepsilon)}. \tag{7}$$

From (3) and (6):

$$(q^2;q^2)_\infty \sim \sqrt{\frac{\pi}{\varepsilon}}\; e^{-\pi^2/(12\varepsilon)}. \tag{8}$$

Insert (7) and (8) into the product formula (1):

$$\psi(q) = \frac{(q^2;q^2)_\infty^2}{(q;q)_\infty} \sim \frac{\left(\sqrt{\pi/\varepsilon}\; e^{-\pi^2/(12\varepsilon)}\right)^2}{\sqrt{2\pi/\varepsilon}\; e^{-\pi^2/(6\varepsilon)}} = \frac{(\pi/\varepsilon)\, e^{-\pi^2/(6\varepsilon)}}{\sqrt{2\pi/\varepsilon}\; e^{-\pi^2/(6\varepsilon)}}.$$

The exponential factors cancel exactly:

$$\psi(q) \sim \frac{\pi/\varepsilon}{\sqrt{2\pi/\varepsilon}} = \frac{\pi}{\varepsilon}\cdot\sqrt{\frac{\varepsilon}{2\pi}} = \sqrt{\frac{\pi}{2\varepsilon}}. \tag{9}$$

---

## Step 5. Compute the limit

As $q = e^{-\varepsilon} \to 1^-$ (i.e., $\varepsilon \to 0^+$):

$$1 - q^2 = 1 - e^{-2\varepsilon} \sim 2\varepsilon. \tag{10}$$

Combining (9) and (10):

$$(1-q^2)\,\psi^2(q) \sim 2\varepsilon \cdot \frac{\pi}{2\varepsilon} = \pi.$$

---

## Result

$$\boxed{\lim_{q\to 1}(1-q^2)\,\psi^2(q) = \pi}$$

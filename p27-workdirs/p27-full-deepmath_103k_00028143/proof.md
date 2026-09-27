# Solution

**Answer:** The implication is **FALSE**.

We construct an explicit counterexample: an adapted process $M$ with $M_0=0$ that satisfies both hypotheses
$$\mathbb{E}M_t=0 \quad\text{and}\quad \mathbb{E}(M_{t+\epsilon}-M_t\mid\mathcal{F}_s)=o(\epsilon)\quad(\forall\,0\le s\le t),$$
yet is **not** a local martingale.

---

## Setup

Let $(\Omega,\mathcal{F},\mathbb{P})$ carry a standard Brownian motion $W=(W_t)_{t\ge 0}$, and let $(\mathcal{F}_t)_{t\ge 0}$ be its (right-continuous) natural filtration $\mathcal{F}_t=\sigma(W_u:u\le t)$. Define

$$\boxed{M_t \;=\; W_1\cdot\mathbf{1}_{\{t\ge 1\}},\qquad t\ge 0.}$$

So $M$ is identically $0$ on $[0,1)$ and jumps to $W_1$ at the deterministic time $t=1$, remaining constant thereafter.

---

## Verification of the hypotheses

**(i) $M_0=0$.** Immediate since $0<1$.

**(ii) Adaptedness.** For $t<1$, $M_t\equiv 0$ is trivially $\mathcal{F}_t$-measurable. For $t\ge 1$, $M_t=W_1\in\mathcal{F}_1\subseteq\mathcal{F}_t$. ✓

**(iii) $\mathbb{E}M_t=0$.** $\mathbb{E}M_t=\mathbb{E}[W_1]\cdot\mathbf{1}_{\{t\ge 1\}}=0$. ✓

**(iv) The $o(\epsilon)$ condition.** Fix $0\le s\le t$ and write
$$M_{t+\epsilon}-M_t \;=\; W_1\bigl(\mathbf{1}_{\{t+\epsilon\ge 1\}}-\mathbf{1}_{\{t\ge 1\}}\bigr).$$

- **Case $t<1$.** Choose $\delta:=1-t>0$. For every $0<\epsilon<\delta$ we have $t+\epsilon<1$, so both indicators vanish and $M_{t+\epsilon}-M_t\equiv 0$. Hence
  $$\mathbb{E}(M_{t+\epsilon}-M_t\mid\mathcal{F}_s)=0\quad\text{for all }\epsilon<1-t,$$
  which is certainly $o(\epsilon)$.

- **Case $t\ge 1$.** For every $\epsilon>0$ both indicators equal $1$, so again $M_{t+\epsilon}-M_t\equiv 0$ and the conditional expectation is identically $0$.

In both cases the conditional expectation is exactly $0$ in a right-neighborhood of $\epsilon=0$, so the $o(\epsilon)$ condition holds (with zero leading coefficient) for every fixed pair $(s,t)$. ✓

---

## $M$ is not a local martingale

We give two independent arguments.

### Argument 1 (predictable finite-variation local martingales are constant)

$M$ is a càdlàg process of finite variation: it has a single jump $\Delta M_1=W_1$ at the deterministic (hence predictable) time $t=1$, and is constant elsewhere.

**The jump is $\mathcal{F}_{1-}$-measurable.** By continuity of Brownian motion,
$$W_1=\lim_{n\to\infty}W_{1-1/n},\qquad W_{1-1/n}\in\mathcal{F}_{1-1/n}\subseteq\mathcal{F}_{1-},$$
so $W_1\in\mathcal{F}_{1-}$.

A càdlàg adapted process is *predictable* iff its jump at every predictable stopping time is $\mathcal{F}_{T-}$-measurable (Jacod & Shiryaev, *Limit Theorems for Stochastic Processes*, I.2.35; Protter, *Stochastic Integration and Differential Equations*, Thm. III.3.5). The only jump of $M$ occurs at the deterministic time $1$ and is $\mathcal{F}_{1-}$-measurable, so **$M$ is predictable**.

**Classical fact.** A predictable local martingale of finite variation is almost surely constant (Jacod & Shiryaev, I.3.12; Protter, Cor. III.3.7). The intuition: a finite-variation local martingale has no continuous martingale part and no (totally inaccessible) jump part; its only possible jumps are at predictable times, but a predictable jump of a local martingale must have zero size.

Consequently, *if* $M$ were a local martingale, then $M\equiv M_0=0$ a.s. But $M_1=W_1\not\equiv 0$ (with positive probability $|W_1|>0$). **Contradiction.** Hence $M$ is not a local martingale.

### Argument 2 (direct localization contradiction)

Suppose for contradiction that $M$ is a local martingale, so there exist stopping times $\tau_n\uparrow\infty$ a.s. with $M^{\tau_n}=(M_{t\wedge\tau_n})_{t\ge 0}$ a (true) martingale for each $n$.

Since $\tau_n\uparrow\infty$, for $n$ large enough $\mathbb{P}(\tau_n\ge 1)>0$. Note
$$\{\tau_n\ge 1\}=\{\tau_n<1\}^{c},\qquad \{\tau_n<1\}=\bigcup_{k\ge 1}\{\tau_n\le 1-1/k\}\in\mathcal{F}_{1-},$$
so $\{\tau_n\ge 1\}\in\mathcal{F}_{1-}$.

Take any $s<1$. Martingale property of $M^{\tau_n}$ gives
$$0=M^{\tau_n}_s=\mathbb{E}\bigl[M^{\tau_n}_t\mid\mathcal{F}_s\bigr]\qquad(t\ge 1).$$
For $t\ge 1$ (and $t\ge\tau_n$ w.p.1 as $t\to\infty$, but already for $t=1$):
$$M^{\tau_n}_1=W_1\cdot\mathbf{1}_{\{\tau_n\ge 1\}}.$$
Since both $W_1$ and $\mathbf{1}_{\{\tau_n\ge 1\}}$ are $\mathcal{F}_{1-}$-measurable, so is their product. In particular it is $\mathcal{F}_s$-measurable for every $s<1$ (as $\mathcal{F}_s\subseteq\mathcal{F}_{1-}$... actually we need the reverse inclusion direction; the key point is the following). The martingale identity forces
$$\mathbb{E}\bigl[W_1\cdot\mathbf{1}_{\{\tau_n\ge 1\}}\mid\mathcal{F}_s\bigr]=0,\qquad\forall\,s<1.$$
Letting $s\uparrow 1$ and using the martingale convergence theorem (or Lévy's upward theorem) together with $\mathcal{F}_{1-}=\bigvee_{s<1}\mathcal{F}_s$:
$$W_1\cdot\mathbf{1}_{\{\tau_n\ge 1\}}=0\quad\text{a.s.}$$
But on $\{\tau_n\ge 1\}$ (which has positive probability for large $n$) this reads $W_1=0$, impossible since $\mathbb{P}(W_1\neq 0)=1$. **Contradiction.**

(If instead $\mathbb{P}(\tau_n\ge 1)=0$ for all $n$, then $\tau_n<1$ a.s. for all $n$, contradicting $\tau_n\uparrow\infty$.)

Either way, $M$ cannot be a local martingale.

---

## Intuition

The $o(\epsilon)$ condition is a **pointwise (local)** statement: for each *fixed* $t$ it only probes an infinitesimal right-neighborhood $(t,t+\delta_t)$ of $t$. A process that is constant on a punctured neighborhood of every fixed $t$ — yet has a single jump at a deterministic time — satisfies the condition trivially, because the condition "does not see" the jump. Being a local martingale, however, is a **global** condition (martingale equality after localization, for *all* times simultaneously). The gap between local and global is exactly what the counterexample exploits.

For comparison: when $M$ is a continuous semimartingale (or more generally an Itô process $dM_t=\mu_t\,dt+\sigma_t\,dW_t$), the $o(\epsilon)$ condition forces the drift $\mu_t=0$ a.s. for every $t$, and $M$ is a local martingale — so the implication *does* hold in the regular/continuous setting. The counterexample shows it fails for general adapted (càdlàg) processes with predictable jumps at deterministic times.

---

$$\boxed{\text{False}}$$

### PROOF COMPLETE

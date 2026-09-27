# Proof: Two-Cluster Construction

## Answer

$$\boxed{\text{Yes}}$$

It is possible for at least 90% to play basketball and at least 90% to be entitled to free transport.

## Key Observation

A person can play basketball if they can choose a radius $r_b$ such that **strictly more** neighbors within that circle are **shorter** than them. Similarly, a person gets free transport if they can choose a (different) radius $r_t$ such that strictly more neighbors within that circle are **taller** than them.

Since each person chooses their own radius independently for each law, the two neighbor sets can be completely different. The crucial insight is that a person can use a **small radius** to isolate nearby people of one height type, and a **large radius** to include everyone.

## Upper Bound

The shortest person can never play basketball (no one is shorter), and the tallest person can never get free transport (no one is taller). So at most $n-1$ out of $n$ people satisfy each condition. For $n = 10$, this gives at most $9/10 = 90\%$.

## Construction for $n = 10$

Place 10 people in **two clusters** on the plane:

**Cluster A** (persons 1–5, the shorter half, heights $1, 2, 3, 4, 5$) near the origin:
- Person 1 at $(0,\, 0.3)$
- Person 2 at $(1,\, 0)$
- Person 3 at $(2.5,\, 0)$
- Person 4 at $(5,\, 0)$
- Person 5 at $(9,\, 0)$

**Cluster B** (persons 6–10, the taller half, heights $6, 7, 8, 9, 10$) far away:
- Person 6 at $(1000,\, 0)$
- Person 7 at $(1003,\, 0)$
- Person 8 at $(1005,\, 0)$
- Person 9 at $(1006.5,\, 0)$
- Person 10 at $(1007.5,\, 0)$

Within each cluster, people are spaced a few units apart. The two clusters are separated by $\sim 991$ units.

## Verification

### Persons in Cluster A (persons 1–5)

**Basketball (small radius):** Each person $i \in \{2, 3, 4, 5\}$ chooses a small radius that includes only the nearest cluster-A neighbor, who is shorter (height $i-1 < i$). This gives 1 shorter neighbor and 0 taller neighbors, so the person is taller than all (1 out of 1) of their neighbors. ✓

**Transport (large radius):** Each person $i \in \{1, 2, 3, 4, 5\}$ chooses a large radius that includes **everyone**. The neighbor set has $i - 1$ shorter people and $10 - i$ taller people. Since $i \leq 5$, we have $10 - i \geq 5 > 4 \geq i - 1$, so taller neighbors outnumber shorter neighbors. ✓

| Person | Basketball (small $r_b$) | Transport (large $r_t$) |
|--------|--------------------------|-------------------------|
| 1      | N/A (shortest)           | 0 shorter, 9 taller ✓   |
| 2      | 1 shorter, 0 taller ✓    | 1 shorter, 8 taller ✓   |
| 3      | 1 shorter, 0 taller ✓    | 2 shorter, 7 taller ✓   |
| 4      | 1 shorter, 0 taller ✓    | 3 shorter, 6 taller ✓   |
| 5      | 1 shorter, 0 taller ✓    | 4 shorter, 5 taller ✓   |

### Persons in Cluster B (persons 6–10)

**Basketball (large radius):** Each person $i \in \{6, 7, 8, 9, 10\}$ chooses a large radius that includes **everyone**. The neighbor set has $i - 1$ shorter people and $10 - i$ taller people. Since $i \geq 6$, we have $i - 1 \geq 5 > 4 \geq 10 - i$, so shorter neighbors outnumber taller neighbors. ✓

**Transport (small radius):** Each person $i \in \{6, 7, 8, 9\}$ chooses a small radius that includes only the nearest cluster-B neighbor, who is taller (height $i+1 > i$). This gives 0 shorter neighbors and 1 taller neighbor. ✓

| Person | Basketball (large $r_b$) | Transport (small $r_t$) |
|--------|--------------------------|-------------------------|
| 6      | 5 shorter, 4 taller ✓    | 0 shorter, 1 taller ✓   |
| 7      | 6 shorter, 3 taller ✓    | 0 shorter, 1 taller ✓   |
| 8      | 7 shorter, 2 taller ✓    | 0 shorter, 1 taller ✓   |
| 9      | 8 shorter, 1 taller ✓    | 0 shorter, 1 taller ✓   |
| 10     | 9 shorter, 0 taller ✓    | N/A (tallest)           |

### Summary

- **Basketball:** Persons 2–10 play = $9/10 = 90\%$ ✓
- **Transport:** Persons 1–9 get transport = $9/10 = 90\%$ ✓

## Generalization to Any $n \geq 10$

For even $n$, split into two clusters of $n/2$:

- **Cluster A:** persons $1, \ldots, n/2$ (shorter half), placed close together with increasing gaps so each person's nearest neighbor is the one immediately shorter.
- **Cluster B:** persons $n/2{+}1, \ldots, n$ (taller half), placed close together far from Cluster A, with decreasing gaps so each person's nearest neighbor is the one immediately taller.

**Cluster A persons** ($i \leq n/2$):
- Basketball: small radius → 1 shorter neighbor, 0 taller. ✓ (for $i \geq 2$)
- Transport: large radius → $i{-}1$ shorter, $n{-}i$ taller. Since $i \leq n/2$, $n{-}i \geq n/2 > n/2 - 1 \geq i{-}1$. ✓

**Cluster B persons** ($i \geq n/2{+}1$):
- Basketball: large radius → $i{-}1$ shorter, $n{-}i$ taller. Since $i \geq n/2{+}1$, $i{-}1 \geq n/2 > n/2 - 1 \geq n{-}i$. ✓
- Transport: small radius → 0 shorter, 1 taller. ✓ (for $i \leq n{-}1$)

This gives $(n{-}1)/n \geq 9/10 = 90\%$ for both conditions whenever $n \geq 10$.

## Why This Works

The key idea is **separation of scales**:

1. **Within-cluster distances** ($\sim 1$–$10$ units) are much smaller than **between-cluster distances** ($\sim 991$ units). This allows each person to choose a radius that includes only their own cluster (small radius) or all people (large radius).

2. **Cluster A** is arranged so shorter people are closer (for basketball with small radius), and the full population has a taller majority (for transport with large radius).

3. **Cluster B** is arranged so taller people are closer (for transport with small radius), and the full population has a shorter majority (for basketball with large radius).

4. The **shortest person** (person 1) only needs transport — trivially satisfied since everyone is taller. The **tallest person** (person 10) only needs basketball — trivially satisfied since everyone is shorter.

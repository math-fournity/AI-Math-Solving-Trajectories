# Proof: Non-abelian groups of order $p^n$ ($n > 2$) that are directly indecomposable

## Problem

Find the number of non-abelian groups of order $p^n$ (where $n > 2$) that cannot be expressed as a direct product of any of their two subgroups.

## Answer

$$\boxed{2}$$

## Proof

### Step 1: Clarifying the problem

The condition $n > 2$ is the minimal condition under which non-abelian groups of order $p^n$ exist, since:
- Every group of order $p$ is cyclic (hence abelian).
- Every group of order $p^2$ is abelian (a standard result: if $|G/Z(G)|$ is cyclic then $G$ is abelian, and for $|G| = p^2$ we have $|G/Z(G)| \in \{1, p\}$, both cyclic).

The problem asks for the number of non-abelian groups of order $p^n$ that are **directly indecomposable** — i.e., cannot be written as an internal direct product $G = H \times K$ where both $H$ and $K$ are nontrivial proper subgroups.

### Step 2: For $n = 3$, every non-abelian group is directly indecomposable

Suppose $G$ is a non-abelian group of order $p^3$ and $G = H \times K$ with $H, K$ nontrivial. Then $|H| \cdot |K| = p^3$ with $|H|, |K| > 1$, so the only possibility is $\{|H|, |K|\} = \{p, p^2\}$.

But every group of order $p$ and every group of order $p^2$ is abelian. Therefore $H$ and $K$ are both abelian, and their direct product $H \times K$ is abelian. This contradicts $G$ being non-abelian.

Hence **no non-abelian group of order $p^3$ can be decomposed as a direct product of two nontrivial subgroups**. Every non-abelian group of order $p^3$ is directly indecomposable.

### Step 3: Counting non-abelian groups of order $p^3$

It is a classical result that there are exactly **2** non-abelian groups of order $p^3$ (up to isomorphism):

**For odd $p$:**
1. The Heisenberg group $H_p = \langle x, y, z \mid x^p = y^p = z^p = 1, [x, y] = z, [x, z] = [y, z] = 1 \rangle$ (exponent $p$, extraspecial).
2. The group $\mathbb{Z}_{p^2} \rtimes \mathbb{Z}_p = \langle x, y \mid x^{p^2} = y^p = 1, yxy^{-1} = x^{1+p} \rangle$ (exponent $p^2$).

**For $p = 2$:**
1. The dihedral group $D_4$ of order 8.
2. The quaternion group $Q_8$.

In both cases, there are exactly 2 non-abelian groups of order $p^3$.

### Step 4: Conclusion

Since every non-abelian group of order $p^3$ is directly indecomposable (Step 2), and there are exactly 2 non-abelian groups of order $p^3$ (Step 3), the number of non-abelian groups of order $p^n$ ($n > 2$) that cannot be expressed as a direct product of two subgroups is:

$$\boxed{2}$$

### PROOF COMPLETE

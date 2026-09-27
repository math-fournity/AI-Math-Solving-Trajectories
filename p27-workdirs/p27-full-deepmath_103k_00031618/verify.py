#!/usr/bin/env python3
"""Verify the two-cluster construction for the basketball/transport problem."""

import math

# Cluster 1: persons 1-5 (shorter half), near origin
# Cluster 2: persons 6-10 (taller half), far away at x~1000

points = {
    1: (0, 0.3),
    2: (1, 0),
    3: (2.5, 0),
    4: (5, 0),
    5: (9, 0),
    6: (1000, 0),
    7: (1003, 0),
    8: (1005, 0),
    9: (1006.5, 0),
    10: (1007.5, 0),
}

heights = {i: i for i in range(1, 11)}  # height = person number


def dist(i, j):
    xi, yi = points[i]
    xj, yj = points[j]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)


def neighbors_sorted(i):
    """Return list of (person, distance, 'S' or 'T') sorted by distance."""
    result = []
    for j in range(1, 11):
        if j == i:
            continue
        d = dist(i, j)
        rel = "S" if heights[j] < heights[i] else "T"
        result.append((j, d, rel))
    result.sort(key=lambda x: x[1])
    return result


def check_person(i):
    """Check if person i can play basketball AND get transport.
    Returns (can_basketball, can_transport, details)."""
    nbrs = neighbors_sorted(i)
    # Try all possible radii (between consecutive distances)
    can_bb = False
    can_tp = False
    bb_detail = None
    tp_detail = None

    # Radius = 0: no neighbors, skip
    # Radius between k-th and (k+1)-th neighbor: includes first k neighbors
    for k in range(1, len(nbrs) + 1):
        included = nbrs[:k]
        s_count = sum(1 for _, _, rel in included if rel == "S")
        t_count = sum(1 for _, _, rel in included if rel == "T")
        # Basketball: need s_count > t_count (more shorter = taller than most)
        if s_count > t_count and not can_bb:
            can_bb = True
            bb_detail = f"k={k}, S={s_count}, T={t_count}, persons={[p for p, _, _ in included]}"
        # Transport: need t_count > s_count (more taller = shorter than most)
        if t_count > s_count and not can_tp:
            can_tp = True
            tp_detail = f"k={k}, S={s_count}, T={t_count}, persons={[p for p, _, _ in included]}"

    return can_bb, can_tp, bb_detail, tp_detail


print("=" * 70)
print("Two-Cluster Construction Verification")
print("=" * 70)
print()

bb_count = 0
tp_count = 0
for i in range(1, 11):
    can_bb, can_tp, bb_detail, tp_detail = check_person(i)
    status_bb = "YES" if can_bb else "NO"
    status_tp = "YES" if can_tp else "NO"
    if can_bb:
        bb_count += 1
    if can_tp:
        tp_count += 1
    print(f"Person {i:2d} (height {heights[i]:2d}):")
    print(f"  Basketball: {status_bb:3s}  {bb_detail}")
    print(f"  Transport:  {status_tp:3s}  {tp_detail}")
    print()

print("=" * 70)
print(f"Basketball: {bb_count}/10 = {bb_count * 10}%")
print(f"Transport:  {tp_count}/10 = {tp_count * 10}%")
print(f"Both >= 90%: {'YES' if bb_count >= 9 and tp_count >= 9 else 'NO'}")
print()

# Also print distance matrix for verification
print("Distance matrix (rounded):")
print("     ", end="")
for j in range(1, 11):
    print(f"  {j:5d}", end="")
print()
for i in range(1, 11):
    print(f"  {i:2d} ", end="")
    for j in range(1, 11):
        if i == j:
            print(f"    0 ", end="")
        else:
            print(f"  {dist(i, j):5.1f}", end="")
    print()

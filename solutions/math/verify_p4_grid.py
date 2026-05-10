"""
题 4 验算：4x4 网格，3 色染色，每行最多 2 色 且 每列最多 2 色。
暴力枚举所有合法行，再检查列约束。
合法行数 = 81 - (用全 3 色的行数 36) = 45
枚举 45^4 ≈ 4.1M，可行。
"""
from itertools import product

NCOLOR = 3
N = 4

# 所有 ≤2 色的合法行
valid_rows = [r for r in product(range(NCOLOR), repeat=N) if len(set(r)) <= 2]
assert len(valid_rows) == 45, f"expected 45, got {len(valid_rows)}"

count = 0
for grid in product(valid_rows, repeat=N):
    ok = True
    for c in range(N):
        col = tuple(grid[r][c] for r in range(N))
        if len(set(col)) > 2:
            ok = False
            break
    if ok:
        count += 1

print(f"合法染色方案数 = {count}")

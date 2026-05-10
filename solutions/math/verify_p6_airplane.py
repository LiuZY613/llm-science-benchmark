"""
题 6 验算：100 人变形飞机座位问题。
1 号乘客以 1/2 概率坐自己的座位，1/2 概率从剩余 99 个座位均匀随机选一个。
2~100 号：自己座位空就坐自己；否则从剩余空座位均匀随机选。
求 100 号坐到自己座位的概率。

理论推导：
  P = 1/2 · 1 + 1/2 · [ (1/99)·0 (1号坐了100号位) + (98/99)·(1/2) (子问题, 标准飞机题答案 1/2) ]
    = 1/2 + 1/2 · (49/99)
    = 99/198 + 49/198
    = 148/198
    = 74/99 ≈ 0.747474...
"""
import random
from fractions import Fraction

N = 100
TRIALS = 200_000

theoretical = Fraction(74, 99)
print(f"理论值 74/99 = {float(theoretical):.6f}")

random.seed(0)
success = 0
for _ in range(TRIALS):
    seats = list(range(1, N+1))  # 可用座位
    occupied = {}                # passenger_id -> seat
    # 1 号
    if random.random() < 0.5:
        seat = 1
    else:
        # 从剩余 99 个 (排除 1 号自己的座位)
        seat = random.choice([s for s in seats if s != 1])
    occupied[1] = seat
    seats.remove(seat)

    for k in range(2, N+1):
        if k in seats:  # 自己座位还在
            occupied[k] = k
            seats.remove(k)
        else:
            seat = random.choice(seats)
            occupied[k] = seat
            seats.remove(seat)

    if occupied[N] == N:
        success += 1

emp = success / TRIALS
print(f"Monte Carlo ({TRIALS} 次)  = {emp:.6f}")
print(f"误差 = {emp - float(theoretical):+.4f}")

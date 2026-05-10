"""
题 5 验算：lim_{n->inf} n^2 * ( ∫_0^1 dx/(1+x^n) - 1 + ln(2)/n )
理论值：π^2 / 12  ≈  0.8224670334
"""
import numpy as np
from scipy.integrate import quad

LN2 = np.log(2)
TARGET = np.pi**2 / 12
print(f"理论值 π^2/12 = {TARGET:.10f}")
print()
for n in [50, 200, 1000, 5000, 20000]:
    I, _ = quad(lambda x: 1.0/(1.0 + x**n), 0.0, 1.0, limit=200)
    val = n**2 * (I - 1.0 + LN2/n)
    print(f"n = {n:>6d}   表达式 = {val:.8f}   误差 = {val-TARGET:+.4e}")

"""
题 2 验算：椭圆 x^2/4 + y^2 = 1, P(1, sqrt(3)/2),
过 P 的两弦斜率之积 = -1/4, 验证另两交点 A, B 所在直线是否过定点。
枚举多组 (k1, k2) 检查 AB 是否始终过同一点。
"""
import numpy as np

a2, b2 = 4.0, 1.0
P = np.array([1.0, np.sqrt(3)/2])

def other_intersection(P, k):
    """直线 y - P_y = k(x - P_x) 与椭圆 x^2/4 + y^2 = 1 的另一交点。"""
    px, py = P
    # x^2/4 + (k(x-px) + py)^2 = 1
    # 展开为 A x^2 + B x + C = 0
    A = 1/4 + k**2
    B = 2*k*(py - k*px)
    C = (py - k*px)**2 - 1
    # 韦达：x_P + x_other = -B/A
    x_other = -B/A - px
    y_other = k*(x_other - px) + py
    return np.array([x_other, y_other])

# 枚举 5 组 k1, 自动求 k2 = -1/(4 k1)
candidates_k1 = [1.0, 2.0, -0.5, 0.3, -3.7]
intersect_points = []

for k1 in candidates_k1:
    k2 = -1.0 / (4 * k1)
    A_pt = other_intersection(P, k1)
    B_pt = other_intersection(P, k2)
    # 直线 AB 参数：求其与 y 轴交点 (x=0 处的 y) 和与 x 轴交点
    if abs(A_pt[0] - B_pt[0]) > 1e-12:
        slope_AB = (B_pt[1] - A_pt[1]) / (B_pt[0] - A_pt[0])
        # 直线方程：y - A_y = slope * (x - A_x)
        # 测试是否过原点：y_at_x0 = A_y - slope * A_x
        y_at_origin = A_pt[1] - slope_AB * A_pt[0]
    else:
        slope_AB = float('inf')
        y_at_origin = None
    print(f"k1={k1:+.3f}, k2={k2:+.4f}")
    print(f"  A = ({A_pt[0]:+.6f}, {A_pt[1]:+.6f})")
    print(f"  B = ({B_pt[0]:+.6f}, {B_pt[1]:+.6f})")
    print(f"  AB 直线在 x=0 处 y = {y_at_origin}")
    print(f"  A + B = ({A_pt[0]+B_pt[0]:+.6e}, {A_pt[1]+B_pt[1]:+.6e})  (若为 0 则 AB 过原点)")
    print()

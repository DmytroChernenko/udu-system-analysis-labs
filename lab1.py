from scipy.optimize import linprog

c = [-140, -90]


A = [
    [0.6, 0.8],
    [0.4, 0.2],
    [-1, 1],
    [0, 1]
]

b = [50, 30, 20, 40]


x_bounds = (0, None)  # xA ≥ 0
y_bounds = (0, None)  # xB ≥ 0

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if res.success:
    xA, xB = res.x
    profit = -res.fun  
    print(f"Оптимальний план виробництва:")
    print(f"  Бензин A: {xA:.2f} тонн")
    print(f"  Бензин B: {xB:.2f} тонн")
    print(f"Максимальний прибуток: {profit:.2f} у.г.о.")
else:
    print("Не вдалося знайти оптимальне рішення.")

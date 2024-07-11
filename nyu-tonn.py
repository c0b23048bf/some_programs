x0 = -2
# xk = (x**3) - (5*x**2) + x + 2
# xkd = (3*x**2) - (10*x) + 1

x = x0
for i in range(10):
    x1 = x
    x = x - (((x**3) - (5*x**2) + x + 2)/((3*x**2) - (10*x) + 1))
    print(f"k={i}")
    print(x)
    print(abs(x1 - x))
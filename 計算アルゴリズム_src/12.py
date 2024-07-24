def k(x):   # 元の関数
    return (x**3) - (5*x**2) + x + 2


def kd(x):  # 微分後の関数
    return (3*x**2) - (10*x) + 1


def main(x, kmax):
    x = float(x)
    for i in range(int(kmax)+1):
        x1 = x
        x = x - (k(x)/kd(x))
        print(f"k={i}\n{x}\n{abs(x1-x)}")
        
        
if __name__ == '__main__':
    print("関数k,関数kxで指定されている式は適宜変えること")
    k0 = input("初期値x0を入れてください:")
    kmax = input("探索するkの最大値を入れてください:")
    main(k0, kmax)
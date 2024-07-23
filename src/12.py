def k(x):
    return (x**3) - (5*x**2) + x + 2


def kd(x):
    return (3*x**2) - (10*x) + 1


def main(x, kmax):
    x = float(x)
    for i in range(int(kmax)+1):
        x1 = x
        x = x - (k(x)/kd(x))
        print(f"k={i}\n{x}\n{abs(x1-x)}")
        
        
if __name__ == '__main__':
    k0 = input("初期値x0を入れてください:")
    kmax = input("探索するkの最大値を入れてください:")
    main(k0, kmax)
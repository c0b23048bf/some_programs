import math

def gennmitu(a, b , c):
    x1, x2 = ((-1*b)+math.sqrt((b**2)-(4*a*c)))/(2*a), ((-1*b)-math.sqrt((b**2)-(4*a*c)))/(2*a)
    if x2 > x1:
        xa = x2
    else:
        xa = x1
    return xa 

def main():
    print("厳密解を出力します")
    a = input("aを入れよ(4x**2-x-1であれば4)：")
    b = input("aを入れよ(4x**2-x-1であれば-1)：")
    c = input("aを入れよ(4x**2-x-1であれば-1)：")
    print(f"xa={gennmitu(float(a),float(b),float(c))}")
    x0 = input("x0を入れなさい：")
    num = input("何回繰り返しますか？：")
    for i in range(int(num)):
        x0 = math.sqrt((float(x0)+1)/float(a))
        print(f"x{i+1}は{x0}です。")

if __name__ == '__main__':
    main()
        
    
def keisann(x, f, w):
    f_l = [f]
    while f != 2:
        f = f //2 
        f_l.append(f)
        
    for g, i in enumerate(f_l):
        print(f"P{g+1}:{(x**i)%w}")
        
def main():
    x = input("x:")
    f = input("f:")
    w = input("w:")
    keisann(x,f,w)

if __name__ == '__main__':
    main()
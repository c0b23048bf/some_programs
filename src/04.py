def addh(h,a):
    if len(h) == 0:
        h = [a]
    else:
        h.append(a)
    return h

def delh(h):
    m = max(h)
    mi = h.index(m)
    x = h.pop(mi)
    return h

def main():
    h = []
    while True:
        g = input("数値の追加はaddh,最大値の取り出しはdelh,やめる場合はbreakを入れよ：")
        if g == "addh":
            a = input("入れる値を入れよ")
            h = addh(h,a)
        elif g == "delh":
            h = delh(h)
        elif g == "break":
            break
        print(h)

if __name__ == '__main__':
    main()
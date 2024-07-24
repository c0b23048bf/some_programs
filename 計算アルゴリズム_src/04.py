import heapq

def addh(h,a):
    heapq.heappush(h,-a)

def delh(h):
    return -heapq.heappop(h)

def main():
    h = []
    while True:
        g = input("数値の追加はaddh,最大値の取り出しはdelh,やめる場合はbreakを入れよ：")
        if g == "addh":
            a = input("入れる値を入れよ")
            addh(h,int(a))
        elif g == "delh":
            s = delh(h)
        elif g == "break":
            break
        
        print([-i for i in h])

if __name__ == '__main__':
    main()
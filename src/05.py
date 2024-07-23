def quicksort(h):
    k = input("基準値を答えよ：")
    k = int(k)
    ki = h.index(k)
    a = h[len(h)-1]
    h[len(h)-1] = h[ki]
    h[ki] = a
    while True:
        i = 0
        j = 0
        for jjj in range(len(h)-1):
            if h[jjj] > k:
                i = k
                break
        for hhh in range(len(h)-1,0,-1):
            if h[hhh] < k:
                j = k
                break
        
        if i < j:
            ii = h.index(i)
            ji = h.index(j)
            w = h[ii]
            h[ii] = h[ji]
            h[ji] = w
        if i>j:
            ii = h.index(i)
            w = h[ii]
            h[ii] = h[len(h)-1]
            h[len(h)-1] = w
        print(h)
            
    
def main():
    h = input("配列を入れよ(例:23,4,6)：")
    h = h.split(",")
    hi = []
    for i in range(len(h)):
        hi.append(int(h[i]))
    print(hi)
    f = quicksort(hi)
    print(f"結果:{f}")
    
if __name__ == '__main__':
    main()
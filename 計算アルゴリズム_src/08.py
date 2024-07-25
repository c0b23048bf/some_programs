# Thanks for gpt

def knapsack(omosa, kakaku, m):
    m += 1
    n = len(omosa)

    frame = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dd = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n + 1):
        for w in range(m + 1):
            if omosa[i-1] <= w:
                frame[i][w] = max(frame[i-1][w], frame[i-1][w-omosa[i-1]] + kakaku[i-1])
                dd[i][w] = i-1
            else:
                frame[i][w] = frame[i-1][w]
                dd[i][w] = i-1

    del frame[0]
    del dd[0]
    for i in range(len(frame)):
        del frame[i][0]
        del dd[i][0]
    return frame,dd, frame[n-1][m-1]

def main():
    # ここにデータを入れなさい
    print("omosaリスト、kakakuリスト、どの長さにするか？を指定しなさい")
    omosa = [2, 1, 4, 5]
    kakaku = [2, 3, 3, 4]
    m = 4

    d, dd, max_value = knapsack(omosa, kakaku, m)
    print(f"最大価値: {max_value}\n完成したデータ")
    
    for i in range(len(d)):
        print(d[i])
    print("何を入れたか？(間違っています)")
    for i in range(len(d)):
        print(dd[i])
    
if __name__ == '__main__':
    main()

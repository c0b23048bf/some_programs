# Thanks for gpt and s.i

import re

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    index = 3  # 基準値のインデックスを3に固定
    value = arr[index]
    arr[index], arr[-1] = arr[-1], arr[index]  # 基準値を最後の位置と交換
    
    i = 0
    j = len(arr) - 2

    while i <= j:
        # 左から基準値以上の値を見つける
        while i <= j and arr[i] < value:
            i += 1
        # 右から基準値未満の値を見つける
        while i <= j and arr[j] >= value:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # 基準値を適切な位置に移動する
    arr[i], arr[-1] = arr[-1], arr[i]
    return arr


            
    
def main():
    # ユーザーからの入力を受け取る
    ls = input("各要素を入力してください。例：47, 74, 51, 49, 19, 31, 27, 13: ")

    # 数値を抽出する
    word = re.findall("-?\d+", ls)
    D = [int(num) for num in word]

    #print("ソート前の配列:", D)
    D = quicksort(D)
    print("クイックソート処理後の配列:", D)
    
if __name__ == '__main__':
    main()
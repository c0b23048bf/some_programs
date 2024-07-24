def quicksort(arr, left, right):
    if left < right:
        # 基準値の選択とパーティションの分割
        pivot_index = partition(arr, left, right)
        # 左側の部分と右側の部分をそれぞれ再帰的にソート
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

def partition(arr, left, right):
    # 基準値を選択（ここでは一番右の要素を基準値とする）
    pivot = 49
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 基準値を正しい位置に移動
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def main():
    h = input("配列を入れよ(例:23,4,6)：")
    h = list(map(int, h.split(",")))
    quicksort(h, 0, len(h) - 1)
    print(f"結果:{h}")

if __name__ == '__main__':
    main()

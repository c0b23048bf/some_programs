# Thanks for gpt and s.i

def create_bad_char_table(pattern):
    max_char = max(map(ord, pattern)) + 1
    bad_char_table = [-1] * max_char
    for i, char in enumerate(pattern):
        bad_char_table[ord(char)] = i
    return bad_char_table

def boyer_moore_analysis(text, pattern,w1,w2):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    # 配列 L を生成
    bad_char_table = create_bad_char_table(pattern)
    
    # 各文字の値を表示
    print(f"L[{w1}] の値を半角数字: {bad_char_table[ord(w1)]}")
    print(f"L[{w2}] の値を半角数字: {bad_char_table[ord(w2)]}")

    # シフト回数の計算
    shifts = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            shifts.append(0)
            s += 1
        else:
            bad_char_shift = j - bad_char_table[ord(text[s + j])] if ord(text[s + j]) < len(bad_char_table) else j + 1
            s += max(1, bad_char_shift)
            shifts.append(max(1, bad_char_shift))

    # 各シフト回数を表示
    for i, shift in enumerate(shifts[:4]):
        print(f"{i+1}回目に右にずらす文字数を半角数字: {shift}")
def main():
    text = input("テキストを入力してください: ")
    pattern = input("パターンを入力してください: ")
    w1 = input("１つ目の文字を入力してください。例）配列L[?]: ")
    w2 = input("２つ目の文字を入力してください。例）配列L[?]: ")
    boyer_moore_analysis(text, pattern,w1,w2)

if __name__ == '__main__':
    main()


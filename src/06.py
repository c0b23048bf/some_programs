def boyer_moore(text, pattern):
    def create_bad_char_table(pattern):
        max_char = max(map(ord, pattern)) + 1
        bad_char_table = [-1] * max_char
        for i, char in enumerate(pattern):
            bad_char_table[ord(char)] = i
        return bad_char_table

    def create_good_suffix_table(pattern):
        m = len(pattern)
        good_suffix_table = [-1] * m
        last_prefix_index = m

        for i in reversed(range(m)):
            if is_prefix(pattern, i + 1):
                last_prefix_index = i + 1
            good_suffix_table[m - 1 - i] = last_prefix_index - i + m - 1

        for i in range(m - 1):
            slen = suffix_length(pattern, i)
            good_suffix_table[slen] = m - 1 - i + slen

        return good_suffix_table

    def is_prefix(pattern, p):
        m = len(pattern)
        j = 0
        for i in range(p, m):
            if pattern[i] != pattern[j]:
                return False
            j += 1
        return True

    def suffix_length(pattern, p):
        m = len(pattern)
        length = 0
        j = m - 1
        i = p
        while i >= 0 and pattern[i] == pattern[j]:
            length += 1
            i -= 1
            j -= 1
        return length

    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    bad_char_table = create_bad_char_table(pattern)
    good_suffix_table = create_good_suffix_table(pattern)

    s = 0
    while s <= n - m:
        print(f"Shift: {s}")  # 探索の過程を出力
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            print(f"Comparing pattern[{j}] and text[{s + j}]: {pattern[j]} == {text[s + j]}")  # 探索の過程を出力
            j -= 1

        if j < 0:
            print(f"Pattern found at index {s}")  # パターンが見つかった位置を出力
            return s
        else:
            bad_char_shift = j - bad_char_table[ord(text[s + j])] if ord(text[s + j]) < len(bad_char_table) else j + 1
            good_suffix_shift = good_suffix_table[j] if j < m - 1 else 1
            s += max(bad_char_shift, good_suffix_shift)

    print("Pattern not found")  # パターンが見つからなかった場合のメッセージ
    return -1

# 使用例
text = input("a")
pattern = input("aa")
result = boyer_moore(text, pattern)
print(f"Result: {result}")


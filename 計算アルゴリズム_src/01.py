import struct

def float_to_ieee754(num):
    
    #符号ビットの決定
    if num >= 0:
        sign = 0
    else:
        sign = 1
    
    #絶対値の取得
    num = abs(num)

    # 整数部と小数部に分ける
    int_num = int(num)
    float_num = num - int_num

    # 整数部を2進数に変換して0bを消す
    int_bin = bin(int_num).replace('0b', '')

    # 小数部の2進数変換
    frac_bin = []
    while float_num:
        float_num *= 2
        bit = int(float_num)
        frac_bin.append(str(bit))
        float_num -= bit
        if len(frac_bin) > 23:
            break
    
    #文字列に変換
    frac_bin = ''.join(frac_bin)

    # 正規化
    ex = len(int_bin) - 1
    m = int_bin[1:] + frac_bin
    m = m[:23]

    # 指数部の計算
    ex = ex + 127
    ex_bin = bin(ex).replace('0b', '').zfill(8)

    # 仮数部の計算
    m = m.ljust(23, '0')

    # IEEE 754形式の組み合わせ
    ieee754 = f'{sign}{ex_bin}{m}'
    return ieee754

def main():
    num = float(input("10進数を入力してください"))
    ieee754 = float_to_ieee754(num)
    print("IEEE 754単精度浮動小数点形式:", ieee754)
    w = str(ieee754)
    print("s:",w[0])
    print("e:",w[1:9])
    print("f:",w[9:])

if __name__ == '__main__':
    main()
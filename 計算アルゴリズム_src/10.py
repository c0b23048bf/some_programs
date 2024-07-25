def douteki(r1,r2,r3,r4,c1,c2,c3,c4):
    m12 = r1*c1*c2
    m23 = r2*c2*c3
    m34 = r3*c3*c4

    m131 = r1*c1*c3 + m23
    m132 = r1*c2*c3 + m12
    if m131 > m132:
        m13 = m132
    else:
        m13 = m131
        
    m241 = r2*c2*c4 + m34
    m242 = r2*c3*c4 + m23

    if m241 > m242:
        m24 = m242
    else:
        m24 = m241
        
    m141 = r1*c1*c4 + m24
    m142 = r1*c2*c4 + m12+ m34
    m143 = r1*c3*c4 + m13
    return m12,m23,m34,m13,m24,m141,m142,m143

def main():
    r1=31
    r2=13
    r3=10
    r4=19
    c1=13
    c2=10
    c3=19
    c4=26
    m12,m23,m34,m13,m24,m141,m142,m143 = douteki(r1,r2,r3,r4,c1,c2,c3,c4)

    print("このプログラムは一般化されていません。小テストの仕様でのみ有効です")
    print(m12,m23,m34,m13,m24)
    print("下は大きさ判断して")
    print(m141,m142,m143)

if __name__ == '__main__':
    main()
    

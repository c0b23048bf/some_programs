x = 98
f = 77  
w = 119
f_l = [f]

# ここで演算の過程を準備
while f != 2:
    f = f //2 
    f_l.append(f)
    
# 演算の過程のprint
for g, i in enumerate(f_l):
    print(f"P{g+1}:{(x**i)%w}")
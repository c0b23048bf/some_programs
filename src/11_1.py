import numpy as np

# 行列Aの定義
A = np.array([[8, 2],
              [2, 5]])

# 初期値の設定
x = np.array([1, 1])
lambda_old = 0

# 反復の数
iterations = 3

for k in range(iterations):
    y = np.dot(A, x)
    x = y / y[1]
    lambda_new = y[1] / x[1]
    print(f"Iteration {k}: x = {x}, λ = {lambda_new}")
    lambda_old = lambda_new

# 結果を出力
x_1_0 = round(x[0], 3)
x_1_1 = round(x[0], 3)
x_1_2 = round(x[0], 3)
lambda_3 = round(lambda_new, 3)

print(f"反復 k = 0 における x1^(1) の値: {x_1_0}")
print(f"反復 k = 1 における x1^(2) の値: {x_1_1}")
print(f"反復 k = 2 における x1^(3) の値: {x_1_2}")
print(f"反復 k = 2 における A の最大固有値 λ1^(3) の値: {lambda_3}")


# 特性方程式を解くために行列Aの固有値を求める
eigenvalues, eigenvectors = np.linalg.eig(A)

# 最大固有値を取得
max_eigenvalue = np.max(eigenvalues)
max_eigenvalue = round(max_eigenvalue, 3)

# 最大固有値に対応する固有ベクトルを取得
max_eigenvector = eigenvectors[:, np.argmax(eigenvalues)]
max_eigenvector /= max_eigenvector[1]  # x2 = 1とする
max_eigenvector = max_eigenvector / max_eigenvector[1]  # 正規化

x1 = round(max_eigenvector[0], 3)

print(f"特性方程式を用いて求めた A の最大固有値 |λ1| の値: {max_eigenvalue}")
print(f"特性方程式を用いて求めた A の最大固有値に対する固有ベクトルの1番目の要素 x1 の値: {x1}")

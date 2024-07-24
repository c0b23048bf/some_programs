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

# Thanks for gpt

import numpy as np
def hannpuku(A,iterations,x):
    for k in range(iterations):
        y = np.dot(A, x)
        x = y / y[1]
        lambda_new = y[1] / x[1]
        print(f"Iteration {k}: x = {x}, λ = {lambda_new}")
        print(f"反復k={k}におけるx1の値は:{x[0]}")
        lambda_old = lambda_new

    print(f"最終反復における A の最大固有値 λ1^(3) の値: {lambda_new}")
    
def tokusei(A):
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
    
def main():
    print("適宜、行列と初期値の設定を変えること")
    # 行列Aの定義
    A = np.array([[8, 2],
                [2, 5]])

    # 初期値の設定
    x = np.array([1, 1])
    lambda_old = 0

    # 反復の数
    iterations = 3
    
    hannpuku(A,iterations,x)
    tokusei(A)

if __name__ == '__main__':
    main()



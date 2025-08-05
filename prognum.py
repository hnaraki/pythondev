# 整数の階乗を求める関数
def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n - 1)


# フィボナッチ数列を計算する関数
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

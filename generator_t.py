# 杨辉三角表示
def triangles(s):
    L , n = [1], 1
    # 生成器可以利用上一次的数据,也可不利用完全自己生成
    # rang()是从0开始生成

    while n < s:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(n-1)] + [1]
        n += 1


for n in triangles(10):
    print(n)

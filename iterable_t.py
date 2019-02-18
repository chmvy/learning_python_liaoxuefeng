# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def FindMinAndMax(L):
    if L != []:
        min = L[0]
        max = L[0]
        for l in L:
            if min > l:
                min = l
            if max < l:
                max = l
        return (min, max)
    else:
        return (None, None)

print(FindMinAndMax([]))
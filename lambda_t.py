# 导入列表中的值,结果是True就保留这个值,结果为False 就删除这个值
# 所以函数的return只能是True或者False

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))



print(L)
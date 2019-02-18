# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# 闭包调用的时候不会再重新从包头开始执行,而是直接运行闭包函数

s = 0
def createCounter():
    def counter():
        # s 是一个全局变量,所有的s都指向同一个地址,新值进来,旧值被抛弃
        global s
        s = s + 1
        return s
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
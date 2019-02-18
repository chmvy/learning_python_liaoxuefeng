def createCounter():
    def f():
        n = 0
        while True:
            n = n + 1
            yield n
    # 包含yield的函数是生成器,要调用,先要生成一个生成器对象(赋值)
    it = f()
    # 在这里,要导入闭包的变量就是it,他符合闭包对导入变量的要求:指向确定内存地址
    def g():
        return next(it)
    return g
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
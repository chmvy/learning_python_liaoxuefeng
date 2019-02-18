# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# 闭包调用的时候不会再重新从包头开始执行,而是直接运行闭包函数
# 因此在本例中不会再执行 ln6: s = [0]
# 所以使用闭包的关键是创建变量,你创建的这个变量要是可以传入闭包并正常使用的
# 那为什么不直接再闭包内部创建呢,因为在闭包内部创建的变量再调用函数的时候只会调用最后一个变量值,无法更新变量
# 引入变量的关键是外部创建,指向不能变,变得是内容,所以本例里面用了列表的方式,指向一直不变,一直都是同一个变量(名)
# 结论来了:能够传递进闭包的变量必须是不可变的变量,必须指向一个确定的内存地址,变量被重新赋值,虽然变量名没变,但是地址变了

def createCounter():
    s = [0]
    def counter():
        # 引用变量,变量没有变,序列是可变的
        # 闭包的引用只能引用不变的变量指向(变量),但是变量如果是可变类型,内部变化了,是可以照常使用的
        s[0] = s[0] + 1
        return s[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA(),counterA())
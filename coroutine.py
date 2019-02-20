def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 返回的r,但是赋值上一个值为n,所以这里c.send(n)的值为'200 ok'
        # send n,返回的r,这个巧妙,往上传递一个变量,返回另一个变量,执行代码(代码还接受了参数)关键返回的值一直不变,
        # 执行完就进行了赋值操作,所以赋值操作分两步,第一步计算右边的值(接收参数执行上面的代码),执行完了就完成了计算接着
        # 进行赋值.然后继续执行下面一个
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
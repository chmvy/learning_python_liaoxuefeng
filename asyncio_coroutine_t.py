import threading
import asyncio
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(5)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
# 新建两个协程,扔到event_loop中,第一个hello打印完,跳过等待,接着运行第二个hello,本来都是要跳过的等待,两个一秒可以重复
# 所以应该是等待2秒,但是因为是协程了,两个1秒是重合的,这里只等待了大约1秒,我换成5秒测试过
# 再接着分别执行剩下的两半协程
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
# print(now.__name__)
import time, functools

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(func):
    @functools.wraps(func)
    def cal_time(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        time_wasted = (end - start) * 1000
        print('The %s function has wast %s'%(func.__name__, time_wasted))
        return time_wasted
    return cal_time

@metric
def fast(x, y):
    time.sleep(1)
    return x + y

fast(1,2)

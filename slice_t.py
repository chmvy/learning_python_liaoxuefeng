"""利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法："""
def trim(s):
    if len(s) == 0:
        return s
    while s[0] == ' ':
        s = s[1:]
        if len(s) == 0:
            return s
    while s[-1] == ' ':
        s = s[:-1]
        if len(s) == 0:
            return s
    return s
s = '        lilingtao '
print(len(s))
trim(s)
print(trim(s))
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]
# for l in L1:
#     if not isinstance(l, str):
#         L1.remove(l)
L2 = [ s.lower() for  s in L1 if isinstance(s, str)]
print(L2)



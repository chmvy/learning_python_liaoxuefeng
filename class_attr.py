# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # 每实例化一次,就执行一次这一段代码
        Student.count += 1

a = Student("bb")
b = Student("bb")
b = Student("bb")
b = Student("bb")
print(Student.count)

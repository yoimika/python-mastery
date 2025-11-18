'''
slots 应该是一个字符串列表
定义了 __slots__ 之后，实例就不能再动态添加属性了
如果想让实例既能使用 __slots__ 又能动态添加属性，可以在 __slots__ 中添加 '__dict__'
优点是节省内存
'''
class A:
    __slots__ = ['__dict__', 'x', 'y']
    def __init__(self, z=10):
        self.z = z

a = A()
a.x = 10

print(a.x, a.z)
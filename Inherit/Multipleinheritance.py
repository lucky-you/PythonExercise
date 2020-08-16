# python 中多继承的使用

class A:
    def text(self):
        print("A的text方法")


class B:
    def demo(self):
        print("B的demo方法")


class C(A, B):

    def query(self):
        print("C自己的query方法")


if __name__ == '__main__':
    c = C()
    c.text()
    c.demo()
    c.query()
    # 确定C类对象调用方法的顺序
    print(C.__mro__)

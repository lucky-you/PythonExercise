class Woman:
    def __init__(self, name):
        self.name = name
        # __ 年龄是私有属性，加__ 操作
        self.__age = 20

    def secret(self):
        # 在对象的内部是可以访问对象的私有属性的
        print('%s 的年龄是 %d' % (self.name, self.__age))

    def __secretText(self):
        # 在对象的内部是可以访问对象的私有属性的
        print('%s 的年龄是 %d' % (self.name, self.__age))


if __name__ == '__main__':
    xiaofang = Woman("小芳")
    # 伪私有属性在外界不能被直接访问
    # print(xiaofang._Woman__age)
    # 伪私有方法同样不能被外界访问
    # xiaofang._Woman__secretText()
    xiaofang.secret()

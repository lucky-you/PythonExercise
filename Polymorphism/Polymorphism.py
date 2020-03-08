class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaoTianQuan(Dog):

    def game(self):
        print("%s 飞到天上去玩耍。。" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍。。" % (self.name, dog.name))
        dog.game()


if __name__ == '__main__':
    # 1.创建一个狗对象
    # 2.创建一个小明对象
    # 3.让小明调用和狗玩耍的方法
    # dog = Dog("旺财")
    dog = XiaoTianQuan("飞天旺财")
    xiaoming = Person("小明")
    xiaoming.game_with_dog(dog)

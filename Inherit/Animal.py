
# 单继承的使用

class Animal:

    def eat(self):
        print("吃。。。")

    def brank(self):
        print("喝。。。")

    def run(self):
        print("跑。。。")

    def sleep(self):
        print("睡。。。")


class Dog(Animal):
    # Dog 继承自Animal 子类具有父类的所有方法

    def brak(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞。。。")

    def brak(self):
        # 重写父类的方法，自己重新实现自己的独特需求
        print("叫的和神一样的。。")
        # 使用super() 调用原本在父类中的方法
        super().brak()
        # 父类名.方法名(self)
        # Dog.brak(self)
        # 增加其他子类的代码
        print("叫唤完毕")


class cat(Animal):
    def catch(self):
        print("抓老鼠")


if __name__ == '__main__':
    wangcai = XiaoTianQuan()
    # wangcai.eat()
    # wangcai.brank()
    # wangcai.run()
    # wangcai.sleep()
    # wangcai.fly()
    wangcai.brak()

    # miaomiao = cat()
    # miaomiao.sleep()
    # miaomiao.catch()

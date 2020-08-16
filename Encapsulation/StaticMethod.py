# 静态方法的使用

class Dog:
    # 静态方法，在类中封装一个方法，这个方法既不需要访问实例属性或者调用实例方法，也不需要访问类属性或者调用类方法
    @staticmethod
    def run():
        print("小狗要跑。。。")


if __name__ == '__main__':
    Dog.run()
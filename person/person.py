class Person:

    def __init__(self, name, weight):
        # self.属性=形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return '我的名字叫%s ,体重是%d公斤' % (self.name, self.weight)

    def run(self):
        print('%s爱跑步，跑步锻炼身体' % self.name)
        self.weight -= 1

    def eat(self):
        print('%s是吃货，吃完这餐再减肥' % self.name)
        self.weight += 2


def main():
    xiaoming = Person('小明', 79)
    print(xiaoming)
    xiaoming.run()
    xiaoming.eat()
    print(xiaoming)
    print("************")
    xiaomei = Person('小美', 45)
    print(xiaomei)
    xiaomei.eat()
    xiaomei.run()
    print(xiaomei)


if __name__ == '__main__':
    main()

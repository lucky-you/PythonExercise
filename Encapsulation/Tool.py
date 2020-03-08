class Tool:
    # 类属性的使用，通常记录与这个类相关的属性，不会记录具体对象的特征
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


if __name__ == '__main__':
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")
    tool3 = Tool("剪刀")
    print(Tool.count)

#     看到了面向对象第52期

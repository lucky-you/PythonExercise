class Tool:
    # 类属性的使用，通常记录与这个类相关的属性，不会记录具体对象的特征
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %s " % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


if __name__ == '__main__':
    # 创建工具对象
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")
    tool3 = Tool("剪刀")
    print(Tool.count)
    # 调用类方法
    Tool.show_tool_count()

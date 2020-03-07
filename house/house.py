class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f平米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f平米[剩余：%.2f平米]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_Item(self, item):
        print("要添加 %s" % item)
        # 1.判断家具的面积
        if item.area > self.free_area:
            print('%s 的面积太大了，无法添加 ' % item.name)
            return
        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area


def startMain():
    # 创建家具
    print("开始创建家具***\n")
    bed = HouseItem("席梦思", 12.0)
    chest = HouseItem("衣柜", 13.0)
    table = HouseItem("餐桌", 7.6)
    print(bed)
    print(chest)
    print(table)
    print("家具常见完成-----\n")
    #  创建房子对象
    my_house = House("两室一厅", 65)
    print(my_house)

    my_house.add_Item(bed)
    my_house.add_Item(chest)
    my_house.add_Item(table)
    print(my_house.__str__())

if __name__ == '__main__':
    startMain()

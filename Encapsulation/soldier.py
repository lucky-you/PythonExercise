class Gun:
    def __init__(self, model):
        # 1.枪的型号
        self.model = model
        # 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        #  增加枪的子弹数量
        self.bullet_count += count
        print('[%s]添加子弹[%s]发' % (self.model, count))

    def shoot(self):
        # 1.判断子弹的数量
        if self.bullet_count <= 0:
            print('[%s]没有子弹了...' % self.model)
            return
        # 2.发射子弹,count -1
        self.bullet_count -= 1
        # 3.给出提示信息
        print('[%s]突突突... 剩余子弹[%d]发' % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):
        # 1.姓名
        self.name = name
        # 2.枪，新兵没有枪
        self.gun = None

    def fire(self):
        # 1.判断有没有枪
        if self.gun is None:
            print("[%s]还没有枪" % self.name)
            return
        # 2.高喊口含
        print("[%s] 冲啊。。。" % self.name)
        # 3.装填子弹
        self.gun.add_bullet(50)
        # 4.发射子弹
        self.gun.shoot()


if __name__ == '__main__':
    ak47 = Gun("AK-47")
    xusanduo = Soldier("许三多")
    xusanduo.gun = ak47
    xusanduo.fire()

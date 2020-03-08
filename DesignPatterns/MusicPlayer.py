class MusicPlayer:
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空
        # 2.调用父类的方法，为对象分配空间
        # 3.返回类属性保存的对象引用
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        # 1.判断是否执行过初始化动作
        # 2.如果没有执行过，现在执行初始化动作
        # 3.修改类属性的标记
        if MusicPlayer.init_flag:
            return
        print("初始化。。")
        MusicPlayer.init_flag = True


if __name__ == '__main__':
    music1 = MusicPlayer()
    music2 = MusicPlayer()
    print(music1)
    print(music2)

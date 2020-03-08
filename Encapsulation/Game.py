class Game:
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        # 既不需要实例属性，也不需要类属性
        print("帮助信息:让僵尸进入大门。")

    @classmethod
    def show_top_score(cls):
        # 类属性
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        # 实例属性
        print("%s 开始游戏了..." % self.player_name)


if __name__ == '__main__':
    # 1.查看游戏的帮助信息
    Game.show_help()
    # 2.查看历史最高分
    Game.show_top_score()
    # 3.创建游戏对象
    game = Game("小明")
    # 4.开始游戏
    game.start_game()

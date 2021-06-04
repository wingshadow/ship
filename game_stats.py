import os


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = self.read_high_score(self.ai_settings.high_score_file_name)

    def read_high_score(self, path):
        f = open(path, "r")
        high_score_str = f.read()
        high_score_str = high_score_str.replace(",", "")
        f.flush()
        f.close()
        return int(high_score_str)

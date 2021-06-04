# _*_ coding:utf-8 _*_

import os

class Settings():
    """存储《外星人入侵》 的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # # 飞船移动距离
        self.ship_speed_factor = 1.5
        # 飞船条数
        self.ship_limit = 3
        # 子弹参数设置
        # 子弹速度
        self.bullet_speed_factor = 3
        # 子弹宽度
        self.bullet_width = 3
        # 子弹高度
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 每次允许发送3枚子弹
        self.bullets_allowed = 3

        # 外星人设置速度
        self.alien_speed_factor = 0.3
        # 外星人下落速度
        self.fleet_drop_speed = 5
        # fleet_direction为1表示向右移， 为-1表示向左移
        self.fleet_direction = 1

        self.alien_points = None

        # 飞碟速度区间
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.fire_sound = "sound/fire.wav"
        self.bomb_sound = "sound/bomb.wav"
        self.ship_bomb_sound = "sound/ship_bomb.wav"

        self.high_score_file_name = os.getcwd() + "\highScore.txt"

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3
        # fleet_direction为1表示向右； 为-1表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        # 游戏等级提高，单个飞碟分值提高
        self.alien_points = int(self.alien_points * self.score_scale)
        print("飞碟分值:%d" % (self.alien_points))

# _*_ coding:utf-8 _*_

import pygame
import sys
# 系统配置类
from button import Button
from settings import Settings
from ship import Ship
from alien import Alien
import gameFunction as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard


def run_game():
    # 初始化背景
    pygame.init()

    ali_settings = Settings()

    # 设置背景大小
    screen = pygame.display.set_mode((ali_settings.screen_width, ali_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(ali_settings, screen)

    # 创建一群外星人
    aliens = Group()

    gf.create_fleet(ali_settings, screen, ship, aliens)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ali_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ali_settings)

    # 创建记分牌
    sb = Scoreboard(ali_settings, screen, stats)

    while True:
        # 事件处理
        gf.check_events(ali_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            # 刷新飞船移动位置
            ship.update()
            # 刷新子弹状态
            gf.update_bullets(ali_settings, screen, stats, sb, ship, aliens, bullets)
            # 刷新外星人状态
            gf.update_aliens(ali_settings, screen, stats, sb, ship, aliens, bullets)
        # 刷新屏幕
        gf.update_screen(ali_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

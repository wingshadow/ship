# _*_ coding:utf-8 _*_

import pygame
import sys
# 系统配置类
from settings import Settings
from ship_v4 import ShipV4
import gameFunction as gf


def run_game():
    # 初始化背景
    pygame.init()

    ali_settings = Settings()

    # 设置背景大小
    screen = pygame.display.set_mode((ali_settings.screen_width, ali_settings.screen_height))

    # 创建一艘飞船
    ship = ShipV4(screen)

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    while True:
        # 事件处理
        gf.check_event(ship)
        ship.update()
        # 刷新屏幕
        gf.update_screen(ali_settings, screen, ship)

        # 最近绘制的屏幕
        pygame.display.flip()


run_game()

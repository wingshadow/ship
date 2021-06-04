# _*_ coding:utf-8 _*_

import pygame
import sys
# 系统配置类
from settings import Settings
from ship import Ship


def run_game():
    # 初始化背景
    pygame.init()

    ali_settings = Settings()

    # 设置背景大小
    screen = pygame.display.set_mode((ali_settings.screen_width, ali_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(screen)

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 设置背景颜色
        screen.fill(ali_settings.bg_color)
        ship.blitme()

        # 最近绘制的屏幕
        pygame.display.flip()


run_game()

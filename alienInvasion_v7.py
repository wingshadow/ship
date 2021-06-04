# _*_ coding:utf-8 _*_

import pygame
import sys
# 系统配置类
from settings import Settings
from ship import Ship
from alien import Alien
import gameFunction as gf
from pygame.sprite import Group


def run_game():
    # 初始化背景
    pygame.init()

    ali_settings = Settings()

    # 设置背景大小
    screen = pygame.display.set_mode((ali_settings.screen_width, ali_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(ali_settings, screen)

    # 创建一个外星人
    alien = Alien(ali_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    while True:
        # 事件处理
        gf.check_events(ali_settings, screen, ship, bullets)
        # 属性飞船移动位置
        ship.update()
        gf.update_bullets(bullets)
        # 刷新屏幕
        gf.update_screen(ali_settings, screen, ship, alien, bullets)

        # 最近绘制的屏幕
        pygame.display.flip()


run_game()

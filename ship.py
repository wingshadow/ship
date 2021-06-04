# _*_ coding:utf-8 _*_

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ali_settings, screen):
        """初始化飞船， 并设置其起始位置"""
        super(Ship, self).__init__()
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ali_settings = ali_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.center += self.ali_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ali_settings.ship_speed_factor

        # 移动距离赋值坐标X
        self.rect.centerx = self.center

        # 飞船移动范围在屏幕内
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width >= self.ali_settings.screen_width:
            self.rect.x = self.ali_settings.screen_width - self.rect.width


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx

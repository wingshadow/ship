# _*_ coding:utf-8 _*_

import pygame
from pygame.sprite import Sprite

# 子弹类
# Sprite表示动画中一帧，继承Sprite，实现动画中一帧的效果
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ali_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形， 再设置正确的位置
        self.rect = pygame.Rect(0, 0, ali_settings.bullet_width, ali_settings.bullet_height)
        # 子弹发射位置就是飞船中心位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ali_settings.bullet_color
        self.speed_factor = ali_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
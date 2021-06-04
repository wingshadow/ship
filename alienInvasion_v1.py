# _*_ coding:utf-8 _*_

import pygame
import sys


def run_game():
    # 初始化背景
    pygame.init()

    # 设置背景大小
    screen = pygame.display.set_mode((1200, 800))
    
    # 设置标题
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 最近绘制的屏幕
        pygame.display.flip()


run_game()

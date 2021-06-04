import sys
import pygame
import os
from bullet import Bullet
from alien import Alien
from time import sleep


# 事件处理及屏幕刷新

def check_keydown_events(event, ai_settings, screen, stats, ship, bullets):
    """键盘事件处理"""
    # 按键Q退出游戏
    if event.key == pygame.K_q:
        write_high_score(stats)
        sys.exit()

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    # 开火
    if event.key == pygame.K_SPACE:
        fire(ai_settings, screen, ship, bullets)


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """事件检查"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_high_score(ai_settings,stats)
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # 点击play按钮并且游戏状态为False，游戏重置
    if button_clicked and not stats.game_active:
        # 初始化游戏参数
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空子弹
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人， 并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ali_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """绘制屏幕"""
    screen.fill(ali_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态， 就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 更新整个待显示的Surface对象到屏幕上
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹的位置， 并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def fire(ai_settings, screen, ship, bullets):
    """发射子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        # 创建一颗子弹， 并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """单行外星人数目"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建单个外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 设置外星人X坐标
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # 设置外星人Y坐标
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """飞船击中处理"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1
        sb.prep_ships()

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人， 并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        # 光标显示
        pygame.mouse.set_visible(False)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘， 并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
        print("Ship hit!!!")

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移， 并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # 判断击中飞碟个数
        for aliens in collisions.values():
            # 更新得分
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    # 外星人全部消灭重新创建一群外星人
    if len(aliens) == 0:
        # 删除现有的所有子弹， 并创建一个新的外星人群
        bullets.empty()
        # 提高游戏难度
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        # 重建飞碟群
        create_fleet(ai_settings, screen, ship, aliens)


def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def write_high_score(ai_settings,stats):
    f = open(ai_settings.high_score_file_name, "w")
    high_score_str = "{:,}".format(stats.high_score)
    f.write(high_score_str)
    f.flush()
    f.close()

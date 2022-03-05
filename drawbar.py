import pygame


# 创建一个绘制角色血条和蓝条, 爆气条的类
import demo


class Drawbar():
    # 初始化
    # role：角色（1或2）
    # blood：血条（填写角色的血量，例如98）
    # blue：蓝条（填写角色的蓝条，例如98）
    def __init__(self, screen, role, blood, blue, orange, white):
        # 根据传入的血条和蓝条的计算要绘制的宽度
        self.screen = screen
        self.blood_bar_width = 297
        self.blue_bar_width = 281
        self.player_blood = blood
        self.player_blue = blue
        self.blue_width = self.blue_bar_width * (blue / 100)
        self.one_orange_width = 281 * (orange / 100)
        self.two_orange_width = 281 * (orange / 100)

        self.one_white_width = 85 * (white / 100)
        self.two_white_width = 85 * (white / 100)

        self.role = role
        # # 在窗口两边分别绘制一个白色的矩形框
        # pygame.draw.rect(self.screen, (255,255,255), (20, 90, 520, 92), 1)
        # pygame.draw.rect(self.screen, (255, 255, 255), (1375, 90, 520, 92), 1)

    # 绘制血条方法
    def blood(self):
        if demo.Role.life == 2:
            if demo.Role.one_person_blood > 100:
                demo.Role.one_person_life = 2
            elif demo.Role.one_person_blood <= 100:
                demo.Role.one_person_life = 1
            if demo.Role.two_person_blood > 100:
                demo.Role.two_person_life = 2
            elif demo.Role.two_person_blood <= 100:
                demo.Role.two_person_life = 1
        elif demo.Role.life == 3:
            if demo.Role.one_person_blood > 200:
                demo.Role.one_person_life = 3
            elif demo.Role.one_person_blood <= 200 and demo.Role.one_person_blood > 100:
                demo.Role.one_person_life = 2
            elif demo.Role.one_person_blood <= 100:
                demo.Role.one_person_life = 1

            if demo.Role.two_person_blood > 200:
                demo.Role.two_person_life = 3
            elif demo.Role.two_person_blood <= 200 and demo.Role.two_person_blood > 100:
                demo.Role.two_person_life = 2
            elif demo.Role.two_person_blood <= 100:
                demo.Role.two_person_life = 1
        if self.role == 1:
            # 绘制角色一血条
            if demo.Role.one_person_life == 1:
                self.blood_width = self.blood_bar_width * (self.player_blood / 100)
                pygame.draw.rect(self.screen, (189, 25, 25), (221, 35, self.blood_width, 45), 0)
            elif demo.Role.one_person_life == 2:
                self.blood_width = self.blood_bar_width * ((self.player_blood - 100) / 100)
                pygame.draw.rect(self.screen, (189, 25, 25), (221, 35, self.blood_bar_width, 45), 0)
                pygame.draw.rect(self.screen, (0, 0, 255), (221, 35, self.blood_width, 45), 0)
            elif demo.Role.one_person_life == 3:
                self.blood_width = self.blood_bar_width * ((self.player_blood - 200) / 100)
                pygame.draw.rect(self.screen, (0, 0, 255), (221, 35, self.blood_bar_width, 45), 0)
                pygame.draw.rect(self.screen, (0, 255, 0), (221, 35, self.blood_width, 45), 0)
        else:
            if demo.Role.two_person_life == 1:
                self.blood_width = self.blood_bar_width * (self.player_blood / 100)
                pygame.draw.rect(self.screen, (189, 25, 25), (1696 - self.blood_width, 35, self.blood_width, 45), 0)
            elif demo.Role.two_person_life == 2:
                self.blood_width = self.blood_bar_width * ((self.player_blood - 100) / 100)
                pygame.draw.rect(self.screen, (189, 25, 25),(1696 - self.blood_bar_width, 35, self.blood_bar_width, 45), 0)
                pygame.draw.rect(self.screen, (0, 0, 255), (1696 - self.blood_width, 35, self.blood_width, 45), 0)
            elif demo.Role.two_person_life == 3:
                self.blood_width = self.blood_bar_width * ((self.player_blood - 200) / 100)
                pygame.draw.rect(self.screen, (0, 0, 255),(1696 - self.blood_bar_width, 35, self.blood_bar_width, 45), 0)
                pygame.draw.rect(self.screen, (0, 255, 0), (1696 - self.blood_width, 35, self.blood_width, 45), 0)

    # 绘制蓝条方法
    def blue(self):
        if demo.Role.energy == 2:
            if demo.Role.one_person_blue > 100:
                demo.Role.one_person_energy = 2
            elif demo.Role.one_person_blue <= 100:
                demo.Role.one_person_energy = 1
            if demo.Role.two_person_blue > 100:
                demo.Role.two_person_energy = 2
            elif demo.Role.two_person_blue <= 100:
                demo.Role.two_person_energy = 1
        elif demo.Role.energy == 3:
            if demo.Role.one_person_blue > 200:
                demo.Role.one_person_energy = 3
            elif demo.Role.one_person_blue <= 200 and demo.Role.one_person_blue > 100:
                demo.Role.one_person_energy = 2
            elif demo.Role.one_person_blue <= 100:
                demo.Role.one_person_energy = 1

            if demo.Role.two_person_blue > 200:
                demo.Role.two_person_energy = 3
            elif demo.Role.two_person_blue <= 200 and demo.Role.two_person_blue > 100:
                demo.Role.two_person_energy = 2
            elif demo.Role.two_person_blue <= 100:
                demo.Role.two_person_energy = 1

        if self.role == 1:
            # 绘制角色一蓝条
            if demo.Role.one_person_energy == 1:
                self.blue_width = self.blue_bar_width * (self.player_blue / 100)
                pygame.draw.rect(self.screen, (68,173,255), (221, 92, self.blue_width, 12), 0)
            elif demo.Role.one_person_energy == 2:
                self.blue_width = self.blue_bar_width * ((self.player_blue - 100) / 100)
                pygame.draw.rect(self.screen, (68,173,255), (221, 92, self.blue_bar_width, 12), 0)
                pygame.draw.rect(self.screen, (19, 143, 240), (221, 92, self.blue_width, 12), 0)
            elif demo.Role.one_person_energy == 3:
                self.blue_width = self.blue_bar_width * ((self.player_blue - 200) / 100)
                pygame.draw.rect(self.screen, (19, 143, 240), (221, 92, self.blue_bar_width, 12), 0)
                pygame.draw.rect(self.screen, (16,124,209), (221, 92, self.blue_width, 12), 0)
        else:
            if demo.Role.two_person_energy == 1:
                self.blue_width = self.blue_bar_width * (self.player_blue / 100)
                pygame.draw.rect(self.screen, (68,173,255), (1696 - self.blue_width, 92, self.blue_width, 12), 0)
            elif demo.Role.two_person_energy == 2:
                self.blue_width = self.blue_bar_width * ((self.player_blue - 100) / 100)
                pygame.draw.rect(self.screen, (68,173,255),(1696 - self.blue_bar_width, 92, self.blue_bar_width, 12), 0)
                pygame.draw.rect(self.screen, (19, 143, 240), (1696 - self.blue_width, 92, self.blue_width, 12), 0)
            elif demo.Role.two_person_energy == 3:
                self.blue_width = self.blue_bar_width * ((self.player_blue - 200) / 100)
                pygame.draw.rect(self.screen, (19, 143, 240),(1696 - self.blue_bar_width, 92, self.blue_bar_width, 12), 0)
                pygame.draw.rect(self.screen, (16,124,209), (1696 - self.blue_width, 92, self.blue_width, 12), 0)

    # 绘制爆气条
    def orange(self):
        # 如果爆气条宽度小于等于0
        # if self.orange_width >= 0:
        # 如果玩家为角色一
        if self.role == 1:
            # 绘制角色一爆气条
            pygame.draw.rect(self.screen, (255, 119, 0), (221, 115, self.one_orange_width, 12), 0)
        else:
            # 绘制角色二爆气条
            pygame.draw.rect(self.screen, (255, 140, 40),(1696 - self.two_orange_width, 115, self.two_orange_width, 12), 0)

    # 绘制爆气格
    def white(self):
        # 如果玩家为角色一
        if self.role == 1:
            # 绘制角色一爆气格
            pygame.draw.rect(self.screen, (0, 222, 255), (194, 152, self.one_white_width, 26), 0)
        else:
            # 绘制角色二爆气格
            pygame.draw.rect(self.screen, (0, 222, 255), (1725 - self.two_white_width, 152, self.two_white_width, 26),0)

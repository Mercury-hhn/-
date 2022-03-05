# 障碍物
import demo
import pygame
# TODO 障碍物跳跃

# 障碍物
class Obstacles():
    def __init__(self, role = 0, segment_jump_set = 2):
        # 障碍物
        self.role = role
        # 设置地面高度
        self.ground_y = 800
        # 段跳设置
        self.segment_jump = 0
        self.segment_jump_set = segment_jump_set
        # 跳跃高度
        self.jump_height = 0
        self.jump_height_set = 20.0

        if demo.Role.background_img_type == 1:
            self.obstacle_img = pygame.image.load('images/障碍物/obstacle1.png')
            self.obstacle1_x = 0
            self.obstacle1_y = 800
            self.obstacle2_x = demo.display_width // 2 - self.obstacle_img.get_width() // 2
            self.obstacle2_y = 580
            self.obstacle3_x = 1920 - self.obstacle_img.get_width()
            self.obstacle3_y = 800
        elif demo.Role.background_img_type == 2:
            self.obstacle_img = pygame.image.load('images/障碍物/obstacle2.png')
            self.obstacle1_x = 300
            self.obstacle1_y = 750
            self.obstacle2_x = 0
            self.obstacle2_y = 530
            self.obstacle3_x = 1280
            self.obstacle3_y = 750
            self.obstacle4_x = 1920 - self.obstacle_img.get_width()
            self.obstacle4_y = 530
        elif demo.Role.background_img_type == 3:
            self.obstacle_img = pygame.image.load('images/障碍物/obstacle3.png')
            self.obstacle1_x = 300
            self.obstacle1_y = 800
            self.obstacle2_x = demo.display_width // 2 - self.obstacle_img.get_width() // 2
            self.obstacle2_y = 580
            self.obstacle3_x = 1280
            self.obstacle3_y = 800
        if demo.Role.background_img_type == 1:
            left1_x = self.obstacle1_x - 100
            right1_x = self.obstacle1_x + self.obstacle_img.get_width() - 100
            up1_y = self.obstacle1_y - 165
            down1_y = self.obstacle1_y - 115

            left2_x = self.obstacle2_x - 100
            right2_x = self.obstacle2_x + self.obstacle_img.get_width() - 100
            up2_y = self.obstacle2_y - 165
            down2_y = self.obstacle2_y - 115

            left3_x = self.obstacle3_x - 100
            right3_x = self.obstacle3_x + self.obstacle_img.get_width() - 100
            up3_y = self.obstacle3_y - 165
            down3_y = self.obstacle3_y - 115

            self.obstacle = {'1': {'up_y': up1_y, 'down_y': down1_y, 'left_x': left1_x, 'right_x': right1_x},
                            '2': {'up_y': up2_y, 'down_y': down2_y, 'left_x': left2_x, 'right_x': right2_x},
                            '3': {'up_y': up3_y, 'down_y': down3_y, 'left_x': left3_x, 'right_x': right3_x}}
            self.obstacles_num = len(self.obstacle)
        elif demo.Role.background_img_type == 2:
            left1_x = self.obstacle1_x - 100
            right1_x = self.obstacle1_x + self.obstacle_img.get_width() - 100
            up1_y = self.obstacle1_y - 165
            down1_y = self.obstacle1_y - 115

            left2_x = self.obstacle2_x - 100
            right2_x = self.obstacle2_x + self.obstacle_img.get_width() - 100
            up2_y = self.obstacle2_y - 165
            down2_y = self.obstacle2_y - 115

            left3_x = self.obstacle3_x - 100
            right3_x = self.obstacle3_x + self.obstacle_img.get_width() - 100
            up3_y = self.obstacle3_y - 165
            down3_y = self.obstacle3_y - 115

            left4_x = self.obstacle4_x - 100
            right4_x = self.obstacle4_x + self.obstacle_img.get_width() - 100
            up4_y = self.obstacle4_y - 165
            down4_y = self.obstacle4_y - 115
            self.obstacle = {'1': {'up_y': up1_y, 'down_y': down1_y, 'left_x': left1_x, 'right_x': right1_x},
                            '2': {'up_y': up2_y, 'down_y': down2_y, 'left_x': left2_x, 'right_x': right2_x},
                            '3': {'up_y': up3_y, 'down_y': down3_y, 'left_x': left3_x, 'right_x': right3_x},
                            '4': {'up_y': up4_y, 'down_y': down4_y, 'left_x': left4_x, 'right_x': right4_x}}
            self.obstacles_num = len(self.obstacle)
        elif demo.Role.background_img_type == 3:
            left1_x = self.obstacle1_x - 100
            right1_x = self.obstacle1_x + self.obstacle_img.get_width() - 100
            up1_y = self.obstacle1_y - 165
            down1_y = self.obstacle1_y - 115

            left2_x = self.obstacle2_x - 100
            right2_x = self.obstacle2_x + self.obstacle_img.get_width() - 100
            up2_y = self.obstacle2_y - 165
            down2_y = self.obstacle2_y - 115

            left3_x = self.obstacle3_x - 100
            right3_x = self.obstacle3_x + self.obstacle_img.get_width() - 100
            up3_y = self.obstacle3_y - 165
            down3_y = self.obstacle3_y - 115
            self.obstacle = {'1': {'up_y': up1_y, 'down_y': down1_y, 'left_x': left1_x, 'right_x': right1_x},
                            '2': {'up_y': up2_y, 'down_y': down2_y, 'left_x': left2_x, 'right_x': right2_x},
                            '3': {'up_y': up3_y, 'down_y': down3_y, 'left_x': left3_x, 'right_x': right3_x}}
            self.obstacles_num = len(self.obstacle)
    def draw(self, screen):
        screen.blit(self.obstacle_img, (self.obstacle1_x, self.obstacle1_y))
        screen.blit(self.obstacle_img, (self.obstacle2_x, self.obstacle2_y))
        screen.blit(self.obstacle_img, (self.obstacle3_x, self.obstacle3_y))
        if demo.Role.background_img_type == 2:
            screen.blit(self.obstacle_img, (self.obstacle4_x, self.obstacle4_y))
    def jump(self):
        if self.segment_jump < self.segment_jump_set:
            self.jump_height = -self.jump_height_set
            self.segment_jump += 1
            if self.role == 1:
                demo.Role.one_person_jump = True
            else:
                demo.Role.two_person_jump = True
    def judge(self):
        if self.role == 1:
            demo.Role.one_person_y += self.jump_height
        else:
            demo.Role.two_person_y += self.jump_height
        self.jump_height += 2
        # TODO 障碍物
        for i in range(1,self.obstacles_num + 1):
            # 0 => up_y
            # 1 => down_y
            # 2 => left_x
            # 3 => right_x
            if self.role == 1:
                self.player_x = demo.Role.one_person_x
                self.player_y = demo.Role.one_person_y
            else:
                self.player_x = demo.Role.two_person_x
                self.player_y = demo.Role.two_person_y
            if self.player_y >= int(self.obstacle[str(i)]['up_y']) and self.player_y <= int(self.obstacle[str(i)]['down_y']) and self.player_x >= int(self.obstacle[str(i)]['left_x']) and self.player_x <= int(self.obstacle[str(i)]['right_x']):
                if self.role == 1:
                    demo.Role.one_person_jump = False
                    demo.Role.one_person_y = int(self.obstacle[str(i)]['up_y']) + 5
                else:
                    demo.Role.two_person_jump = False
                    demo.Role.two_person_y = int(self.obstacle[str(i)]['up_y']) + 5

                # self.player_y = int(self.obstacle[str(i)]['up_y']) + 5
                self.jump_height = 0
                self.segment_jump = 0
            elif self.player_y >= self.ground_y:
                if self.role == 1:
                    demo.Role.one_person_jump = False
                    demo.Role.one_person_y = self.ground_y
                else:
                    demo.Role.two_person_jump = False
                    demo.Role.two_person_y = self.ground_y
                # self.player_y = self.ground_y
                self.jump_height = 0
                self.segment_jump = 0
    def out(self):
        if self.role == 1:
            self.player_x = demo.Role.one_person_x
            self.player_y = demo.Role.one_person_y
        else:
            self.player_x = demo.Role.two_person_x
            self.player_y = demo.Role.two_person_y
        for i in range(1, self.obstacles_num + 1):
            if (self.player_x <= int(self.obstacle[str(i)]['left_x']) or self.player_x >= int(self.obstacle[str(i)]['right_x'])) and self.player_y >= int(self.obstacle[str(i)]['up_y']) and self.player_y <= int(self.obstacle[str(i)]['down_y']):
                if self.role == 1:
                    demo.Role.one_person_jump = True
                else:
                    demo.Role.two_person_jump = True
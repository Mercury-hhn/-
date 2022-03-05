# 远程攻击类
import pygame

import demo
import special
# 创建飞镖列表
dart_img_list_MU = []
dart_img_list_ICE = []
dart_img_list_WATER = []
dart_img_list_FIRE = []

# 载入所有图标
for pic_num in range(1,5):
    dart_img_list_ICE.append(pygame.image.load('images/新角色/golem_1/darts/'+str(pic_num)+'-min.png'))
    dart_img_list_MU.append(pygame.image.load('images/新角色/golem_4/darts/'+str(pic_num)+'.png'))
    dart_img_list_FIRE.append(pygame.image.load('images/新角色/golem_2/darts/'+str(pic_num)+'-min.png'))
dart_img_list_WATER.append(pygame.image.load('images/新角色/golem_3/darts/1.png'))


class Dart(object):
    def __init__(self,screen, x, y, role, direction):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.role = role
        self.direction = direction
        self.speed = 50 * direction
        self.count = 0
        if role == 1:
            demo.Role.one_person_blue -= demo.Role.deduct_dart_blue
            demo.Role.one_person_dart = False
        else:
            demo.Role.two_person_blue -= demo.Role.deduct_dart_blue
            demo.Role.two_person_dart = False
        self.person_special = special.Special(screen)
    def draw(self):

        if self.role == 1:
            if self.count >= 3:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动效果
                self.count = 0
            if self.direction == 1:
                # 判断使用的是哪个人物，绘制特色飞镖
                if demo.Role.one_person_name == 'golem_4':
                    self.screen.blit(dart_img_list_MU[self.count], (self.x, self.y))
                elif demo.Role.one_person_name == 'golem_1':
                    self.screen.blit(dart_img_list_ICE[self.count],(self.x,self.y))
                elif demo.Role.one_person_name == 'golem_3':
                    self.screen.blit(dart_img_list_WATER[0],(self.x,self.y))
                elif demo.Role.one_person_name == 'golem_2':
                    self.screen.blit(dart_img_list_FIRE[self.count],(self.x,self.y))
            else:
                if demo.Role.one_person_name == 'golem_1':
                    # 图片翻转
                    ultimate_skill = pygame.transform.flip(dart_img_list_ICE[self.count], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
                elif demo.Role.one_person_name == 'golem_4':
                    ultimate_skill = pygame.transform.flip(dart_img_list_MU[self.count], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
                elif demo.Role.one_person_name == 'golem_3':
                    ultimate_skill = pygame.transform.flip(dart_img_list_WATER[0], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
                elif demo.Role.one_person_name == 'golem_2':
                    ultimate_skill = pygame.transform.flip(dart_img_list_FIRE[self.count], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
            self.count += 1
        else:
            if self.count >= 3:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动效果
                self.count = 0
            if self.direction == -1:
                # 判断人物属性，绘制飞镖
                if demo.Role.two_person_name == 'golem_1':
                    # 图片翻转
                    ultimate_skill = pygame.transform.flip(dart_img_list_ICE[self.count], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
                elif demo.Role.two_person_name == 'golem_4':
                    ultimate_skill = pygame.transform.flip(dart_img_list_MU[self.count], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
                elif demo.Role.two_person_name == 'golem_3':
                    ultimate_skill = pygame.transform.flip(dart_img_list_WATER[0], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
                elif demo.Role.two_person_name == 'golem_2':
                    ultimate_skill = pygame.transform.flip(dart_img_list_FIRE[self.count], True, False)
                    self.screen.blit(ultimate_skill, (self.x, self.y))
            else:
                # 判断使用的是哪个人物，绘制特色飞镖
                if demo.Role.two_person_name == 'golem_4':
                    self.screen.blit(dart_img_list_MU[self.count], (self.x, self.y))
                elif demo.Role.two_person_name == 'golem_1':
                    self.screen.blit(dart_img_list_ICE[self.count], (self.x, self.y))
                elif demo.Role.two_person_name == 'golem_3':
                    self.screen.blit(dart_img_list_WATER[0], (self.x, self.y))
                elif demo.Role.two_person_name == 'golem_2':
                    self.screen.blit(dart_img_list_FIRE[self.count], (self.x, self.y))
            self.count += 1

    # 碰撞检测角色1
    def collision_check(self, role, a, b):
        if role == 1:
            temp1 = b.x <= a.two_person_x + a.two_person_width <= b.x + b.width
            temp2 = b.y <= a.two_person_y + a.two_person_height <= b.y + b.height
        else:
            temp1 = b.x <= a.one_person_x + a.one_person_width <= b.x + b.width
            temp2 = b.y <= a.one_person_y + a.one_person_height <= b.y + b.height
        return temp1 and temp2

    # 碰撞检测角色2
    def collision_check2(self, role, a, b):
        if role == 1:
            temp1 = b.two_person_x <= a.x + a.width <= b.two_person_x + b.two_person_width
            temp2 = b.two_person_y <= a.y + a.height <= b.two_person_y + b.two_person_height
        else:
            temp1 = b.one_person_x <= a.x + a.width <= b.one_person_x + b.one_person_width
            temp2 = b.one_person_y <= a.y + a.height <= b.one_person_y + b.one_person_height
        return temp1 and temp2
    def judge(self , dart):
        if self.role == 1:
            if self.collision_check(1,demo.Role,dart) or self.collision_check2(1,dart,demo.Role):
                self.person_special.hit(2)
                demo.Role.two_person_blood -= demo.Role.deduct_dart_blood
                demo.dart_img.remove(dart)
        else:
            if self.collision_check(2,demo.Role,dart) or self.collision_check2(2,dart,demo.Role):
                self.person_special.hit(1)
                demo.Role.one_person_blood -= demo.Role.deduct_dart_blood
                demo.dart_img.remove(dart)
        if (dart.x > 0 and dart.y < demo.display_height) and (dart.x < demo.display_width and dart.y < demo.display_height):
            dart.x += self.speed
        else:
            demo.dart_img.remove(dart)
        dart.draw()


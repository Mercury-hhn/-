import pygame
import demo
import special
import anger.golem_1

class Gas:
    def __init__(self, screen, x, y, role, direction):
        self.screen = screen
        self.role = role
        self.x = x
        self.y = y
        self.direction = direction
        self.count = 0
        self.role = role
        self.width = 308
        self.height = 352
        self.release_count = 0
        if role == 1:
            self.role_name = demo.Role.one_person_name
            demo.Role.one_person_white -= 40
        else:
            self.role_name = demo.Role.two_person_name
            demo.Role.two_person_white -= 40
        if self.role_name == 'golem_1' or self.role_name == 'golem_2' or self.role_name == 'golem_3' or self.role_name == 'golem_4' :
            self.y -= 150
        self.person_special = special.Special(screen)

    def draw(self):
        if self.role_name == 'golem_1':
            if self.direction == -1:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
                    self.count = 0
                self.screen.blit(anger.golem_1.gas_img[self.count], (self.x, self.y))
                self.count += 1
            else:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:
                    self.count = 0
                # 水平翻转图片
                ultimate_skill = pygame.transform.flip(anger.golem_1.gas_img[self.count], True, False)
                self.screen.blit(ultimate_skill, (self.x, self.y))
                self.count += 1
        elif self.role_name == 'golem_2':
            if self.direction == -1:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
                    self.count = 0
                self.screen.blit(anger.golem_1.gas_img[self.count], (self.x, self.y))
                self.count += 1
            else:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:
                    self.count = 0
                # 水平翻转图片
                ultimate_skill = pygame.transform.flip(anger.golem_1.gas_img[self.count], True, False)
                self.screen.blit(ultimate_skill, (self.x, self.y))
                self.count += 1
        elif self.role_name == 'golem_3':
            if self.direction == -1:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
                    self.count = 0
                self.screen.blit(anger.golem_1.gas_img[self.count], (self.x, self.y))
                self.count += 1
            else:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:
                    self.count = 0
                # 水平翻转图片
                ultimate_skill = pygame.transform.flip(anger.golem_1.gas_img[self.count], True, False)
                self.screen.blit(ultimate_skill, (self.x, self.y))
                self.count += 1
        elif self.role_name == 'golem_4':
            if self.direction == -1:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
                    self.count = 0
                self.screen.blit(anger.golem_1.gas_img[self.count], (self.x, self.y))
                self.count += 1
            else:
                if self.count >= anger.golem_1.FRAME_PER_SECONDS:
                    self.count = 0
                # 水平翻转图片
                ultimate_skill = pygame.transform.flip(anger.golem_1.gas_img[self.count], True, False)
                self.screen.blit(ultimate_skill, (self.x, self.y))
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
    def judge(self, ultimate_skill):
        # 龙大招
        if self.role == 1:
            self.person_special.release(1)
        else:
            self.person_special.release(2)
        if self.role_name == 'golem_1':
            if self.role == 1:
                if self.collision_check(1, demo.Role, ultimate_skill) or self.collision_check2(1, ultimate_skill, demo.Role):
                    demo.Role.two_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色一大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(2)
                        demo.Role.two_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.two_person_x += 100
                        else:
                            demo.Role.two_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)
            else:
                if self.collision_check(2, demo.Role, ultimate_skill) or self.collision_check2(2, ultimate_skill, demo.Role):
                    demo.Role.one_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色二大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(1)
                        demo.Role.one_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.one_person_x += 100
                        else:
                            demo.Role.one_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)
        elif self.role_name == 'golem_2':
            if self.role == 1:
                if self.collision_check(1, demo.Role, ultimate_skill) or self.collision_check2(1, ultimate_skill, demo.Role):
                    demo.Role.two_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色一大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(2)
                        demo.Role.two_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.two_person_x += 100
                        else:
                            demo.Role.two_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)
            else:
                if self.collision_check(2, demo.Role, ultimate_skill) or self.collision_check2(2, ultimate_skill, demo.Role):
                    demo.Role.one_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色二大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(1)
                        demo.Role.one_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.one_person_x += 100
                        else:
                            demo.Role.one_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)
        elif self.role_name == 'golem_3':
            if self.role == 1:
                if self.collision_check(1, demo.Role, ultimate_skill) or self.collision_check2(1, ultimate_skill,demo.Role):
                    demo.Role.two_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色一大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(2)
                        demo.Role.two_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.two_person_x += 100
                        else:
                            demo.Role.two_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)
            else:
                if self.collision_check(2, demo.Role, ultimate_skill) or self.collision_check2(2, ultimate_skill,demo.Role):
                    demo.Role.one_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色二大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(1)
                        demo.Role.one_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.one_person_x += 100
                        else:
                            demo.Role.one_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)

        elif self.role_name == 'golem_4':
            if self.role == 1:
                if self.collision_check(1, demo.Role, ultimate_skill) or self.collision_check2(1, ultimate_skill,
                                                                                               demo.Role):
                    demo.Role.two_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色一大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(2)
                        demo.Role.two_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.two_person_x += 100
                        else:
                            demo.Role.two_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)
            else:
                if self.collision_check(2, demo.Role, ultimate_skill) or self.collision_check2(2, ultimate_skill,
                                                                                               demo.Role):
                    demo.Role.one_person_blood -= anger.golem_1.deduct_orange_blood
                    # 角色二大招击退效果
                    if self.count >= 8:
                        self.release_count += 1
                        self.person_special.hit(1)
                        demo.Role.one_person_controlled = True
                    if self.release_count >= 3:
                        if self.direction == 1:
                            demo.Role.one_person_x += 100
                        else:
                            demo.Role.one_person_x -= 100
                        demo.gas_img.remove(ultimate_skill)
            # if (ultimate_skill.x >= 0 - ultimate_skill.width and ultimate_skill.y < demo.display_height) and (ultimate_skill.x <= demo.display_width + ultimate_skill.width and ultimate_skill.y < demo.display_height):
            #     ultimate_skill.x += ultimate_skill.speed
            # else:
            #
        ultimate_skill.draw()


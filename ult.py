# 召唤类
import pygame
import demo
import special
import call.dragon
import call.human
import call.rigidity

# 召唤类
class UltimateSkill:
    def __init__(self, screen, x, y, role, direction):
        self.screen = screen
        self.role = role
        self.x = x
        self.y = y
        
        # 大招击退距离
        self.ult_value = 20
        
        # # 大招僵直效果
        # self.one_ult_rigidity = False
        # self.two_ult_rigidity = False
        
        self.direction = direction
        self.count = 0
        if role == 1:
            self.call_role = demo.Role.one_person_call_role
            # 龙大招
            if demo.Role.one_person_call_role == 'dragon':
                self.speed = call.dragon.speed * self.direction
                self.width = call.dragon.width
                self.height = call.dragon.height
                if self.direction == -1:
                    self.x = self.x
                else:
                    self.x = self.x - call.dragon.width
                self.y = self.y - call.dragon.height // 2 // 2
                demo.Role.one_person_blue -= call.dragon.deduct_ultimate_skill_blue
            # 回血大招
            elif self.call_role == 'human':
                self.speed = call.human.speed * self.direction
                self.width = call.human.width
                self.height = call.human.height
                if self.direction == -1:
                    self.x = self.x
                else:
                    self.x = self.x - call.human.width
                self.y = self.y - call.human.height // 2
                demo.Role.one_person_blue -= call.human.deduct_ultimate_skill_blue
            
            # 僵直大招
            elif self.call_role == "rigidity":
                self.speed = call.rigidity.speed * self.direction
                self.width = call.rigidity.width
                self.height = call.rigidity.height
                if self.direction == -1:
                    self.x = self.x
                else:
                    self.x = self.x - call.rigidity.width
                self.y = self.y - call.rigidity.height // 2
                demo.Role.one_person_blue -= call.rigidity.deduct_ultimate_skill_blue
            demo.Role.one_person_ultimate_skill = False
            
        else:
            self.call_role = demo.Role.two_person_call_role
            if demo.Role.two_person_call_role == 'dragon':
                self.speed = call.dragon.speed * self.direction
                self.width = call.dragon.width
                self.height = call.dragon.height
                if self.direction == -1:
                    self.x = self.x
                else:
                    self.x = self.x - call.dragon.width
                self.y = self.y - call.dragon.height // 2 // 2
                demo.Role.two_person_blue -= call.dragon.deduct_ultimate_skill_blue
            elif self.call_role == 'human':
                self.speed = call.human.speed * self.direction
                self.width = call.human.width
                self.height = call.human.height
                if self.direction == -1:
                    self.x = self.x
                else:
                    self.x = self.x - call.human.width
                self.y = self.y - call.human.height // 2
                demo.Role.two_person_blue -= call.human.deduct_ultimate_skill_blue
            
            # 僵直大招
            elif self.call_role == "rigidity":
                self.speed = call.rigidity.speed * self.direction
                self.width = call.rigidity.width
                self.height = call.rigidity.height
                if self.direction == -1:
                    self.x = self.x
                else:
                    self.x = self.x - call.rigidity.width
                self.y = self.y - call.rigidity.height // 2
                demo.Role.two_person_blue -= call.rigidity.deduct_ultimate_skill_blue
            demo.Role.two_person_ultimate_skill = False
        self.person_special = special.Special(screen)
    # 绘制
    def draw(self):
        if self.call_role == 'dragon':
            if self.direction == -1:
                if self.count >= call.dragon.FRAME_PER_SECONDS:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
                    self.count = 0
                self.screen.blit(call.dragon.call_img[self.count], (self.x, self.y))
                self.count += 1
            else:
                if self.count >= call.dragon.FRAME_PER_SECONDS:
                    self.count = 0
                # 水平翻转图片
                ultimate_skill = pygame.transform.flip(call.dragon.call_img[self.count], True, False)
                self.screen.blit(ultimate_skill, (self.x, self.y))
                self.count += 1
        elif self.call_role == 'human':
            self.speed = call.human.speed * self.direction
            if self.direction == -1:
                if self.count >= call.human.FRAME_PER_SECONDS:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
                    self.count = 0
                self.screen.blit(call.human.call_img[self.count], (self.x, self.y))
                self.count += 1
            else:
                if self.count >= call.human.FRAME_PER_SECONDS:
                    self.count = 0
                # 水平翻转图片
                ultimate_skill = pygame.transform.flip(call.human.call_img[self.count], True, False)
                self.screen.blit(ultimate_skill, (self.x, self.y))
                self.count += 1
        
        elif self.call_role == 'rigidity':
            self.speed = call.rigidity.speed * self.direction
            if self.direction == -1:
                if self.count >= call.rigidity.FRAME_PER_SECONDS:  # 如果count大于12重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
                    self.count = 0
                self.screen.blit(call.rigidity.call_img[self.count], (self.x, self.y))
                self.count += 1
            else:
                if self.count >= call.rigidity.FRAME_PER_SECONDS:
                    self.count = 0
                # 水平翻转图片
                ultimate_skill = pygame.transform.flip(call.rigidity.call_img[self.count], True, False)
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
    
    def Sound(self,src):
        sound = pygame.mixer.Sound(src)
        sound.set_volume(2.5)
        sound.play()
    
    def judge(self, ultimate_skill):
        # 龙大招
        if self.role == 1:
            self.person_special.release(1)
        else:
            self.person_special.release(2)
        if self.call_role == 'dragon':
            if self.role == 1:
                if self.collision_check(1, demo.Role, ultimate_skill) or self.collision_check2(1, ultimate_skill, demo.Role):
                    demo.Role.two_person_blood -= call.dragon.deduct_ultimate_skill_blood
                    # 角色一大招击退效果
                    self.person_special.hit(2)
                    demo.Role.two_person_controlled = True
                    if self.count % 3 == 0:
                        if self.direction == 1:
                            demo.Role.two_person_x += self.ult_value
                        else:
                            demo.Role.two_person_x -= self.ult_value
                    demo.player_two_jump.out()
            else:
                if self.collision_check(2, demo.Role, ultimate_skill) or self.collision_check2(2, ultimate_skill, demo.Role):
                    demo.Role.one_person_blood -= call.dragon.deduct_ultimate_skill_blood
                    # 角色二大招击退效果
                    self.person_special.hit(1)
                    demo.Role.one_person_controlled = True
                    if self.count % 3 == 0:
                        if self.direction == 1:
                            demo.Role.one_person_x += self.ult_value
                        else:
                            demo.Role.one_person_x -= self.ult_value
                    demo.player_one_jump.out()
            if (ultimate_skill.x >= 0 - ultimate_skill.width and ultimate_skill.y < demo.display_height) and (ultimate_skill.x <= demo.display_width + ultimate_skill.width and ultimate_skill.y < demo.display_height):
                ultimate_skill.x += ultimate_skill.speed
            else:
                demo.ultimate_skill_img.remove(ultimate_skill)
            ultimate_skill.draw()
        # 回血大招
        elif self.call_role == 'human':
            if self.role == 1:
                if self.collision_check(1, demo.Role, ultimate_skill) or self.collision_check2(1, ultimate_skill, demo.Role):
                    self.person_special.hit(2)
                    demo.Role.two_person_controlled = True
                    self.person_special.reply(1)
                    if demo.Role.one_person_blood < 100 * demo.Role.life:
                        demo.Role.one_person_blood += call.human.deduct_ultimate_skill_blood  # 加角色一血量
                    if self.count % 2 == 0:
                        if self.direction == 1:
                            demo.Role.two_person_x += self.ult_value
                        else:
                            demo.Role.two_person_x -= self.ult_value
            else:
                if self.collision_check(2, demo.Role, ultimate_skill) or self.collision_check2(2, ultimate_skill, demo.Role):
                    self.person_special.hit(1)
                    demo.Role.one_person_controlled = True
                    self.person_special.reply(2)
                    if demo.Role.two_person_blood < 100 * demo.Role.life:
                        demo.Role.two_person_blood += call.human.deduct_ultimate_skill_blood  # 加血量
                    if self.count % 2 == 0:
                        if self.direction == 1:
                            demo.Role.one_person_x += self.ult_value
                        else:
                            demo.Role.one_person_x -= self.ult_value
            if (ultimate_skill.x >= 0 - ultimate_skill.width and ultimate_skill.y < demo.display_height) and (ultimate_skill.x <= demo.display_width + ultimate_skill.width and ultimate_skill.y < demo.display_height):
                ultimate_skill.x += ultimate_skill.speed
            else:
                demo.ultimate_skill_img.remove(ultimate_skill)
            ultimate_skill.draw()
        # 僵直大招
        elif self.call_role == 'rigidity':
            if self.role == 1:
                if self.collision_check(1, demo.Role, ultimate_skill) or self.collision_check2(1, ultimate_skill, demo.Role):
                    self.person_special.hit(2)
                    demo.Role.two_person_controlled_number = 5
            else:
                if self.collision_check(2, demo.Role, ultimate_skill) or self.collision_check2(2, ultimate_skill, demo.Role):
                    self.person_special.hit(1)
                    demo.Role.one_person_controlled_number = 5

            if (ultimate_skill.x >= 0 - ultimate_skill.width and ultimate_skill.y < demo.display_height) and (ultimate_skill.x <= demo.display_width + ultimate_skill.width and ultimate_skill.y < demo.display_height):
                ultimate_skill.x += ultimate_skill.speed
            else:
                demo.ultimate_skill_img.remove(ultimate_skill)
            ultimate_skill.draw()








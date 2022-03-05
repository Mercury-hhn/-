import pygame
import demo
import special
# 创建角色类
class Role(object):
    # 创建一个构造函数（self,图片路径,图片距离左上角坐标位置）
    def __init__(self, screen, one_person_x, one_person_y, one_person_width, one_person_height, two_person_x, two_person_y,two_person_width, two_person_height):

        # # 加载角色图片 行走
        # for pic_num in range(1, 25):
        #     one_person_walk_img.append(pygame.image.load('images/新角色/' + one_person_name + '/walk/' + str(pic_num) + '-min' + '.png'))
        #     two_person_walk_img.append(pygame.image.load('images/新角色/' + two_person_name + '/walk/' + str(pic_num) + '-min' + '.png'))
        # 将站立图片载入列表
        self.background_img_type = 1
        self.one_person_controlled_number = 0
        self.two_person_controlled_number = 0
        self.life = 1
        self.one_person_life = 1
        self.two_person_life = 1
        self.energy = 1
        self.one_person_energy = 1
        self.two_person_energy = 1
        self.time = 60
        self.one_person_name = 'golem_1'
        self.two_person_name = 'golem_2'
        self.one_person_call_role = 'dragon'
        self.two_person_call_role = 'human'
        self.one_person_dodge_img = []
        self.one_person_stand_img = []
        self.one_person_walk_img = []
        self.one_person_attack_img = []
        self.one_person_hurt_img = []
        self.two_person_dodge_img = []
        self.two_person_stand_img = []
        self.two_person_walk_img = []
        self.two_person_attack_img = []
        self.two_person_hurt_img = []
        self.orange_img = []
        # 默认移动速度
        self.speed = 15
        # 闪避状态
        self.one_person_dodge = False
        self.two_person_dodge = False

        self.two_person_special = False
        self.one_person_skill = False  # 被动技能
        self.two_person_skill = False
        # 大招状态True释放，False不释放
        self.one_person_ultimate_skill = False
        self.two_person_ultimate_skill = False
        self.deduct_dart_blue = 5  # 飞镖扣除蓝条
        self.deduct_dart_blood = 5  # 飞镖扣除血条
        self.deduct_attack_blood = 5  # 普攻扣除血条
        self.deduct_attack_blue = 5  # 普攻回复蓝条
        self.deduct_dodge_blue = 5  # 闪避扣除蓝条
        # 大招扣除血量
        self.deduct_ultimate_skill_blood = 1
        # 大招扣除蓝量
        self.deduct_ultimate_skill_blue = 50

        self.deduct_orange = 0.5  # 按键回复爆气条的值
        self.deduct_white = 40  # 加减爆气格
        
        # 角色一
        # 角色x位置
        self.one_person_x = one_person_x
        # 角色y位置
        self.one_person_y = one_person_y
        # 角色宽度
        self.one_person_width = one_person_width
        # 角色高度
        self.one_person_height = one_person_height
        # 角色朝左
        self.one_person_left = False
        # 角色朝右，True即默认为朝右
        self.one_person_right = True
        # 角色站立状态，True即默认战立
        self.one_person_stand = True
        # 角色跳跃状态
        self.one_person_jump = False
        # 角色攻击状态
        self.one_person_attack = False
        # 角色扔飞镖状态
        self.one_person_dart = False
        # 角色防御状态
        self.one_person_defense = False
        # 角色攒爆气状态
        self.one_person_bring_orange = False
        
        # 角色1跳跃高度
        self.one_person_jump_t = 10
        
         # 角色读取列表默认第一张图片   读取走动图片
        self.one_person_walk_num = 0
        self.one_person_walk_allnum = 24
        # 读取静止图片
        self.one_person_stand_num = 0
        self.one_person_stand_allnum = 18
        # 读取攻击图片
        self.one_person_attack_num = 0
        self.one_person_attack_allnum = 7
        # 受到伤害图片
        self.one_person_hurt_num = 0
        self.one_person_hurt_allnum = 12
        # 攒爆气图片
        self.one_person_orange_num = 0
        self.one_person_orange_allnum = 6
        # 闪避
        self.one_person_dodge_num = 0
        self.one_person_dodge_allnum = 5
        # # 起跳图片
        # self.one_jump = 0
        
        # 角色血量
        self.one_person_blood = 100
        # 角色蓝量
        self.one_person_blue = 100
        # 角色一爆气量
        self.one_person_orange = 0
        self.one_person_white = 40  # 角色一爆气格
        # 角色被控制状态
        self.one_person_controlled = False
        self.one_person_attack_attacknum = 0  # 普攻次数
        
        # 角色二
        self.two_person_x = two_person_x
        self.two_person_y = two_person_y
        self.two_person_width = two_person_width
        self.two_person_height = two_person_height
        self.two_person_left = True
        self.two_person_right = False
        self.two_person_stand = True
        self.two_person_jump = False
        self.two_person_attack = False
        self.two_person_dart = False
        self.two_person_defense = False
        self.two_person_bring_orange = False
        self.two_person_jump_t = 10
        self.two_person_img = 1
        self.two_person_blood = 100
        self.two_person_blue = 100
        # 角色二爆气量
        self.two_person_orange = 0
        self.two_person_white = 40  # 角色二爆气格
        self.two_person_controlled = False
        # 角色读取列表默认第一张图片
        # 读取走动图片
        self.two_person_walk_num = 0
        self.two_person_walk_allnum = 24
        # 读取静止图片
        self.two_person_stand_num = 0
        self.two_person_stand_allnum = 18
        # 读取攻击图片
        self.two_person_attack_num = 0
        self.two_person_attack_allnum = 7
        # 受到伤害图片
        self.two_person_hurt_num = 0
        self.two_person_hurt_allnum = 12
        # 攒爆气图片
        self.two_person_orange_num = 0
        self.two_person_orange_allnum = 6
        # 闪避
        self.two_person_dodge_num = 0
        self.two_person_dodge_allnum = 5
        # # 起跳图片
        # self.two_jump = 0
        self.person_special = special.Special(screen)
    def Sound(self,src):
        sound = pygame.mixer.Sound(src)
        sound.set_volume(2.5)
        sound.play()
    # 碰撞检测
    def one_person_collision_check(self):
        temp1 = self.two_person_x <= self.one_person_x + self.one_person_width <= self.two_person_x + self.two_person_width
        temp2 = self.two_person_y <= self.one_person_y + self.one_person_height <= self.two_person_y + self.two_person_height
        return temp1 and temp2
    
    def two_person_collision_check(self):
        temp1 = self.one_person_x <= self.two_person_x + self.two_person_width <= self.one_person_x + self.one_person_width
        temp2 = self.one_person_y <= self.two_person_y + self.two_person_height <= self.one_person_y + self.one_person_height
        return temp1 and temp2
    def defense(self,role):
        pass

    # 绘制人物
    def draw(self, screen):
        # 检测是否走出窗体
        if self.one_person_x < - 65:
            self.one_person_x = - 65
        if self.one_person_x > screen.get_size()[0] - 135:
            self.one_person_x = screen.get_size()[0] - 135
        if self.one_person_y < 0:
            self.one_person_y = 0
        # TODO 判断图片数量
        # 如果循环次数大于设置的图片数量  控制走动图片数量
        if self.one_person_walk_num >= self.one_person_walk_allnum:
            # 重置角色动作图片数量为0
            self.one_person_walk_num = 0
        # 控制静止站立图片数量
        if self.one_person_stand_num >= self.one_person_stand_allnum:
            self.one_person_stand_num = 0
        # 控制攻击图片数量
        if self.one_person_attack_num >= self.one_person_attack_allnum:
            self.one_person_attack_num = 0
        # 控制攒爆气图片数量
        if self.one_person_orange_num >= self.one_person_orange_allnum:
            self.one_person_orange_num = 0
        # 控制闪避图片数量
        if self.one_person_dodge_num >= self.one_person_dodge_allnum:
            self.one_person_dodge_num = 0
        # # 控制起跳图片
        # if self.one_jump >= 6:
        #     self.one_jump = 0
        # 如果角色朝左
        
        if self.one_person_orange == False:
            self.one_person_orange_num = 0
        if self.one_person_left and not self.one_person_stand and not self.one_person_jump:
            
            image = pygame.transform.flip(self.one_person_walk_img[self.one_person_walk_num], True, False)
            screen.blit(image, (self.one_person_x, self.one_person_y))
            self.one_person_walk_num += 1
        elif self.one_person_right and not self.one_person_stand and not self.one_person_jump:
            screen.blit(self.one_person_walk_img[self.one_person_walk_num], (self.one_person_x, self.one_person_y))
            self.one_person_walk_num += 1
        # 判断攻击图片
        elif self.one_person_attack:
            if self.one_person_left:
                image = pygame.transform.flip(self.one_person_attack_img[self.one_person_attack_num], True, False)
                screen.blit(image, (self.one_person_x, self.one_person_y))
                self.one_person_attack_num += 1
            else:
                screen.blit(self.one_person_attack_img[self.one_person_attack_num], (self.one_person_x, self.one_person_y))
                self.one_person_attack_num += 1
            if self.one_person_attack_num >= self.one_person_attack_allnum:
                self.deduct(1,'attack')
        # elif self.one_person_dart:
        #     self.deduct(1,'dart')
        elif self.one_person_controlled:
            
            if self.one_person_left:
                image = pygame.transform.flip(self.one_person_hurt_img[self.one_person_hurt_num], True, False)
                screen.blit(image, (self.one_person_x, self.one_person_y))
            else:
                screen.blit(self.one_person_hurt_img[self.one_person_hurt_num], (self.one_person_x, self.one_person_y))
            # 受到伤害图片
            if self.one_person_hurt_num < self.one_person_hurt_allnum - 1:
                self.one_person_hurt_num += 1
            else:
                if self.one_person_controlled_number >= 0:
                    self.one_person_controlled_number -= 1
                self.one_person_controlled = False
                self.one_person_dodge = False
                self.one_person_dodge_num = 0
                self.one_person_hurt_num = 0
        # elif self.one_person_ultimate_skill:
        #     self.deduct(1, 'ultimate_skill')
        elif self.one_person_defense:
            if self.one_person_left:
                if not self.one_person_jump:
                    image = pygame.transform.flip(self.one_person_stand_img[self.one_person_stand_num], True, False)
                    screen.blit(image, (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num += 1
                else:
                    image = pygame.transform.flip(self.one_person_stand_img[self.one_person_stand_num], True, False)
                    screen.blit(image, (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num = 1
            else:
                if not self.one_person_jump:
                    screen.blit(self.one_person_stand_img[self.one_person_stand_num], (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num += 1
                else:
                    screen.blit(self.one_person_stand_img[self.one_person_stand_num], (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num = 1
            screen.blit(pygame.image.load("images/新角色/defense/defense.png"),(self.one_person_x + 20, self.one_person_y + 20))
        elif self.one_person_dodge:

            screen.blit(self.one_person_dodge_img[self.one_person_dodge_num],(self.one_person_x - 70, self.one_person_y - 50))
            self.one_person_dodge_num += 1
            if self.one_person_dodge_num >= 5:
                if self.one_person_left:
                    self.one_person_x -= 300
                else:
                    self.one_person_x += 300
                demo.player_one_jump.out()
                self.one_person_dodge = False
        elif self.one_person_bring_orange:
            if self.one_person_left:
                if not self.one_person_jump:
                    image = pygame.transform.flip(self.one_person_stand_img[self.one_person_stand_num], True, False)
                    screen.blit(image, (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num += 1
                else:
                    image = pygame.transform.flip(self.one_person_stand_img[self.one_person_stand_num], True, False)
                    screen.blit(image, (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num = 1
            else:
                if not self.one_person_jump:
                    screen.blit(self.one_person_stand_img[self.one_person_stand_num], (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num += 1
                else:
                    screen.blit(self.one_person_stand_img[self.one_person_stand_num], (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num = 1
            screen.blit(self.orange_img[self.one_person_orange_num], (self.one_person_x + 10, self.one_person_y + 40))
            self.one_person_orange_num += 1
            if self.one_person_orange <= 100:
                self.one_person_orange += self.deduct_orange  # self.deduct_attack_orange = 0.5  # 按i键回复爆气条的值
            if self.one_person_orange == 100:  # 爆气值等于100 加爆气格
                if self.one_person_white < 100:  # 爆气值<100才会执行 防止溢出
                    self.one_person_white += self.deduct_white
                    self.one_person_orange = 0  # 爆气条重置为0
            self.one_person_bring_orange = False
        else:
            if self.one_person_left:
                if not self.one_person_jump:
                    image = pygame.transform.flip(self.one_person_stand_img[self.one_person_stand_num], True, False)
                    screen.blit(image, (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num += 1
                else:
                    image = pygame.transform.flip(self.one_person_stand_img[self.one_person_stand_num], True, False)
                    screen.blit(image, (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num = 1
            else:
                if not self.one_person_jump:
                    screen.blit(self.one_person_stand_img[self.one_person_stand_num], (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num += 1
                else:
                    screen.blit(self.one_person_stand_img[self.one_person_stand_num], (self.one_person_x, self.one_person_y))
                    self.one_person_stand_num = 1
        # 角色1红框
        # pygame.draw.rect(screen, [255, 0, 0], [self.one_person_x+80, self.one_person_y+30, self.one_person_width, self.one_person_height], 5)
        if self.two_person_x < - 65:
            self.two_person_x = - 65
        if self.two_person_x > screen.get_size()[0] - 135:
            self.two_person_x = screen.get_size()[0] - 135
        if self.two_person_y < 0:
            self.two_person_y = 0
        # 如果循环次数大于设置的图片数量  控制走动图片数量
        if self.two_person_walk_num >= self.two_person_walk_allnum:
            # 重置角色动作图片数量为0
            self.two_person_walk_num = 0
        # 控制静止站立图片数量
        if self.two_person_stand_num >= self.two_person_stand_allnum:
            self.two_person_stand_num = 0
        # 控制攻击图片数量
        if self.two_person_attack_num >= self.two_person_attack_allnum:
            self.two_person_attack_num = 0
        # 控制攒爆气图片数量
        if self.two_person_orange_num >= self.two_person_orange_allnum:
            self.two_person_orange_num = 0
        # 控制闪避图片数量
        if self.two_person_dodge_num >= self.two_person_dodge_allnum:
            self.two_person_dodge_num = 0
        # # 控制起跳图片
        # if self.two_jump >= 6:
        #     self.two_jump = 0
        
        if self.two_person_left and not self.two_person_stand and not self.two_person_jump:
            image = pygame.transform.flip(self.two_person_walk_img[self.two_person_walk_num], True, False)
            screen.blit(image, (self.two_person_x, self.two_person_y))
            self.two_person_walk_num += 1
        elif self.two_person_right and not self.two_person_stand and not self.two_person_jump:
            screen.blit(self.two_person_walk_img[self.two_person_walk_num], (self.two_person_x, self.two_person_y))
            self.two_person_walk_num += 1
        # 角色2攻击图片设置
        elif self.two_person_attack:
            if self.two_person_left:
                image = pygame.transform.flip(self.two_person_attack_img[self.two_person_attack_num], True, False)
                screen.blit(image, (self.two_person_x, self.two_person_y))
                self.two_person_attack_num += 1
            else:
                screen.blit(self.two_person_attack_img[self.two_person_attack_num], (self.two_person_x, self.two_person_y))
                self.two_person_attack_num += 1
            if self.two_person_attack_num >= self.two_person_attack_allnum:
                self.deduct(2,'attack')
                
        # elif self.two_person_dart:
        #     self.deduct(2,'dart')
            
        elif self.two_person_controlled:
            
            if self.two_person_left:
                image = pygame.transform.flip(self.two_person_hurt_img[self.two_person_hurt_num], True, False)
                screen.blit(image, (self.two_person_x, self.two_person_y))
            else:
                screen.blit(self.two_person_hurt_img[self.two_person_hurt_num], (self.two_person_x, self.two_person_y))
            # 受到伤害图片
            if self.two_person_hurt_num < self.two_person_hurt_allnum - 1:
                self.two_person_hurt_num += 1
            else:
                if self.two_person_controlled_number >= 0:
                    self.two_person_controlled_number -= 1
                self.two_person_controlled = False
                self.two_person_dodge = False
                self.two_person_dodge_num = 0
                self.two_person_hurt_num = 0
        # 判断状态
        # elif self.two_person_ultimate_skill:
        #     self.deduct(2, 'ultkulou')
        elif self.two_person_defense:
            if self.two_person_left:
                if not self.two_person_jump:
                    image = pygame.transform.flip(self.two_person_stand_img[self.two_person_stand_num], True, False)
                    screen.blit(image, (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num += 1
                else:
                    image = pygame.transform.flip(self.two_person_stand_img[self.two_person_stand_num], True, False)
                    screen.blit(image, (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num = 1
            else:
                if not self.one_person_jump:
                    screen.blit(self.two_person_stand_img[self.two_person_stand_num],(self.two_person_x, self.two_person_y))
                    self.two_person_stand_num += 1
                else:
                    screen.blit(self.two_person_stand_img[self.two_person_stand_num],(self.two_person_x, self.two_person_y))
                    self.two_person_stand_num = 1
            screen.blit(pygame.image.load("images/新角色/defense/defense.png"), (self.two_person_x + 20, self.two_person_y + 20))
        elif self.two_person_dodge:
            screen.blit(self.two_person_dodge_img[self.two_person_dodge_num],(self.two_person_x - 70, self.two_person_y - 50))
            self.two_person_dodge_num += 1
            if self.two_person_dodge_num >= 5:
                if self.two_person_left:
                    self.two_person_x -= 300
                else:
                    self.two_person_x += 300
                demo.player_two_jump.out()
                self.two_person_dodge = False
        elif self.two_person_bring_orange:
            if self.two_person_left:
                if not self.two_person_jump:
                    image = pygame.transform.flip(self.two_person_stand_img[self.two_person_stand_num], True, False)
                    screen.blit(image, (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num += 1
                else:
                    image = pygame.transform.flip(self.two_person_stand_img[self.two_person_stand_num], True, False)
                    screen.blit(image, (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num = 1
            else:
                if not self.one_person_jump:
                    screen.blit(self.two_person_stand_img[self.two_person_stand_num],(self.two_person_x, self.two_person_y))
                    self.two_person_stand_num += 1
                else:
                    screen.blit(self.two_person_stand_img[self.two_person_stand_num],(self.two_person_x, self.two_person_y))
                    self.two_person_stand_num = 1
            screen.blit(self.orange_img[self.two_person_orange_num], (self.two_person_x + 10, self.two_person_y + 40))
            self.two_person_orange_num += 1
            if self.two_person_orange <= 100:
                self.two_person_orange += self.deduct_orange  # self.deduct_attack_orange = 0.5  # 按小键盘6键回复爆气条的值
            if self.two_person_orange == 100:  # 爆气值等于100 加爆气格
                if self.two_person_white < 100:  # 爆气值<100才会执行 防止溢出
                    self.two_person_white += self.deduct_white
                    self.two_person_orange = 0  # 爆气条重置为0
            self.two_person_bring_orange = False
        else:
            if self.two_person_left:
                if not self.two_person_jump:
                    image = pygame.transform.flip(self.two_person_stand_img[self.two_person_stand_num], True, False)
                    screen.blit(image, (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num += 1
                else:
                    image = pygame.transform.flip(self.two_person_stand_img[self.two_person_stand_num], True, False)
                    screen.blit(image, (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num = 1
            else:
                if not self.two_person_jump:
                    screen.blit(self.two_person_stand_img[self.two_person_stand_num], (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num += 1
                else:
                    screen.blit(self.two_person_stand_img[self.two_person_stand_num], (self.two_person_x, self.two_person_y))
                    self.two_person_stand_num = 1
        # 角色2红框
        # pygame.draw.rect(screen, [255, 0, 0],[self.two_person_x+80, self.two_person_y+30, self.two_person_width, self.two_person_height], 5)
        # 攻击检测（角色，攻击类型）
    def deduct(self, role, type):
        # 如果为角色1
        if role == 1:
            # 攻击类型为普攻
            if type == 'attack':
                # 碰撞检测
                if self.one_person_collision_check() or self.two_person_collision_check():
                    # 扣除角色2血量
                    if self.two_person_defense:
                        self.person_special.hit(2)
                        self.Sound("images/新角色/defense/hit.mp3")
                    else:
                        self.two_person_blood -= self.deduct_attack_blood
                        self.Sound("sound/击中音效.mp3")
                        # 普攻回蓝
                        if 100 * self.energy - (self.one_person_blue + self.deduct_attack_blue) >= 0:
                            # 蓝量小于100才会加蓝，目的防止蓝量溢出白色矩形边框
                            if self.one_person_blue < 100 * self.energy:
                                self.one_person_blue += self.deduct_attack_blue
                        else:
                            # 蓝量小于100才会加蓝，目的防止蓝量溢出白色矩形边框
                            if self.one_person_blue < 100 * self.energy:
                                self.one_person_blue += (self.one_person_blue + self.deduct_attack_blue) - 100 * self.energy
                        # 角色二被控制
                        self.two_person_controlled = True
                # # 普攻次数
                # self.one_person_attack_attacknum += 1
                # 攻击状态
                self.one_person_attack = False
            # 如果为飞镖
            elif type == 'dart':
                # 扣除角色1蓝量
                self.one_person_blue -= self.deduct_dart_blue
                # 扔飞镖状态
                self.one_person_dart = False
            # 释放大招状态
            elif type == 'ultimate_skill':
                self.Sound("sound/大招音效.wav")
                # 扣除角色1蓝量
                self.one_person_blue -= self.deduct_ultimate_skill_blue
                # 角色1大招释放状态
                self.one_person_ultimate_skill = False
        # 如果为角色2
        else:
            if type == 'attack':
                if self.two_person_collision_check() or self.one_person_collision_check():

                    if self.one_person_defense:
                        self.person_special.hit(1)
                        self.Sound("images/新角色/defense/hit.mp3")
                    else:
                        self.one_person_blood -= self.deduct_attack_blood
                        self.Sound("sound/击中音效.mp3")
                        if 100 * self.energy - (self.two_person_blue + self.deduct_attack_blue) >= 0:
                            # 蓝量小于100才会加蓝，目的防止蓝量溢出白色矩形边框
                            if self.two_person_blue < 100 * self.energy:
                                self.two_person_blue += self.deduct_attack_blue
                        else:
                            # 蓝量小于100才会加蓝，目的防止蓝量溢出白色矩形边框
                            if self.two_person_blue < 100 * self.energy:
                                self.two_person_blue += (self.two_person_blue + self.deduct_attack_blue) - 100 * self.energy
                        self.one_person_controlled = True
                self.two_person_attack = False
            elif type == 'dart':
                self.two_person_blue -= self.deduct_dart_blue
                self.two_person_dart = False
                # 释放大招状态
            elif type == 'ultkulou':
                self.Sound("sound/大招音效2.mp3")
                # 扣除角色2蓝量
                self.two_person_blue -= self.deduct_ultimate_skill_blue
                # 角色2大招释放状态
                self.two_person_ultimate_skill = False
    # 攻击方法
    def attack(self, attack_role):
        # 如果攻击的为
        if attack_role == 1:
            self.two_person_controlled = True
        if attack_role == 2:
            self.one_person_controlled = True
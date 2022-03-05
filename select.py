import sys

import pygame
import os
import time
import demo


array_of_img = []

class Choose():
    def __init__(self,screen,bgimg):
        self.screen = screen
        self.bgimg = bgimg
        self.width = 100
        self.height = 100
        self.picnum = 0
        self.player_one_role = False
        self.player_two_role = False
        self.player_one_call = False
        self.player_two_call = False
        self.picnum = 4 # 人物数量
        self.one_person_walk = 0
        self.two_person_walk = 0
        self.bgimg_select = []
        self.background_images = []
        self.attributebool = True
    def read_directory(self, array, directory_name, type = 1):
        # for filename in os.listdir(r"./" + directory_name):
        #     img = pygame.image.load(directory_name + "/" + filename)
        #     array.append(img)
        #     self.picnum += 1
        picnum = 0
        for i in os.listdir(r"./" + directory_name):
            picnum += 1
        if type == 1:
            for pic_num in range(1, picnum+1):
                img = pygame.image.load(directory_name + '/' + str(pic_num) + '-min.png')
                array.append(img)
        else:
            for pic_num in range(1, picnum+1):
                img = pygame.image.load(directory_name + '/' + str(pic_num) + '.png')
                array.append(img)

    def draw_choose(self,player,x,y):
        if player == 1:
            img = pygame.image.load('images/other/one_choose.png')
            self.screen.blit(img, (x-3, y-5))
            # pygame.draw.rect(self.screen,[255,0,0],[x,y,self.width,self.height],10)
        elif player == 2:
            img = pygame.image.load('images/other/two_choose.png')
            self.screen.blit(img, (x-3, y-5))
            # pygame.draw.rect(self.screen, [0, 0, 255], [x-10, y-10, self.width+20, self.height+20], 10)
        else:
            img = pygame.image.load('images/other/chooses.png')
            self.screen.blit(img, (x-3, y-5))
    def choose_role(self,player,line,x):

        line = int(line)
        x = int(x)
        role = {'1':{'1':'golem_1','2':'golem_2'},'2':{'1':'golem_3','2':'golem_4'}}
        self.read_directory(demo.Role.orange_img, 'images/新角色/orange',0)
        if player == 1:
            self.read_directory(demo.Role.one_person_dodge_img, 'images/新角色/dodge',0)
            self.read_directory(demo.Role.one_person_walk_img, 'images/新角色/' + role[str(line)][str(x)] + '/walk')
            self.read_directory(demo.Role.one_person_stand_img, 'images/新角色/' + role[str(line)][str(x)] + '/idle')
            self.read_directory(demo.Role.one_person_attack_img, 'images/新角色/' + role[str(line)][str(x)] + '/remote_attack')
            self.read_directory(demo.Role.one_person_hurt_img, 'images/新角色/' + role[str(line)][str(x)] + '/hurt')
            demo.Role.one_person_name = role[str(line)][str(x)]
            self.player_one_role = True
            self.ticks = time.time()
        else:
            self.read_directory(demo.Role.two_person_dodge_img, 'images/新角色/dodge', 0)
            self.read_directory(demo.Role.two_person_walk_img, 'images/新角色/' + role[str(line)][str(x)] + '/walk')
            self.read_directory(demo.Role.two_person_stand_img, 'images/新角色/' + role[str(line)][str(x)] + '/idle')
            self.read_directory(demo.Role.two_person_attack_img, 'images/新角色/' + role[str(line)][str(x)] + '/remote_attack')
            self.read_directory(demo.Role.two_person_hurt_img, 'images/新角色/' + role[str(line)][str(x)] + '/hurt')
            # for pic_num in range(1, 25):
            #     two_person_walk_img.append(pygame.image.load('images/新角色/' + role[str(line)][str(x)] + '/walk/' + str(pic_num) + '-min' + '.png'))
            # for pic_num in range(1, 19):
            #     two_person_stand_img.append(pygame.image.load('images/新角色/' + role[str(line)][str(x)] + '/idle/' + str(pic_num) + '-min' + '.png'))
            # # 将攻击图片载入列表
            # for pic_num in range(1, 8):
            #     two_person_attack_img.append(pygame.image.load('images/新角色/' + role[str(line)][str(x)] + '/slashing/' + str(pic_num) + '-min' + '.png'))
            # # 将受到伤害图片载入列表
            # for pic_num in range(1, 13):
            #     two_person_hurt_img.append(pygame.image.load('images/新角色/' + role[str(line)][str(x)] + '/hurt/' + str(pic_num) + '-min' + '.png'))
            demo.Role.two_person_name = role[str(line)][str(x)]
            self.player_two_role = True
            self.ticks = time.time()
    def draw(self):

        self.screen.fill([0,0,0])
        # 第一张图片x和y位置
        x = 852
        y = 712

        # x值每次固定的增加量
        add_x_value = 140
        # 一行允许出现的图片数量
        line = 2
        # y值每次固定的增加量
        add_y_value = 140

        one_choose_x = x
        one_choose_y = y
        two_choose_x = x + add_x_value
        two_choose_y = y
        if self.picnum % line == 0:
            x_num = line
        else:
            x_num = self.picnum % line
        # if self.picnum % line == 0:
        #     all_line = int(self.picnum / line)
        # else:
        all_line = 1

        while True:
            self.screen.fill((0, 0, 0))
            one_now_line = (one_choose_y - y) / add_y_value + 1
            one_now_x_num = (one_choose_x - x) / add_x_value + 1
            two_now_line = (two_choose_y - y) / add_y_value + 1
            two_now_x_num = (two_choose_x - x) / add_x_value + 1
            self.screen.blit(self.bgimg, (0, 0))

            for event in pygame.event.get():
                # 如果窗口操作类型为QUIT
                if event.type == pygame.QUIT:
                    # 执行关闭窗口操作
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        demo.starting_screen()
                        break
                    if self.player_one_role == False:
                        if event.key == pygame.K_d:
                            if one_choose_x + add_x_value < x + add_x_value * line:
                                if all_line == one_now_line:
                                    if one_now_x_num < x_num:
                                        one_choose_x += add_x_value
                                else:
                                    one_choose_x += add_x_value
                        elif event.key == pygame.K_a:
                            if one_choose_x != x:
                                one_choose_x -= add_x_value
                        elif event.key == pygame.K_s:
                            if one_choose_y + add_y_value < y + add_y_value * x_num:
                                if all_line - 1 == one_now_line:
                                    if one_now_x_num < x_num + 1:
                                        one_choose_y += add_y_value
                                else:
                                    one_choose_y += add_y_value
                        elif event.key == pygame.K_w:
                            if one_choose_y != y:
                                one_choose_y -= add_y_value
                        if event.key == pygame.K_j:
                            self.choose_role(1, one_now_line, one_now_x_num)
                    if self.player_two_role == False:
                        if event.key == pygame.K_RIGHT:
                            if two_choose_x + add_x_value < x + add_x_value * line:
                                if all_line == two_now_line:
                                    if two_now_x_num < x_num:
                                        two_choose_x += add_x_value
                                else:
                                    two_choose_x += add_x_value
                        elif event.key == pygame.K_LEFT:
                            if two_choose_x != x:
                                two_choose_x -= add_x_value
                        elif event.key == pygame.K_DOWN:
                            if two_choose_y + add_y_value < y + add_y_value * x_num:
                                if all_line - 1 == two_now_line:
                                    if two_now_x_num < x_num + 1:
                                        two_choose_y += add_y_value
                                else:
                                    two_choose_y += add_y_value
                        elif event.key == pygame.K_UP:
                            if two_choose_y != y:
                                two_choose_y -= add_y_value
                        if event.key == pygame.K_KP1:
                            self.choose_role(2, two_now_line, two_now_x_num)




            if self.player_one_role == True:
                if self.one_person_walk >= 24:
                    # 重置角色动作图片数量为0
                    self.one_person_walk = 0
                self.screen.blit(demo.Role.one_person_walk_img[self.one_person_walk], (350, 700))
                self.one_person_walk += 1
            if self.player_two_role == True:
                if self.two_person_walk >= 24:
                    # 重置角色动作图片数量为0
                    self.two_person_walk = 0
                image = pygame.transform.flip(demo.Role.two_person_walk_img[self.two_person_walk], True, False)
                self.screen.blit(image, (1395, 700))
                self.two_person_walk += 1
            if one_choose_x == two_choose_x and one_choose_y == two_choose_y:
                self.draw_choose(3, one_choose_x, one_choose_y)
            else:
                self.draw_choose(1,one_choose_x, one_choose_y)
                self.draw_choose(2,two_choose_x, two_choose_y)
            pygame.draw.rect(self.screen, [255, 0, 0], [380, 380, 3, 3], 5)
            if self.player_one_role == True and self.player_two_role == True:
                    self.call()
                    break
            pygame.display.update()
    def draw_call(self,player,call):
        if call == 1:
            x = 797
            y = 552
        elif call == 2:
            x = 797 + 117
            y = 552
        elif call == 3:
            x = 797 + 117 * 2
            y = 552
        if player == 1:
            img = pygame.image.load('images/other/one_choose.png')
            self.screen.blit(img, (x-3, y-5))
            # pygame.draw.rect(self.screen,[255,0,0],[x,y,self.width,self.height],10)
        elif player == 2:
            img = pygame.image.load('images/other/two_choose.png')
            self.screen.blit(img, (x-3, y-5))
            # pygame.draw.rect(self.screen, [0, 0, 255], [x-10, y-10, self.width+20, self.height+20], 10)
        else:
            img = pygame.image.load('images/other/chooses.png')
            self.screen.blit(img, (x-3, y-5))
    def choose_call(self,player,call):

        role = {'1':{'1':'human','2':'dragon','3':'rigidity'}}
        self.read_directory(demo.Role.orange_img, 'images/新角色/orange',0)
        if player == 1:
            demo.Role.one_person_call_role = role['1'][str(call)]
            self.player_one_call = True
            self.ticks = time.time()
        else:
            demo.Role.two_person_call_role = role['1'][str(call)]
            self.player_two_call = True
            self.ticks = time.time()
    def call(self):
        one_call = 1
        two_call = 1
        vs = 5
        vs_img = []
        for num in range(1, 7):
            img = pygame.image.load('images/other/vs' + str(num) + '.png')
            vs_img.append(img)
        while True:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.bgimg, (0, 0))

            for event in pygame.event.get():
                # 如果窗口操作类型为QUIT
                if event.type == pygame.QUIT:
                    # 执行关闭窗口操作
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        demo.starting_screen()
                        break
                    if self.player_one_call == False:
                        if event.key == pygame.K_d:
                            if one_call == 3:
                                one_call = 1
                            else:
                                one_call += 1
                        elif event.key == pygame.K_a:
                            if one_call == 1:
                                one_call = 3
                            else:
                                one_call -= 1
                        if event.key == pygame.K_j:
                            self.choose_call(1, one_call)
                    if self.player_two_call == False:
                        if event.key == pygame.K_RIGHT:
                            if two_call == 3:
                                two_call = 1
                            else:
                                two_call += 1
                        elif event.key == pygame.K_LEFT:
                            if two_call == 1:
                                two_call = 3
                            else:
                                two_call -= 1
                        if event.key == pygame.K_KP1:
                            self.choose_call(2, two_call)

            if self.one_person_walk >= 24:
                # 重置角色动作图片数量为0
                self.one_person_walk = 0
            self.screen.blit(demo.Role.one_person_walk_img[self.one_person_walk], (350, 700))
            self.one_person_walk += 1

            if self.two_person_walk >= 24:
                # 重置角色动作图片数量为0
                self.two_person_walk = 0
            image = pygame.transform.flip(demo.Role.two_person_walk_img[self.two_person_walk], True, False)
            self.screen.blit(image, (1395, 700))
            self.two_person_walk += 1

            if one_call == two_call:
                self.draw_call(3, one_call)
            else:
                self.draw_call(1, one_call)
                self.draw_call(2, two_call)
            pygame.draw.rect(self.screen, [255, 0, 0], [380, 380, 3, 3], 5)
            if self.player_one_call == True and self.player_two_call == True:

                if vs <= 0:
                    vs = 0
                self.screen.blit(vs_img[vs], (
                1920 // 2 - vs_img[vs].get_width() // 2 + 15, 1080 // 2 - vs_img[vs].get_height() // 2 - 100))
                vs -= 1
                if time.time() - self.ticks >= 1:
                    self.attribute()
                    break
            pygame.display.update()
    def draw_choose_attribute(self,type):
        img = pygame.image.load('images/other/checked.png')
        if type == 1:
            img = pygame.image.load('images/other/checked1.png')
            self.screen.blit(img, (1920 // 2 - img.get_width() // 2, 200))
        elif type == 2:
            self.screen.blit(img, (1920 // 2 - img.get_width() // 2, 460))
        elif type == 3:
            self.screen.blit(img, (1920 // 2 - img.get_width() // 2, 585))
        elif type == 4:
            self.screen.blit(img, (1920 // 2 - img.get_width() // 2, 710))
    def draw_attribute(self, num, time_type, life, energy):
        arrow_right = pygame.image.load('images/other/arrow.png')
        arrow_left = pygame.transform.flip(arrow_right, True, False)
        bgimg = pygame.image.load('images/other/bgbox2.png')
        time_font = pygame.font.Font('other/字魂4550号-芝麻体.TTF',60)
        life_font = pygame.font.Font('other/字魂4550号-芝麻体.TTF', 60)
        energy_font = pygame.font.Font('other/字魂4550号-芝麻体.TTF', 60)
        bg_text = pygame.font.Font('other/字魂4550号-芝麻体.TTF', 80)
        time_text = pygame.font.Font('other/字魂4550号-芝麻体.TTF',80)
        life_text = pygame.font.Font('other/字魂4550号-芝麻体.TTF', 80)
        energy_text = pygame.font.Font('other/字魂4550号-芝麻体.TTF', 80)

        # 背景框
        self.screen.blit(bgimg, (1920 // 2 - bgimg.get_width() // 2, 1080 // 2 - bgimg.get_height() // 2))

        self.screen.blit(bg_text.render('背景', True, (0, 0, 0)), (1920 // 2 - 470, 295))
        # 选择背景
        img = self.bgimg_select[num-1]
        self.screen.blit(img, (1920 // 2 - img.get_width() // 2, 250))
        self.screen.blit(arrow_right, (1920 // 2 - img.get_width() // 2 + 198 + 100, 292))
        self.screen.blit(arrow_left, (1920 // 2 - img.get_width() // 2 - 100, 292))

        # 选择时间
        self.screen.blit(time_text.render('时间', True, (0, 0, 0)), (1920 // 2 - 470, 478))
        if time_type == 1:
            font = time_font.render('60', True, (255, 0, 0))
            self.screen.blit(font, (1920 // 2 - 30, 490))
        elif time_type == 2:
            font = time_font.render('无限制', True, (255, 0, 0))
            self.screen.blit(font, (1920 // 2 - 90, 490))
        self.screen.blit(arrow_right, (1920 // 2 - img.get_width() // 2 + 198 + 100, 480))
        self.screen.blit(arrow_left, (1920 // 2 - img.get_width() // 2 - 100, 480))

        # 选择生命
        self.screen.blit(life_text.render('生命', True, (0, 0, 0)), (1920 // 2 - 470, 592))
        if life == 1:
            font = life_font.render('X 1', True, (255, 0, 0))
        elif life == 2:
            font = life_font.render('X 2', True, (255, 0, 0))
        elif life == 3:
            font = life_font.render('X 3', True, (255, 0, 0))
        self.screen.blit(font, (1920 // 2 - 50, 612))
        self.screen.blit(arrow_right, (1920 // 2 - img.get_width() // 2 + 198 + 100, 605))
        self.screen.blit(arrow_left, (1920 // 2 - img.get_width() // 2 - 100, 605))

        # 能量
        self.screen.blit(energy_text.render('能量', True, (0, 0, 0)), (1920 // 2 - 470, 717))
        if energy == 1:
            font = energy_font.render('X 1', True, (255, 0, 0))
        elif energy == 2:
            font = energy_font.render('X 2', True, (255, 0, 0))
        elif energy == 3:
            font = energy_font.render('X 3', True, (255, 0, 0))
        self.screen.blit(font, (1920 // 2 - 50, 737))
        self.screen.blit(arrow_right, (1920 // 2 - img.get_width() // 2 + 198 + 100, 730))
        self.screen.blit(arrow_left, (1920 // 2 - img.get_width() // 2 - 100, 730))

        tip_text = pygame.font.Font('other/字魂4550号-芝麻体.TTF', 40)
        font = tip_text.render('按Enter确定，按退格键重选角色', True, (255, 255, 255))
        self.screen.blit(font, (1920 // 2 - 300, 1020))
        # 按钮组
        self.draw_button(1, 1)
        self.draw_button(2, 1)
    def draw_button(self, type, select):
        if type == 1:
            if select == 1:
                surface = pygame.image.load('images/menu/determine3.png')
            else:
                surface = pygame.image.load('images/menu/determine4.png')
            self.screen.blit(surface, (1920 // 2 - surface.get_width() // 2 - 100, 930))
        elif type == 2:
            if select == 1:
                surface = pygame.image.load('images/menu/cancel3.png')
            else:
                surface = pygame.image.load('images/menu/cancel4.png')
            self.screen.blit(surface, (1920 // 2 - surface.get_width() // 2 + 100, 930))

    def attribute(self):
        self.read_directory(self.bgimg_select, 'images/选择背景')
        self.read_directory(self.background_images, 'images/背景')
        bgimg = pygame.image.load('images/other/bg.jpg')
        type = 1
        num = 1
        time_type = 1
        life = 1
        energy = 1


        while self.attributebool:
            self.screen.fill((0, 0, 0))
            self.screen.blit(bgimg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        demo.starting_screen()
                        break
                    elif event.key == pygame.K_a:
                        if type == 1:
                            if num == 1:
                                num = 3
                            elif num == 2:
                                num = 1
                            elif num == 3:
                                num = 2
                        elif type == 2:
                            if time_type == 1:
                                time_type = 2
                            elif time_type == 2:
                                time_type = 1
                        elif type == 3:
                            if life == 1:
                                life = 3
                            elif life == 2:
                                life = 1
                            elif life == 3:
                                life = 2
                        elif type == 4:
                            if energy == 1:
                                energy = 3
                            elif energy == 2:
                                energy = 1
                            elif energy == 3:
                                energy = 2
                    elif event.key == pygame.K_d:
                        if type == 1:
                            if num == 1:
                                num = 2
                            elif num == 2:
                                num = 3
                            elif num == 3:
                                num = 1
                        elif type == 2:
                            if time_type == 1:
                                time_type = 2
                            elif time_type == 2:
                                time_type = 1
                        elif type == 3:
                            if life == 1:
                                life = 2
                            elif life == 2:
                                life = 3
                            elif life == 3:
                                life = 1
                        elif type == 4:
                            if energy == 1:
                                energy = 2
                            elif energy == 2:
                                energy = 3
                            elif energy == 3:
                                energy = 1
                    elif event.key == pygame.K_s:
                        if type == 1:
                            type = 2
                        elif type == 2:
                            type = 3
                        elif type == 3:
                            type = 4
                        elif type == 4:
                            type = 1
                    elif event.key == pygame.K_w:
                        if type == 1:
                            type = 4
                        elif type == 2:
                            type = 1
                        elif type == 3:
                            type = 2
                        elif type == 4:
                            type = 3
                    elif event.key == pygame.K_RETURN:
                        demo.bg_location3 = self.background_images[num-1]
                        demo.Role.time_type = time_type
                        demo.Role.life = life
                        demo.Role.one_person_life = life
                        demo.Role.one_person_blood = life * 100
                        demo.Role.two_person_life = life
                        demo.Role.two_person_blood = life * 100
                        demo.Role.energy = energy
                        demo.Role.one_person_energy = energy
                        demo.Role.one_person_blue = energy * 100
                        demo.Role.two_person_energy = energy
                        demo.Role.two_person_blue = energy * 100
                        demo.Role.background_img_type = num
                        demo.player_one_jump = demo.hinder.Obstacles(1)
                        demo.player_two_jump = demo.hinder.Obstacles(2)
                        demo.main(True,False)
                        self.attributebool = False
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_one_role = False
                        self.player_two_role = False
                        self.player_one_call = False
                        self.player_two_call = False
                        self.draw()
                        self.attributebool = False
                        break
            self.draw_attribute(num,time_type,life,energy)
            self.draw_choose_attribute(type)
            pygame.display.update()







import pygame
import demo
import time

class Time():
    def __init__(self,screen):
        self.screen = screen
        self.one_img = pygame.image.load('images/时间/1.png')
        self.two_img = pygame.image.load('images/时间/2.png')
        self.three_img = pygame.image.load('images/时间/3.png')
        self.four_img = pygame.image.load('images/时间/4.png')
        self.five_img = pygame.image.load('images/时间/5.png')
        self.six_img = pygame.image.load('images/时间/6.png')
        self.seven_img = pygame.image.load('images/时间/7.png')
        self.eight_img = pygame.image.load('images/时间/8.png')
        self.nine_img = pygame.image.load('images/时间/9.png')
        self.zero_img = pygame.image.load('images/时间/0.png')
        self.time_img = pygame.image.load('images/时间/time.png')
        self.timeover_img = pygame.image.load('images/时间/timeover.png')
        self.time_arr = []
    def timeover(self):
        self.screen.blit(self.timeover_img, (1920 // 2 - self.timeover_img.get_width() // 2, 1080 // 2 - self.timeover_img.get_height() // 2))
    def draw(self):
        self.screen.blit(self.time_img,(1920 // 2 - self.time_img.get_width() // 2,50))
        if demo.Role.time_type == 1:
            numlist = list(str(demo.Role.time))
            if demo.Role.time == 0:
                    numlist = ['0','0']
            elif demo.Role.time < 10:
                numlist.insert(0, '0')
                if demo.Role.time < 0:
                    # 游戏暂停
                    demo.main(False, True)
            i = 0
            for num in numlist:
                if num == '0':
                    self.screen.blit(self.zero_img, (1920 // 2 - self.zero_img.get_width() // 2 - 15 + i, 100))
                if num == '1':
                    self.screen.blit(self.one_img, (1920 // 2 - self.one_img.get_width() // 2 - 15 + i, 100))
                if num == '2':
                    self.screen.blit(self.two_img, (1920 // 2 - self.two_img.get_width() // 2 - 15 + i, 100))
                if num == '3':
                    self.screen.blit(self.three_img, (1920 // 2 - self.three_img.get_width() // 2 - 15 + i, 100))
                if num == '4':
                    self.screen.blit(self.four_img, (1920 // 2 - self.four_img.get_width() // 2 - 15 + i, 100))
                if num == '5':
                    self.screen.blit(self.five_img, (1920 // 2 - self.five_img.get_width() // 2 - 15 + i, 100))
                if num == '6':
                    self.screen.blit(self.six_img, (1920 // 2 - self.six_img.get_width() // 2 - 15 + i, 100))
                if num == '7':
                    self.screen.blit(self.seven_img, (1920 // 2 - self.seven_img.get_width() // 2 - 15 + i, 100))
                if num == '8':
                    self.screen.blit(self.eight_img, (1920 // 2 - self.eight_img.get_width() // 2 - 15 + i, 100))
                if num == '9':
                    self.screen.blit(self.nine_img, (1920 // 2 - self.nine_img.get_width() // 2 - 15 + i, 100))
                i += 30
            now_time = pygame.time.get_ticks() // 1000
            if (now_time not in self.time_arr):
                self.time_arr.append(now_time)
                demo.Role.time -= 1
        else:
            font = pygame.font.Font('other/汉仪橄榄体简.TTF',25)
            self.screen.blit(font.render('无限制', True, (255, 255, 255)), (1920 // 2 - 40, 108))






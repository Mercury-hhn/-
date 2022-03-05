import pygame
import demo

reply_img = []
for pic_num in range(1, 13):
    reply_img.append(pygame.image.load('images/新角色/reply/' + str(pic_num) + '.png'))
release_img = []
for pic_num in range(1, 9):
    release_img.append(pygame.image.load('images/新角色/release/' + str(pic_num) + '.png'))
hit_img = []
for pic_num in range(0, 4):
    hit_img.append(pygame.image.load('images/新角色/hit/' + str(pic_num) + '.png'))
dodge_img = []
for pic_num in range(1, 6):
    dodge_img.append(pygame.image.load('images/新角色/dodge/' + str(pic_num) + '.png'))
class Special():
    def __init__(self, screen):
        self.screen = screen

        self.reply_num = 0
        self.reply_allnum = 12
        self.release_num = 0
        self.release_allnum = 8
        self.hit_num = 0
        self.hit_allnum = 4
        self.dodge_num = 0
        self.dodge_allnum = 4
    def reply(self , role):
        if role == 1:
            self.x = demo.Role.one_person_x
            self.y = demo.Role.one_person_y
        else:
            self.x = demo.Role.two_person_x
            self.y = demo.Role.two_person_y
        if self.reply_num >= self.reply_allnum:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
            self.reply_num = 0
        self.screen.blit(reply_img[self.reply_num], (self.x + 50 , self.y + 50))
        self.reply_num += 1
    def release(self , role):
        if role == 1:
            self.x = demo.Role.one_person_x
            self.y = demo.Role.one_person_y
        else:
            self.x = demo.Role.two_person_x
            self.y = demo.Role.two_person_y
        if self.release_num >= self.release_allnum:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
            self.release_num = 0
        self.screen.blit(release_img[self.release_num], (self.x , self.y + 100))
        self.release_num += 1
    def hit(self , role):
        if role == 1:
            self.x = demo.Role.one_person_x
            self.y = demo.Role.one_person_y
        else:
            self.x = demo.Role.two_person_x
            self.y = demo.Role.two_person_y
        if self.hit_num >= self.hit_allnum:  # 如果count大于6重置为0，目的防止下标越界，从而达到无限抖动翅膀的效果
            self.hit_num = 0
        self.screen.blit(hit_img[self.hit_num], (self.x + 50, self.y + 50))
        self.hit_num += 1
import pygame

width = 649
height = 466
speed = 20
deduct_orange_blood = 10
deduct_orange_white = 40
gas_img = []
FRAME_PER_SECONDS = 13
for pic_num in range(1, 14):
    gas_img.append(pygame.image.load('anger/golem_1/' + str(pic_num) + '.png'))
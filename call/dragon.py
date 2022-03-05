import pygame

width = 649
height = 466
speed = 20
deduct_ultimate_skill_blood = 1
deduct_ultimate_skill_blue = 50
call_img = []
FRAME_PER_SECONDS = 6
for pic_num in range(1, 7):
    call_img.append(pygame.image.load('call/dragon/' + str(pic_num) + '.png'))
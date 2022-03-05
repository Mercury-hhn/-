import pygame

width = 141
height = 208
speed = 30
deduct_ultimate_skill_blood = 1
deduct_ultimate_skill_blue = 50
call_img = []
FRAME_PER_SECONDS = 12
for pic_num in range(1, 13):
    call_img.append(pygame.image.load('call/rigidity/' + str(pic_num) + '.png'))
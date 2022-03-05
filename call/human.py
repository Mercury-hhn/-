import pygame

width = 436
height = 648
speed = 20
deduct_ultimate_skill_blood = 1
deduct_ultimate_skill_blue = 50
call_img = []
FRAME_PER_SECONDS = 9
for pic_num in range(1, 10):
    call_img.append(pygame.image.load('call/human/' + str(pic_num) + '.png'))
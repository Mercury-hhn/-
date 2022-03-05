import pygame

pygame.init()

font_addr = pygame.font.get_default_font()
font = pygame.font.Font(font_addr, 36)


# 创建一个菜单按钮的类
class Button(object):
    # 初始化
    def __init__(self, screen, text, select, display_width, display_height, x=None, y=None, **kwargs):
        self.screen = screen
        if text == 'Play':
            if select == 1:
                self.surface = pygame.image.load('images/menu/play1.png')
            else:
                self.surface = pygame.image.load('images/menu/play2.png')
        elif text == 'Doc':
            if select == 1:
                self.surface = pygame.image.load('images/menu/doc1.png')
            else:
                self.surface = pygame.image.load('images/menu/doc2.png')
        elif text == 'About':
            if select == 1:
                self.surface = pygame.image.load('images/menu/about1.png')
            else:
                self.surface = pygame.image.load('images/menu/about2.png')
        elif text == 'Continue':
            if select == 1:
                self.surface = pygame.image.load('images/menu/continue1.png')
            else:
                self.surface = pygame.image.load('images/menu/continue2.png')
        elif text == 'Menu':
            if select == 1:
                self.surface = pygame.image.load('images/menu/menu1.png')
            else:
                self.surface = pygame.image.load('images/menu/menu2.png')
        elif text == 'Exit':
            if select == 1:
                self.surface = pygame.image.load('images/menu/exit1.png')
            else:
                self.surface = pygame.image.load('images/menu/exit2.png')
        elif text == 'Volume':
            if select == 1:
                self.surface = pygame.image.load('images/menu/volume1.png')
            elif select == 2:
                self.surface = pygame.image.load('images/menu/volume3.png')
            elif select == 3:
                self.surface = pygame.image.load('images/menu/volume2.png')
            elif select == 4:
                self.surface = pygame.image.load('images/menu/volume4.png')
        # 获取窗口宽高
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        if text == 'Exit':
            self.x = display_width - 100
            self.y = display_height - 200
        elif text == 'Volume':
            self.x = display_width - 100
            self.y = display_height - 100

        else:
            if 'centered_x' in kwargs and kwargs['centered_x']:
                self.x = display_width // 2 - self.WIDTH // 2
            else:
                self.x = x

            if 'centered_y' in kwargs and kwargs['cenntered_y']:
                self.y = display_height // 2 - self.HEIGHT // 2
            else:
                self.y = y
    # 绘制方法
    def display(self):
        self.screen.blit(self.surface, (self.x, self.y))
    # 判断点击
    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False
    
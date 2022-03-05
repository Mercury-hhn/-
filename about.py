import pygame
import demo

class Team():
    def __init__(self,screen):
        self.screen = screen
        self.bg1_img = pygame.image.load('other/about/bg-1.png')
        self.bg2_img = pygame.image.load('other/about/bg-2.png')
        self.bg3_img = pygame.image.load('other/about/bg-3.png')
        self.team_img = pygame.image.load('other/about/team.png')
    def backgroundimg(self):
        self.screen.blit(self.bg2_img, (0, 0))
        self.screen.blit(self.bg1_img,(0, 1080 - self.bg1_img.get_height() - 120))
        self.screen.blit(self.bg3_img, (0, 1080 - self.bg3_img.get_height()))
        self.screen.blit(self.team_img, (1920 // 2 - self.team_img.get_width() // 2, 1080 // 2 - self.team_img.get_height() // 2))
    def main(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.backgroundimg()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        demo.starting_screen(True)
                        break
            pygame.display.update()



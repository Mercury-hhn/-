import pygame,sys
import demo

class Doc():
    def __init__(self,screen):
        self.screen = screen
        self.bgimg = 'other/doc/doc.png'
    def backgroundimg(self):
        bg = pygame.image.load(self.bgimg)
        self.screen.blit(bg,[0,0])
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
    def draw(self):
        self.backgroundimg()
        pygame.display.update()
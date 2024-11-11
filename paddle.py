import pygame

# define color
black = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        # call sprite constructor
        super().__init__()
        
        # set color, width and height of paddle
        # set background color and make it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
 
        # draw the paddle, rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # fetch rectangle with dimensions of image
        self.rect = self.image.get_rect()
        
    def Up(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
          
    def Down(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 400:
          self.rect.y = 400
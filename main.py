# pygame is required
import pygame
pygame.init()

# import paddle
from paddle import Paddle

# import ball
from ball import Ball

# define colors
black = (0, 0, 0)
white = (255, 255, 255)

# create pygame window
width = 700
height = 500
gamewindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# paddles
paddleA = Paddle(white, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(white, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# ball
ball = Ball(white,10,10)
ball.rect.x = 345
ball.rect.y = 195

# list of all sprites/paddles
allsprites = pygame.sprite.Group()

# add paddles to list
allsprites.add(paddleA)
allsprites.add(paddleB)

# add ball to list
allsprites.add(ball)

# determines when game ends
carryon = True

# clock for screen update speed
clock = pygame.time.Clock()

# for scoreboard, start scores
scoreA = 0
scoreB = 0

# for end screen
def end_(message):
    pygame.time.delay(200)
    gamewindow.fill(black)
    text = font.render(message, 1, white)
    gamewindow.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

# -------- main program loop -----------
while carryon:
    # main event look
    for event in pygame.event.get(): # user does something
        if event.type == pygame.QUIT: # if user click close
            carryon = False # so exit this loop
    
    # moving paddles with arrow keys
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_w]:
        paddleA.Up(5)
    if keys[pygame.K_s]:
        paddleA.Down(5)
    if keys[pygame.K_UP]:
        paddleB.Up(5)
    if keys[pygame.K_DOWN]:
        paddleB.Down(5)    

    # insert game logic here
    allsprites.update()

    # check if  ball is bouncing against any 4 walls
    # if on wall, add point for score
    if ball.rect.x>=690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 

    # if ball hit paddle
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
    
    # for background
    # clear screen to black
    gamewindow.fill(black)
    # draw the middle line/net
    pygame.draw.line(gamewindow, white, [349, 0], [349, 500], 5)

    # draw all sprites
    allsprites.draw(gamewindow)

    # dispay scores
    font = pygame.font.Font(None, 74)
    # for scoreA
    text = font.render(str(scoreA), 1, white)
    gamewindow.blit(text, (250, 10))
    # for scoreB
    text = font.render(str(scoreB), 1, white)
    gamewindow.blit(text, (420, 10))
    # update screen for new drawing
    pygame.display.flip()

    # display scores
    if scoreA == 5:
            end_("Winner: Left")
            pygame.quit
            break
    if scoreB == 5:
            end_("Winner: Right")
            pygame.quit
            break

    # frames per second
    clock.tick(60)
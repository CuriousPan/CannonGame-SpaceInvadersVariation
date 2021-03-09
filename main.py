import pygame
import sys
from CannonClass import *
from CannonballClass import *
from EnemyClass import *
import time

BLACK = (0, 0, 0)
GREEN = (26, 148, 49)
BRIGHT_GREEN = (89, 182, 91)
RED = (130, 0, 0)
BRIGHT_RED = (238, 0, 0)
YELLOW = (255, 255, 0)
BRIGHT_YELLOW = (255, 215, 0)
SIZE = WIDTH, HEIGHT = 720, 640
FPS = 60

clock = pygame.time.Clock()
pygame.init()

#display
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("All king's Vodka")

#sounds
wastedSound = pygame.mixer.Sound("WastedSound.mp3")
buttonSound = pygame.mixer.Sound("NewButtonClick.mp3")
bottleBreakSound = pygame.mixer.Sound("BottleBreak.mp3")
hitSound = pygame.mixer.Sound("HitSound.mp3")
wilhelmSound = pygame.mixer.Sound("Wilhelm.mp3")

def game_loop():
    wastedSound.stop()
    score = 0
    failsLeft = 3
    seconds = time.time()
    font = pygame.font.SysFont(None, 25)

    background = pygame.image.load("Background.png")
    heart = pygame.image.load("Heart.png")
    
    cannon = Cannon(360, 515) 
    pygame.mouse.set_visible(False)
    
    cannonballs = []
    enemies = []
    
    for i in range(8):
        enemies.append(Enemy())
    
    while True:
        cursor = pygame.mouse.get_pos()
        cursorList = [cursor[0], cursor[1]]
        if cursorList[1] >= 500:
            cursorList[1] = 500
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (time.time() - seconds >= 0.3):
                    x = cannon.rect.center[0]
                    y = cannon.rect.center[1]
                    tx = cursorList[0] 
                    ty = cursorList[1] 
                    cannonballs.append(Cannonball(x, y, tx, ty))
                    seconds = time.time()
                        
     
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            cannon.moveRight()
        if keys[pygame.K_a]:
            cannon.moveLeft()
        
        cannon.mouseRotation(cursorList)
        
        #i'm not sure that it's the correct way of doing coz Internet says it's quite ineffective
        pygame.display.update()
        screen.blit(background, (0, 0))
        
        #drawing and moving cannonballs
        for cannonball in cannonballs:
            cannonball.move()
            screen.blit(cannonball.cannonball_img_blit, cannonball.cannonball_rect)
            if cannonball.cannonball_rect.midtop[1] <= 0:
                cannonballs.remove(cannonball)
                bottleBreakSound.play()
            elif cannonball.cannonball_rect.midleft[0] <= 0 or cannonball.cannonball_rect.midright[0] >= WIDTH:
                cannonballs.remove(cannonball)
                bottleBreakSound.play()
  
        #drawing and moving enemies
        for enemy in enemies:
            enemy.move()
            screen.blit(enemy.image, enemy.rect)
            if enemy.rect.midbottom[1] >= 520:
                wilhelmSound.play()
                failsLeft -= 1
                enemies.remove(enemy)
        
        #collision
        for cannonball in cannonballs:
            for enemy in enemies:
                if cannonball.cannonball_rect.colliderect(enemy.rect):
                    hitSound.play()
                    cannonballs.remove(cannonball)
                    enemies.remove(enemy)
                    score += 1
                    if score % 4 == 0:
                        enemies.append(Enemy())
                    elif score % 2 == 0:
                        enemies.append(Enemy())
                        enemies.append(Enemy())
                    elif score % 3 == 0:
                        enemies.append(Enemy())
                        enemies.append(Enemy())
                    break       #not sure there, have to think
         
        #cannon and base 
        screen.blit(cannon.cannon_img_blit, cannon.rect)
        screen.blit(cannon.base_img, cannon.base)
        pygame.draw.circle(screen, (0, 0, 0), cannon.rect.center, 4)
        
        #crosshair
        pygame.draw.circle(screen, (178, 34, 34), cursorList, 2)
        pygame.draw.line(screen, (0, 0, 0), (cursorList[0] - 6, cursorList[1] - 1), (cursorList[0] - 19, cursorList[1] - 1), 2)
        pygame.draw.line(screen, (0, 0, 0), (cursorList[0] - 1, cursorList[1] - 6), (cursorList[0] - 1, cursorList[1] - 19), 2)
        pygame.draw.line(screen, (0, 0, 0), (cursorList[0] + 6, cursorList[1] - 1), (cursorList[0] + 19, cursorList[1] - 1), 2)
        pygame.draw.line(screen, (0, 0, 0), (cursorList[0] - 1, cursorList[1] + 6), (cursorList[0] - 1, cursorList[1] + 19), 2)
        
        #wheels
        screen.blit(cannon.wheel_img_blit, cannon.leftWheelRect)
        screen.blit(cannon.wheel_img_blit, cannon.rightWheelRect)
            
        if failsLeft <= 0:
            gameOver(score)
        
        #score displaying 
        scoreText = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(scoreText, (620, 610))
        
        
        #hearts
        for _heart in range(failsLeft):
            screen.blit(heart, (10 + 50*_heart, 25))
        
        pygame.display.flip()
        clock.tick(FPS)

def make_button(x, y, width, height, acolor, pcolor, action=None, text=None):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, acolor, rect)
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < cursor[0] < x + width and y < cursor[1] < y + height:
        pygame.draw.rect(screen, pcolor, rect)
        if click[0] and action != None:
            buttonSound.play()
            pygame.time.wait(50)
            action()
    
    if text != None:
        font = pygame.font.SysFont("Helvetica", 23)
        buttonText = font.render(text, True, (0, 0, 0))
        blitRect = buttonText.get_rect()
        blitRect.center = (x + width/2, y + height/2)
        screen.blit(buttonText, blitRect)


def end():
    pygame.quit()
    quit()

    
def intro():
    
    font = pygame.font.SysFont("Comic Sans MS", 62)
    nameText = font.render("All king's Vodka", True, (255, 255, 255))
    
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit(0)
        
        screen.fill(BLACK)
        screen.blit(nameText, (130, 200))
        make_button(140, 440, 100, 50, GREEN, BRIGHT_GREEN, game_loop, "Play")
        make_button(WIDTH-240, 440, 100, 50, RED, BRIGHT_RED, end, "Quit")
          
        clock.tick(FPS)
        pygame.display.flip()

def gameOver(score):
    wastedSound.play()
    pygame.mouse.set_visible(True)
    wasted_img = pygame.image.load("Wasted.png")
    screen.blit(wasted_img, wasted_img.get_rect(center = (WIDTH/2, HEIGHT/2)))
    font = pygame.font.SysFont("Comicaa Sans MS", 62)
    scoreText = font.render("Your score: " + str(score), True, (0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        
        make_button(140, 440, 100, 50, BRIGHT_YELLOW, YELLOW, game_loop, "Play again")
        make_button(WIDTH-240, 440, 100, 50, RED, BRIGHT_RED, end, "Quit")
        
        screen.blit(scoreText, scoreText.get_rect(center = (WIDTH/2, 200)))
        
        clock.tick(FPS)
        pygame.display.flip()
    
    
if __name__ == "__main__":
    intro()
    pygame.quit()
    exit(0)
    
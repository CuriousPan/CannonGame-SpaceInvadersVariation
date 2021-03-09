import pygame
import math


class Cannon():
    
    def __init__(self, x, y):
        self.currentAngle = 0
        self.speed = 6
        
        self.cannon_img = pygame.image.load("Cannon.png")
        self.base_img = pygame.image.load("Base.png")
        self.wheel_img = pygame.image.load("Wheel.png")
        
        self.wheel_img_blit = self.wheel_img
    
        self.cannon_img_blit = self.cannon_img
        self.rect = self.cannon_img.get_rect(center = (x, y))
        self.base = self.base_img.get_rect(center = (x , y + 35))
        
        self.leftWheelRect = self.wheel_img.get_rect(midleft=(self.base.midleft[0], self.base.midright[1] + 40))
        self.rightWheelRect = self.wheel_img.get_rect(midright=(self.base.midright[0], self.base.midright[1] + 40))
        
    def fire(self, mousePos):
        pass
        
    def mouseRotation(self, mousePos):
        x = mousePos[0] - self.rect.center[0]
        y = mousePos[1] - self.rect.center[1]
        angle = -math.degrees(math.atan2(y, x)) - 90
        
        cloc = self.rect.center
        self.cannon_img_blit = pygame.transform.rotozoom(self.cannon_img, angle, 1)
        self.rect = self.cannon_img_blit.get_rect(center = cloc)
        
    
    def moveRight(self):
        if self.base.x >= 720 - self.base.width - 45:
            self.rect.x = 720 - (self.rect.width/2 + self.base.width/2) - 45
            self.base.x = 720 - self.base.width - 45
            #seems work fine, but I guess it better to fix
            self.leftWheelRect = self.wheel_img.get_rect(midleft=(self.base.midleft[0], self.base.midright[1] + 40))
            self.rightWheelRect = self.wheel_img.get_rect(midright=(self.base.midright[0], self.base.midright[1] + 40))
        else:
            self.base.x += self.speed
            self.rect.x += self.speed
            self.leftWheelRect.x += self.speed
            self.rightWheelRect.x += self.speed
        
        self.currentAngle -= 6
        lcLoc = self.leftWheelRect.center
        rcLoc = self.rightWheelRect.center
        
        self.wheel_img_blit = pygame.transform.rotozoom(self.wheel_img, self.currentAngle, 1)
        
        self.leftWheelRect = self.wheel_img_blit.get_rect(center = lcLoc)
        self.rightWheelRect = self.wheel_img_blit.get_rect(center = rcLoc)
    
        
    def moveLeft(self):    
        if self.base.x <= 45:
            self.base.x = 45
            self.rect.x = 45 + (self.base.width/2 - self.rect.width/2)
            #seems work fine, but I guess it better to fix
            self.leftWheelRect = self.wheel_img.get_rect(midleft=(self.base.midleft[0], self.base.midright[1] + 40))
            self.rightWheelRect = self.wheel_img.get_rect(midright=(self.base.midright[0], self.base.midright[1] + 40))
        else:
            self.base.x -= self.speed
            self.rect.x -= self.speed
            self.leftWheelRect.x -= self.speed
            self.rightWheelRect.x -= self.speed
            
        self.currentAngle += 6
        lcLoc = self.leftWheelRect.center
        rcLoc = self.rightWheelRect.center
        
        self.wheel_img_blit = pygame.transform.rotozoom(self.wheel_img, self.currentAngle, 1)
        
        self.leftWheelRect = self.wheel_img_blit.get_rect(center = lcLoc)
        self.rightWheelRect = self.wheel_img_blit.get_rect(center = rcLoc)
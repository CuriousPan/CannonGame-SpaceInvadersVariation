import pygame
import math

class Cannonball():
    
    def __init__(self, x, y, targetX, targetY):
        self.speed = 15
        
        self.angle = math.atan2(targetY-y, targetX-x) 

        self.x = x
        self.y = y
        
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        
        self.cannonball_img = pygame.image.load("Vodka.png")
        self.cannonball_rect = self.cannonball_img.get_rect(center = (x, y))
        cloc = self.cannonball_rect.center
        
        self.cannonball_img_blit = pygame.transform.rotozoom(self.cannonball_img, abs(math.degrees(self.angle) - 270), 1)
        self.cannonball_rect = self.cannonball_img_blit.get_rect(center = (cloc))
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.cannonball_rect = self.cannonball_img_blit.get_rect(center = (int(self.x), int(self.y)))
import pygame
import random

WIDTH = 720
HEIGHT = 640

class Enemy():
    def __init__(self):
        
        self.speed = random.randint(2, 4) #6
        
        number = random.randint(1, 3) #3
        
        if number == 1:
            self.image = pygame.image.load("Trp.png")
        elif number == 2:
            self.image = pygame.image.load("Ptn.png")
        else:
            self.image = pygame.image.load("Kim.png")
        
        #it might be stupid there, but I don't know more efficient way yet.
        self.rect = self.image.get_rect() 
        position = (random.randrange(self.rect.width//2, WIDTH - self.rect.width//2), random.randrange(-800, -300))
        self.rect = self.image.get_rect(center = position)
        
        
    def move(self):
        self.rect.y += self.speed
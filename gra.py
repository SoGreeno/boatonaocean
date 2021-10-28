#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import time
screen = pygame.display.set_mode([100,100])
pygame.display.set_caption("boatonaocean")
ocean = pygame.image.load("ocean.png")
playerImg = pygame.image.load("lodz.png")

def player(x,y):
	screen.blit(playerImg, (x, y))
	
#loop
running = True
while running:

#wypełnij ocean
	screen.blit(ocean, [0,0])
	screen.blit(ocean, [50,0])
	screen.blit(ocean, [0,50])
	screen.blit(ocean, [50,50])
	
#zmienne
	playerX = 0
	playerY = 0
	x = 0
	y= 0
	


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	player(playerX,playerY)
	playerX += 0.1
	pygame.display.flip()


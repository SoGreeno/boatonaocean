#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import time
okno = pygame.display.set_mode([100,100])
pygame.display.set_caption("boatonaocean")
ocean = pygame.image.load("ocean.png")
lodz = pygame.image.load("lodz.png")
okno.blit(ocean, [0,0])
okno.blit(ocean, [50,0])
okno.blit(ocean, [0,50])
okno.blit(ocean, [50,50])
while True:
	pygame.display.flip()


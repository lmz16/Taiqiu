# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:12:12 2020

@author: Lenovo
"""
import pygame
import variable
import config

def update():
  
  variable.screen.blit(variable.background, (0, 0))
  for ball in variable.game.balls:
    pygame.draw.circle(variable.screen, ball.color, (int(ball.rect.x), int(ball.rect.y)), int(config.diameter/2), 0)
  pygame.display.update()
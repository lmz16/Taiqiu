# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:01:16 2020

@author: Lenovo
"""

import pygame
from sys import exit
import config
import display
import init
import variable

from pygame.locals import *

pygame.init()
variable.screen = init.screen_init()

background = pygame.image.load(config.qiuzhuo_path)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
            
  variable.screen.blit(background, (0, 0))
  pygame.display.update()
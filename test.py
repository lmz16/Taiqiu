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
import game

from pygame.locals import *

pygame.init()
variable.game = game.Game() 
variable.screen = init.screen_init()
variable.background = pygame.image.load(config.qiuzhuo_path)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
            
  display.update()
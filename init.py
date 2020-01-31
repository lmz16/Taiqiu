# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:19:12 2020

@author: Lenovo
"""

import pygame

from pygame.locals import *
from sys import exit
import variable
import game
import config

def screen_init():
  
  variable.screen = pygame.display.set_mode((config.main_window_width, config.main_window_height), 0, 32)
  pygame.display.set_caption("Tai Qiu")
  variable.background = pygame.image.load(config.qiuzhuo_path)
  
  
def game_init():
  
  variable.game = game.Game() 
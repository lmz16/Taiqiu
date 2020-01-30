# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:19:12 2020

@author: Lenovo
"""

import pygame

from pygame.locals import *
from sys import exit

import config

def screen_init():
  
  screen = pygame.display.set_mode((config.main_window_width, config.main_window_height), 0, 32)
  pygame.display.set_caption("Tai Qiu")
  
  return screen
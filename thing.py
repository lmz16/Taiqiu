# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:39:54 2020

@author: Lenovo
"""
import pygame
from pygame.locals import *
import config

class ball(pygame.sprite.Sprite):
  
  def __init__(self, color, diameter=config.diameter, center=None):
    
    pygame.sprite.Sprite.__init__(self)
    self.color = color
    self.rect = pygame.Rect([center[0] - diameter/2, center[1] - diameter/2, diameter, diameter])
    
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:39:54 2020

@author: Lenovo
"""
import pygame
from pygame.locals import *
import config
import numpy as np

class ball(pygame.sprite.Sprite):
  
  def __init__(self, color, diameter=config.diameter, center=None):
    
    pygame.sprite.Sprite.__init__(self)
    self.color = color
    self.rect = pygame.Rect([center[0] - diameter/2, center[1] - diameter/2, diameter, diameter])
    self.speed = [0, 0]
    self.direct = [0.707, 0.707]
    
    
  def move(self):
    
    if self.speed[0] == 0 and self.speed[1] == 0:
      return
    else:
      self.rect.x += self.speed[0]
      self.rect.y += self.speed[1]
    if config.is_friction:
      self.moderate()
      
  
  def moderate(self):
    
    self.speed[0] -= self.direct[0]*config.miu
    self.speed[1] -= self.direct[1]*config.miu
    if self.speed[0] * self.direct[0] < 0:
      self.speed[0] = 0
    if self.speed[1] * self.direct[1] < 0:
      self.speed[1] = 0
      
      
  def accelerate(self, given_speed):
    
    self.speed = given_speed
    speed_abs = np.sqrt(np.square(self.speed[0]) + np.square(self.speed[1]))
    self.direct = np.divide(self.speed, speed_abs)
    
  
  def set_loc(self, loc):
    
    self.rect.x = loc[0]
    self.rect.y = loc[1]
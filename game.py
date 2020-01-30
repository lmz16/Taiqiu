# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:01:46 2020

@author: Lenovo
"""
import thing
import config
import numpy
from pygame.locals import *

class Game:
  
  def __init__(self):
    
    self.balls = []
    for i in range(2):
      self.add_balls(color=config.colors[i])
    
  def add_balls(self, color, center=None):
    
    self.balls.append(thing.ball(color=color, center=[numpy.random.randint(65, 1535), numpy.random.randint(65, 735)]))
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:01:46 2020

@author: Lenovo
"""
import thing
import config
import numpy as np
from pygame.locals import *

class Game:
  
  def __init__(self):
    
    self.balls = []
    for i in range(2):
      self.add_balls(color=config.colors[i])
    for ball in self.balls:
      ball.accelerate([np.random.randint(50), np.random.randint(50)])
      
    
  def add_balls(self, color, center=None):
    
    if center:
      self.balls.append(thing.ball(color=color, center=center))
    else:
      self.balls.append(thing.ball(color=color, center=[np.random.randint(65, 1535), np.random.randint(65, 735)]))
      
  
  def update(self):
    
    for ball in self.balls:
      ball.accelerate(np.multiply(ball.speed, Game.wall_collide(ball)))
      ball.move()
      
      
  def refresh(self):
    
    for ball in self.balls:
      ball.accelerate([np.random.randint(50), np.random.randint(50)])
      ball.set_loc([np.random.randint(65, 1535), np.random.randint(65, 735)])
      
  
  def wall_collide(ball):
    
    collide = [1, 1]
    if (ball.rect.x < config.left_edge and ball.speed[0] < 0) or \
    (ball.rect.x > config.right_edge - config.diameter and ball.speed[0] > 0):
      collide[0] = -1
    if (ball.rect.y < config.up_edge and ball.speed[1] < 0) or \
    (ball.rect.y > config.down_edge - config.diameter and ball.speed[1] > 0):
      collide[1] = -1
    return collide
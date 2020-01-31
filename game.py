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
    for i in range(8):
      self.add_balls(color=config.colors[0])
    for ball in self.balls:
      ball.accelerate([np.random.randint(5), np.random.randint(5)])
      
    
  def add_balls(self, color, center=None):
    
    if center:
      self.balls.append(thing.ball(color=color, center=center))
    else:
      self.balls.append(thing.ball(color=color, center=[np.random.randint(65, 1535), np.random.randint(65, 735)]))
      
  
  def update(self):
    
    for i in range(config.accelerate):
      move_ball_index = [j for j in range(len(self.balls)) if np.linalg.norm(self.balls[j].speed) > 0]
      all_index = [j for j in range(len(self.balls))]
      for j in move_ball_index:
        all_index.remove(j)
        for k in all_index:
          if Game.ball_collide(self.balls[j], self.balls[k]):
            Game.ball_collide_process(self.balls[j], self.balls[k])

      for ball in self.balls:
        ball.accelerate(np.multiply(ball.speed, Game.wall_collide(ball)))
        ball.move()
      
      
  def refresh(self):
    
    for ball in self.balls:
      #ball.accelerate([np.random.randint(50), np.random.randint(50)])
      ball.accelerate([np.random.randint(5), np.random.randint(5)])
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
  
  
  def ball_collide(ball1, ball2):
    
    center1 = np.array([ball1.rect.x + config.diameter / 2, ball1.rect.y + config.diameter / 2])
    center2 = np.array([ball2.rect.x + config.diameter / 2, ball2.rect.y + config.diameter / 2])
    link = center1 - center2
    if np.linalg.norm(link) < config.diameter:
      return np.sum(np.multiply(link, ball1.speed)) < np.sum(np.multiply(link, ball2.speed))
    return False
  
  
  def ball_collide_process(ball1, ball2):
    
    link = np.array([ball1.rect.x - ball2.rect.x, ball1.rect.y - ball2.rect.y])
    x = (link[0] * ball2.speed[0] + link[1] * ball2.speed[1] - link[0] * ball1.speed[0] - link[1] * ball1.speed[1]) \
    / (2 * np.sum(np.square(link)))
    ball1.accelerate([ball1.speed[0] + x * link[0], ball1.speed[1] + x * link[1]])
    ball2.accelerate([ball2.speed[0] - x * link[0], ball2.speed[1] - x * link[1]])
    
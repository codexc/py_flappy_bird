#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from gameobjects.vector2 import Vector2
import os
import sys

class Game(object):
	#init resource
	def __init__(self):
		#pic resource
		bg_img = r'background.png'
		bird_img = r'bird1.png'
		field_img = r'field.png'
		pipe1_img = r'pipe1.png'
		pipe2_img = r'pipe2.png'
		
		#size of the game window
		screen_size = (240,460)

		#init pygame
		pygame.init()
		
		#init score and time
		self.score = 0
		self.total_time = 0
		
		#init game screen
		self.screen = pygame.display.set_mode(screen_size, 0, 32)
		pygame.display.set_caption('flappy bird')
		
		#init game background
		self.background = self.__load_img(bg_img)
		self.screen.blit(self.background,(0,0))
		
		#init game clock
		self.clock = pygame.time.Clock()
		
		#init game object
		self.bird = Bird(self.__load_img(bird_img))
		self.field = Field(self.__load_img(field_img))
		self.pipes = []
		self.pipes.append(Pipe(self.__load_img(pipe1_img), Vector2(200, -140), 1))
		self.pipes.append(Pipe(self.__load_img(pipe2_img), Vector2(200, 260), 2))
		self.pipes.append(Pipe(self.__load_img(pipe1_img), Vector2(60, -140), 1))
		self.pipes.append(Pipe(self.__load_img(pipe2_img), Vector2(60, 260), 2))
		pygame.display.flip()
		
		
	#game main method
	def main(self):
		pass
		
	def __load_img(self,img):
		img_path = os.path.join('data','image',img)
		try:
			img_resource = pygame.image.load(img_path)
		except pygame.error,message:
			print ('cant load img: ' + img,message)
			sys.exit()
		img_resource = img_resource.convert_alpha()
		return img_resource
			
	
		
class Bird(pygame.sprite.Sprite):
	def __init__(self,img):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.topleft = Vector2(120.0,180.0)
		self.direction = 0
		self.speed = 400
		#zhong li jia su du
		self.gravity = 3.5
		self.alive = True
	def update(self, time_passed_seconds):
			if self.alive:
				self.rect.top += self.direction * self.speed * time_passed_seconds + self.gravity
		
		

class Field(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = Vector2(0, 380)
    def update(self,cls):
        pass
		
class Pipe(pygame.sprite.Sprite):
    def __init__(self, img, position, num):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 120
        self.pipe_mid = 440
        self.direction = Vector2(-1, 0)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.number = num
    def update(self, time_passed_seconds, pipe_down):
        pipe_move = self.direction * self.speed * time_passed_seconds
        self.rect = self.rect.move(pipe_move)
        if self.rect.left < -40:
            self.rect.left = 240
            temp = self.rect.top + pipe_down
            if self.number is 1:
                if temp < -110 or temp > -170:
                    self.rect.top = -140 + pipe_down
                else:
                    self.rect.top = -140
            if self.number is 2:
                if temp > 230 or temp < 290:
                    self.rect.top = 260 + pipe_down
                else:
                    self.rect.top = 260


play = Game()


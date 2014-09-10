#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from gameobjects.vector2 import Vector2
import os
import sys
import random

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
		self.font = pygame.font.SysFont("arial", 16)
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
		
		#pygame.sprite.RenderPlain()：RenderPlain类型是Sprite的容器，对RenderPlain的操作，就是对内部所有Sprite的操作
		self.pipes_group = pygame.sprite.RenderPlain(*self.pipes)
		self.objs_group = pygame.sprite.RenderPlain(self.bird, *self.pipes)
	
	
	#game main method
	def main(self):
		#the main loop
		while True:
			#clock.tick(20)实现延时，为图像帧数
			self.clock.tick(40)
			self.screen.blit(self.background, (0,0))
			#capture user event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			user_pressed = pygame.key.get_pressed()
			self.bird.direction = 0
			if user_pressed[pygame.K_UP]:
				self.bird.direction = -1
			time_passed = self.clock.get_time()
			time_passed_seconds = time_passed/1000.0				
			self.total_time += time_passed
			
			#game over if bird touches the field
			if pygame.sprite.collide_rect(self.bird, self.field) == True:
				self.bird.alive = False
			#game over if bird touches the pipe
			for i in xrange(4):
				if pygame.sprite.collide_rect(self.bird, self.pipes[i]) == True:
					self.bird.alive = False
					
			#update
			self.bird.update(time_passed_seconds)
			self.pipes_group.update(time_passed_seconds, random.randint(-50, 50))
			self.objs_group.draw(self.screen)
			self.screen.blit(self.field.image, self.field.rect)
			if self.bird.alive:
				self.score = self.total_time/1000
				score_surface = self.font.render("Score:"+str(self.score), True, (0,0,0))
				self.screen.blit(score_surface,(90, 400))
			else:
				sys.exit()
			pygame.display.flip()
			
			
			
			
			
			
			
		
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
play.main()


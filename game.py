#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import os
import sys

class Game(object):
	#pic resource
	bg_img = r'background.png'
	bird_img = r'bird1.png'
	field_img = r'field.png'
	pipe1_img = r'pipe1.png'
	pipe2_img = r'pipe2.png'
	
	#size of the game window
	screen_size = (240,460)
	
	#game score
	score = 0
	
	#init resource
	def __init__(self):
		pass
		
		
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
		pass
		

class Field(pygame.sprite.Sprite):
	def __init__(self):
		pass
		
class Pipe(pygame.sprite.Sprite):
	def __init__(self):
		pass


play = Game()


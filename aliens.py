import random
import pygame

class alien:
	def __init__(self,time):
		self.atime=time
		self.x_coor=random.randint(0,7)*100
		self.health=10
		self.sprite=pygame.image.load('./alien.png')
		self.y_coor=random.randint(0,1)*100
		self.flag=0
		self.stun=0
		self.pf=1
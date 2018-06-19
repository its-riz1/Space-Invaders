import pygame

class missile:
	def __init__(self,x,y,time):
		self.x=x
		self.y=y
		self.time=time

class damage_m:
	def __init__(self,x,y,time):
		missile.__init__(self,x,y,time)
		self.firepower=10
		self.sprite=pygame.image.load('./dmis.png')
		self.sprite=pygame.transform.scale(self.sprite,(100,100))
		def is_collided_with(self,sprite):
			return self.rect.colliderect(sprite.rect)

class slow_m:
	def __init__(self,x,y,time):
		missile.__init__(self,x,y,time)
		self.firepower=0
		self.sprite=pygame.image.load('./smis.png')
		self.sprite=pygame.transform.scale(self.sprite,(100,100))
		def is_collided_with(self,sprite):
			return self.rect.colliderect(sprite.rect)
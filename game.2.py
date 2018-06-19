import pygame
import time
import aliens
import missiles
import spaceship

pygame.init()
pygame.font.init()
DISPLAY=pygame.display.set_mode((800,900))
DISPLAY.fill([0,0,0])
pygame.mouse.set_visible(0)

DISPLAY.blit(pygame.image.load('./spaceship.jpeg'),(400,700))
sship=spaceship.spaceship()
def game_main():
	mind=True
	aliens_ingame=[]
	missiles_fired=[]
	state=0
	score=0
	start_t=round(time.time())
	clock=pygame.time.Clock()
	while mind:
		DISPLAY.blit(pygame.image.load('./spaceship.jpeg'),(sship.x_coor,700))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				mind=False
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_d and sship.x_coor<=600:
					sship.x_coor+=100
				if event.key==pygame.K_a and sship.x_coor>=100:
					sship.x_coor-=100
				if event.key==pygame.K_s:
					x=sship.x_coor
					y=600
					m=missiles.damage_m(x,y,time.time())
					missiles_fired.append(m)
				if event.key==pygame.K_SPACE:
				 	x=sship.x_coor
				 	y=600
				 	m=missiles.slow_m(x,y,time.time())
				 	missiles_fired.append(m)
				if event.key==pygame.K_q:
					mind=False
		DISPLAY.fill([0,0,0])

		cur_t=round(time.time())-start_t
		if cur_t%10==0 and state==0:
			a=aliens.alien(cur_t)
			DISPLAY.blit(pygame.image.load('./spaceship.jpeg'),(sship.x_coor,700))
			state=1
			if a not in aliens_ingame:
				aliens_ingame.append(a)
				DISPLAY.blit(pygame.image.load('./spaceship.jpeg'),(sship.x_coor,700))
			text=str("Score: ")+str(score)
			font_here = pygame.font.SysFont('Calibri', 50)
			text_v = font_here.render(text,False, (255,255,255))
			DISPLAY.blit(text_v,(300,800))
		else:
			DISPLAY.blit(pygame.image.load('./spaceship.jpeg'),(sship.x_coor,700))
			text=str("Score: ")+str(score)
			font_here = pygame.font.SysFont('Calibri', 50)
			text_v = font_here.render(text,False, (255,255,255))
			DISPLAY.blit(text_v,(300,800))
		if cur_t%10==9:
			state=0
		for a in aliens_ingame:
			DISPLAY.blit(pygame.image.load('./spaceship.jpeg'),(sship.x_coor,700))
			DISPLAY.blit(a.sprite,(a.x_coor,a.y_coor))
		vella_time=time.time()

		for m in missiles_fired:
			DISPLAY.blit(m.sprite,(m.x,m.y))
			if time.time()-m.time <=10:
				if m.__class__== missiles.damage_m:
					m.y-=.35
					for a in aliens_ingame:
						if round(m.y) in range(a.y_coor-1,a.y_coor+50) and m.x==a.x_coor:
							aliens_ingame.remove(a)
							score+=1
							# print(score)
							missiles_fired.remove(m)
							DISPLAY.fill([0,0,0])
							for x in aliens_ingame:
								DISPLAY.blit(x.sprite,(x.x_coor,x.y_coor))
				elif m.__class__== missiles.slow_m:
					m.y-=.7
					for a in aliens_ingame:
						if round(m.y) in range(a.y_coor-1,a.y_coor+50) and m.x==a.x_coor:
							a.atime+=5
							a.sprite=pygame.image.load('./all.png')
							for x in aliens_ingame:
								DISPLAY.blit(x.sprite,(x.x_coor,x.y_coor))
							missiles_fired.remove(m)
			else:
				missiles_fired.remove(m)

		pygame.display.update()
		for a in aliens_ingame:
			if a.health==10 and cur_t-a.atime==8 and a.flag==0:
				aliens_ingame.remove(a)
				a.flag=1
				# print(a.flag,cur_t)	

		text=str("Score: ")+str(score)
		font_here = pygame.font.SysFont('Calibri', 50)
		text_v = font_here.render(text,False, (255,255,255))
		DISPLAY.blit(text_v,(300,800))

		DISPLAY.blit(pygame.image.load('./spaceship.jpeg'),(sship.x_coor,700))
		pygame.display.update()
	clock.tick(60)
game_main()
pygame.quit()	
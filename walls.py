import pygame
class Wall(object):
	def __init__(self, pos):
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

def build_level():		
	global walls
	walls = [] #holds walls
	level = [
		"WWWWWWWWWWWWWWWWWWWW",
		"W                  W",
		"W                  W",
		"W   WWWW       WWW W",
		"W   W              W",
		"W WWW     W        W",
		"W   W   WWW W      W",
		"W   W     W   WWW WW",
		"W   WW    W   W W  W",
		"W         W   W W  W",
		"WWW       WWWWW W  W",
		"W     WW           W",
		"W                  W",
		"W          WW      W",
		"WWWWWWWWWWWWWWWWWWWW",
		]
		
	x = y = 0
	for row in level:
		for col in row:
			if col == "W":
				Wall((x,y))
			x += 32
		y += 32
		x = 0
	return walls
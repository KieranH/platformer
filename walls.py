import pygame
class Wall(object):
	def __init__(self, pos):
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

class Exit(object):
	def __init__(self, pos):
		exit_rect.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

def build_level():		
	global walls
	global exit_rect
	walls = [] #holds walls
	exit_rect = []
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
		"W         WE  W W  W",
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
			if col == "E":
				Exit((x,y))
			x += 32
		y += 32
		x = 0
	print exit_rect
	return walls, exit_rect
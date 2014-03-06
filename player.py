import pygame
import math
import walls
import os
class Character(pygame.sprite.Sprite):
	def __init__(self, (pos), clock):
		pygame.sprite.Sprite.__init__(self)
		self.still = load_png("guy.png")
		self.walk1 = load_png("guy2.png")
		self.walk2 = load_png("guy3.png")
		self.sprite = self.still
		self.clock = pygame.time.Clock()
		self.actual_clock = clock
		self.rect = self.sprite.get_rect()
		self.speed = 30
		self.pos = pos
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.wall_data = walls.build_level()
		self.on_ground = False
		self.dy = self.dx = 0
		self.frame_rate = 60
		
	def update(self, up, left, right):
		if self.actual_clock.get_fps() != 0:
			self.frame_rate = self.actual_clock.get_fps()
		if up:
			#if on ground, jump
			self.jump()
		if left:
			#Move left
			self.dx = (-300 * (1/self.frame_rate))
		if right:
			#Move right
			self.dx = (300 * (1/self.frame_rate))
		if not (left or right):
			self.dx = 0
			self.sprite = self.still
			
		self.gravity()
		
		#Move in x
		self.rect.x += self.dx
		self.collision(self.dx, 0)
		#Move in y
		self.rect.y += self.dy
		#we're (probably) in the air
		self.on_ground = False
		self.collision(0, self.dy)
		pygame.event.pump()
		
	def jump(self):
		if self.on_ground:
			self.dy = -10
			self.on_ground = False
			
	def gravity(self):
		if not self.on_ground:
			if self.dy == 0:
				self.dy = 1
			else:
				self.dy += 0.35
		self.collision(0, self.dy)
			
		
	def change_sprite(self):
		if self.sprite == self.walk1:
			self.sprite = self.walk2
		else:
			self.sprite = self.walk1
	
	def collision(self, dx, dy):
		for wall in self.wall_data:
			if self.rect.colliderect(wall.rect):
				if dx > 0: self.rect.right = wall.rect.left
				if dx < 0: self.rect.left = wall.rect.right
				if dy < 0:
					self.rect.top = wall.rect.bottom
					self.dy = 0
				if dy > 0:
					self.rect.bottom = wall.rect.top
					self.on_ground = True
					self.dy = 0
		
def load_png(filename):
	file = os.path.join('resources', filename)
	image = pygame.image.load(file)
	if image.get_alpha():
		image.convert_alpha()
	else:
		image.convert()
	return image
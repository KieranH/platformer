import pygame
import player
from player import *
import menu
from menu import *
import walls
import sys

#25x20 blocks
DISPLAY = (800, 640)
DEPTH = 32
FLAGS = 0

def main():
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	screen.fill((255,255,255))
	
	clock = pygame.time.Clock()
	
	#Init Objects
	guy = Character([32,32], clock)
	playersprite = pygame.sprite.RenderPlain(guy)
	
	#level data
	wall_data, exit_location = walls.build_level()
	level = 0
	up = left = right = change_sprite = timer_running = False
	menu = Menu(DISPLAY, DEPTH, FLAGS, screen, clock)
	menu.menu()
	while True:
		#limit framerate to 60fps
		clock.tick(60)
		pygame.display.set_caption("Testing FPS = %.2f" % (clock.get_fps()))
		
		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_UP or event.key == pygame.K_SPACE: #Alex made me add space to jump....
					up = True
				if event.key == pygame.K_LEFT:
					left = True
				if event.key == pygame.K_RIGHT:
					right = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_SPACE: #I forgot to check for space key up, kept jumping forever
					up = False
				if event.key == pygame.K_LEFT:
					left = False
				if event.key == pygame.K_RIGHT:
					right = False
			if event.type == (pygame.USEREVENT + 1):
				change_sprite = True
			if event.type == (pygame.USEREVENT + 2):
				level += 1
				wall_data, exit_location = walls.build_level(level)
				guy = Character([32,32], clock, level)
				
		if (left or right) and not timer_running:
			pygame.time.set_timer(pygame.USEREVENT + 1, 100)
			timer_running = True
		if (left or right) and change_sprite:
			guy.change_sprite()
			change_sprite = False
			timer_running = False
		#Update Screen
		#img_test = load_png("guy.png")
		screen.fill((255,255,255))
		for wall in wall_data:
			pygame.draw.rect(screen, (0,0,0), wall.rect)
		
		#draw the exit
		pygame.draw.rect(screen, (255,0,0), exit_location[0].rect)
		guy.update(up, left, right)
		screen.blit(guy.sprite, guy.rect)
		#print guy.rect
		pygame.display.flip()

if __name__ == "__main__": main()
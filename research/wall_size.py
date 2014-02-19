import pygame

#Define display mode constants
DISPLAY = (800, 600)
DEPTH = 32
FLAGS = 0

def main():
	#setup the screen (right size, filled white)
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	screen.fill((255,255,255))
	clock = pygame.time.Clock()
	
	rect0 = pygame.Rect(32, 32, 16, 16)
	rect1 = pygame.Rect(80, 32, 32, 32)
	rect2 = pygame.Rect(144, 32, 64, 64)
	rect3 = pygame.Rect(272, 32, 128, 128)
	
	
	while True:
		#Limit to 60 FPS (static images, shouldn't matter too much)
		clock.tick(60)
		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		screen.fill((255,255,255))
		pygame.draw.rect(screen, (0,0,0), rect0)
		pygame.draw.rect(screen, (0,0,0), rect1)
		pygame.draw.rect(screen, (0,0,0), rect2)
		pygame.draw.rect(screen, (0,0,0), rect3)
		pygame.display.flip()

if __name__ == "__main__": main()
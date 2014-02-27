import pygame
import sys

#keep this the same size as the game will be, 25x20 blocks
DISPLAY = (800, 640)
DEPTH = 32
FLAGS = 0

pygame.init()

#define font that will be used throughout the game
#print pygame.font.get_fonts()
font = pygame.font.SysFont("arial", 20)
print font
text = [["Play", [(0,0,0), (100,100)], [None, None]], ["Instructions", [(0,0,0), (100,200)], [None, None]]]

def render_text(text, colour):
	return font.render(text, 0, colour)
	
for item in text:
	item[2][0] = render_text(item[0], item[1][0])
	item[2][1] = render_text(item[0], (255, 0, 0))

def menu():
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	screen.fill((255,255,255))
	
	clock = pygame.time.Clock()
	
	while True:
		#limit framerate to 60fps
		clock.tick(1000000000)
		pygame.display.set_caption("MENU TEST - FPS = %.2f" % (clock.get_fps()))
		
		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
					sys.exit()
		for item in text:
			screen.blit(item[2][0], item[1][1])
	
		pygame.display.flip()
		
if __name__ == "__main__": menu()
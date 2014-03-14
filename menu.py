import pygame
import sys

class Menu:

	def __init__(self, DISPLAY, DEPTH, FLAGS, screen, clock):
		"""Setup Menu class"""
		self.DISPLAY = DISPLAY
		self.DEPTH = DEPTH
		self.FLAGS = FLAGS
		self.screen = screen
		#will be used for an array
		self.current_position = 0
		self.clock = clock
		self.font = pygame.font.SysFont("arial", 20)
		
		#setup array to hold text data
		self.text = [["Play", [(0,0,0), (50,300)], [None, None]], ["Instructions", [(0,0,0), (50,325)], [None, None]]]
		#fill the screen white
		self.screen.fill((255,255,255))
		self.render_all_text()

	def render_text(self, text, colour):
		"""Gives me a nice way to render text"""
		return self.font.render(text, 0, colour)

	def render_all_text(self):
		for item in self.text:
			item[2][0] = self.render_text(item[0], item[1][0])
			item[2][1] = self.render_text(">"+item[0]+"<", (255, 0, 0))

	def move_pos(self, num, list):
		"""This will allow the user to select something in the menu and let them scroll through the items available"""
		if self.current_position + num < len(list) and self.current_position + num >= 0:
			self.current_position = self.current_position + num
		elif self.current_position + num == len(list):
			self.current_position = 0
		else: self.current_position = len(list) - 1
	
	def next_event(self, pos):
		"""This function determines what will happen next based on what's currently selected in the menu"""
		if pos == 0:
			#main()
			self.running = False
		elif pos == 1:
			print "instructions"
		else:
			sys.exit()

	def menu(self):
		"""We only want stuff relevant to only the running of the menu here"""
		self.running = True
		while self.running:
			#limit framerate to 60fps
			self.clock.tick(60)
			#set title
			pygame.display.set_caption("MENU TEST - FPS = %.2f" % (self.clock.get_fps()))
			
			#Events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					#exit cleanly
					sys.exit()
				if event.type == pygame.KEYDOWN:
					#Handle keyboard inputs
					if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
						sys.exit()
					if event.key == pygame.K_UP:
						self.move_pos(-1, self.text)
					if event.key == pygame.K_DOWN:
						self.move_pos(1, self.text)
					if event.key == pygame.K_RETURN:
						self.next_event(self.current_position)
			for item in self.text:
				#if the current item is the same as the user selected one, draw it in a different colour
				if item == self.text[self.current_position]:
					self.screen.blit(item[2][1], item[1][1])
				else:
					self.screen.blit(item[2][0], item[1][1])
		
			#draw changes to the screen
			pygame.display.flip()
			#fill in the screen so we can write text over it again
			self.screen.fill((255,255,255))
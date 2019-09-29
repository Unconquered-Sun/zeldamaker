import sys
import pygame
import pymunk
import pymunk.pygame_util
from pygame_functions import *
from player import Player


class ZeldaGame:

	def __init__(self):
		pygame.init()

		self.size = width, height = [1024,567]
		# self.screen = pygame.display.set_mode(self.size)
		self.screen = screenSize(width,height)
		self.clock = pygame.time.Clock()

		self.player = Player("Sprites/links.gif",32)

		running = True

		self.space = pymunk.Space()

		moveUp = False
		moveDown = False
		moveRight = False
		moveLeft = False

		while running:
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit(0)

				elif event.type == pygame.KEYDOWN:
					print("DOWN",event.key)
					if event.key == pygame.K_ESCAPE:
						sys.exit(0)
					elif event.key == pygame.K_d:
						moveRight = True
					elif event.key == pygame.K_a:
						moveLeft = True
					elif event.key == pygame.K_w:
						moveUp = True
					elif event.key == pygame.K_s:
						moveDown = True

				elif event.type == pygame.KEYUP:
					print("UP",event.key)
					if event.key == pygame.K_d:
						moveRight = False
					elif event.key == pygame.K_a:
						moveLeft = False
					elif event.key == pygame.K_w:
						moveUp = False
					elif event.key == pygame.K_s:
						moveDown = False


			if moveUp == True:

			elif moveDown == True:

			if moveRight == True:

			elif moveLeft == True:
				


if __name__ == '__main__':
	game = ZeldaGame()

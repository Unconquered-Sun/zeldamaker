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
		nextFrame = clock()
		frame = 0

		self.player = Player("Sprites/links.gif",32)

		running = True

		self.space = pymunk.Space()

		moveUp = False
		moveDown = False
		moveRight = False
		moveLeft = False

		while running:

			if clock() > nextFrame:
				frame += 1
				nextFrame += 60
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
							self.player.animationDirection(0,0)
						elif event.key == pygame.K_a:
							moveLeft = False
							self.player.animationDirection(2,0)
						elif event.key == pygame.K_w:
							moveUp = False
							self.player.animationDirection(3,0)
						elif event.key == pygame.K_s:
							moveDown = False
							self.player.animationDirection(1,0)

				#Player Animation
				if moveUp == True:
					self.player.animationDirection(3,frame)
				elif moveDown == True:
					self.player.animationDirection(1,frame)
				elif moveRight == True:
					self.player.animationDirection(0,frame)
				elif moveLeft == True:
					self.player.animationDirection(2,frame)

				#Player Movement
				if moveUp == True:
					self.player.moveDirection(3,5)
				elif moveDown == True:
					self.player.moveDirection(1,5)
				if moveRight == True:
					self.player.moveDirection(0,5)
				elif moveLeft == True:
					self.player.moveDirection(2,5)



if __name__ == '__main__':
	game = ZeldaGame()

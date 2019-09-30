import sys
import pygame
import pymunk
import pymunk.pygame_util
from pygame_functions import *
from player import Player
from zeldamap import Block, ZeldaMap


class ZeldaGame:

	def __init__(self):
		pygame.init()

		self.size = width, height = [1024,567]
		# self.screen = pygame.display.set_mode(self.size)
		self.screen = screenSize(width,height)
		self.clock = pygame.time.Clock()
		nextFrame = clock()
		frame = 0

		self.map = ZeldaMap(["wallcorner1.png/skip/walltop1.png/skip/walltop1.png/skip/walltop1.png/skip","","wallleft1.png/skip/block1.png/block1.png/block1.png"])

		self.block = Block("Sprites/block1.png",[0,0])

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
					self.player.moveDirection(3,10)
				elif moveDown == True:
					self.player.moveDirection(1,10)
				if moveRight == True:
					self.player.moveDirection(0,10)
				elif moveLeft == True:
					self.player.moveDirection(2,10)



if __name__ == '__main__':
	game = ZeldaGame()

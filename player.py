import pygame
import pymunk
import pymunk.pygame_util
from pygame_functions import *

class Player(pygame.sprite.Sprite):
	def __init__(self, imageFile, frames):
		self.sprite = makeSprite(imageFile, frames)

		moveSprite(self.sprite,512,283,True)
		transformSprite(self.sprite,0, .5)
		showSprite(self.sprite)

	#0=right, 1=down, 2=left, 3=up
	def animationDirection(self, direction ,frame):
		print(frame,frame%8)
		changeSpriteImage(self.sprite, direction*8+(frame%8) )

	def moveDirection(self, direction, speed):
		center = self.sprite.rect.center
		print(center)
		#Right
		if direction == 0:
			moveSprite(self.sprite, center[0]+speed, center[1], True)
		#Down
		elif direction == 1:
			moveSprite(self.sprite, center[0], center[1]+speed, True)
		#Left
		elif direction == 2:
			moveSprite(self.sprite, center[0]-speed, center[1], True)
		#Up
		elif direction == 3:
			moveSprite(self.sprite, center[0], center[1]-speed, True)
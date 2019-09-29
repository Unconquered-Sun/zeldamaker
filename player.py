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


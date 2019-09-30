import pygame
import pymunk
import pymunk.pygame_util
from pygame_functions import *

class Block(pygame.sprite.Sprite):
	def __init__(self,imagefile,position):
		self.sprite = makeSprite(imagefile)

		moveSprite(self.sprite, position[0],position[1],False)
		showSprite(self.sprite)

	# def collide(self):
	# 	

# class Wall(Block):


class ZeldaMap:
	def __init__(self, mapfile):
		#The mapfile is a list of strings. Each string is a single row of sprites separated by a /.
		self.mapSprites = []
		y=0
		for row in mapfile:
			if row != "":
				rowSprites = []
				sprite_row = row.split("/")
				x=0
				for single_string in sprite_row:
					if single_string == "skip":
						x+=16
					else:

						single_sprite = makeSprite("Sprites/"+single_string)
						moveSprite(single_sprite,x,y,False)
						showSprite(single_sprite)

						rowSprites.append(single_sprite)

						x+=16

				self.mapSprites.append(rowSprites)
			
			y+=16

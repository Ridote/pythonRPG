import pygame
import sys
from pygame.locals import *
from Utils import *
from Spritesheet import *
class Character:
	def __init__(self):
		self.spritesheet = Spritesheet(S_CHARACTER, CHARACTER_SPRITESHEET_SIZE)
		(spr_unit_x, spr_unit_y) = CHARACTER_SPRITESHEET_UNIT
		self.standing = self.spritesheet.imagesAt([(0,0,spr_unit_x,spr_unit_y), (24,30,spr_unit_x,spr_unit_y)])
		self.index = 0
		self.image = self.standing[self.index]
		self.pos = self.image.get_rect()
	def move(self, key):
		if key[pygame.K_LEFT]:
			self.pos.x -= 1
		elif key[pygame.K_RIGHT]:
			self.pos.x += 1
	def setPos(self, x = 0, y = 0):
		self.pos.x = x
		self.pos.y = y
	def update(self):
		self.index += 0.1#pygame.time.Clock.get_time()
		if self.index >= len(self.standing):
			self.index = 0
		self.image = self.standing[int(self.index)]
	def render(self, screen):
		screen.blit(self.image, self.pos, self.image.get_rect())
import pygame
from Utils import *

class Spritesheet(object):
	def __init__(self, filename, size):
		self.sheet = pygame.transform.scale(load_image(filename, True), size)
	def imageAt(self, rectangle, colorkey = None):
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert_alpha()
		image.blit(self.sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image
	def imagesAt(self, rects, colorkey = None):
		return [self.imageAt(rect, colorkey) for rect in rects]
	def loadStrip(self, rect, image_count, colorkey = None):
		tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
		return self.imagesAt(tups, colorkey)
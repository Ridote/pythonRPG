from Utils import *
class Cursor():
	def __init__(self, posx = 0, posy = 0, size = CURSOR_SIZE, sprite = S_CURSOR):
		self.image = pygame.transform.scale(load_image(sprite, True), size)
		self.rect = self.image.get_rect()
		self.rect.left = posx
		self.rect.top = posy
	def update(self, position):
		self.rect.left = position.left - (self.image.get_width() + CURSOR_OFFSET)
		self.rect.centery = position.centery + self.image.get_height()/5
	def render(self, screen):
		screen.blit(self.image, self.rect)
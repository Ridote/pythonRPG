import sys, pygame
from pygame.locals import *
from Utils import *
from Scene import *
from Spritesheet import *
def main():
	#Initial configuration
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_icon(load_image(I_ICON, True))
	pygame.display.set_caption("Platform")
	clock = pygame.time.Clock()

	active_scene = TitleScene()
	#Main loop
	while active_scene != None:
		pressed_keys = pygame.key.get_pressed()

		# Event filtering 
		filtered_events = []
		for event in pygame.event.get():
			quit_attempt = False
			if event.type == pygame.QUIT:
				quit_attempt = True
			if quit_attempt:
				active_scene.terminate()
			else:
				filtered_events.append(event)

		active_scene.processInput(filtered_events, pressed_keys)
		active_scene.update()
		active_scene.render(screen)
		active_scene = active_scene.next
		pygame.display.flip()
		clock.tick(N_FPS)
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
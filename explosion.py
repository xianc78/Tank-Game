import pygame, sys
import constants

explosionSound = pygame.mixer.Sound("resources/explosion.wav")

class Explosion:
	def __init__(self, x, y, map):
		try:
			self.image = pygame.image.load("resources/explosion.png")
		except pygame.error:
			print "explosion.png has been deleted"
			raw_input("<press enter>")
			pygame.quit()
			sys.exit()
		#self.image = pygame.transform.scale(self.image, (32, 32))
		self.image.set_colorkey(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.map = map
		self.life = 20
		explosionSound.play()

	def update(self):
		self.life -= 1
		if self.life <= 0:
			self.map.explosion_list.remove(self)

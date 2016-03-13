import pygame
import constants

class Bullet:
	def __init__(self, x, y, change_x, change_y, tank):
		self.image = pygame.Surface([10, 10])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.y = y
		self.change_x = change_x
		self.change_y = change_y
		self.tank = tank
		self.map = self.tank.map
		
	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		for wall in self.map.wall_list:
			if self.rect.colliderect(wall.rect):
				try:
					self.map.bullet_list.remove(self)
				except ValueError:
					pass
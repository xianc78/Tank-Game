import pygame, sys, easygui
import constants
from bullet import Bullet
from explosion import Explosion
from mine import Mine

explosionSound = pygame.mixer.Sound("resources/explosion.wav")

class Tank():
	score = 0
	def update(self):
		self.image = self.images[self.facing]
		self.rect.x += self.change_x
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > constants.SCREEN_WIDTH:
			self.rect.right = constants.SCREEN_WIDTH
		for wall in self.map.wall_list:
			if self.rect.colliderect(wall.rect):
				if self.change_x > 0:
					self.rect.right = wall.rect.left
				else:
					self.rect.left = wall.rect.right
		self.rect.y += self.change_y
		if self.rect.top < 0:
			self.rect.top = 0
		elif self.rect.bottom > constants.SCREEN_HEIGHT:
			self.rect.bottom = constants.SCREEN_HEIGHT
		for wall in self.map.wall_list:
			if self.rect.colliderect(wall.rect):
				if self.change_y > 0:
					self.rect.bottom = wall.rect.top
				else:
					self.rect.top = wall.rect.bottom
		for bullet in self.map.bullet_list:
			if self.rect.colliderect(bullet.rect):
				if bullet.tank != self:
					#explosionSound.play()
					self.map.explosion_list.append(Explosion(self.rect.centerx, self.rect.centery, self.map))
					bullet.tank.score += 1
					self.rect.topleft = (self.startx, self.starty)
					self.map.bullet_list.remove(bullet)
		for mine in self.map.mine_list:
			if self.rect.colliderect(mine.rect):
				if mine.tank != self:
					self.map.explosion_list.append(Explosion(self.rect.centerx, self.rect.centery, self.map))
					mine.tank.score += 1
					self.rect.topleft = (self.startx, self.starty)
					self.map.mine_list.remove(mine)
		
	def shoot(self):
		if self.facing == "u":
			self.map.bullet_list.append(Bullet(self.rect.centerx, self.rect.y - 10, 0, -6, self))
		elif self.facing == "d":
			self.map.bullet_list.append(Bullet(self.rect.centerx, self.rect.bottom, 0, 6, self))
		elif self.facing == "l":
			self.map.bullet_list.append(Bullet(self.rect.left - 10, self.rect.centery, -6, 0, self))
		elif self.facing == "r":
			self.map.bullet_list.append(Bullet(self.rect.right, self.rect.centery, 6, 0, self))
			
	def lay_mine(self):
		self.map.mine_list.append(Mine(self.rect.x, self.rect.y, self))

class Tank1(Tank):
	def __init__(self, x, y, map):
		try:
			self.image = pygame.image.load("resources/tank1.png")
			self.image = pygame.transform.scale2x(self.image)
		except pygame.error():
			easygui.msgbox("tank1.png does not exist.")
			pygame.quit()
			sys.exit()
		self.images = {"u":self.image, "d":pygame.transform.flip(self.image, False, True), "l":pygame.transform.rotate(self.image, 90), "r":pygame.transform.rotate(self.image, -90)}
		self.rect = self.image.get_rect()
		self.startx = x
		self.starty = y
		self.rect.x = x
		self.rect.y = y
		self.map = map
		self.change_x = 0
		self.change_y = 0
		self.facing = "u"
		
class Tank2(Tank):
	def __init__(self, x, y, map):
		try:
			self.image = pygame.image.load("resources/tank2.png")
			self.image = pygame.transform.scale2x(self.image)
		except pygame.error():
			easygui.msgbox("tank2.png does not exist.")
			pygame.quit()
			sys.exit()
		self.images = {"u":self.image, "d":pygame.transform.flip(self.image, False, True), "l":pygame.transform.rotate(self.image, 90), "r":pygame.transform.rotate(self.image, -90)}
		self.rect = self.image.get_rect()
		self.startx = x
		self.starty = y
		self.rect.x = x
		self.rect.y = y
		self.map = map
		self.change_x = 0
		self.change_y = 0
		self.facing = "u"
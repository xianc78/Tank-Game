import pygame, sys, os, time, easygui
import constants, textfunctions
from wall import Wall
from map import Map
pygame.init()

titleText = textfunctions.centerText(constants.TITLE)
scoreText = textfunctions.ScoreText()

class Game:
	def __init__(self, mode):
		self.screen = pygame.display.get_surface()
		self.mode = mode
		self.start_time = time.time()
		self.time = 60
	
	def check_events(self):
		if self.mode == "menu":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
				elif event.type == pygame.KEYDOWN:
					try:
						map = easygui.fileopenbox("Open File", "Tank Game", "resources/map1.txt")
						self.map = Map(map)
						self.mode = "game"
					except IOError:
						pass
		elif self.mode == "game":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LCTRL:
						self.map.tank1.shoot()
					elif event.key == pygame.K_RCTRL:
						self.map.tank2.shoot()
				
			self.map.tank1.change_x = self.map.tank1.change_y = 0
			self.map.tank2.change_x = self.map.tank2.change_y = 0
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_w]:
				self.map.tank1.change_y = -4
				self.map.tank1.facing = "u"
			elif pressed[pygame.K_s]:
				self.map.tank1.change_y = 4
				self.map.tank1.facing = "d"
			elif pressed[pygame.K_a]:
				self.map.tank1.change_x = -4
				self.map.tank1.facing = "l"
			elif pressed[pygame.K_d]:
				self.map.tank1.change_x = 4
				self.map.tank1.facing = "r"
				
			if pressed[pygame.K_i]:
				self.map.tank2.change_y = -4
				self.map.tank2.facing = "u"
			elif pressed[pygame.K_k]:
				self.map.tank2.change_y = 4
				self.map.tank2.facing = "d"
			elif pressed[pygame.K_j]:
				self.map.tank2.change_x = -4
				self.map.tank2.facing = "l"
			elif pressed[pygame.K_l]:
				self.map.tank2.change_x = 4
				self.map.tank2.facing = "r"
		
		
	def update_screen(self):
		#self.screen.fill(constants.BLACK)
		if self.mode == "menu":
			self.screen.fill(constants.RED)
			self.screen.blit(titleText.text, titleText.rect)
		elif self.mode == "game":
			self.screen.fill(constants.GREY)
			self.screen.blit(self.map.tank1.image, self.map.tank1.rect.topleft)
			self.screen.blit(self.map.tank2.image, self.map.tank2.rect.topleft)
			for bullet in self.map.bullet_list:
				self.screen.blit(bullet.image, bullet.rect.topleft)
			for wall in self.map.wall_list:
				self.screen.blit(wall.image, wall.rect.topleft)
			self.screen.blit(scoreText.text, scoreText.rect)
		pygame.display.update()
	
	def run_logic(self):
		if self.mode == "menu":
			pass
		elif self.mode == "game":
			self.map.tank1.update()
			self.map.tank2.update()
			for bullet in self.map.bullet_list:
				bullet.update()
			scoreText.update(self.map.tank1.score, self.map.tank2.score, self.time)
				
	def update_timer(self):
		if time.time() >= self.start_time + 1:
			self.start_time = time.time()
			self.time -= 1
		if self.time <= 0:
			if self.map.tank1.score > self.map.tank2.score:
				#easygui.msgbox("Tank 1 Wins")
				textfunctions.splashText("Tank 1 Wins")
				pygame.display.update()
				pygame.time.wait(1000)
			elif self.map.tank2.score > self.map.tank1.score:
				#easygui.msgbox("Tank 2 Wins")
				textfunctions.splashText("Tank 2 Wins")
				pygame.display.update()
				pygame.time.wait(1000)
			else:
				#easygui.msgbox("Tie")
				textfunctions.splashText("Tie")
				pygame.display.update()
				pygame.time.wait(1000)
			self.map.tank1.score = self.map.tank2.score = 0
			self.__init__("menu")
		
	def terminate(self):
		pygame.quit()
		sys.exit()
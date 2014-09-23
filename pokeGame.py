#!/usr/bin/python3.3

import pygame
#import pokemon
pygame.init()

#Define colors
BLACK   = (   0,   0,   0)
WHITE   = ( 255, 255, 255)
GREEN   = (   0, 255,   0)
RED     = ( 255,   0,   0)
BLUE    = (   0,   0, 255)
ORANGE  = ( 255, 128,   0)
PINK    = ( 245, 111, 176)
YELLOW	= ( 255, 255, 100)

#Screen size
SCREEN_WIDTH = 1599
SCREEN_HEIGHT = 899
bgimage = pygame.image.load("media/PokemonWallpaper.jpg")
ashK = pygame.image.load("media/RedSprite.png")
lasersound = pygame.mixer.Sound("media/laser5.ogg")

class Laser(pygame.sprite.Sprite):
	#Vector
	change_x = 10

	#Damage
	damage = 1

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([35, 5])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		pygame.draw.ellipse(self.image, PINK, [self.rect.x, self.rect.y, 35, 5])

	def sound(self):
		lasersound.play()

	def update(self):
		self.rect.x += self.change_x


class Pikachu(pygame.sprite.Sprite):
	#Vector
	change_x = 2
	change_y = 1

	#Health
	health = 10

	#Damage
	damage = 1

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([50, 89])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

		#Left ear
		pygame.draw.polygon(self.image, YELLOW, [[self.rect.x+9, self.rect.y], [self.rect.x+3, self.rect.y+49], [self.rect.x+19, self.rect.y+38]], 0)
		pygame.draw.polygon(self.image, BLACK, [[self.rect.x+9, self.rect.y], [self.rect.x+6, self.rect.y+20], [self.rect.x+14, self.rect.y+15]], 0)

		#Right ear
		pygame.draw.polygon(self.image, YELLOW, [[self.rect.x+39, self.rect.y], [self.rect.x+29, self.rect.y+38], [self.rect.x+45, self.rect.y+49]], 0)
		pygame.draw.polygon(self.image, BLACK, [[self.rect.x+39, self.rect.y], [self.rect.x+34, self.rect.y+15], [self.rect.x+42, self.rect.y+20]], 0)

		#Head
		pygame.draw.ellipse(self.image, YELLOW, [self.rect.x, self.rect.y+29, 50, 60], 0)

		#Cheeks
		pygame.draw.circle(self.image, RED, [self.rect.x+10, self.rect.y+70], 6, 0)
		pygame.draw.circle(self.image, RED, [self.rect.x+38, self.rect.y+70], 6, 0)

		#Eyes
		pygame.draw.circle(self.image, BLACK, [self.rect.x+15, self.rect.y+45], 4, 0)
		pygame.draw.circle(self.image, BLACK, [self.rect.x+33, self.rect.y+45], 4, 0)

		#Mouth
		pygame.draw.line(self.image, BLACK, [self.rect.x+10, self.rect.y+80], [self.rect.x+38, self.rect.y+80], 1)

	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y

		#Bounce pikachu off of side
		if self.rect.x+50 >= SCREEN_WIDTH:
			self.rect.x = SCREEN_WIDTH-50
			self.change_x *= -1
		if self.rect.x <= 0:
			self.rect.x = 0
			self.change_x *= -1
		#Bounce pikachu off of top or bottom
		if self.rect.y+89 >= SCREEN_HEIGHT:
			self.rect.y = SCREEN_HEIGHT-89
			self.change_y *= -1
		if self.rect.y <= 0:
			self.rect.y = 0
			self.change_y *= -1


class Ash(pygame.sprite.Sprite):
	#Health
	health = 10

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = ashK.convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

	def update(self):
		pos = pygame.mouse.get_pos()
		self.rect.x = pos[0]
		self.rect.y = pos[1]


class Damage(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([50,90])
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		pygame.draw.ellipse(self.image, RED, [self.rect.x, self.rect.y, 50, 90], 0)


class Game(object):
	"""
	This class represents an instance of the game. If we need to
	reset the game, we'd just need to create a new instance of this
	class.
	"""

	##### Class attributes #####

	#Sprite lists
	weapon_list = None
	enemy_list = None
	all_sprites_list = None

	#Other data
	game_over = False
	score = 0

	##### Class methods #####
	def __init__(self):
		self.score = 0
		self.game_over = False

		#Create sprite lists
		self.weapon_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()

		#Create the pikachu sprite
		self.pikachu = Pikachu()
		self.pikachu.rect.x = 400
		self.pikachu.rect.y = 400
		self.all_sprites_list.add(self.pikachu)
		self.enemy_list.add(self.pikachu)

		#Create the player sprite
		self.player = Ash()
		self.all_sprites_list.add(self.player)

		#Create a damage sprite, but don't add it to any group,
		#that way it will not be drawn until it is added to a group
		#(i.e. main function has a condition that is met)
		self.damage = Damage()

	def process_events(self):
		"""
		Process all events. Return True if closing the window.
		"""

		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
				return True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if not self.game_over:
					laser = Laser()
					laser.sound()
					laser.rect.x = self.player.rect.x
					laser.rect.y = self.player.rect.y
					self.all_sprites_list.add(laser)
					self.weapon_list.add(laser)
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				if self.game_over:
					self.__init__()
		return False

	def run_logic(self):
		"""
		This method is run each time through the frame. It
		updates positions and checks for collisions.
		"""
		if not self.game_over:
			#Remove the damage sprites
			self.all_sprites_list.remove(self.damage)
			#Move all the sprites
			self.all_sprites_list.update()

			"""
			Check if enemies have been hit. If any weapon hits an enemy, do damage to the enemy equivalent to the damage value of the weapon. The values of the dictionary are lists of items
			that have collided with the keys, thus it is necessary to loop through each value to get the damage accumulated from each weapon. If the enemy's health reaches 0, kill it.
			"""
			hit_dict = pygame.sprite.groupcollide(self.enemy_list, self.weapon_list, False, True)
			for enemy, weapons in hit_dict.items():
				for weapon in weapons:
					enemy.health -= weapon.damage
					self.damage.rect = enemy.rect
					self.all_sprites_list.add(self.damage)
				if enemy.health <= 0:
					self.enemy_list.remove(enemy)
					self.all_sprites_list.remove(enemy)
			if not self.enemy_list:
				self.game_over = True

			#The player has collided with an enemy
			hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False)
			for enemy in hit_list:
				#Do damage to the player
				self.player.health -= enemy.damage
				self.damage.rect = self.player.rect
				self.all_sprites_list.add(self.damage)
				if self.player.health <= 0:
					self.game_over = True
				#Bounce the enemy away
				if self.player.rect.x < enemy.rect.x and self.player.rect.y < enemy.rect.y:
					enemy.rect.x += 100
					enemy.rect.y += 100
					pygame.mouse.set_pos([self.player.rect.x-100, self.player.rect.y-100])
				elif self.player.rect.x < enemy.rect.x and self.player.rect.y > enemy.rect.y:
					enemy.rect.x += 100
					enemy.rect.y -= 100
					pygame.mouse.set_pos([self.player.rect.x-100, self.player.rect.y+100])
				elif self.player.rect.x > enemy.rect.x and self.player.rect.y > enemy.rect.y:
					enemy.rect.x -= 100
					enemy.rect.y -= 100
					pygame.mouse.set_pos([self.player.rect.x+100, self.player.rect.y+100])
				elif self.player.rect.x > enemy.rect.x and self.player.rect.y < enemy.rect.y:
					enemy.rect.x -= 100
					enemy.rect.y += 100
					pygame.mouse.set_pos([self.player.rect.x+100, self.player.rect.y-100])

			#Remove laser if it goes offscreen
			for weapon in self.weapon_list:
				if weapon.rect.x >= SCREEN_WIDTH:
					#Remove it from the game
					self.weapon_list.remove(weapon)
					self.all_sprites_list.remove(weapon)

	def display_frame(self, screen):
		"""
		Display everything to the screen for the game.
		"""
		screen.fill(WHITE)

		if self.game_over and self.player.health <= 0:
			#Print the game over screen
			font = pygame.font.SysFont("serif", 25)
			text = font.render("Game Over, press space to restart. Press 'Q' to quit.", True, BLACK)
			center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
			center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			screen.blit(text, [center_x, center_y])

		elif self.game_over and self.player.health > 0:
			#Print the winning screen
			font = pygame.font.SysFont("serif", 25)
			text = font.render("YOU WIN!!! Press space to restart. Press 'Q' to quit.", True, BLACK)
			center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
			center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			screen.blit(text, [center_x, center_y])

		elif not self.game_over:
			screen.blit(bgimage.convert(), [0, 0])
			#Some info to be printed to the screen
			font = pygame.font.Font(None, 25)
			player_health = font.render("Health: %s"%self.player.health, True, RED)
			screen.blit(player_health, [1500, 0])
			#Draw all the sprites
			self.all_sprites_list.draw(screen)

		pygame.display.flip()


def main():
	"""
	Main program function
	"""

	size = (SCREEN_WIDTH, SCREEN_HEIGHT)
	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Pokemon")
	#For ending main program loop
	done = False
	#Update speed
	clock = pygame.time.Clock()
	#Hide Mouse
	pygame.mouse.set_visible(False)

	game = Game()

	while not done:
		done = game.process_events()

		game.run_logic()

		game.display_frame(screen)

		clock.tick(60)

	#Close
	pygame.quit()

#Call main function
if __name__ == "__main__":
	main()

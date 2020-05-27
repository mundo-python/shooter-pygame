#
#	En este script creamos la ventana de nuestro juego
#						y
#	creamos nuestro jugador y le damos movimiento
#
#			Creador: Mundo Python
#
#			youtube: Mundo Python
#
#

import pygame, random

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

all_sprites = pygame.sprite.Group()


player = Player()
all_sprites.add(player)


# Game Loop
running = True
while running:
	# Keep loop running at the right speed
	clock.tick(60)
	# Process input (events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
		

	# Update
	all_sprites.update()

	#Draw / Render
	screen.fill(BLACK)
	all_sprites.draw(screen)
	# *after* drawing everything, flip the display.
	pygame.display.flip()

pygame.quit()

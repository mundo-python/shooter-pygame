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

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/meteorGrey_med1.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

# Cargar fondo.
background = pygame.image.load("assets/background.png").convert()


all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
	meteor = Meteor()
	all_sprites.add(meteor)
	meteor_list.add(meteor)

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
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()

	# Update
	all_sprites.update()
	# Colisiones meteoro - laser
	hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
	for hit in hits:
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)
		
	# Colisiones jugador - meteoro
	hits = pygame.sprite.spritecollide(player, meteor_list, False)
	if hits:
		running = False
	#Draw / Render
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)
	# *after* drawing everything, flip the display.
	pygame.display.flip()

pygame.quit()

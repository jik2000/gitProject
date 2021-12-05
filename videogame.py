# https://linuxhint.com/design-video-games-pygame/
import pygame
import sys
import time
import os
import random


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# настройка папки ассетов
game_folder = os.path.dirname(__file__)
player_folder = os.path.join(game_folder, 'assets\\Base pack\\Player')
enemies_folder = os.path.join(game_folder, 'assets\\Base pack\\Enemies')
backgrounds_folder = os.path.join(game_folder, 'assets\\Mushroom expansion\\Backgrounds')
items_folder = os.path.join(game_folder, 'assets\\Base pack\\Items')
hud_folder = os.path.join(game_folder, 'assets\\Base pack\\HUD')

# initialize
pygame.init()

# initialize the clock
clock = pygame.time.Clock()

# set screen geometry
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# set title of window
pygame.display.set_caption("Video Game")

# set the icon
# image = pygame.image.load("icon.png")
image = pygame.image.load(os.path.join(items_folder, 'mushroomRed.png')).convert()
pygame.display.set_icon(image)

# create the background image
# bg_image = pygame.image.load("bg_image_3.jpg")
bg_image = pygame.image.load(os.path.join(backgrounds_folder, 'bg_shroom.png')).convert()


def background():
    screen.blit(bg_image, (-15, -25))


# person image
person_x = 400
person_y = 550
# image_person = pygame.image.load("girl.png")
# image_person = pygame.image.load(os.path.join(player_folder, 'p1_front.png')).convert()
# image_person = pygame.image.load(os.path.join(enemies_folder, 'flyFly1.png')).convert()
image_person = pygame.image.load(os.path.join(enemies_folder, 'snailWalk1.png')).convert()
image_person.set_colorkey(WHITE)


def person(x, y):
    screen.blit(image_person, (x, y))


# enemy image
enemy_x = random.randint(0, 750)
enemy_y = random.randint(0, 300)
# image_enemy = pygame.image.load("enemy.png")
# image_enemy = pygame.image.load(os.path.join(enemies_folder, 'fishSwim1.png')).convert()
image_enemy = pygame.image.load(os.path.join(hud_folder, 'hud_coins.png')).convert()
image_enemy.set_colorkey(BLACK)


def enemy(x, y):
    screen.blit(image_enemy, (x, y))


# initialize enemy variables
enemy_diff = 0.6
# enemy_x = 0

# initialize variables
books_diff = 4
# books_y = 520
books_y = 420
books_x = 420

# books image
books_state = "not moving"
# image_books = pygame.image.load("books.png")
# image_books = pygame.image.load(os.path.join(items_folder, 'coinBronze.png')).convert()
image_books = pygame.image.load(os.path.join(enemies_folder, 'snailShell.png')).convert()
image_books.set_colorkey(BLACK)


def books(x, y):
    global books_state
    books_state = "moving"
    # screen.blit(image_books, (x + 15, y + 1))
    screen.blit(image_books, (x + 15, y + 1))


score = 0

# initialize font
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)


def text_score(x, y):
    text = myfont.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(text, (x, y))


# initialize sounds
pygame.mixer.init()
# pygame.mixer.music.load("gun-cocking-01.wav")

text_game_over = pygame.font.SysFont('Comic Sans MS', 80)


# game over function
def game_over(x, y):
    text_game_over_2 = myfont.render('YOU WON', True, (0, 0, 0))
    screen.blit(text_game_over_2, (x, y))


def timer(x, y):
    text_timer = myfont.render('Time: ' + str(pygame.time.get_ticks()), True, (0, 0, 0))
    screen.blit(text_timer, (x, y))


# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # check for keys pressed
    pressed_keys = pygame.key.get_pressed()

    # if the key pressed is the right arrow,
    # then move to the right
    if pressed_keys[pygame.K_RIGHT] and person_x < 750:
        person_x += 0.8

    # if the key pressed is the left arrow,
    # then move to the left
    if pressed_keys[pygame.K_LEFT] and person_x > 0:
        person_x += -0.8

    # activate the background function
    background()

    # activate the person function
    person(person_x, person_y)

    # move the enemy
    enemy_x += enemy_diff
    if enemy_x <= 0:
        enemy_x = 0
        enemy_diff = 0.6
    if enemy_x >= 730:
        enemy_x = 730
        enemy_diff = -0.6

    # books movement
    if books_y <= 0:
        books_y = 420
        books_state = "not moving"

    if books_state == "moving":
        books_x = person_x
        books(books_x, books_y)
        books_y -= books_diff

        # fire if the space button is pressed
    if pressed_keys[pygame.K_SPACE]:
        books_x = person_x
        books(books_x, books_y)

    # activate the enemy
    enemy(enemy_x, enemy_y)

    # collision detection
    # enemy_rect = pygame.Rect(enemy_x, enemy_y, 64, 64)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 32, 32)
    # books_rect = pygame.Rect(books_x, books_y, 64, 64)
    books_rect = pygame.Rect(books_x, books_y, 32, 32)

    if books_rect.colliderect(enemy_rect):
        enemy_x = random.randrange(0, 800)
        enemy_y = random.randrange(0, 300)
        score += 1
        bullet_state = "not moving"
        enemy(enemy_x, enemy_y)
        books_y = 0
        # pygame.mixer.music.play()

    # check for win
    if score > 5:
        game_over(400, 300)
        pygame.display.flip()
        time.sleep(5)
        break

    # activate text score
    text_score(6, 6)
    timer(500, 6)

    # update everything
    pygame.display.update()

    clock.tick(60)

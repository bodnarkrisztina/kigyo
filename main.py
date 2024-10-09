import pygame
import random
import sys

# Pygame inicializálás
pygame.init()

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

# Ablak mérete
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kígyós játék - Űr és Bánya")

# Frissítési sebesség
clock = pygame.time.Clock()

# Kígyó kezdőpozíciója és mérete
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Játék sebessége
speed = 15

# Csillag/kristály kezdő pozíció
star_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
star_spawn = True

# Játék pontszám
score = 0

# Játék mód kiválasztása: űr vagy bánya
environment = input("Válassz játék helyszínt: űr vagy bánya? (írj 'ur' vagy 'banya'): ").strip().lower()

# Háttér beállítása
if environment == 'ur':
    background_color = BLACK  # Űr háttér
    star_color = YELLOW  # Csillag
else:
    background_color = (139, 69, 19)  # Bánya háttér (barna)
    star_color = PURPLE  # Kristály

# Funkció a pontszám megjelenítéséhez
def show_score(choice=1):
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Pontszám: ' + str(score), True, WHITE)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (WIDTH / 10, 15)
    else:
        score_rect.center = (WIDTH / 2, HEIGHT / 2)
    win.blit(score_surface, score_rect)

# Játék vége
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    GO_surface = font.render('Játék vége', True, RED)
    GO_rect = GO_surface.get_rect()
    GO_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    win.blit(GO_surface, GO_rect)
    show_score(0)
    pygame.display.flip()
    pygame.time.sleep(3)
    pygame.quit()
    sys.exit()

# Fő játékhurok
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Irányítás
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_direction != 'DOWN':
                    change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                if snake_direction != 'UP':
                    change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                if snake_direction != 'RIGHT':
                    change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                if snake_direction != 'LEFT':
                    change_to = 'RIGHT'

    # Ha megváltozik az irány
    snake_direction = change_to

    # Kígyó mozgatása
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Kígyó növelése, ha csillagot/kristályt eszik
    snake_body.insert(0, list(snake_pos))
    if snake_pos == star_pos:
        score += 10
        star_spawn = False
    else:
        snake_body.pop()

    # Új csillag/kristály
    if not star_spawn:
        star_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    star_spawn = True

    # Háttér rajzolása
    win.fill(background_color)

    # Kígyó rajzolása
    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Csillag/kristály rajzolása
    pygame.draw.rect(win, star_color, pygame.Rect(star_pos[0], star_pos[1], 10, 10))

    # Játék vége, ha a kígyó nekiütközik a falnak vagy saját magának
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Pontszám megjelenítése
    show_score()

    # Képernyő frissítése
    pygame.display.update()

    # Játék sebessége
    clock.tick(speed)

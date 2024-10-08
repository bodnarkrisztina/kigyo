import pygame
import time
import random

pygame.init()

# Színek meghatározása
feher = (255, 255, 255)
fekete = (0, 0, 0)
piros = (213, 50, 80)
zold = (0, 255, 0)
kek = (50, 153, 213)

# Ablak mérete
dis_width = 800
dis_height = 600

# Játék kijelző
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Kígyós játék')

# Kígyó paraméterek
kigyocsko_meret = 10
kigyocsko_sebesseg = 15

# Idő kezelése
clock = pygame.time.Clock()

# Betűtípus - alapértelmezett betűtípus használata, hogy elkerüld a figyelmeztetést
font_style = pygame.font.SysFont(None, 25)

# Üzenet megjelenítése
def az_uzeneget(szoveg, szin):
    uzenet = font_style.render(szoveg, True, szin)
    dis.blit(uzenet, [dis_width / 6, dis_height / 3])

# Kígyó kirajzolása
def kigyo(kigyocsko_meret, kigyo_lista):
    for x in kigyo_lista:
        pygame.draw.rect(dis, zold, [x[0], x[1], kigyocsko_meret, kigyocsko_meret])

# Játék logika
def jatek():
    jatek_vege = False
    jatek_bezar = False

    x = dis_width / 2
    y = dis_height / 2

    x_valtozas = 0
    y_valtozas = 0

    kigyo_lista = []
    kigyo_hossza = 1

    # Kaja pozíciója
    kaja_x = round(random.randrange(0, dis_width - kigyocsko_meret) / 10.0) * 10.0
    kaja_y = round(random.randrange(0, dis_height - kigyocsko_meret) / 10.0) * 10.0

    while not jatek_vege:

        while jatek_bezar:
            dis.fill(fekete)
            az_uzeneget("Vesztettél! Nyomj meg egy Q-t a kilépéshez vagy C-t az újraindításhoz", piros)
            pygame.display.update()

            for esemeny in pygame.event.get():
                if esemeny.type == pygame.KEYDOWN:
                    if esemeny.key == pygame.K_q:
                        jatek_vege = True
                        jatek_bezar = False
                    if esemeny.key == pygame.K_c:
                        jatek()

        # Események kezelése
        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                jatek_vege = True
            if esemeny.type == pygame.KEYDOWN:
                if esemeny.key == pygame.K_LEFT:
                    x_valtozas = -kigyocsko_meret
                    y_valtozas = 0
                elif esemeny.key == pygame.K_RIGHT:
                    x_valtozas = kigyocsko_meret
                    y_valtozas = 0
                elif esemeny.key == pygame.K_UP:
                    y_valtozas = -kigyocsko_meret
                    x_valtozas = 0
                elif esemeny.key == pygame.K_DOWN:
                    y_valtozas = kigyocsko_meret
                    x_valtozas = 0

        # Ha a kígyó elér a falhoz
        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            jatek_bezar = True

        # Kígyó mozgása
        x += x_valtozas
        y += y_valtozas

        # Játéktér kirajzolása
        dis.fill(fekete)

        # Kaja kirajzolása
        pygame.draw.rect(dis, kek, [kaja_x, kaja_y, kigyocsko_meret, kigyocsko_meret])

        # Kígyó fejének pozíciója
        kigyo_feje = []
        kigyo_feje.append(x)
        kigyo_feje.append(y)
        kigyo_lista.append(kigyo_feje)

        # Kígyó hossza
        if len(kigyo_lista) > kigyo_hossza:
            del kigyo_lista[0]

        # Ha a kígyó a saját testébe ütközik
        for blokk in kigyo_lista[:-1]:
            if blokk == kigyo_feje:
                jatek_bezar = True

        # Kígyó kirajzolása
        kigyo(kigyocsko_meret, kigyo_lista)

        # Képernyő frissítése
        pygame.display.update()

        # Ha a kígyó megette a kaját
        if x == kaja_x and y == kaja_y:
            kaja_x = round(random.randrange(0, dis_width - kigyocsko_meret) / 10.0) * 10.0
            kaja_y = round(random.randrange(0, dis_height - kigyocsko_meret) / 10.0) * 10.0
            kigyo_hossza += 1

        # Játék sebessége
        clock.tick(kigyocsko_sebesseg)

    # Kilépés a játékból
    pygame.quit()
    quit()

# Játék indítása
jatek()

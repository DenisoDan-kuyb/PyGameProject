from random import shuffle

import pygame
from PIL import Image


def load_image(name, n):
    global im2
    if n == 0:
        image = pygame.image.load('black_cell.png')
        return image
    if n == 1:
        im2 = Image.open(name).crop((300, 0, 600, 300))
    if n == 2:
        im2 = Image.open(name).crop((600, 0, 900, 300))
    if n == 3:
        im2 = Image.open(name).crop((0, 300, 300, 600))
    if n == 4:
        im2 = Image.open(name).crop((300, 300, 600, 600))
    if n == 5:
        im2 = Image.open(name).crop((600, 300, 900, 600))
    if n == 6:
        im2 = Image.open(name).crop((0, 600, 300, 900))
    if n == 7:
        im2 = Image.open(name).crop((300, 600, 600, 900))
    if n == 8:
        im2 = Image.open(name).crop((600, 600, 900, 900))
    if n == 9:
        image = pygame.image.load(name)
        return image

    newname = ''.join([str(n), name])
    im2.save(newname)
    fullname = newname
    image = pygame.image.load(fullname)
    return image


lst = ['chef', 'kobe', 'carter', 'bulls9697']

basketball = pygame.sprite.Group()
abaldet = pygame.sprite.Group()


class Abaldet(pygame.sprite.Sprite):

    def __init__(self, *group, name, n):
        super().__init__(*group)
        self.image = load_image(name, n)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 10


abal = Abaldet(basketball, name='abaldet.png', n=9)


class Chef(pygame.sprite.Sprite):

    def __init__(self, *group, name, n):
        super().__init__(*group)
        self.image = load_image(name, n)
        self.n = n
        if n == 0:
            self.black_cell = True
        else:
            self.black_cell = False
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10


class Kobe(pygame.sprite.Sprite):

    def __init__(self, *group, name, n):
        super().__init__(*group)
        self.image = load_image(name, n)
        self.n = n
        if n == 0:
            self.black_cell = True
        else:
            self.black_cell = False
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10


class Carter(pygame.sprite.Sprite):

    def __init__(self, *group, name, n):
        super().__init__(*group)
        self.image = load_image(name, n)
        self.n = n
        if n == 0:
            self.black_cell = True
        else:
            self.black_cell = False
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10


class Bulls9697(pygame.sprite.Sprite):

    def __init__(self, *group, name, n):
        super().__init__(*group)
        self.image = load_image(name, n)
        self.n = n
        if n == 0:
            self.black_cell = True
        else:
            self.black_cell = False
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height // self.cell_size):
            for x in range(self.width // self.cell_size):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        pass

    def get_cell(self, mouse_pos):
        if not (self.left <= mouse_pos[0] < self.left + self.width * self.cell_size and
                self.top <= mouse_pos[1] < self.top + self.height * self.cell_size):
            return None
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return False
        self.on_click(cell)
        return cell

itog = pygame.sprite.Group()
lst = ['K', 'Ch', 'B', 'Ca']
game = []
flx = 0
fly = 0
q = [0, 1, 2, 3, 4, 5, 6, 7, 8]
shuffle(q)
shuffle(lst)
if lst[0] == 'Ch':
    for g in q:
        l = Chef(basketball, name='chef.png', n=g)
        l.rect.x = 10 + (flx % 900)
        flx += 300
        l.rect.y = 10 + (fly // 900) * 300
        fly += 300
        game.append(l)
    l = Chef(itog, name='chef.png', n=9)
elif lst[0] == 'B':
    for g in q:
        l = Bulls9697(basketball, name='Bulls9697.png', n=g)
        l.rect.x = 10 + (flx % 900)
        flx += 300
        l.rect.y = 10 + (fly // 900) * 300
        fly += 300
        game.append(l)
    l = Bulls9697(itog, name='chef.png', n=9)
elif lst[0] == 'K':
    for g in q:
        l = Kobe(basketball, name='kobe.png', n=g)
        l.rect.x = 10 + (flx % 900)
        flx += 300
        l.rect.y = 10 + (fly // 900) * 300
        fly += 300
        game.append(l)
    l = Kobe(itog, name='chef.png', n=9)
else:
    for g in q:
        l = Carter(basketball, name='carter.png', n=g)
        l.rect.x = 10 + (flx % 900)
        flx += 300
        l.rect.y = 10 + (fly // 900) * 300
        fly += 300
        game.append(l)
    l = Carter(itog, name='chef.png', n=9)

board = Board(900, 900)
board.set_view(10, 10, 300)

size = width, num = 1600, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = board.get_click(event.pos)
            for h in game:
                if h.black_cell:
                    q = board.get_click((h.rect.x, h.rect.y))
                    break
            if a == q:
                print('негры')
                abaldet.draw(screen)
                continue
            print(a, q)
            if (a[0] + 1 == q[0] and a[1] == q[1]) or (a[0] == q[0] + 1 and a[1] == q[1]) or (
                    a[0] == q[0] and a[1] + 1 == q[1]) or (a[0] == q[0] and a[1] == q[1] + 1) or (
                    a[0] + 1 == q[0] and a[1] + 1 == q[1]) or (a[0] == q[0] + 1 and a[1] == q[1] + 1) or (
                    a[0] == q[0] + 1 and a[1] == q[1] - 1) or (a[0] == q[0] - 1 and a[1] == q[1] + 1):
                print(a, q)
                game[q[0] + q[1] * 3].rect.x, game[q[0] + q[1] * 3].rect.y, game[a[0] + a[1] * 3].rect.x, game[
                    a[0] + a[1] * 3].rect.y = game[a[0] + a[1] * 3].rect.x, game[
                    a[0] + a[1] * 3].rect.y, game[q[0] + q[1] * 3].rect.x, game[q[0] + q[1] * 3].rect.y
                game[q[0] + q[1] * 3], game[a[0] + a[1] * 3] = game[a[0] + a[1] * 3], game[q[0] + q[1] * 3]
    flaag = 0
    flagbool = False
    for h in game:
        if h.n == flaag:
            flagbool = True
        else:
            flagbool = False
            break
    if flagbool:
        itog.draw(screen)
    board.render()
    screen.fill(pygame.Color('black'))
    basketball.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()

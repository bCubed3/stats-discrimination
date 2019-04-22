import random
import pygame
import sys
import math
from collections import Counter

pygame.init()
size = width, height = (1740, 600)
screen = pygame.display.set_mode(size)

cases = []
counts = []

for j in range(10000):
    cases.append([])
    c = 0
    for i in range(870):
        n = random.random()
        if n <= 0.791:
            r = "mexican"
            c += 1
        else:
            r = "other"
        cases[j].append(r)
    counts.append(c)

total = 0
for i in counts:
    total += i
mean = total / len(counts)
print("Mean: ", mean)
print("Frequency:", mean / 870)

counts_sort = sorted(counts)
k = list(Counter(counts_sort).keys())
v = list(Counter(counts_sort).values())

kvs = {}

for i in range(len(k)):
    kvs[k[i]] = v[i]

mx = 339 * 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mouse_state = pygame.mouse.get_pressed()
    if mouse_state[0] == 1:
        mx = pygame.mouse.get_pos()[0]
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(math.floor(mx / 2) * 2, 0, 2, height))
    for i in range(len(k)):
        r = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(k[i] * 2, height - v[i], 2, v[i]))
    pygame.draw.line(screen, (255, 0, 0), (339 * 2, 0), (339 * 2, height))
    pygame.draw.line(screen, (0, 255, 0), (mean * 2, 0), (mean * 2, height))
    font = pygame.font.SysFont("arial", 20)
    tx = font.render(str(math.floor(mx / 2)), True, (255, 255, 255))
    if math.floor(math.floor(mx / 2)) in k:
        th = font.render(str(kvs[math.floor(mx / 2)]), True, (255, 255, 255))
    else:
        th = font.render("0", True, (255, 255, 255))
    screen.blit(tx, (mx + 10, 30))
    screen.blit(th, (mx + 10, 60))
    pygame.display.flip()

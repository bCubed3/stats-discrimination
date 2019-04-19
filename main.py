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

for j in range(1000):
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
print(counts_sort)
k = list(Counter(counts_sort).keys())
print(k)
v = list(Counter(counts_sort).values())

print(k[0], k[len(k) - 1])
for i in range(len(k)):
    print(k[i], v[i])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 255))
    for i in range(len(k)):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(k[i] * 2, 0, 10, height - v[i] * 10))
    # pygame.draw.line(screen, (255, 0, 0,), (0, height - 339), (width, height - 339))
    # pygame.draw.line(screen, (0, 0, 255,), (0, height - mean), (width, height - mean))
    pygame.display.flip()

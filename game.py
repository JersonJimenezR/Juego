
import pygame, gm, obj

if __name__ == '__main__':

fin = False

while not fin:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            fin = True

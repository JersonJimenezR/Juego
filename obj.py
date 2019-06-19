import pygame, gm


class Estado (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.cargarImagen(imagen)
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]

class Rival (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.cargarImagen(imagen)
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx=2
        self.vely=2
    def update( self ):
        self.rect.x += self.velx
        # self.rect.y += self.vely

class Fondo (pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.cargarImagen(imagen)
        self.rect = self.image.get_rect()

class Jugador (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.cargarImagen(imagen)
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx=0
        self.vely=0
    def update( self ):
        self.rect.x += self.velx
        self.rect.y += self.vely

class Poder (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.cargarImagen(imagen)
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.vely=0
    def update( self ):
        self.rect.y += self.vely

class Muerte (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.cargarImagen(imagen)
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.time=80
    def update(self):
        self.time-=1

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
        self.image = imagen[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx=2
        self.vely=2
        self.state = 0
        self.imagen = imagen
        self.type = 4
    def update(self,pantalla):
        self.rect.x += self.velx
        # self.rect.y += self.vely
        gm.clean(pantalla)
        if self.state<60:
            limite=int(round(self.state/30,0))
            if self.type == 1:
                self.image = self.imagen[3][9+limite]
                self.state +=1
            elif self.type == 2:
                self.image = self.imagen[0][9+limite]
                self.state +=1
            elif self.type == 3:
                self.image = self.imagen[1][9+limite]
                self.state +=1
            elif self.type == 4:
                self.image = self.imagen[2][9+limite]
                self.state +=1
        else:
            self.state = 0

# class Fondo (pygame.sprite.Sprite):
#     def __init__(self,imagen):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = gm.cargarImagen(imagen)
#         self.rect = self.image.get_rect()

class Jugador (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx=0
        self.vely=0
        self.state = 0
        self.imagen = imagen
    def update(self,pantalla,type):
        self.rect.x += self.velx
        self.rect.y += self.vely
        gm.clean(pantalla)
        if self.state<60:
            limite=int(round(self.state/30,0))
            if type == 1:
                self.image = self.imagen[3][6+limite]
                self.state +=1
            elif type == 2:
                self.image = self.imagen[0][6+limite]
                self.state +=1
            elif type == 3:
                self.image = self.imagen[1][6+limite]
                self.state +=1
            elif type == 4:
                self.image = self.imagen[2][6+limite]
                self.state +=1
        else:
            self.state = 0

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

class Muro (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen[7][4]
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]

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

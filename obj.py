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
    def gravedad(self):
        if self.vely != 0:
            self.vely += 0.1
        else:
            self.vely = 1
    def update( self,type):
        self.rect.x += self.velx
        self.gravedad()
        self.rect.y+=self.vely
        if type == 1:
            if self.state<80:
                limite=int(round(self.state/40,0))
                self.image = self.imagen[0][2-limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 2:
            if self.state<80:
                limite=int(round(self.state/40,0))
                self.image = self.imagen[0][0+limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 3:
            if self.state<30:
                limite=int(round(self.state/15,0))
                self.image = self.imagen[0][2-limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 4:
            if self.state<30:
                limite=int(round(self.state/15,0))
                self.image = self.imagen[0][0+limite]
                self.state +=1
            else:
                self.state = 0

class Rival2 (pygame.sprite.Sprite):
    def __init__(self,pto,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx=2
        self.state = 0
        self.imagen = imagen
        self.type = 4
    def update( self,type):
        self.rect.x += self.velx
        if type == 1:
            if self.state<80:
                limite=int(round(self.state/40,0))
                self.image = self.imagen[0][2-limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 2:
            if self.state<80:
                limite=int(round(self.state/40,0))
                self.image = self.imagen[0][0+limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 3:
            if self.state<30:
                limite=int(round(self.state/15,0))
                self.image = self.imagen[0][2-limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 4:
            if self.state<30:
                limite=int(round(self.state/15,0))
                self.image = self.imagen[0][0+limite]
                self.state +=1
            else:
                self.state = 0

class Fondo (pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm.cargarMapa(imagen)
        self.rect = self.image.get_rect()
        self.velx=0
    def update( self):
        self.rect.x += self.velx

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

    def gravedad(self):
        if self.vely != 0:
            self.vely += 0.5
        else:
            self.vely = 1

    def update( self,type):
        self.rect.x += self.velx
        self.gravedad()
        self.rect.y+=self.vely
        if type == 1:
            if self.state<80:
                limite=int(round(self.state/40,0))
                self.image = self.imagen[0][2-limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 2:
            if self.state<80:
                limite=int(round(self.state/40,0))
                self.image = self.imagen[0][0+limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 3:
            if self.state<30:
                limite=int(round(self.state/6,0))
                self.image = self.imagen[0][5-limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 4:
            if self.state<30:
                limite=int(round(self.state/6,0))
                self.image = self.imagen[0][0+limite]
                self.state +=1
            else:
                self.state = 0
        elif type == 0:
            if self.state<180:
                limite=int(round(self.state/60,0))
                self.image = self.imagen[0][0+limite]
                self.state +=1
            else:
                self.state = 0
        elif type == -1:
            if self.state<180:
                limite=int(round(self.state/60,0))
                self.image = self.imagen[0][6-limite]
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
        self.velx=0
    def update( self ):
        self.rect.x += self.velx

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

class Muro (pygame.sprite.Sprite):
    def __init__(self,pto,imagen,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen[pos[0]][pos[1]]
        self.rect = self.image.get_rect()
        self.rect.x = pto[0]
        self.rect.y = pto[1]
        self.velx=0
    def update( self):
        self.rect.x += self.velx

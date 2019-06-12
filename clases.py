import pygame, fn, random, sprites

# Jugador

class Jugador ( pygame.sprite.Sprite ):

    def __init__( self, position, img = 'iron-standBy', color = fn.getColors( 'blanco' )):

        pygame.sprite.Sprite.__init__( self )
        self.image = sprites.getImage( img )
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        self.vidas = 3

    def update( self ):
        self.rect.x += self.velx
        self.rect.y += self.vely


# Rival

class Rival ( pygame.sprite.Sprite ):

    def __init__( self, position, img = 'rivals', color = fn.getColors( 'rojo' )):

        pygame.sprite.Sprite.__init__(self)
        self.image = sprites.getImage( img )
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 3
        self.vely = 3
        self.tiempo = random.randrange( 800 )

    def update( self ):

        self.rect.x += self.velx
        self.tiempo += -1


# Bala Rival

class BalaRival ( pygame.sprite.Sprite ):

    def __init__( self, position, color = fn.getColors( 'azul' )):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( [10,20] )
        self.image.fill( color )
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.vely = 0

    def update( self ):
        self.rect.y += self.vely


# Bala Jugador

class BalaJugador ( pygame.sprite.Sprite ):

    def __init__( self, position, img = 'shooting-up', color = fn.getColors( 'verde' )):

        pygame.sprite.Sprite.__init__(self)
        self.image = sprites.getImage( img )
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.vely = 0


    def update( self ):
        self.rect.y += self.vely

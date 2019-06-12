import clases, random, fn, pygame, sprites

'''
    Crear nuevos Rivales

    Params
        numero: cantidad de rivales a crear
        position: punto (x,y) donde se creará el rival
'''

def createRivals( numero, pantalla, aleatorio = False, position = [ 400, 400 ] ):

    rivals = []

    if aleatorio:

        rivals.append( clases.Rival( position ))

    else:

        for i in range( numero ):

            positionX = random.randrange( pantalla.get_size()[0] - 50 )
            positionY = random.randrange( 80, (pantalla.get_size()[1] / 2) )

            rivals.append( clases.Rival( [ positionX, positionY ]))

    return rivals


def text( pantalla, position, text = '', font = None, size = 32,  color = fn.getColors( 'blanco' ) ):

    fuente = pygame.font.Font( font , size )
    texto = fuente.render( text, True, color )
    pantalla.blit( texto, position )

def image( pantalla, position, img = '' ):

    fuente = pygame.font.Font( font , size )
    texto = fuente.render( text, True, color )
    pantalla.fill( fn.getColors('negro') )
    pantalla.blit( texto, position )
    fn.refresh()

'''
    Funcion para recortar imagen

    Params
        filas: cantidad de sprites que tiene la imagen en las filas
        columnas: cantidad de sprites que tiene la imagen en la columnas
        imagen: nombre de la imagen (String) Ej: 'imagen1'
        limites[]: cantidad de sprites que tiene la imagen en cada fila 
'''

def recortarImagen( filas, columnas, imagen, limites ):

    lista = []
    matriz = []

    imageToRecort = sprites.getImage( imagen )
    metadata = imageToRecort.get_rect() # return posx, posy, ancho, alto

    anchoImage = metadata[2]
    altoImage = metadata[3]
    anchoCorte = int( anchoImage / columnas )
    altoCorte = int( altoImage / filas )

    for i in range( filas ):

        fila = []

        for j in range( limites[i] ): # limites = cantidad de imagenes en la columna i

            cuadroRecortado = imageToRecort.subsurface( j * anchoCorte, i * altoCorte, anchoCorte, altoCorte)
            fila.append( cuadroRecortado )

        matriz.append( fila )

    return matriz

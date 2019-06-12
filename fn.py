import pygame, math, sprites




def iniciar( sizePantalla ):

    pygame.init()
    pantalla = pygame.display.set_mode( sizePantalla )
    pygame.display.set_caption('Juego')
    limpiarPantalla( pantalla )

    return pantalla

def limpiarPantalla( pantalla, sizePantalla = [0,0] ):

    # imagen = sprites.getImage( 'city' )
    # imagen = imagen.convert()
    # pantalla.blit( imagen, sizePantalla )
    # refresh()

    pantalla.fill( getColors('negro') )

def getColors( color ):

    if( color == 'negro' ):
        return [0,0,0]

    if( color == 'blanco' ):
        return [255,255,255]

    if( color == 'rojo' ):
        return [255,0,0]

    if( color == 'verde' ):
        return [0,155,0]

    if( color == 'azul' ):
        return [26, 29, 255]

    if( color == 'amarillo' ):
        return [233, 252, 1]

    if( color == 'naranja' ):
        return [255, 100, 0]

def refresh():

    pygame.display.flip()

def reloj():

    return pygame.time.Clock()

def toRadians( grados ):

    return math.radians( grados )

def centroPantalla( pantalla ):

    x = round( pantalla.get_size()[0]/2 )
    y = round( pantalla.get_size()[1]/2 )

    return pantallaToCartesiano( pantalla , [ x,y ] )

def centroPantalla2( pantalla, param ):

    if( param == 'x' ):
        return round( pantalla.get_size()[0]/2 )

    if( param == 'y' ):
        return round( pantalla.get_size()[1]/2 )




# Conversiones

def pantallaToCartesiano( pantalla, puntoPantalla ):

    x=puntoPantalla[0]-round(pantalla.get_size()[0]/2)
    y=round(pantalla.get_size()[1]/2)-puntoPantalla[1]
    return [x,y]

def cartersianoToPantalla( pantalla, puntoCartesiano ):

    x = round( pantalla.get_size()[0]/2) + puntoCartesiano[0]
    y = round( pantalla.get_size()[1]/2) - puntoCartesiano[1]

    return [ x,y ]

def cartesianoToPolar( puntoCartesiano ):

    r= math.sqrt( pow(puntoCartesiano[0],2) + pow( puntoCartesiano[1],2 ))
    g= math.degrees( math.atan( puntoCartesiano[1]/puntoCartesiano[0] ))

    return [ r,g ]

def polarToCartesiano( crd ):

    x = crd[0] * math.cos( toRadians( crd[1] ))
    y = crd[0] * math.sin( toRadians( crd[1] ))

    return [ x,y ]




# Dibujos

def drawPunto( pantalla, punto, width = 2, color = getColors('rojo')):

    pygame.draw.circle( pantalla, color, cartersianoToPantalla( pantalla, punto ), width)

def drawLinea( pantalla, punto1, punto2, color = getColors('rojo'), fill = 2):

    pygame.draw.line( pantalla, color, cartersianoToPantalla( pantalla, punto1 ) , cartersianoToPantalla( pantalla, punto2 ), fill )

def drawPlano( pantalla, width = 800, color = getColors('blanco'), fill = 2):

    pygame.draw.line( pantalla, color,
        [ round( centroPantalla2( pantalla, 'x' )) - width, round( centroPantalla2( pantalla, 'y' )) ],
        [ round( centroPantalla2( pantalla, 'x' )) + width, round( centroPantalla2( pantalla, 'y' )) ],
    fill)

    pygame.draw.line( pantalla, color,
        [ round( centroPantalla2( pantalla, 'x' )), round( centroPantalla2( pantalla, 'y' )) - width ],
        [ round( centroPantalla2( pantalla, 'x' )), round( centroPantalla2( pantalla, 'y' )) + width ],
    fill)

    refresh()

def drawCruz( pantalla, puntoCartesiano, width = 100, color = getColors('rojo'), fill = 2):

    centro = cartersianoToPantalla( pantalla, puntoCartesiano )

    pygame.draw.line( pantalla, color,
        [ centro[0] - width, centro[1] ],
        [ centro[0] + width, centro[1] ],
    fill)

    pygame.draw.line( pantalla, color,
        [ centro[0], centro[1] - width ],
        [ centro[0], centro[1] + width ],
    fill)

    refresh()

def drawCirculo( pantalla, punto, radio = 2, color = getColors('rojo'), fill = 2):
    pygame.draw.circle( pantalla, color, cartersianoToPantalla( pantalla, punto), radio, fill)

def drawPoligono( pantalla, puntoCartesiano = [0,0], n = 5, width = 50, color = getColors('rojo')):

    g = 360/n
    Puntos = [ cartersianoToPantalla( pantalla, [ puntoCartesiano[0], puntoCartesiano[1] + width ])]

    for i in range(n-1):

        Puntos.append( cartersianoToPantalla( pantalla, trasladar( rotar( [ 0,width ], g*(i+1)), puntoCartesiano)))
        drawPunto( pantalla, trasladar( rotar( [ 0,width ], g*(i+1)), puntoCartesiano), 3, getColors('verde'))

    drawPunto( pantalla, [ puntoCartesiano[0],puntoCartesiano[1] + width ], 3, getColors('verde'))

    pygame.draw.polygon( pantalla, color, Puntos, 2)

def drawRosa( pantalla, punto = [0,0], n = 5, width = 100, color = getColors('rojo') ):

    Puntos = []

    if n == 1:
        for i in range(60):
            r = width * math.sin( toRadians( 3*i ))
            Puntos.append( cartersianoToPantalla( pantalla, trasladar( polarToCartesiano( [ r,i ] ), punto )))

    elif n%4 == 0:
        for i in range(360):

            r = width * math.sin( toRadians( (n/2) * i ))
            Puntos.append( cartersianoToPantalla( pantalla, trasladar( polarToCartesiano( [ r,i ] ), punto )))

    else:
        for i in range(180):

            r = width * math.sin( toRadians( n*i ))
            Puntos.append( cartersianoToPantalla( pantalla, trasladar( polarToCartesiano( [ r,i ] ), punto )))

    pygame.draw.polygon( pantalla, color, Puntos, 2)

def drawRiso( pantalla, punto = [0,0], width = 100, color = getColors('rojo')):

    Puntos = []

    for i in range(12*360): #12 Pi

        a = -0.9
        b = 3

        r = (a * width) + (b * width) * math.sin( toRadians( (145 * i) / 51 ))
        Puntos.append( cartersianoToPantalla( pantalla, trasladar( polarToCartesiano( [r,i]) , punto )))

    pygame.draw.polygon( pantalla, color, Puntos, 2)





# Movimientos

def rotar(  punto, grados = 90 ):

    xp = ( punto[0] * math.cos( toRadians(grados) )) - ( punto[1] * math.sin( toRadians(grados) ))
    yp = ( punto[0] * math.sin( toRadians(grados) )) + ( punto[1] * math.cos( toRadians(grados) ))

    return [ round(xp), round(yp) ]

def trasladar( punto , t = [5,5] ):

    x = punto[0] + t[0]
    y = punto[1] + t[1]

    return [ x,y ]

def rotarConCentro( centro, punto , grados = 90):

    xp = centro[0] + rotar( regress( punto,centro ), grados )[0]
    yp = centro[1] + rotar( regress( punto,centro ), grados )[1]

    return [ round(xp), round(yp) ]

def regress( punto , t = [5,5] ):

    x = punto[0] - t[0]
    y = punto[1] - t[1]

    return [ x,y ]






def scaledC( punto, centro, size = [2,2] ):

    xp = centro[0] + size[0] * ( punto[0] - centro[0] )
    yp = centro[1] + size[1] * ( punto[1] - centro[1] )

    return [ xp,yp ]

def scaled( punto, size = [2,2] ):

    xp = punto[0] * size[0]
    yp = punto[1] * size[1]

    return [ xp, yp ]

def move( punto, tipoMovimiento, t = 5):

    if tipoMovimiento == 1: # Arriba
        x = punto[0]
        y = punto[1]+t

    if tipoMovimiento == 2: # Abajo
        x = punto[0]
        y = punto[1]-t

    if tipoMovimiento == 3: # Izquiera
        x = punto[0]-t
        y = punto[1]

    if tipoMovimiento == 4: # Derecha
        x = punto[0]+t
        y = punto[1]

    return [ x,y ]

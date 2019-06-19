import pygame

#Miscelanea
def clean(p):
    p.fill(RGB().get('blanco'))
def up():
    pygame.display.flip()
def Centro(p):
    x=round(p.get_size()[0]/2)
    y=round(p.get_size()[1]/2)
    return [x,y]
def RGB():
    return dict(rojo=[255,0,0],negro=[0,0,0],blanco= [255,255,255],verde=[0,155,0],naranja=[250,140,10])
def reloj():
    return pygame.time.Clock()
def pantalla(title,size=[640,480]):
    pygame.init()
    pygame.display.set_caption(title)
    P=pygame.display.set_mode(size)
    return P

#Indicadores
def health(p,life,pto=[50,5],base=20):
    lifet = round((life/base)*100)
    font = pygame.font.Font(None, 25)
    if lifet <33:
        color = RGB().get('rojo')
    elif lifet <66:
        color = RGB().get('naranja')
    else:
        color = RGB().get('verde')
    vida = font.render('Health= '+str(lifet)+'%', True,color)
    p.blit(vida,pto)
def score(p,score,color=RGB().get('blanco'),pto=[50,45]):
    font = pygame.font.Font(None, 25)
    puntaje= font.render('Score= '+str(score), True,color)
    p.blit(puntaje,pto)
def gameover(p,score,color=RGB().get('blanco')):
    font = pygame.font.Font(None, 25)
    puntaje= font.render('Total Score= '+str(score), True,color)
    final= font.render('GAMEOVER', True,RGB().get('rojo'))
    end=pygame.sprite.Group()
    f=obj.Fondo(spt.final)
    end.add(f)
    end.draw(p)
    p.blit(puntaje,[Centro(p)[0]-round(p.get_size()[0]/12),Centro(p)[1]+40-round(p.get_size()[1]/12)])
    p.blit(final,[Centro(p)[0]-round(p.get_size()[0]/12)+10,Centro(p)[1]-round(p.get_size()[1]/12)])
    up()

#Control




#Conversiones
def CaToPo(pto):
    r=math.sqrt(pow(pto[0],2)+pow(pto[1],2))
    g=math.degrees(math.atan(pto[1]/pto[0]))
    return [r,g]
def PoToCa(crd):
    x=crd[0]*math.cos(math.radians(crd[1]))
    y=crd[0]*math.sin(math.radians(crd[1]))
    return [x,y]
def PaToCa(p,pto):
    x=pto[0]-round(p.get_size()[0]/2)
    y=round(p.get_size()[1]/2)-pto[1]
    return [x,y]
    '''
    Funcion pantalla a cartesiano
    p: Superficie de dibujo
    pto: Punto en la superficie
    '''
def CaToPa(p,pto):
    x=round(p.get_size()[0]/2)+pto[0]
    y=round(p.get_size()[1]/2)-pto[1]
    return [x,y]
    '''
    Funcion pantalla a cartesiano
    p: Superficie de dibujo
    pto: Punto en la superficie
    '''


#Formas
def Rosa(p,pto=[0,0],n=5,lg=100,cl=RGB().get('rojo')):
    Puntos = []
    if n==1:
        for i in range(60):
            r=lg*math.sin(math.radians(3*i))
            Puntos.append(CaToPa(p,translate(PoToCa([r,i]),pto)))
    elif n%4 == 0:
        for i in range(360):
            r=lg*math.sin(math.radians((n/2)*i))
            Puntos.append(CaToPa(p,translate(PoToCa([r,i]),pto)))
    else:
        for i in range(180):
            r=lg*math.sin(math.radians(n*i))
            Puntos.append(CaToPa(p,translate(PoToCa([r,i]),pto)))
    pygame.draw.polygon(p,cl,Puntos,2)
<<<<<<< HEAD
=======
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
    '''
        Funcion para recortar imagen

        Params
            filas: cantidad de sprites que tiene la imagen en las filas
            columnas: cantidad de sprites que tiene la imagen en la columnas
            imagen: nombre de la imagen (String) Ej: 'imagen1'
            limites[]: cantidad de sprites que tiene la imagen en cada fila
    '''
def cargarImagen(imagen):
    return pygame.image.load('img/'+imagen)
>>>>>>> feature/animacion

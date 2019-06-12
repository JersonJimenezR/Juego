
import pygame, math, fn, random, clases, objects, sprites



if __name__ == '__main__':

    ANCHO = 800
    ALTO = 800

    fin = False
    pantalla = fn.iniciar( [ANCHO,ALTO] )

    posicionJugador = [400,700]

    # Todos los sprites deben estar contenidos en un grupo

    # Creación de grupos

    jugadores = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balasRivales = pygame.sprite.Group()
    cabeceras = pygame.sprite.Group()

    # Jugadores

    jugador = clases.Jugador( posicionJugador )
    jugadores.add( jugador )



    nivel = 3

    if nivel == 1:
        vidas = 3
        numeroRivales = 10
        powerRival = 1000

    elif nivel == 2:
        vidas = 2
        numeroRivales = 15
        powerRival = 500

    elif nivel == 3:
        vidas = 1
        numeroRivales = 20
        powerRival = 100


    puntos = 0
    fin_juego = False
    balasDisparadasJugador = 0
    balasDisparadasRival = 0

    # Rivales

    for nuevoRival in objects.createRivals( numeroRivales, pantalla ):
        rivales.add( nuevoRival )



while not ( fin or fin_juego ):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            fin = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
               jugador.velx = 5
               jugador.vely = 0
               jugador.image = sprites.getImage( 'iron-right' )

            if event.key == pygame.K_LEFT:
                jugador.velx = -5
                jugador.vely = 0
                jugador.image = sprites.getImage( 'iron-left' )

            if event.key == pygame.K_UP:
               jugador.vely = 0
               jugador.velx = 0
               jugador.image = sprites.getImage( 'iron-standBy' )

            if event.key == pygame.K_DOWN:
                jugador.vely = 0
                jugador.velx = 0
                jugador.image = sprites.getImage( 'iron-standBy' )

            if event.key == pygame.K_SPACE:

                b = clases.BalaJugador([ jugador.rect.x + 10 , jugador.rect.y ])
                b.vely = -7
                balas.add(b)
                balasDisparadasJugador +=1

        if event.type == pygame.KEYUP:

            if event.type == pygame.K_RIGHT:
                j.velx = 0

            if event.type == pygame.K_LEFT:
                j.velx = 0

    # Control

    for j in jugadores:

        if j.rect.x > ANCHO:
            j.rect.x = 0
            j.velx = 5

        if j.rect.x < -1 :
            j.rect.x = ANCHO - (j.rect.width)
            j.velx = -5

        if j.rect.y > ALTO:
            j.rect.y = 0
            j.vely = +5

        if j.rect.y < 0 :
            j.rect.y = ALTO -j.rect.height
            j.vely = -5

        vidas = j.vidas


    for r in rivales:

        if r.rect.x > ( ANCHO - r.rect.width ):
            # r.rect.x =
            r.velx = -3

        if r.rect.x < 0:
            # r.rect.x =
            r.velx = 3

        if r.tiempo <= 0:
            b = clases.BalaRival( [ r.rect.x , r.rect.y] )
            b.vely = 5
            balasRivales.add( b )
            r.tiempo = random.randrange( powerRival )
            balasDisparadasRival +=1


    for b in balas:

        for e in pygame.sprite.spritecollide(b, rivales, True):
            balas.remove( b )
            puntos += 1

        # Eliminar balas

        if b.rect.y < -10:
            balas.remove( b )

        # Si existen menos de n rivales se deben crear más

        if len( rivales ) < 5:

            for nuevoRival in objects.createRivals( numeroRivales, pantalla ):
                rivales.add( nuevoRival )


    for balaRival in balasRivales:

        # En la lista ls quedan guardados los jugadores que la bala le pego

        ls = pygame.sprite.spritecollide( balaRival, jugadores, False)

        for jugadorEliminado in ls:

            vidas -= 1
            balasRivales.remove( balaRival )
            jugadorEliminado.vidas -= 1

            if jugadorEliminado.vidas <= 0:
                ls = pygame.sprite.spritecollide( balaRival, jugadores, True)
                fin_juego = True

        # Eliminar balasRivales que salieron de pantalla

        if balaRival.rect.y > ALTO:
            balasRivales.remove( balaRival )




    # Refresh

    fn.limpiarPantalla( pantalla )

    # Cabecera

    objects.text( pantalla, [ 50,50 ], 'Vidas: ' + str(vidas) )
    objects.text( pantalla, [ 50,80 ], 'Score: ' + str( puntos ))

    objects.text( pantalla, [ 300,50 ], 'Balas Jugador: ' + str( balasDisparadasJugador ))
    objects.text( pantalla, [ 300,80 ], 'Balas Rival: ' + str( balasDisparadasRival ))

    objects.text( pantalla, [ 550,50 ], 'Nivel de juego: ' + str( nivel ))


    # Actualizar posiciones

    jugadores.update()
    rivales.update()
    balas.update()
    balasRivales.update()

    # Dibujar

    jugadores.draw( pantalla )
    rivales.draw( pantalla )
    balas.draw( pantalla )
    balasRivales.draw( pantalla )
    cabeceras.draw( pantalla )

    fn.refresh()

fn.limpiarPantalla( pantalla )
objects.text( pantalla, [ 400,400 ], 'Fin de Juego' )
objects.text( pantalla, [ 400,350 ], 'Puntos obtenidos: ' + str( puntos ))
fn.refresh()

fin = False

while not fin:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            fin = True

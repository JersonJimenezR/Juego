
import pygame, math, gm, obj



if __name__ == '__main__':

    ANCHO = 800
    ALTO = 800

    fin = False
    pantalla = gm.pantalla('Animacion Juego', [ANCHO,ALTO],  )

    imagenRecortada = gm.recortarImagen( 8, 12, 'animales.png', [12,12,12,12,12,12,12,12] )
    contador = 0



while not fin:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            fin = True

    gm.clean( pantalla )
    pantalla.blit( imagenRecortada[0][ contador ] , [40,40])
    gm.up()

    contador += 1

    if contador > 2:
        contador = 0


    gm.reloj().tick(5)

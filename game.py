
import pygame, math, fn, random, clases, objects, sprites



if __name__ == '__main__':

    ANCHO = 800
    ALTO = 800

    fin = False
    pantalla = fn.iniciar( [ANCHO,ALTO] )

    imagenRecortada = objects.recortarImagen( 8, 12, 'animales', [12,12,12,12,12,12,12,12] )
    contador = 0



while not fin:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            fin = True

    fn.limpiarPantalla( pantalla )
    pantalla.blit( imagenRecortada[0][ contador ] , [40,40])
    fn.refresh()

    contador += 1

    if contador > 2:
        contador = 0


    fn.reloj().tick(5)

# imagenRecortada = objects.recortarImagen( 8, 12, 'animales', [12,12,12,12,12,12,12,12] )
# contador = 0

# contador += 1
#
# if contador > 2:
#     contador = 0

import pygame,math,random, obj, gm

if __name__ == '__main__':

    size = [620,465]
    pantalla=gm.pantalla("Juego_Goku",size)
    fin =False
    gameover = False
    life = 20
    score = 0
    level=200

    # Grupos de sprites
    muertes=pygame.sprite.Group()
    estados=pygame.sprite.Group()
    fondos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    poderes=pygame.sprite.Group()
    rivalpoderes=pygame.sprite.Group()
    rivales=pygame.sprite.Group()

    # creación del fondo
    f=obj.Fondo('fondo.jpg')
    fondos.add(f)

    # creación del jugador
    pto=[310,410] #ubicación inicial del jugador
    vj=[3,3] #velocidad del jugador
    j=obj.Jugador('goku stop.png')
    jugadores.add(j)

    # creación de n rivales
    gm.CreateRv('Saibaman right.png',10,rivales)

while not (fin or gameover):

    # Movimientos de personaje
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jugadores.remove(j)
                j = obj.Jugador([j.rect.x,j.rect.y],'goku up.png')
                jugadores.add(j)
                j.vely = -vj[1]
                j.velx = 0
            if event.key == pygame.K_DOWN:
                jugadores.remove(j)
                j = obj.Jugador([j.rect.x,j.rect.y],'goku down.png')
                jugadores.add(j)
                j.vely = vj[1]
                j.velx = 0
            if event.key == pygame.K_LEFT:
                jugadores.remove(j)
                j = obj.Jugador([j.rect.x,j.rect.y],'goku left.png')
                jugadores.add(j)
                j.velx = -vj[0]
                j.vely = 0
            if event.key == pygame.K_RIGHT:
                jugadores.remove(j)
                j = obj.Jugador([j.rect.x,j.rect.y],'goku right.png')
                jugadores.add(j)
                j.velx = vj[0]
                j.vely = 0
            if event.key == pygame.K_SPACE:
                # creación de la bala
                jugadores.remove(j)
                j = obj.Jugador([j.rect.x,j.rect.y],'goku stop.png')
                jugadores.add(j)
                p = obj.Poder([j.rect.x,j.rect.y],'power.png')
                p.vely = -3
                poderes.add(p)

        if event.type == pygame.KEYUP:
            jugadores.remove(j)
            j = obj.Jugador([j.rect.x,j.rect.y],'goku stop.png')
            jugadores.add(j)
            j.vely = 0
            j.velx = 0

    # Control de jugador y rivales en pantalla
    for j in jugadores:

        if j.rect.x > (size[0] + j.rect.width) :
            j.rect.x = 0
            j.velx = vj[0]

        if j.rect.x < 0 - j.rect.height:
            j.rect.x = size[0]
            j.velx = -vj[0]

        if j.rect.y > (size[1] + j.rect.height) :
            j.rect.y = 0
            j.vely = vj[1]

        if j.rect.y < 0 - j.rect.height:
            j.rect.y = size[1]
            j.vely = -vj[1]
    for r in rivales:
        if r.rect.x > (size[0] - r.rect.width) :
            rivales.remove(r)
            r = obj.Rival([r.rect.x,r.rect.y],'Saibaman left.png')
            r.velx = -2
            rivales.add(r)
        if r.rect.x < 0:
            rivales.remove(r)
            r = obj.Rival([r.rect.x,r.rect.y],'Saibaman right.png')
            r.velx = 2
            rivales.add(r)
        if random.randrange(level)>=int(level*0.999):
            rivales.remove(r)
            rs = obj.Rival([r.rect.x,r.rect.y],'Saibaman shoot.png')
            rs.velx = r.velx
            rivales.add(rs)
            rp = obj.Poder([r.rect.x,r.rect.y],'rivalpower.png')
            rp.vely = 2
            rivalpoderes.add(rp)

    # Ataques
    for p in poderes:
        for r in rivales:
            if pygame.sprite.collide_rect(r,p):
                rivales.remove(r)
                poderes.remove(p)
                score += 1
                m = obj.Muerte([r.rect.x,r.rect.y],'death.png')
                muertes.add(m)
        if p.rect.y < -50:
            poderes.remove(p)
        if len(rivales) <= 3: #len = cantidad en grupo
            gm.CreateRv('Saibaman right.png',6,rivales)
    for rp in rivalpoderes:
        for j in jugadores:
            if pygame.sprite.collide_rect(rp,j):
                rivalpoderes.remove(rp)
                life -= 1
                m = obj.Muerte([j.rect.x,j.rect.y],'death.png')
                muertes.add(m)
        if rp.rect.y > size[1]+50:
            poderes.remove(rp)
    for m in muertes:
        if m.time==0:
            muertes.remove(m)

    # Final del Juego
    if life == 0:
        gameover = True

    # Indicadores, estados, dibujado y refresco
    # Indicadores
    fondos.draw(pantalla)
    gm.StGoku(life,estados,[5,5])
    gm.health(pantalla,life)
    gm.score(pantalla,score)
    # Estado
    estados.draw(pantalla)
    jugadores.update()
    rivales.update()
    poderes.update()
    rivalpoderes.update()
    muertes.update()
    # Dibujado
    jugadores.draw(pantalla)
    rivales.draw(pantalla)
    rivalpoderes.draw(pantalla)
    poderes.draw(pantalla)
    muertes.draw(pantalla)
    # Refresco
    gm.up()
    gm.reloj().tick(400)

gm.gameover(pantalla,score)
while not (fin):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

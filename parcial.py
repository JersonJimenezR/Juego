import pygame,math,random, obj, gm

if __name__ == '__main__':

    size = [640,480]
    pantalla=gm.pantalla("Parcial",size)
    fin =False
    gameover = False
    life = 20
    score = 0
    level=500
    typeJugador=2
    toques=0

    # Grupos de sprites
    jugador=pygame.sprite.Group()
    enemigoX=pygame.sprite.Group()
    enemigoY=pygame.sprite.Group()
    shits=pygame.sprite.Group()
    muertes=pygame.sprite.Group()
    pisses=pygame.sprite.Group()


    # creación del jugador
    pto=[304,60] #ubicación inicial del jugador
    vj=[3,3] #velocidad del jugador
    j=obj.Jugador(pto,gm.recortarImagen(16,14,'chocobo_sheet.png'))
    # j=obj.Jugador(pto,gm.recortarImagen(16,14,'werewolf.png'))
    jugador.add(j)

    # creación de n rivales en y
    gm.CreateRv(gm.recortarImagen(16,14,'chocobo_sheet.png'),3,enemigoX)

    # creación de n rivales en x
    gm.CreateRv(gm.recortarImagen(16,14,'chocobo_sheet.png'),3,enemigoY)

    # m=obj.Muro([100,150],gm.recortarImagen(12,16,'terrenogen.png'))
    # muros.add(m)

    # Estadisticas

    balasJugador=0
    balasRival=0
    colisionesJugador=0
    colisionesRival=0

while not (fin or gameover):

    # Movimientos de personaje
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                j.vely = -vj[1]
                j.velx = 0
                typeJugador = 1
            if event.key == pygame.K_DOWN:
                j.vely = vj[1]
                j.velx = 0
                typeJugador = 2
            if event.key == pygame.K_LEFT:
                j.velx = -vj[0]
                j.vely = 0
                typeJugador = 3
            if event.key == pygame.K_RIGHT:
                j.velx = vj[0]
                j.vely = 0
                typeJugador = 4
            if event.key == pygame.K_SPACE:
                # creación de la bala
                p = obj.Poder([j.rect.x,j.rect.y],'shits.png')
                p.vely = 3
                shits.add(p)
                balasJugador+=1
        #
        if event.type == pygame.KEYUP:
            # gm.clean(pantalla)
            j.vely = 0
            j.velx = 0
            typeJugador = 2

    # Control de colisiones

    # for m in muros:
    #     for p in shits:
    #         if pygame.sprite.collide_rect(m,p):
    #             shits.remove(p)
    #             m = obj.Muerte([p.rect.x,p.rect.y],'death.png')
    #             muertes.add(m)
    #     for rp in pisses:
    #         if pygame.sprite.collide_rect(m,rp):
    #             pisses.remove(rp)
    #             m = obj.Muerte([rp.rect.x,rp.rect.y],'death.png')
    #             muertes.add(m)
    #     for j in jugador:
    #         if pygame.sprite.collide_rect(m,j):
    #             if j.rect.bottom> m.rect.top and (j.vely >0):
    #                 j.rect.bottom = m.rect.top
    #             elif j.rect.top < m.rect.bottom and (j.vely <0):
    #                 j.rect.top = m.rect.bottom
    #             elif (j.rect.right > m.rect.left) and (j.velx >0):
    #                 j.rect.right = m.rect.left
    #             elif j.rect.left < m.rect.right and (j.velx <0):
    #                 j.rect.left = m.rect.right
    #             j.vely = 0
    #             j.velx = 0
    #

    #

     for jug in jugador

        ls = pygame.sprite.spritecollide( jug, ratas, False):

        for final in ls:
            toques += 1
            print( toques )

    # Control de salida en pantalla

    for j in jugador:

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

    for r in enemigoX:
        if r.rect.x > (size[0] - r.rect.width) :
            r.velx = -2
            r.type = 3
        if r.rect.x < 0:
            r.velx = 2
            r.type = 4
        if random.randrange(level)>=int(level*0.999):
            rp = obj.Poder([r.rect.x,r.rect.y],'pis.png')
            rp.vely = -2
            pisses.add(rp)
            # balasRival+=1

    for r in enemigoY:
        if r.rect.y > (size[1] - r.rect.height) :
            r.vely = -2
            r.type = 3
        if r.rect.y < 0:
            r.vely = 2
            r.type = 4
        if random.randrange(level)>=int(level*0.999):
            rp = obj.Poder([r.rect.x,r.rect.y],'pis.png')
            rp.velx = 2
            pisses.add(rp)
            # balasRival+=1

    # # Ataques
    for p in shits:
        for r in enemigoX:
            if pygame.sprite.collide_rect(r,p):
                enemigoX.remove(r)
                shits.remove(p)
                score += 1
        if p.rect.y > size[1]+50:
            shits.remove(p)
        if len(enemigoX) <= 3: #len = cantidad en grupo
            gm.CreateRv(gm.recortarImagen(16,14,'chocobo_sheet.png'),6,enemigoX)

    for p in shits:
        for r in enemigoY:
            if pygame.sprite.collide_rect(r,p):
                enemigoY.remove(r)
                shits.remove(p)
                score += 1
        if p.rect.y > size[1]+50:
            shits.remove(p)
        if len(enemigoY) <= 3: #len = cantidad en grupo
            gm.CreateRv(gm.recortarImagen(16,14,'chocobo_sheet.png'),6,enemigoY)

    for rp in pisses:
        for j in jugador:
            if pygame.sprite.collide_rect(rp,j):
                pisses.remove(rp)
                life -= 1
        if rp.rect.y < -50:
            pisses.remove(rp)
    # for m in muertes:
    #     if m.time==0:
    #         muertes.remove(m)


    # # Final del Juego
    # if life == 0:
    #     gameover = True

    # Indicadores, estados, dibujado y refresco
    # Indicadores
    # fondos.draw(pantalla)
    # gm.StGoku(life,estados,[5,5])
    # gm.health(pantalla,life)
    # gm.score(pantalla,score)
    # # Estado
    # estados.draw(pantalla)
    jugador.update(pantalla,typeJugador)
    shits.update()
    enemigoX.update(pantalla)
    enemigoY.update(pantalla)
    pisses.update()
    # muertes.update()
    # Dibujado
    jugador.draw(pantalla)
    shits.draw(pantalla)
    enemigoX.update(pantalla)
    enemigoY.draw(pantalla)
    pisses.draw(pantalla)
    # muertes.draw(pantalla)
    # muros.draw(pantalla)
    # Refresco
    gm.up()
    gm.reloj().tick(100)

    # Mostrar Estadisticas

    # gm.message(pantalla, 'Balas Jugador: '+ str(balasJugador), [100,20])
    # gm.message(pantalla, 'Balas Rival: '+ str(balasRival), [100,40])


# gm.gameover(pantalla,score)
# while not (fin):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             fin = True

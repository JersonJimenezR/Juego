# imagenRecortada = objects.recortarImagen( 8, 12, 'animales', [12,12,12,12,12,12,12,12] )
# contador = 0

# contador += 1
#
# if contador > 2:
#     contador = 0

import pygame,math,random, obj, gm

if __name__ == '__main__':

    size = [640,480]
    pantalla=gm.pantalla("Palomas",size)
    fin =False
    gameover = False
    life = 20
    score = 0
    level=500
    typepaloma=2

    # Grupos de sprites
    palomas=pygame.sprite.Group()
    shits=pygame.sprite.Group()
    muertes=pygame.sprite.Group()
    pisses=pygame.sprite.Group()
    ratas=pygame.sprite.Group()

    # creación del jugador
    pto=[304,60] #ubicación inicial del jugador
    vj=[3,3] #velocidad del jugador
    j=obj.Jugador(pto,gm.recortarImagen(8,12,'animales.png'))
    palomas.add(j)

    # creación de n rivales
    # gm.CreateRv('Saibaman right.png',10,rivales)

while not (fin or gameover):

    # Movimientos de personaje
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                j.vely = -vj[1]
                j.velx = 0
                typepaloma = 1
            if event.key == pygame.K_DOWN:
                j.vely = vj[1]
                j.velx = 0
                typepaloma = 2
            if event.key == pygame.K_LEFT:
                j.velx = -vj[0]
                j.vely = 0
                typepaloma = 3
            if event.key == pygame.K_RIGHT:
                j.velx = vj[0]
                j.vely = 0
                typepaloma = 4
            if event.key == pygame.K_SPACE:
                # creación de la bala
                p = obj.Poder([j.rect.x,j.rect.y],'shits.png')
                p.vely = 3
                shits.add(p)
        #
        if event.type == pygame.KEYUP:
            gm.clean(pantalla)
            j.vely = 0
            j.velx = 0
            typepaloma = 2

    # Control de jugador y rivales en pantalla
    for j in palomas:

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
    # for r in rivales:
    #     if r.rect.x > (size[0] - r.rect.width) :
    #         rivales.remove(r)
    #         r = obj.Rival([r.rect.x,r.rect.y],'Saibaman left.png')
    #         r.velx = -2
    #         rivales.add(r)
    #     if r.rect.x < 0:
    #         rivales.remove(r)
    #         r = obj.Rival([r.rect.x,r.rect.y],'Saibaman right.png')
    #         r.velx = 2
    #         rivales.add(r)
    #     if random.randrange(level)>=int(level*0.999):
    #         rivales.remove(r)
    #         rs = obj.Rival([r.rect.x,r.rect.y],'Saibaman shoot.png')
    #         rs.velx = r.velx
    #         rivales.add(rs)
    #         rp = obj.Poder([r.rect.x,r.rect.y],'rivalpower.png')
    #         rp.vely = 2
    #         rivalpoderes.add(rp)
    #
    # # Ataques
    # for p in poderes:
    #     for r in rivales:
    #         if pygame.sprite.collide_rect(r,p):
    #             rivales.remove(r)
    #             poderes.remove(p)
    #             score += 1
    #             m = obj.Muerte([r.rect.x,r.rect.y],'death.png')
    #             muertes.add(m)
    #     if p.rect.y < -50:
    #         poderes.remove(p)
    #     if len(rivales) <= 3: #len = cantidad en grupo
    #         gm.CreateRv('Saibaman right.png',6,rivales)
    # for rp in rivalpoderes:
    #     for j in palomas:
    #         if pygame.sprite.collide_rect(rp,j):
    #             rivalpoderes.remove(rp)
    #             life -= 1
    #             m = obj.Muerte([j.rect.x,j.rect.y],'death.png')
    #             muertes.add(m)
    #     if rp.rect.y > size[1]+50:
    #         poderes.remove(rp)
    # for m in muertes:
    #     if m.time==0:
    #         muertes.remove(m)
    #
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
    palomas.update(pantalla,typepaloma)
    shits.update()
    # rivales.update()
    # rivalpoderes.update()
    # muertes.update()
    # Dibujado
    palomas.draw(pantalla)
    shits.draw(pantalla)
    # rivales.draw(pantalla)
    # rivalpoderes.draw(pantalla)
    # muertes.draw(pantalla)
    # Refresco
    gm.up()
    gm.reloj().tick(100)

# gm.gameover(pantalla,score)
# while not (fin):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             fin = True

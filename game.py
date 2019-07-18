import pygame,math,random, obj, gm

if __name__ == '__main__':

    size = [1080,680]
    pantalla=gm.pantalla("Goku saves the Universe",size)
    fin =False
    intro = True
    historia = True
    gameover = False
    direccion = 0
    life = 60
    score = 0
    level=1000
    typegoku = 0
    fase = 1
    saltos = 0
    limite = [50,150]

    # Grupos de sprites
    muertes=pygame.sprite.Group()
    estados=pygame.sprite.Group()
    fondos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    poderes=pygame.sprite.Group()
    rivalpoderes=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    muros=pygame.sprite.Group()

    # creación del fondo
    vf=[0,0]
    f=obj.Fondo('portada.png')
    fondos.add(f)

    # creación del jugador
    ptojugador=[50,size[1]-50] #ubicación inicial del jugador
    vj=[6,6] #velocidad del jugador
    j=obj.Jugador(ptojugador,gm.recortarImagen(16,25,'goku1.png'))
    jugadores.add(j)

    # creación de n rivales
    gm.CreateRv(gm.recortarImagen(8,12,'saibaman.png'),10,rivales)

    #creación de plataformas

    m=obj.Muro([300,640],gm.recortarMapa(2,14,'plataformas.png'),[0,0])
    muros.add(m)
    m2=obj.Muro([340,640],gm.recortarMapa(2,14,'plataformas.png'),[0,1])
    muros.add(m2)
    m3=obj.Muro([380,640],gm.recortarMapa(2,14,'plataformas.png'),[0,2])
    muros.add(m3)


# while (intro):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             intro = False
#             fin =True
#             historia = False
#             gameover = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
#                 intro = False
#     fondos.draw(pantalla)
#     fondos.update()
#     gm.up()
#
# fondos.remove(f)
# f=obj.Fondo('historia.png')
# fondos.add(f)
# while (historia):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             intro = False
#             fin =True
#             historia = False
#             gameover = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
#                 historia = False
#     fondos.draw(pantalla)
#     fondos.update()
#     gm.up()

fondos.remove(f)
f=obj.Fondo('fondo.png')
fondos.add(f)

while not (fin or gameover):
    # print(direccion,j.velx,j.vely)
    # Movimientos de personaje
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if fase == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    saltos += 1
                    if saltos == 1:
                        if direccion == 0:
                            jugadores.remove(j)
                            j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,3,'gokuupdownright.png'))
                            jugadores.add(j)
                            j.velx =+1.5
                            typegoku = 1
                        elif direccion == 1:
                            jugadores.remove(j)
                            j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,3,'gokuupdownleft.png'))
                            jugadores.add(j)
                            j.velx =-1.5
                            typegoku = 2
                        j.vely =-4
                if event.key == pygame.K_LEFT:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,6,'gokuleft.png'))
                    jugadores.add(j)
                    j.velx = -vj[0]
                    j.vely = vj[1]
                    direccion = 1
                    typegoku = 3
                if event.key == pygame.K_RIGHT:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,6,'gokuright.png'))
                    jugadores.add(j)
                    j.velx = vj[0]
                    j.vely = vj[1]
                    direccion = 0
                    typegoku = 4
                if event.key == pygame.K_SPACE:
                    # creación de la bala
                    if direccion == 0:
                        p = obj.Poder([j.rect.x,j.rect.y+round(j.rect.height/3)],'powerright.png')
                        p.velx = 3
                        poderes.add(p)
                    elif direccion == 1:
                        p = obj.Poder([j.rect.x,j.rect.y+round(j.rect.height/3)],'powerleft.png')
                        p.velx = -3
                        poderes.add(p)
            if event.type == pygame.KEYUP:
                if direccion == 0:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,7,'gokustaticright.png'))
                    jugadores.add(j)
                    typegoku = 0
                elif direccion == 1:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,7,'gokustaticleft.png'))
                    jugadores.add(j)
                    typegoku = -1
                j.vely = vj[1]
                j.velx = 0
                f.velx = 0
                for m in muros:
                    m.velx = 0
                for rp in rivalpoderes:
                    rp.velx = rp.velx
                for r1 in rivales:
                    r1.velx = r1.velx

        elif fase == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,3,'gokuupdown.png'))
                    jugadores.add(j)
                    j.vely = -6
                    j.velx = 0
                    typegoku = 1
                if event.key == pygame.K_DOWN:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,3,'gokuupdown.png'))
                    jugadores.add(j)
                    j.velx = 0
                    typegoku = 2
                if event.key == pygame.K_LEFT:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,6,'gokuleft.png'))
                    jugadores.add(j)
                    j.velx = -vj[0]
                    j.vely = vj[1]
                    f.velx = vj[0]
                    typegoku = 3
                if event.key == pygame.K_RIGHT:
                    jugadores.remove(j)
                    j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,6,'gokuright.png'))
                    jugadores.add(j)
                    j.velx = vj[0]
                    j.vely = vj[1]
                    typegoku = 4
                    f.velx = -vj[0]
                if event.key == pygame.K_SPACE:
                    # creación de la bala
                    p = obj.Poder([j.rect.x,j.rect.y],'powerright.png')
                    p.velx = 3
                    poderes.add(p)

            if event.type == pygame.KEYUP:
                jugadores.remove(j)
                j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(16,25,'goku1.png'))
                jugadores.add(j)
                j.vely = vj[1]
                j.velx = 0
                typegoku = 0
                f.velx = 0

    # Control de jugador y rivales en pantalla
    for j in jugadores:

        if j.rect.left > size[0]-limite[1]:
            if f.rect.x < size[0]*5-limite[1]:
                j.rect.x = size[0]-limite[1]
                j.velx = 0
                f.velx =-vj[0]
                for m in muros:
                    m.velx =- vj[0]
                for rp in rivalpoderes:
                    rp.velx =- vj[0]
                for r1 in rivales:
                    r1.velx =- vj[0]
            else:
                j.rect.x = size[0]-limite[1]
                j.velx = 0
                f.velx = 0
        if j.rect.left < 0+limite[0]:
            if f.rect.x < 0:
                j.rect.x = limite[0]
                f.velx =vj[0]
                for m in muros:
                    m.velx = vj[0]
                for rp in rivalpoderes:
                    rp.velx = vj[0]
                for r1 in rivales:
                    r1.velx = vj[0]
                j.velx = 0
            elif f.rect.x >= 0:
                j.rect.x = limite[0]
                f.rect.x = 0
                f.velx = 0
                j.velx = 0
        if j.rect.bottom > size[1]:
            j.rect.y = size[1]-j.rect.height
            j.vely -=1
            saltos = 0
        if j.rect.bottom < 0:
            j.rect.y = 0
            j.vely = vj[1]
    for r in rivales:
        if r.rect.x > (size[0] - r.rect.width) :
            r.velx = -2
            r.type = 3
        if r.rect.x < 0:
            r.velx = 2
            r.type = 4
        if random.randrange(level)>=int(level*0.999):
            rp = obj.Poder([r.rect.x,r.rect.y],'rivalpowerleft.png')
            rp.velx = -3
            rivalpoderes.add(rp)
        if r.rect.bottom > size[1]:
            r.rect.y = size[1]-r.rect.height
            r.vely -=1

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

    # Control de colisiones

    for m in muros:
        for p in poderes:
            if pygame.sprite.collide_rect(m,p):
                poderes.remove(p)
                m = obj.Muerte([p.rect.x,p.rect.y],'death.png')
                muertes.add(m)
        for rp in rivalpoderes:
            if pygame.sprite.collide_rect(m,rp):
                rivalpoderes.remove(rp)
                m = obj.Muerte([rp.rect.x,rp.rect.y],'death.png')
                muertes.add(m)
        for j in jugadores:
            if pygame.sprite.collide_rect(m,j):
                if j.rect.bottom> m.rect.top :
                    j.rect.bottom = m.rect.top
                    j.vely -=1
                elif j.rect.top < m.rect.bottom :
                    j.rect.top = m.rect.bottom
                elif j.rect.right >  m.rect.left and j.rect.left <  m.rect.left:
                    j.rect.right = m.rect.left
                elif j.rect.left < m.rect.right and j.rect.right > m.rect.right:
                    j.rect.left = m.rect.right
        for r in rivales:
            if pygame.sprite.collide_rect(m,r):
                if (r.rect.right > m.rect.left) and (r.velx >0):
                    r.velx *= -1
                elif r.rect.left < m.rect.right and (r.velx <0):
                    r.velx *= -1

    # Final del Juego
    if life <= 0:
        gameover = True
    # Indicadores, estados, dibujado y refresco
    # Indicadores
    fondos.draw(pantalla)
    gm.StGoku(life,estados,[5,5])
    gm.health(pantalla,life)
    gm.score(pantalla,score)
    # Estado
    estados.draw(pantalla)
    jugadores.update(typegoku)
    rivales.update()
    poderes.update()
    rivalpoderes.update()
    fondos.update()
    muros.update()
    muertes.update()
    # Dibujado
    jugadores.draw(pantalla)
    rivales.draw(pantalla)
    rivalpoderes.draw(pantalla)
    poderes.draw(pantalla)
    muertes.draw(pantalla)
    muros.draw(pantalla)
    # Refresco
    gm.up()
    # gm.reloj().tick(1200)
gm.gameover(pantalla,score)
while not (fin):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

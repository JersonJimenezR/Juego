import pygame,math,random, obj, gm

if __name__ == '__main__':

    size = [1080,680]
    pantalla=gm.pantalla("Goku saves the Universe",size)
    fin =False
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
    f=obj.Fondo('fondo.png')
    fondos.add(f)

    # creación del jugador
    ptojugador=[50,size[1]-50] #ubicación inicial del jugador
    vj=[3,3] #velocidad del jugador
    j=obj.Jugador(ptojugador,gm.recortarImagen(16,25,'goku1.png'))
    jugadores.add(j)

    # creación de n rivales
    gm.CreateRv(gm.recortarImagen(8,12,'saibaman.png'),10,rivales)

    #creación de plataformas

    # m=obj.Muro([500,610],gm.recortarImagen(12,16,'terrenogen.png'))
    # muros.add(m)


while not (fin or gameover):

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
                            j.velx =+1
                            typegoku = 1
                        elif direccion == 1:
                            jugadores.remove(j)
                            j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,3,'gokuupdownleft.png'))
                            jugadores.add(j)
                            j.velx =-1
                            typegoku = 2
                        j.vely =-5
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
                    p = obj.Poder([j.rect.x,j.rect.y],'powerright.png')
                    p.velx = 3
                    poderes.add(p)

            if event.type == pygame.KEYUP:
                # if direccion == 0:
                jugadores.remove(j)
                j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,7,'gokustaticright.png'))
                jugadores.add(j)
                typegoku = 0
                # elif direccion == 1:
                #     jugadores.remove(j)
                #     j=obj.Jugador([j.rect.x,j.rect.y],gm.recortarImagen(1,7,'gokustaticleft.png'))
                #     jugadores.add(j)
                #     typegoku = -1
                j.vely = vj[1]
                j.velx = 0
                f.velx = 0
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
            else:
                j.rect.x = size[0]-limite[1]
                j.velx = 0
                f.velx = 0

        if j.rect.left < 0+limite[0]:
            if f.rect.x < 0:
                j.rect.x = limite[0]
                f.velx =vj[0]
                j.velx = 0
            elif f.rect.x >= 0:
                j.rect.x = limite[0]
                f.rect.x = 0
                f.velx = 0
                j.velx = 0

        if j.rect.bottom > size[1]:
            j.rect.y = size[1]-j.rect.height
            j.vely =-0.2
            saltos = 0

        if j.rect.bottom < 0:
            j.rect.y = size[1]
            j.vely = -vj[1]
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
            gm.CreateRv(gm.recortarImagen(8,12,'saibaman.png'),6,rivales)
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
                if j.rect.bottom> m.rect.top and (j.vely >0):
                    j.rect.bottom = m.rect.top
                elif j.rect.top < m.rect.bottom and (j.vely <0):
                    j.rect.top = m.rect.bottom
                elif (j.rect.right > m.rect.left) and (j.velx >0):
                    j.rect.right = m.rect.left
                elif j.rect.left < m.rect.right and (j.velx <0):
                    j.rect.left = m.rect.right
                j.vely = 0
                j.velx = 0

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

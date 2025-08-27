from generalinfo import *
pieces=piececheck(cheesboardmap)
def clickedspace(map,x,y):
    tilevalue=map[y][x]
    if tilevalue=="..":
        return None
    if tilevalue[1]!=turn:
        return None
    else:
        index=None
        for i in range(len(pieces)):
            if pieces[i].x==x and pieces[i].y==y:
                index=i
                break
    return index
def render():
    window.blit(textures["board"],(0,0))
    for i in range(8):
        for j in range(8):
            currentpiece=cheesboardmap[i][j]
            if currentpiece=="..":
                continue
            currentpiece=currentpiece[0]
            if currentpiece=="p":
                slika="pesak"
            if currentpiece=="t":
                slika="top"
            if currentpiece=="s":
                slika="skakac"
            if currentpiece=="l":
                slika="lovac"
            if currentpiece=="k":
                slika="kralj"
            if currentpiece=="d":
                slika="dama"
            window.blit(textures[f"{slika}{cheesboardmap[i][j][1]}"],(j*(WIDTH/8)-(textures[f"{slika}{cheesboardmap[i][j][1]}"].get_width()/2)+(WIDTH/8/2),i*(HEIGHT/8)-(textures[f"{slika}{cheesboardmap[i][j][1]}"].get_height()/2)+(HEIGHT/8/2)))
breaksure=0
turn="w"
while True:
    window.fill("Black")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    if mouseState[0]:
        try:
            polje=cheesboardmap[int(mousePos[1]//(WIDTH/8))][int(mousePos[0]//(WIDTH/8))]
            print(polje)
        except:
            pass
    if keys[pygame.K_ESCAPE]:
        break
    for event in events:
        if event.type == pygame.QUIT:
            breaksure=1
    if breaksure==1:
        break
    render()
    pygame.display.update()
    clock.tick(60)
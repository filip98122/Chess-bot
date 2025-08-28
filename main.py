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

def clickedspacezap(map,x,y):
    tilevalue=map[y][x]
    if tilevalue=="..":
        return None
    if tilevalue[1]==turn:
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
turn="c"
nemoj=False
places=[]
while True:
    window.fill("Black")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    if mouseState[0]:
        try:
            polje=cheesboardmap[int(mousePos[1]//(WIDTH/8))][int(mousePos[0]//(WIDTH/8))]
            
            for i in range(len(places)):
                if places[i][0]==int(mousePos[1]//(WIDTH/8)) and places[i][1]==int(mousePos[0]//(WIDTH/8)):
                    try:
                        pojedena=clickedspacezap(cheesboardmap,int(mousePos[0]//(WIDTH/8)),int(mousePos[1]//(WIDTH/8)))
                        pieces[pojedena].alive=False
                    except:
                        pass
                    try:
                        pieces[pieceindex].moved=True
                    except:
                        pass
                    cheesboardmap[int(mousePos[1]//(WIDTH/8))][int(mousePos[0]//(WIDTH/8))]=cheesboardmap[pieces[pieceindex].y][pieces[pieceindex].x]
                    cheesboardmap[pieces[pieceindex].y][pieces[pieceindex].x]=".."
                    pieces[pieceindex].x=int(mousePos[0]//(WIDTH/8))
                    pieces[pieceindex].y=int(mousePos[1]//(WIDTH/8))
                    nemoj=True
                    #Move piece
            if nemoj:
                nemoj=False
                places=[]
                if turn=="b":
                    turn="c"
                else:
                    turn="b"
                pieceindex=None
            else:
                pieceindex=clickedspace(cheesboardmap,int(mousePos[0]//(WIDTH/8)),int(mousePos[1]//(WIDTH/8)))
                places=pieces[pieceindex].calc_move_opt(cheesboardmap)
        except:
            pass
    countzapojedanjevar=0
    for i in range(len(pieces)):
        if pieces[countzapojedanjevar].alive==False:
            del pieces[countzapojedanjevar]
            countzapojedanjevar-=1
        countzapojedanjevar+=1
    render()
    for i in range(len(places)):
        pygame.draw.circle(window,pygame.Color(147,151,151),(places[i][1]*(WIDTH/8)+(WIDTH/16),places[i][0]*(HEIGHT/8)+(HEIGHT/16)),(WIDTH/32))
    if keys[pygame.K_ESCAPE]:
        break
    for event in events:
        if event.type == pygame.QUIT:
            breaksure=1
    if breaksure==1:
        break
    
    pygame.display.update()
    clock.tick(60)
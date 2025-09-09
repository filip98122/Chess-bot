from generalinfo import *
from spoljasnjinfo import *
def takesave(info):
    info["local"]["cheesboardmap"]=cheesboardmap
    info["local"]["check"]=check
    info["local"]["turn"]=turn
def space(y,x):
    index=None
    for i in range(len(pieces)):
        if pieces[i].x==x and pieces[i].y==y:
            index=i
            break
    return index
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
            if pieceindex!=None:
                if pieces[pieceindex].y==i and pieces[pieceindex].x==j:
                    pygame.draw.rect(window,(255, 219, 88),pygame.rect.Rect(j*(WIDTH/8),i*(HEIGHT/8),textures["board"].get_width()/8,textures["board"].get_height()/8))
            window.blit(textures[f"{slika}{cheesboardmap[i][j][1]}"],(j*(WIDTH/8)-(textures[f"{slika}{cheesboardmap[i][j][1]}"].get_width()/2)+(WIDTH/8/2),i*(HEIGHT/8)-(textures[f"{slika}{cheesboardmap[i][j][1]}"].get_height()/2)+(HEIGHT/8/2)))
breaksure=0
turn="b"
nemoj=False
places=[]
da=True
currenttrack=[-1,-1]
takedeep=copy.deepcopy(cheesboardmap)
check=False
prozor=-1
sa1da=False
lprom=["dama","top","lovac","skakac"]
daenpassant=False
checkt=textures["font"].render("Check!",True,(0,0,0))
checkmatet=textures["font"].render("Checkmate!",True,(0,0,0))
stalemate=textures["font"].render("Stalemate!",True,(0,0,0))
hold=False
while True:
    window.fill((165,169,180))
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    if prozor==-1:
        currenttrack=[-1,-1]
        window.blit(textures["mainm"],(0,0))
        
        if keys[pygame.K_ESCAPE] and hold==False:
            hold=True
            break
        else:
            hold=False
    if keys[pygame.K_ESCAPE]:
        hold=True
        takesave(info)
        prozor=-1
    else:
        hold=False
    if prozor==0:
        if mouseState[0]:
            try:
                if daenpassant==False:
                    polje=cheesboardmap[int(mousePos[1]//(WIDTH/8))][int(mousePos[0]//(WIDTH/8))]
                if daenpassant:
                    for j in range(4):
                        a=button_colision(textures[f"{lprom[j]}{turn}"].get_width(),textures[f"{lprom[j]}{turn}"].get_height(),WIDTH+(tilewh/2)+tilewh*j-(tilewh/8),tilewh-textures[f"{lprom[j]}{turn}"].get_height(),mousePos,mouseState)
                        if a:
                            pieces[pieceindex].alive=False
                            if turn=="b":
                                l2=[pieces[pieceindex].x,pieces[pieceindex].y-1]
                            else:
                                l2=[pieces[pieceindex].x,pieces[pieceindex].y+1]
                            cheesboardmap[pieces[pieceindex].y][l2[0]]=".."
                            f=f"{lprom[j]}"
                            cheesboardmap[l2[1]][l2[0]]=f"{f[0]}{turn}"
                            if f=="dama":
                                pieces.append(dama(l2[0],l2[1],turn))
                            if f=="top":
                                pieces.append(top(l2[0],l2[1],turn))
                            if f=="lovac":
                                pieces.append(lovac(l2[0],l2[1],turn))
                            if f=="skakac":
                                pieces.append(knight(l2[0],l2[1],turn))
                            nemoj=False
                            places=[]
                            nemoj=False
                            places=[]
                            daenpassant=False
                            if turn=="b":
                                turn="c"
                            else:
                                turn="b"
                            for r in range(len(pieces)):
                                if pieces[r].color==turn:
                                    try:
                                        a=pieces[r].justtwo
                                        pieces[r].justtwo=False
                                    except:
                                        pass
                            pieceindex=None
                            takedeep=copy.deepcopy(cheesboardmap)
                            check=seeifcheck(turn,pieces,cheesboardmap,takedeep)
                            currenttrack=[-1,-1]
                            verdict=seeifcheckmate(check,turn,cheesboardmap,takedeep)
                            cheesboardmap=takedeep
                            if verdict=="n":
                                pass
                            else:
                                if verdict=="c":
                                    prozor=2
                                else:
                                    prozor=1
                for i in range(len(places)):
                    if places[i][0]==int(mousePos[1]//(WIDTH/8)) and places[i][1]==int(mousePos[0]//(WIDTH/8)):
                        if cheesboardmap[pieces[pieceindex].y][pieces[pieceindex].x][0]=="p" and int(mousePos[1]//(WIDTH/8))==0 or cheesboardmap[pieces[pieceindex].y][pieces[pieceindex].x][0]=="p" and int(mousePos[1]//(WIDTH/8))==7 or daenpassant:

                                        
                            daenpassant=True
                            sa1da=True
                        else:
                            try:
                                pojedena=clickedspacezap(cheesboardmap,int(mousePos[0]//(WIDTH/8)),int(mousePos[1]//(WIDTH/8)))
                                pieces[pojedena].alive=False
                            except:
                                pass
                            try:
                                if pieces[pieceindex].moved==False:
                                    if turn=="b":
                                        if pieces[pieceindex].y==6:
                                            pieces[pieceindex].justtwo=True
                                    else:
                                        if pieces[pieceindex].y==1:
                                            pieces[pieceindex].justtwo=True
                                pieces[pieceindex].moved=True
                            
                            except:
                                pass
                            
                            try:
                                pieces[places[i][2]].alive=False
                                cheesboardmap[pieces[places[i][2]].y][pieces[places[i][2]].x]=".."
                            except:
                                pass
                            cheesboardmap[int(mousePos[1]//(WIDTH/8))][int(mousePos[0]//(WIDTH/8))]=cheesboardmap[pieces[pieceindex].y][pieces[pieceindex].x]
                            cheesboardmap[pieces[pieceindex].y][pieces[pieceindex].x]=".."
                            pieces[pieceindex].x=int(mousePos[0]//(WIDTH/8))
                            pieces[pieceindex].y=int(mousePos[1]//(WIDTH/8))
                            sa1da=False
                            nemoj=True
                        #Move piece
                if nemoj:
                    nemoj=False
                    places=[]
                    daenpassant=False
                    if turn=="b":
                        turn="c"
                    else:
                        turn="b"
                    for i in range(len(pieces)):
                        if pieces[i].color==turn:
                            try:
                                a=pieces[i].justtwo
                                pieces[i].justtwo=False
                            except:
                                pass
                    pieceindex=None
                    takedeep=copy.deepcopy(cheesboardmap)
                    check=seeifcheck(turn,pieces,cheesboardmap,takedeep)
                    currenttrack=[-1,-1]
                    verdict=seeifcheckmate(check,turn,cheesboardmap,takedeep)
                    cheesboardmap=takedeep
                    if verdict=="n":
                        pass
                    else:
                        if verdict=="c":
                            prozor=2
                        else:
                            prozor=1
                elif mousePos[0]!=int(mousePos[0]//(WIDTH/8)) or currenttrack[1]!=int(mousePos[1]//(WIDTH/8)):
                    da=False
                    if sa1da==False:
                        daenpassant=False
                        places=[]
                        pieceindex=clickedspace(cheesboardmap,int(mousePos[0]//(WIDTH/8)),int(mousePos[1]//(WIDTH/8)))
                        places=pieces[pieceindex].calc_move_opt(cheesboardmap,takedeep)
                        currenttrack=[pieces[pieceindex].x,pieces[pieceindex].y]
                        cheesboardmap=takedeep
                        takedeep=copy.deepcopy(cheesboardmap)
                    sa1da=False
            except:
                pass
        countzapojedanjevar=0
        for i in range(len(pieces)):
            if pieces[countzapojedanjevar].alive==False:
                del pieces[countzapojedanjevar]
                countzapojedanjevar-=1
            countzapojedanjevar+=1
        render()
        if check:
            window.blit(checkt,(WIDTH+EXTRAW/2-checkt.get_width()/2,tilewh))
        if daenpassant:
            for i in range(4):
                window.blit(textures[f"{lprom[i]}{turn}"],(WIDTH+(tilewh/2)+tilewh*i-(tilewh/8),tilewh-textures[f"{lprom[i]}{turn}"].get_height()))
        for i in range(len(places)):
            pygame.draw.circle(window,pygame.Color(147,151,151),(places[i][1]*(WIDTH/8)+(WIDTH/16),places[i][0]*(HEIGHT/8)+(HEIGHT/16)),(WIDTH/32))
        if keys[pygame.K_ESCAPE]:
            hold=True
            prozor=-1
        else:
            hold=False
        for event in events:
            if event.type == pygame.QUIT:
                breaksure=1
        if breaksure==1:
            break
        #"""
        color="b"
        piecescheck=[]
        verdictp=False
        gobreak=False
        lovac1=False
        skakac1=False
        lovac2=False
        for i in range(8):
            for j in range(8):
                if cheesboardmap[i][j][1]==color:
                    if cheesboardmap[i][j][0]=="d" or cheesboardmap[i][j][0]=="t" or cheesboardmap[i][j][0]=="p":
                        verdictp=True
                        gobreak=True
                        break
                    if cheesboardmap[i][j][0]=="l":
                        if lovac1:
                            verdictp=True
                            gobreak=True
                            break
                        lovac1=True
                        if lovac1 and skakac1:
                            verdictp=True
                            gobreak=True
                            break
                    piecescheck.append(cheesboardmap[i][j][0])
            if gobreak:
                break
        color="c"
        piecescheck=[]
        gobreak=False
        lovac1=False
        skakac1=False
        lovac2=False
        for i in range(8):
            for j in range(8):
                if cheesboardmap[i][j][1]==color:
                    if cheesboardmap[i][j][0]=="d" or cheesboardmap[i][j][0]=="t" or cheesboardmap[i][j][0]=="p":
                        verdictp=True
                        gobreak=True
                        break
                    if cheesboardmap[i][j][0]=="l":
                        if lovac1:
                            verdictp=True
                            gobreak=True
                            break
                        lovac1=True
                        if lovac1 and skakac1:
                            verdictp=True
                            gobreak=True
                            break
                    piecescheck.append(cheesboardmap[i][j][0])
            if gobreak:
                break
        if verdictp:
            pass
        else:
            prozor=1
        #"""
    if prozor==1:
        timeshell=300
        while timeshell>0:
            for event in events:
                if event.type == pygame.QUIT:
                    breaksure=1
            if breaksure==1:
                break
            window.fill((165,169,180))
            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            mouseState = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()
            render()
            window.blit(stalemate,(WIDTH+EXTRAW/2-stalemate.get_width()/2,tilewh))
            timeshell-=1
            pygame.display.update()
            clock.tick(60)
        prozor=-1
    if prozor==2:
        timeshell=300
        while timeshell>0:
            for event in events:
                if event.type == pygame.QUIT:
                    breaksure=1
            if breaksure==1:
                break
            window.fill((165,169,180))
            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            mouseState = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()
            timeshell-=1
            render()
            window.blit(checkmatet,(WIDTH+EXTRAW/2-checkmatet.get_width()/2,tilewh))
            pygame.display.update()
            clock.tick(60)
        prozor=-1
    for i in range(len(l_buttons)):
        prozor,cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,sa1da,lprom,daenpassant,pieces=l_buttons[i].genral(prozor,mousePos,mouseState,cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,sa1da,lprom,daenpassant,pieces)
    pygame.display.update()
    clock.tick(60)
    currenttrack=[-1,-1]
save(info)
import copy
def clickedspace(map,x,y):
    tilevalue=map[y][x]
    if tilevalue=="..":
        return None
    if tilevalue[1]!=turn:
        return None
    else:
        index=None
        for i in range(len(pieces)):
            if pieces[i].x==x and pieces[i].y==y and pieces[i].alive==True:
                index=i
                break
    return index
prozor=0
def s(x,y,x1,y2):
    spaces=[[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]
    for i in range(len(spaces)):
        if spaces[i][0]+x==x1:
            if spaces[i][1]+y==y2:
                return True
    return False
def t(map,x,y,x1,y2):
    spaces=[[0,1],[0,-1],[1,0],[-1,0]]
    for i in range(len(spaces)):
        for j in range(1,9):
            try:
                if map[y+spaces[i][1]*j][x+spaces[i][0]*j]==".." or x+spaces[i][0]*j==x1 and y+spaces[i][1]*j==y2:
                    if x+spaces[i][0]*j==x1 and y+spaces[i][1]*j==y2:
                        return True
                else:
                    break
            except:
                break
    return False
def d(map,x,y,x1,y2):
    spaces=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
    for i in range(len(spaces)):
        for j in range(1,9):
            try:
                if map[y+spaces[i][1]*j][x+spaces[i][0]*j]==".." or x+spaces[i][0]*j==x1 and y+spaces[i][1]*j==y2:
                    if x+spaces[i][0]*j==x1 and y+spaces[i][1]*j==y2:
                        return True
                else:
                    break
            except:
                break
    return False
def p(color,x,y,x1,y2):
    if color=="b":
        spaces=[[-1,-1],[1,-1]]
    else:
        spaces=[[1,1],[-1,1]]
    for i in range(len(spaces)):
        if spaces[i][0]+x==x1:
            if spaces[i][1]+y==y2:
                return True
    return False
def l(map,x,y,x1,y2):
    spaces=[[-1,-1],[1,-1],[1,1],[-1,1]]
    for i in range(len(spaces)):
        for j in range(1,9):
            try:
                if map[y+spaces[i][1]*j][x+spaces[i][0]*j]==".." or x+spaces[i][0]*j==x1 and y+spaces[i][1]*j==y2:
                    if x+spaces[i][0]*j==x1 and y+spaces[i][1]*j==y2:
                        return True
                else:
                    break
            except:
                break
    return False
def k(x,y,x1,y2):
    spaces=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
    for i in range(len(spaces)):
        if spaces[i][0]+x==x1:
            if spaces[i][1]+y==y2:
                return True
    return False
def functionchoose(s):
    global cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,prozor,sa1da,lprom,daenpassant,pieces,value,playerside,info,allpieces
    if s=="con":
        new(True,info,0)
    if s=="start":
        new(False,info,0)
    if s=="ai":
        new(False,info,3)
    return prozor,cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,sa1da,lprom,daenpassant,pieces,value,playerside,info,allpieces





def weightadder(color,weight,added):
    if color=="c":
        weight-=added
    else:
        weight+=added
    return weight

def board_judge(map,turn):
    pawn=[1,1.1,2,3.6,5.4,8.5]
    weight=0
    skakac=0.0125
    bishop=0.0013
    queen= 0.0006
    rook=  0.0012
    subj=None
    for i in range(8):
        for j in range(8):
            if map[i][j][0]=="p":
                if map[i][j][1]=="c":
                    weight-=pawn[i-1]
                else:
                    weight+=pawn[6-i]
            if map[i][j][0]=="s":
                subj=knight(j,i,map[i][j][1],-1)
                a=subj.calc_move_opt(map,map)
                weight=weightadder(map[i][j][1],weight,len(a)*skakac+3)
            if map[i][j][0]=="l":
                subj=lovac(j,i,map[i][j][1],-1)
                a=subj.calc_move_opt(map,map)
                weight=weightadder(map[i][j][1],weight,len(a)*bishop+3)
            if map[i][j][0]=="d":
                subj=dama(j,i,map[i][j][1],-1)
                a=subj.calc_move_opt(map,map)
                weight=weightadder(map[i][j][1],weight,len(a)*queen+9.5)
            if map[i][j][0]=="t":
                subj=top(j,i,map[i][j][1],-1)
                a=subj.calc_move_opt(map,map)
                weight=weightadder(map[i][j][1],weight,len(a)*rook+5)
            
                
    return weight


def all_moves(color,map):
    global pieces
    a=[]
    mousePos=pygame.mouse.get_pos()
    for i in range(pieces):
        if pieces[i].color==color:
            l=pieces[i].calc_move_opt(map,map)
            for j in range(len(l)):
                a.append([l[j],i])
                if cheesboardmap[pieces[i].y][pieces[i].x][0]=="p" and pieces[i].y==1 or cheesboardmap[pieces[i].y][pieces[i].x][0]=="p" and pieces[i].y==7:
                    pass
                    
    return a
def playmove(map,list,typee,pieceindex,inwhat=None):
    dont=False
    if typee =="k":
        if pieces[pieceindex].pomeranje==False and (list[1]==6 or list[1]==2):
            if list[1]==2:
                rooki=clickedspace(cheesboardmap,0,list[0])
                pieces[rooki].x=3
                map[list[0]][0]=".."
                map[list[0]][3]=f"t{turn}"
            if list[1]==6:
                rooki=clickedspace(cheesboardmap,7,list[0])
                pieces[rooki].x=5
                cheesboardmap[list[0]][7]=".."
                cheesboardmap[list[0]][5]=f"t{turn}"
    if typee =="p" and (list[0]==0 or list[0]==7):
        
        dont=True
        pieces[pieceindex].alive=False
        map[pieces[pieceindex].y][list[1]]=".."
        f=inwhat
        map[list[0]][list[1]]=f"{f[0]}{turn}"
        if f=="dama":
            pieces.append(dama(list[1],list[0],turn))
        if f=="top":
            pieces.append(top(list[1],list[0],turn))
        if f=="lovac":
            pieces.append(lovac(list[1],list[0],turn))
        if f=="skakac":
            pieces.append(knight(list[1],list[0],turn))
        info["lpieces"][f"{pieces[-1].index}"]
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
    
    
    
    #if dont==False:
        
    
    takedeep=copy.deepcopy(map)
    check=seeifcheck(turn,pieces,map,takedeep)
    verdict=seeifcheckmate(check,turn,cheesboardmap,takedeep)
    cheesboardmap=takedeep
    if verdict=="n":
        pass
    else:
        if verdict=="c":
            prozor=2
        else:
            prozor=1
def play(cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,prozor,sa1da,lprom,daenpassant,pieces,value,playerside,allpieces):
    a=all_moves(turn)
    for i in range(len(a)):
        #a[i][0][0]=Y
        #a[i][0][1]=X
        #a[i][0][2]=misc
        #a[i][1]=pieceindex exactly
        if turn=="b":
            turn="c"
        else:
            turn="b"
        ai=all_moves(turn)   #not actual ai, A out of i

        for j in range():
            pieces[a[i][1]].x=a[i][0][1]
            pieces[a[i][1]].y=a[i][0][0]

        
def new(over,info,p):
    go=True
    if info["local"]["cheesboardmap"]==0:
        go=False
    global cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,prozor,sa1da,lprom,daenpassant,pieces,value,playerside,allpieces
    allpieces=[]
    cheesboardmap=[

        ["tc","sc","lc","dc","kc","lc","sc","tc",],
        ["pc","pc","pc","pc","pc","pc","pc","pc",],
        ["..","..","..","..","..","..","..","..",],
        ["..","..","..","..","..","..","..","..",],
        ["..","..","..","..","..","..","..","..",],
        ["..","..","..","..","..","..","..","..",],
        ["pb","pb","pb","pb","pb","pb","pb","pb",],
        ["tb","sb","lb","db","kb","lb","sb","tb",]
    ]
    if over and go:
        cheesboardmap=info["local"]["cheesboardmap"]
    breaksure=0
    turn="b"
    nemoj=False
    places=[]
    da=True
    currenttrack=[-1,-1]
    takedeep=copy.deepcopy(cheesboardmap)
    check=False
    prozor=p
    sa1da=False
    playerside="b"
    lprom=["dama","top","lovac","skakac"]
    daenpassant=False
    if over and go:
        turn=info["local"]["turn"]
    value=board_judge(cheesboardmap,turn)
    if over and go:
        check=info["local"]["check"]
        value=info["local"]["value"]
    piececheckvar=0
    if over and go:
        piececheckvar=1
    pieces,info=piececheck(cheesboardmap,piececheckvar,info)



def seeifcheck(color,pieces,map,takedeep):
    if color=="b":
        oppositecolor="c"
    else:
        oppositecolor="b"
    kingx=0
    kingy=0
    break1=False
    for i in range(8):
        for j in range(8):
            if map[i][j][1]==color:
                if map[i][j][0]=="k":
                    kingx=j
                    kingy=i
                    break1=True
                    break
        if break1:
            break
    a=False
    for i in range(8):
        for j in range(8):
            if map[i][j][1]==oppositecolor:
                sa=map[i][j][0]
                if sa=="p":
                    a=p(oppositecolor,j,i,kingx,kingy)
                if sa=="s":
                    a=s(j,i,kingx,kingy)
                if sa=="t":
                    a=t(map,j,i,kingx,kingy)
                if sa=="d":
                    a=d(map,j,i,kingx,kingy)
                if sa=="l":
                    a=l(map,j,i,kingx,kingy)
                if sa=="k":
                    a=k(j,i,kingx,kingy)
                if a:
                    return True
    return False
                
                        
                
def space(y,x,pieces):
    index=None
    for i in range(len(pieces)):
        if pieces[i].x==x and pieces[i].y==y and pieces[i].alive==True:
            index=i
            break
    return index    





    
def seeifcheckmate(check,color,map,map1):
    verdict="n"
    for i in range(len(pieces)):
        if pieces[i].color==color and pieces[i].alive==True:
            a=pieces[i].calc_move_opt(map,map1)
            if a==[]:
                continue
            else:
                return verdict
    if check:
        return "c"
    else:
        return "s"


#=======================================
#=======================================
#=======================================
#=======================================
class top:
    def __init__(s,x,y,color,index):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        s.times=9
        s.spaces=[[0,1],[0,-1],[1,0],[-1,0]]
        s.alive=True
        s.apifs=False
        s.mrd=False
        s.index=index
    def tojson(s):
        d={}
        d["x"]=s.x
        d["y"]=s.y
        d["color"]=s.color
        d["alive"]=s.alive
        d["mrd"]=s.mrd
        return d
    def fromjson(s,d):
        s.x=d["x"]
        s.y=d["y"]
        s.color=d["color"]
        s.alive=d["alive"]
        s.mrd=d["mrd"]
    def calc_move_opt(s,map,map1):
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        s.apifs=False
        for i in range(len(s.spaces)):
            s.apifs=False
            for j in range(1,1+s.times):
                try:
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]==".." or map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        if s.y+s.spaces[i][1]*j>=0 and s.y+s.spaces[i][1]*j<len(map):
                            if s.x+s.spaces[i][0]*j>=0 and s.x+s.spaces[i][0]*j<len(map[s.y+s.spaces[i][1]*j]):
                                if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                                    s.apifs=True
                                h=map
                                h[s.y][s.x]=".."
                                bilo=h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]
                                h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]=f"t{s.color}"
                                sah=seeifcheck(s.color,pieces,h,map1)
                                h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]=bilo
                                map[s.y][s.x]=f"t{s.color}"
                                
                                if sah:
                                    pass
                                else:
                                    s.moveopt.append([s.y+(s.spaces[i][1]*j),s.x+(s.spaces[i][0]*j)])
                                    if s.apifs:
                                        s.apifs=False
                                        break
                    else:
                        break
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        break
                except:
                    break
        return s.moveopt

#=======================================
#=======================================






#=======================================
#=======================================
class dama:
    def __init__(s,x,y,color,index):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        s.times=9
        s.spaces=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        s.alive=True
        s.apifs=False
        s.index=index
    def tojson(s):
        d={}
        d["x"]=s.x
        d["y"]=s.y
        d["color"]=s.color
        d["alive"]=s.alive
        return d
    def fromjson(s,d):
        s.x=d["x"]
        s.y=d["y"]
        s.color=d["color"]
        s.alive=d["alive"]
    def calc_move_opt(s,map,map1):
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.apifs=False
        s.moveopt=[]
        for i in range(len(s.spaces)):
            s.apifs=False
            for j in range(1,1+s.times):
                try:
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]==".." or map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        if s.y+s.spaces[i][1]*j>=0 and s.y+s.spaces[i][1]*j<len(map):
                            if s.x+s.spaces[i][0]*j>=0 and s.x+s.spaces[i][0]*j<len(map[s.y+s.spaces[i][1]*j]):
                                if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                                    s.apifs=True
                                h=map
                                h[s.y][s.x]=".."
                                bilo=h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]
                                h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]=f"d{s.color}"
                                sah=seeifcheck(s.color,pieces,h,map1)
                                h[s.y][s.x]=f"d{s.color}"
                                h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]=bilo
                                if sah:
                                    pass
                                else:
                                    s.moveopt.append([s.y+(s.spaces[i][1]*j),s.x+(s.spaces[i][0]*j)])
                                    if s.apifs:
                                        s.apifs=False
                                        break
                    else:
                        break
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        break
                except:
                    break
        return s.moveopt



#=======================================
#=======================================
#=======================================
#=======================================




class pesak:
    def __init__(s,x,y,color,moved,index):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
            s.spaces=[[0,-1]]
            s.eatopt=[[-1,-1],[1,-1]]
            s.en_passant=[[-1,-1],[1,-1]]
        else:
            s.oppositecolor="b"
            s.spaces=[[0,1]]
            s.eatopt=[[1,1],[-1,1]]
            s.en_passant=[[-1,1],[1,1]]
        s.moveopt=[]
        s.moved=moved
        s.moveopt=[]
        s.alive=True
        s.justtwo=False
        s.index=index
    def tojson(s):
        d={}
        d["x"]=s.x
        d["y"]=s.y
        d["color"]=s.color
        d["alive"]=s.alive
        d["moved"]=s.moved
        d["justtwo"]=s.justtwo
        return d
    def fromjson(s,d):
        s.x=d["x"]
        s.y=d["y"]
        s.color=d["color"]
        s.alive=d["alive"]
        s.moved=d["moved"]
        s.justtwo=d["justtwo"]
        if s.color=="b":
            s.oppositecolor="c"
            s.spaces=[[0,-1]]
            s.eatopt=[[-1,-1],[1,-1]]
            s.en_passant=[[-1,-1],[1,-1]]
        else:
            s.oppositecolor="b"
            s.spaces=[[0,1]]
            s.eatopt=[[1,1],[-1,1]]
            s.en_passant=[[-1,1],[1,1]]
    def calc_move_opt(s,map,map1):
        s.moveopt=[]
        for i in range(len(s.spaces)):
            try:
                if map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]]=="..":
                    if s.y+s.spaces[i][1]>=0 and s.y+s.spaces[i][1]<len(map):
                        if s.x+s.spaces[i][0]>=0 and s.x+s.spaces[i][0]<len(map[s.y+s.spaces[i][1]]):
                            h=map
                            h[s.y][s.x]=".."
                            bilo=h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]
                            h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=f"p{s.color}"
                            sah=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"p{s.color}"
                            h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=bilo
                            if sah:
                                pass
                            else:
                                s.moveopt.append([s.y+s.spaces[i][1],s.x+s.spaces[i][0]])
                            if s.moved==False:
                                if map[s.y+(s.spaces[i][1]*2)][s.x+s.spaces[i][0]]=="..":
                                    h=map
                                    h[s.y][s.x]=".."
                                    bilo=h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]
                                    h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=f"p{s.color}"
                                    sah=seeifcheck(s.color,pieces,h,map1)
                                    h[s.y][s.x]=f"p{s.color}"
                                    h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=bilo
                                    if sah:
                                        pass
                                    else:
                                        s.moveopt.append([s.y+(s.spaces[i][1]*2),s.x+s.spaces[i][0]])
            
            except:
                continue
        for i in range(len(s.eatopt)):
            try:
                if map[s.y+s.eatopt[i][1]][s.x+s.eatopt[i][0]][1]==s.oppositecolor:
                    if s.y+s.eatopt[i][1]>=0 and s.y+s.eatopt[i][1]<len(map):
                        if s.x+s.eatopt[i][0]>=0 and s.x+s.eatopt[i][0]<len(map[s.y+s.eatopt[i][1]]):
                            h=map
                            h[s.y][s.x]=".."
                            bilo=h[s.y+(s.eatopt[i][1])][s.x+(s.eatopt[i][0])]
                            h[s.y+(s.eatopt[i][1])][s.x+(s.eatopt[i][0])]=f"p{s.color}"
                            sah=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"p{s.color}"
                            h[s.y+(s.eatopt[i][1])][s.x+(s.eatopt[i][0])]=bilo
                            if sah:
                                pass
                            else:
                                s.moveopt.append([s.y+s.eatopt[i][1],s.x+s.eatopt[i][0]])
            except:
                continue
        for i in range(len(s.en_passant)):
            if s.y+0>=0 and s.y+0<len(map):
                if s.x+s.en_passant[i][0]>=0 and s.x+s.en_passant[i][0]<len(map[s.y+0]):
                    if map[s.y+0][s.x+s.en_passant[i][0]][0]=="p":
                        if map[s.y+0][s.x+s.en_passant[i][0]][1]==s.oppositecolor:
                            indexa=space(s.y+0,s.x+s.en_passant[i][0],pieces)
                            if pieces[indexa].justtwo:
                                h=map
                                h[s.y][s.x]=".."
                                bilo=h[s.y+(0)][s.x+(s.en_passant[i][0])]
                                h[s.y+(0)][s.x+(s.en_passant[i][0])]=f"p{s.color}"
                                sah=seeifcheck(s.color,pieces,h,map1)
                                h[s.y][s.x]=f"p{s.color}"
                                h[s.y+(0)][s.x+(s.en_passant[i][0])]=bilo
                                if sah:
                                    pass
                                else:
                                    s.moveopt.append([s.y+s.en_passant[i][1],s.x+s.en_passant[i][0],indexa])
        
        return s.moveopt
        



#=======================================
#=======================================
#=======================================
#=======================================




class lovac:
    def __init__(s,x,y,color,index):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        s.times=9
        s.spaces=[[-1,-1],[1,-1],[1,1],[-1,1]]
        s.alive=True
        s.apifs=False
        s.index=index
    def tojson(s):
        d={}
        d["x"]=s.x
        d["y"]=s.y
        d["color"]=s.color
        d["alive"]=s.alive
        return d
    def fromjson(s,d):
        s.x=d["x"]
        s.y=d["y"]
        s.color=d["color"]
        s.alive=d["alive"]
    def calc_move_opt(s,map,map1):
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.apifs=False
        s.moveopt=[]
        for i in range(len(s.spaces)):
            for j in range(1,1+s.times):
                try:
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]==".." or map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        if s.y+s.spaces[i][1]*j>=0 and s.y+s.spaces[i][1]*j<len(map):
                            if s.x+s.spaces[i][0]*j>=0 and s.x+s.spaces[i][0]*j<len(map[s.y+s.spaces[i][1]*j]):
                                if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                                    s.apifs=True
                                h=map
                                h[s.y][s.x]=".."
                                bilo=h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]
                                h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]=f"l{s.color}"
                                sah=seeifcheck(s.color,pieces,h,map1)
                                h[s.y][s.x]=f"l{s.color}"
                                h[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]=bilo
                                if sah:
                                    pass
                                else:
                                    s.moveopt.append([s.y+(s.spaces[i][1]*j),s.x+(s.spaces[i][0]*j)])
                                    if s.apifs:
                                        s.apifs=False
                                        break
                    else:
                        break
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        break
                except:
                    break
        return s.moveopt


#=======================================
#=======================================
#=======================================
#=======================================

from generalinfo import *
class Button:
    def __init__(s,x,y,text,prozor):
        s.x=x
        s.y=y
        s.prozor=prozor
        s.text=text
        s.scaledimg=textures["button"]
        s.width=s.scaledimg.get_width()
        s.height=s.scaledimg.get_height()
        s.x-=s.width/2
        s.font=pygame.font.SysFont("S",(int(textures["skakacuv"].get_height())))
        s.im=s.font.render(s.text,True,(0,0,0))
    def genral(s,prozor,mousepos,mousestate,cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,sa1da,lprom,daenpassant,pieces,value,playerside,info,allpieces):
        
        if s.prozor==prozor:
            if button_colision(s.width,s.height,s.x,s.y,mousepos,mousestate):
                if s.text=="Continue":
                    n="con"
                if s.text=="Two players":
                    n="start"
                if s.text=="vs AI":
                    n="ai"
                prozor,cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,sa1da,lprom,daenpassant,pieces,value,playerside,info,allpieces=functionchoose(n)
            window.blit(s.scaledimg,(s.x,s.y))
            window.blit(textures["skakacuv"],(s.x+(s.width/14.22727272727263),s.y+(s.height/2)-(textures["skakacuv"].get_height()/2)))
            window.blit(textures["skakacb"],(s.x+s.width-(s.width/14.22727272727263)-textures["skakacb"].get_width(),s.y+(s.height/2)-(textures["skakacb"].get_height()/2)))
            window.blit(s.im,(s.x+s.width/2-s.im.get_width()/2,s.y+s.height/2-s.im.get_height()/2))
        return prozor,cheesboardmap,breaksure,turn,nemoj,places,da,currenttrack,takedeep,check,sa1da,lprom,daenpassant,pieces,value,playerside,info,allpieces
l_buttons=[
    
    Button(WIDTH/2+EXTRAW/2,HEIGHT/5,"Continue",-1),
    Button(WIDTH/2+EXTRAW/2,HEIGHT/5*2,"Two players",-1),
    Button(WIDTH/2+EXTRAW/2,HEIGHT/5*3,"vs AI",-1)
]
class knight:
    def __init__(s,x,y,color,index):
        s.x=x
        s.y=y 
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        s.spaces=[[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]
        s.alive=True
        s.index=index
    def tojson(s):
        d={}
        d["x"]=s.x
        d["y"]=s.y
        d["color"]=s.color
        d["alive"]=s.alive
        return d
    def fromjson(s,d):
        s.x=d["x"]
        s.y=d["y"]
        s.color=d["color"]
        s.alive=d["alive"]
    def calc_move_opt(s,map,map1):
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        for i in range(len(s.spaces)):
            try:
                if map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]]==".." or map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]][1]==s.oppositecolor:
                    if s.y+s.spaces[i][1]>=0 and s.y+s.spaces[i][1]<len(map):
                        if s.x+s.spaces[i][0]>=0 and s.x+s.spaces[i][0]<len(map[s.y+s.spaces[i][1]]):
                            h=map
                            h[s.y][s.x]=".."
                            bilo=h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]
                            h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=f"s{s.color}"
                            sah=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"s{s.color}"
                            h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=bilo
                            if sah:
                                pass
                            else:
                                s.moveopt.append([s.y+s.spaces[i][1],s.x+s.spaces[i][0]])
            except:
                continue
        return s.moveopt



#=======================================
#=======================================
#=======================================
#=======================================




from generalinfo import *
class king:
    def __init__(s,x,y,color,index):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        s.spaces=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        s.alive=True
        s.pomeranje=False
        s.index=index
    def tojson(s):
        d={}
        d["x"]=s.x
        d["y"]=s.y
        d["color"]=s.color
        d["alive"]=s.alive
        d["pomeranje"]=s.pomeranje
        return d
    def fromjson(s,d):
        s.x=d["x"]
        s.y=d["y"]
        s.color=d["color"]
        s.alive=d["alive"]
        s.pomeranje=d["pomeranje"]
    def calc_move_opt(s,map,map1):
        if s.color=="b":
            s.oppositecolor="c"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        current=map[s.y][s.x]
        for i in range(len(s.spaces)):
            try:
                if s.y+s.spaces[i][1]>=0 and s.y+s.spaces[i][1]<len(map):
                    if s.x+s.spaces[i][0]>=0 and s.x+s.spaces[i][0]<len(map[s.y+s.spaces[i][1]]):
                        if map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]]==".." or map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]][1]==s.oppositecolor:
                            h=map1
                            h[s.y][s.x]=".."
                            bilo=h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]
                            h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=f"k{s.color}"
                            sah=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"k{s.color}"
                            h[s.y+(s.spaces[i][1])][s.x+(s.spaces[i][0])]=bilo
                            if sah:
                                pass
                            else:
                                s.moveopt.append([s.y+s.spaces[i][1],s.x+s.spaces[i][0]])
            except:
                continue
        if s.pomeranje==False:
            if map[s.y][s.x+1]==".." and map[s.y][s.x+2]=="..":
                o=space(s.y,s.x+3,pieces)
                cnt=False
                if o==None:
                    pass
                else:
                    try:
                        if pieces[o].mrd==False:
                            cnt=True
                    except:
                        pass
                    if cnt:
                        if check!=True:
                            
                            h=map1
                            h[s.y][s.x]=".."
                            bilo=h[s.y][s.x+1]
                            h[s.y][s.x+1]=f"k{s.color}"
                            sah=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"k{s.color}"
                            h[s.y][s.x+1]=bilo
                            
                            h=map1
                            h[s.y][s.x]=".."
                            bilo=h[s.y][s.x+2]
                            h[s.y][s.x+2]=f"k{s.color}"
                            sah1=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"k{s.color}"
                            h[s.y][s.x+2]=bilo
                            if sah==False and sah1==False:
                                s.moveopt.append([s.y,s.x+2])
            if map[s.y][s.x-1]==".." and map[s.y][s.x-2]==".." and map[s.y][s.x-3]=="..":
                o=space(s.y,s.x-4,pieces)
                cnt=False
                if o==None:
                    pass
                else:
                    try:
                        if pieces[o].mrd==False:
                            cnt=True
                    except:
                        pass
                    if cnt:
                        if check!=True:
                            
                            h=map1
                            h[s.y][s.x]=".."
                            bilo=h[s.y][s.x-1]
                            h[s.y][s.x-1]=f"k{s.color}"
                            sah=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"k{s.color}"
                            h[s.y][s.x-1]=bilo
                            
                            h=map1
                            h[s.y][s.x]=".."
                            bilo=h[s.y][s.x-2]
                            h[s.y][s.x-2]=f"k{s.color}"
                            sah1=seeifcheck(s.color,pieces,h,map1)
                            h[s.y][s.x]=f"k{s.color}"
                            h[s.y][s.x-2]=bilo
                            if sah==False and sah1==False:
                                s.moveopt.append([s.y,s.x-2])
        return s.moveopt


#=======================================
#=======================================
#=======================================
#=======================================



def piececheck(map,goorfrom,info):
    map1=[

        ["tc","sc","lc","dc","kc","lc","sc","tc",],
        ["pc","pc","pc","pc","pc","pc","pc","pc",],
        ["..","..","..","..","..","..","..","..",],
        ["..","..","..","..","..","..","..","..",],
        ["..","..","..","..","..","..","..","..",],
        ["..","..","..","..","..","..","..","..",],
        ["pb","pb","pb","pb","pb","pb","pb","pb",],
        ["tb","sb","lb","db","kb","lb","sb","tb",]
    ]
    pieces=[]
    index1=0
    for i in range(8):
        for j in range(8):
            r=False
            if map1[i][j][0]=="k":
                pieces.append(king(j,i,map[i][j][1],index1))
                r=True
            if map1[i][j][0]=="s":
                pieces.append(knight(j,i,map[i][j][1],index1))
                r=True
            if map1[i][j][0]=="l":
                pieces.append(lovac(j,i,map[i][j][1],index1))
                r=True
            if map1[i][j][0]=="d":
                pieces.append(dama(j,i,map[i][j][1],index1))
                r=True
            if map1[i][j][0]=="t":
                pieces.append(top(j,i,map[i][j][1],index1))
                r=True
            if map1[i][j][0]=="p":
                n=True
                if i==1 or i==6:
                    n=False
                pieces.append(pesak(j,i,map[i][j][1],n,index1))
                r=True
            if r:
                if goorfrom==0:
                    info["lpieces"][f"{pieces[-1].index}"]=pieces[-1].tojson()
                else:
                    pieces[-1].fromjson(info["lpieces"][f"{pieces[-1].index}"])
                index1+=1
                
                
    countzapojedanjevar=0
    for i in range(len(pieces)):
        if pieces[countzapojedanjevar].alive==False:
            info["lpieces"][f"{pieces[countzapojedanjevar].index}"]=pieces[countzapojedanjevar].tojson()
            del pieces[countzapojedanjevar]
            countzapojedanjevar-=1
        
        countzapojedanjevar+=1
    save(info)
    info=read()
    return pieces,info
pieces=[]
import copy

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
        if pieces[i].x==x and pieces[i].y==y:
            index=i
            break
    return index    





    
def seeifcheckmate(check,color,map,map1):
    verdict="n"
    for i in range(len(pieces)):
        if pieces[i].color==color:
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
    def __init__(s,x,y,color):
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
    def calc_move_opt(s,map,map1):
        s.moveopt=[]
        s.apifs=False
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
    def __init__(s,x,y,color):
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
    def calc_move_opt(s,map,map1):
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
    def __init__(s,x,y,color):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
            s.spaces=[[0,-1]]
            s.eatopt=[[-1,-1],[1,-1]]
            s.en_passant=[[-1,0],[1,0]]
        else:
            s.oppositecolor="b"
            s.spaces=[[0,1]]
            s.eatopt=[[1,1],[-1,1]]
            s.en_passant=[[-1,0],[1,0]]
        s.moveopt=[]
        s.moved=False
        s.moveopt=[]
        s.alive=True
        s.justtwo=False
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
            if map[s.y+s.en_passant[i][1]][s.x+s.en_passant[i][0]][1]==s.oppositecolor:
                if s.y+s.en_passant[i][1]>=0 and s.y+s.en_passant[i][1]<len(map):
                    if s.x+s.en_passant[i][0]>=0 and s.x+s.en_passant[i][0]<len(map[s.y+s.en_passant[i][1]]):
                        if map[s.y+s.en_passant[i][1]][s.x+s.en_passant[i][0]][0]=="p":
                            indexa=space(s.y+s.en_passant[i][1],s.x+s.en_passant[i][0],pieces)
                            if pieces[indexa].justtwo:
                                h=map
                                h[s.y][s.x]=".."
                                bilo=h[s.y+(s.spaces[i][1])][s.x+(s.en_passant[i][0])]
                                h[s.y+(s.spaces[i][1])][s.x+(s.en_passant[i][0])]=f"p{s.color}"
                                sah=seeifcheck(s.color,pieces,h,map1)
                                h[s.y][s.x]=f"p{s.color}"
                                h[s.y+(s.spaces[i][1])][s.x+(s.en_passant[i][0])]=bilo
                                if sah:
                                    pass
                                else:
                                    s.moveopt.append([s.y+s.spaces[i][1],s.x+s.en_passant[i][0],indexa])
        return s.moveopt
        



#=======================================
#=======================================
#=======================================
#=======================================




class lovac:
    def __init__(s,x,y,color):
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
    def calc_move_opt(s,map,map1):
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
class knight:
    def __init__(s,x,y,color):
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
    def calc_move_opt(s,map,map1):
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
    def __init__(s,x,y,color):
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
    def calc_move_opt(s,map,map1):
        
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
        return s.moveopt


#=======================================
#=======================================
#=======================================
#=======================================



def piececheck(map):
    pieces=[]
    for i in range(8):
        for j in range(8):
            if map[i][j][0]=="k":
                pieces.append(king(j,i,map[i][j][1]))
            if map[i][j][0]=="s":
                pieces.append(knight(j,i,map[i][j][1]))
            if map[i][j][0]=="l":
                pieces.append(lovac(j,i,map[i][j][1]))
            if map[i][j][0]=="d":
                pieces.append(dama(j,i,map[i][j][1]))
            if map[i][j][0]=="t":
                pieces.append(top(j,i,map[i][j][1]))
            if map[i][j][0]=="p":
                pieces.append(pesak(j,i,map[i][j][1]))
    return pieces
pieces=piececheck(cheesboardmap)
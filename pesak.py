from generalinfo import *
class pesak:
    def __init__(s,x,y,color):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="c"
            s.spaces=[[0,-1]]
            s.eatopt=[[-1,-1],[1,-1]]
        else:
            s.oppositecolor="b"
            s.spaces=[[0,1]]
            s.eatopt=[[1,1],[-1,1]]
        s.moveopt=[]
        s.moved=False
        s.moveopt=[]
    def calc_move_opt(s,map):
        s.moveopt=[]
        for i in range(len(s.spaces)):
            try:
                if map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]]=="..":
                    s.moveopt.append([s.y+s.spaces[i][1],s.x+s.spaces[i][0]])
                    if s.moved==False:
                        if map[s.y+(s.spaces[i][1]*2)][s.x+s.spaces[i][0]]=="..":
                            s.moveopt.append([s.y+(s.spaces[i][1]*2),s.x+s.spaces[i][0]])
            
            except:
                continue
        for i in range(len(s.eatopt)):
            try:
                if map[s.y+s.eatopt[i][1]][s.x+s.eatopt[i][0]][1]==s.oppositecolor:
                    s.moveopt.append([s.y+s.eatopt[i][1],s.x+s.eatopt[i][0]])
            except:
                continue
        return s.moveopt
        
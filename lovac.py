from generalinfo import *
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
    def calc_move_opt(s,map):
        s.moveopt=[]
        for i in range(len(s.spaces)):
            for j in range(1,1+s.times):
                try:
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)]==".." or map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        s.moveopt.append([s.y+(s.spaces[i][1]*j),s.x+(s.spaces[i][0]*j)])
                    else:
                        break
                    if map[s.y+(s.spaces[i][1]*j)][s.x+(s.spaces[i][0]*j)][1]==s.oppositecolor:
                        break
                except:
                    break
        return s.moveopt
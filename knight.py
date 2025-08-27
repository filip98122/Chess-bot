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
    def calc_move_opt(s,map):
        s.moveopt=[]
        for i in range(len(s.spaces)):
            try:
                if map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]]=="" or map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]][1]==s.oppositecolor:
                    s.moveopt.append([s.y+s.spaces[i][1],s.x+s.spaces[i][0]])
            except:
                continue
        return s.moveopt
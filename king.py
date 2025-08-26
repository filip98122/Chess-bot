from generalinfo import *
class king:
    def __init__(s,x,y,color,moveopt):
        s.x=x
        s.y=y
        s.color=color
        if s.color=="b":
            s.oppositecolor="w"
        else:
            s.oppositecolor="b"
        s.moveopt=[]
        s.spaces=[[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
    def calc_move_opt(s,map):
        
        current=map[s.y][s.x]
        for i in range(len(s.spaces)):
            if map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]]=="" or map[s.y+s.spaces[i][1]][s.x+s.spaces[i][0]][1]==s.oppositecolor:
                s.moveopt.append([s.y+s.spaces[i][1],s.x+s.spaces[i][0]])
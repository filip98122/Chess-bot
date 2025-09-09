import pygame
pygame.init()
pygame.font.init()
WIDTH,HEIGHT=680,680
EXTRAW=425

def load():
    textures={}
    imeslika=['skakac','pesak','dama','kralj','lovac','top']
    for i in range(2):
        if i == 1:
            bojaslike='b'
        else:
            bojaslike='c'
        for j in range(6):
            nonscaledpic=pygame.image.load(f'{imeslika[j]}{bojaslike}.png')
            textures[f'{imeslika[j]}{bojaslike}']=pygame.transform.scale(nonscaledpic,((nonscaledpic.get_width()/100)*(WIDTH/8),(nonscaledpic.get_height()/100)*(HEIGHT/8)))
            tilewh=nonscaledpic.get_width()/100*WIDTH/8
    textures["board"]=pygame.transform.scale(pygame.image.load("cheesboard.png"),(WIDTH,HEIGHT))
    textures["checkmate"]=pygame.transform.scale(pygame.image.load("checkmate.png"),(WIDTH+EXTRAW,HEIGHT))
    textures["stalemate"]=pygame.transform.scale(pygame.image.load("stalemate.png"),(WIDTH+EXTRAW,HEIGHT))
    textures["font"]= pygame.font.SysFont('S', int(tilewh*2))
    textures["mainm"]=pygame.transform.scale(pygame.image.load("mainmenub.png"),(WIDTH+EXTRAW,HEIGHT))
    n=pygame.image.load("skakacbsup.png")
    textures["skakacuv"]=pygame.transform.scale(n,((n.get_width()/100)*(WIDTH/8),(n.get_height()/100)*(HEIGHT/8)))
    textures["button"]=pygame.transform.scale(pygame.image.load("button.png"),(tilewh*8,tilewh*3.2))
    return textures,tilewh*2

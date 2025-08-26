from generalinfo import *
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
    textures["board"]=pygame.transform.scale(pygame.image.load("cheesboard.png"),(WIDTH,HEIGHT))
    return textures

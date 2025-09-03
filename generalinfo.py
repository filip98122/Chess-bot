import os
from loader import *
textures,tilewh=load()
import random
import math
import time
import json
from cryptography.fernet import Fernet
pygame.init()
pygame.mixer.init()
keys = pygame.key.get_pressed()
keyE = b'nL5cTPi0324Gk2zgRDR6E4Y2iVHfWnrKu4kGzcB1ZnU='
circlesurface=pygame.Surface((WIDTH/8, HEIGHT/8), pygame.SRCALPHA)
circlecolor=(147,151,151,127)
#    ["tc","sc","lc","dc","kc","lc","sc","tc",],   
#    ["pc","pc","pc","pc","pc","pc","pc","pc",],
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
#"""
cheesboardmap=[

    ["..","..","..","dc","kc","..","..","..",],
    ["..","..","..","..","..","..","..","..",],
    ["..","..","..","..","..","..","..","..",],
    ["..","..","..","..","..","..","..","..",],
    ["..","pc","..","..","..","..","..","..",],
    ["..","..","..","..","..","..","..","..",],
    ["pb","..","..","..","..","..","..","..",],
    ["..","..","..","db","kb","..","..","..",]

]
#"""


def ens(file_data):
    f=Fernet(keyE)
    encrypted_data1=json.dumps(file_data).encode('utf-8')
    encrypted_data = f.encrypt(encrypted_data1)
    with open("infojson.json", "wb") as file:
        file.write(encrypted_data)
def end():
    f=Fernet(keyE)
    with open("infojson.json", "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    decrypted_data1=json.loads(decrypted_data.decode('utf-8'))
    return decrypted_data1
"""
def read():
    info=end()
    return info
info=read()
def save(info):
    ens(info)
"""

def collison(x1,y1,r1,x2,y2,r2): 
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist >= r1 + r2:
        return False
    else:
        return True
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False

char ="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def checker(keys):
    pressed = 0
    for key in range(512):
        if keys[key]:
            pressed = key
            break
    if pressed!=0:
        return pressed

keydict={
    "shot":keys[pygame.K_SPACE],
    "left":keys[pygame.K_a],
    "right":keys[pygame.K_d],
    "heal":keys[pygame.K_h]
    
}
EXTRAW=425
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH+EXTRAW,HEIGHT))
def highlight(width,height,x,y,mousePos):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
        return True
    else:
        return False

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

from generalinfo import *
def render():
    window.blit(textures["board"],(0,0))
    for i in range(8):
        for j in range(8):
            currentpiece=cheesboardmap[i][j]
            if currentpiece=="":
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
            window.blit(textures[f"{slika}{cheesboardmap[i][j][1]}"],(j*(WIDTH/8)-(textures[f"{slika}{cheesboardmap[i][j][1]}"].get_width()/2)+(WIDTH/8/2),i*(HEIGHT/8)-(textures[f"{slika}{cheesboardmap[i][j][1]}"].get_height()/2)+(HEIGHT/8/2)))
breaksure=0
turn="w"
while True:
    window.fill("Black")
    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()
    if keys[pygame.K_ESCAPE]:
        break
    for event in events:
        if event.type == pygame.QUIT:
            breaksure=1
    if breaksure==1:
        break
    render()
    pygame.display.update()
    clock.tick(60)
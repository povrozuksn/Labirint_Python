import pygame
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pygame.init()

class Man():
    def __init__ (self, x, y, w, h, up_list, right_list, down_list, left_list, image_list, i):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.up_list = up_list
        self.right_list = right_list
        self.down_list = down_list
        self.left_list = left_list
        self.image_list = image_list
        self.i = i
    def draw(self):
        screen.blit(self.image_list[self.i//6], (self.x, self.y))

class Wall():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self):
        pygame.draw.rect(screen, 'black', (self.x, self.y, self.w, self.h), 0)

man = Man(100, 100, 38, 37, [pygame.image.load(f"man_0_{i}.png") for i in range(1, 4+1)], [pygame.image.load(f"man_1_{i}.png") for i in range(1, 4+1)], [pygame.image.load(f"man_2_{i}.png") for i in range(1, 4+1)], [pygame.image.load(f"man_3_{i}.png") for i in range(1, 4+1)], [pygame.image.load(f"man_0_{i}.png") for i in range(1, 4+1)], 0)

wall1 = Wall(200, 100, 20, 300)
wall2 = Wall(0, 0, 640, 20)



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keyboard = pygame.key.get_pressed()
    
    if keyboard[pygame.K_UP]:
        man.image_list = man.up_list        
        man.y -= 1 
        man.i+=1
        if man.i == 24:
            man.i=0
    elif keyboard[pygame.K_DOWN]:
        man.image_list = man.down_list       
        man.y += 1 
        man.i+=1
        if man.i == 24:
            man.i=0 
    elif keyboard[pygame.K_RIGHT]:
        man.image_list = man.right_list        
        man.x += 1 
        man.i+=1
        if man.i == 24:
            man.i=0 
    elif keyboard[pygame.K_LEFT]:
        man.image_list = man.left_list        
        man.x -= 1 
        man.i+=1
        if man.i == 24:
            man.i=0   
            
    screen.fill("white")
    man.draw()
    wall1.draw()
    wall2.draw()
    
    if man.x<wall1.x+wall1.w and man.x+man.w>wall1.x and man.y<wall1.y+wall1.h and man.y+man.h>wall1.y:
        if man.image_list == man.right_list:
            man.x -= 1
        elif man.image_list == man.left_list:
            man.x += 1
        elif man.image_list == man.up_list:
            man.y += 1
        elif man.image_list == man.down_list:
            man.y -= 1
            
    if man.x<wall2.x+wall2.w and man.x+man.w>wall2.x and man.y<wall2.y+wall2.h and man.y+man.h>wall2.y:
        if man.image_list == man.right_list:
            man.x -= 1
        elif man.image_list == man.left_list:
            man.x += 1
        elif man.image_list == man.up_list:
            man.y += 1
        elif man.image_list == man.down_list:
            man.y -= 1    

    pygame.display.flip()
    fps.tick(60)
pygame.quit()
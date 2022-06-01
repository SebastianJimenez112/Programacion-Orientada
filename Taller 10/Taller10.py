import pygame
import random

pygame.init()

screen= pygame.display.set_mode((500,500))
clock=pygame.time.Clock()

running=True
while running:
#1 Verificar el evento generado por el usuario
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

#2 Definir configuración basica de la pantalla
    screen.fill((255,255,255))
#3 Agregar los elementos
   

    x=random.randint (0,255)
    y=random.randint (0,255)
    z=random.randint (0,255)
    r=random.randint (0,200)
    k=random.randint (0,500)
    h=random.randint (0,500)

   
    pygame.draw.circle(screen, (x,y,z), (h,k), r)




    pygame.display.flip()
    clock.tick(2)


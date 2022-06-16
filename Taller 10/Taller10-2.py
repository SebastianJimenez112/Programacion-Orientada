import random 
import pygame 
pygame.init()

screen=pygame.display.set_mode((500,500)) 
clock=pygame.time.Clock()

runing=True
#Paso 3: Agregar los elementos
x=random.randint(0,255)
y=random.randint(0,255)
z=random.randint(0,255)
r=random.randint(0,255)
k=random.randint(0,255)
h=random.randint(0,255)
  

while runing:
    #Paso 1: Verificar el evento generado por el usuario
    for event in pygame.event.get(): #get: metodo que genera la lista de los dos ultimos eventos
        if event.type==pygame.QUIT:
            runing=False
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_w:
                y=y-20
            elif event.key == pygame.K_s:
                y=y+20
                                
            elif event.key == pygame.K_d:
                x=x+20
            
            elif event.key == pygame.K_a:
                x=x-20
    #Paso 2: Definir configuración
    
    screen.fill((255,255,255)) #Tuplas      
    
    pygame.draw.circle(screen,(x,y,z),(h,k),r)    
    pygame.display.flip() #coordendas inversas
    clock.tick(100)  
    
    
    
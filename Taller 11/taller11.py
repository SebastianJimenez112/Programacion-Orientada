import pygame

pygame.init()

swidth=500
sheight=500


screen= pygame.display.set_mode((swidth, sheight))
myclock= pygame.time.Clock()

bg_color=(255,255,255)
ball_color=(255,0,0)
ball_size=30
x=swidth/2
y=sheight/2
movimiento_x="izquierda"
movimiento_y="arriba"
Sound=pygame.mixer.Sound("audio_1.wav")

while True: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color,(x,y), ball_size )
    
    if (x+ball_size)>=500:
        movimiento_x="izquierda"
        Sound.play()
    
    if (x-ball_size)<=0:
        movimiento_x="derecha"
        Sound.play()
    
    if movimiento_x=="derecha":
        x+=1
           
    else:
        x-=1
       
   
    if (y+ball_size)>=500:
        movimiento_y="arriba"
        Sound.play()
    
    if (y-ball_size)<=0:
        movimiento_y="abajo"
        Sound.play()
    
    if movimiento_y=="abajo":
        y+=1  
         
    else:
        y-=3
    
    
   
    
        
    pygame.display.update()
    myclock.tick(500)
# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

#variabel running game
isRun = True

#windows display surface object

window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

#object game
#koordinat
x = 250
y = 250

#ukuran
panjang = 20
lebar   = 20

#kecepatan gerak
speed = 10





while isRun:
    pygame.time.delay(10)
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    #asset
    window.fill((255, 255, 255))
    pygame.draw.rect(window,(255, 0,0),(x, y,lebar,panjang))
    #keyboard
    keys = pygame.key.get_pressed()
    #keyboard ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed 
        
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
        
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed    
        
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    
    #render assets
    pygame.display.update()


pygame.quit()
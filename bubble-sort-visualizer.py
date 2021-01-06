import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Bubble Sort Visualizer")
font = pygame.font.Font('freesansbold.ttf', 28)


x = 40
y = 40

# width of each bar
width = 20
# height of each bar ( array )
height = [200, 50, 140, 89, 48, 49, 190, 20, 58, 143, 59, 343, 239]

run = True

def show(height):
    for i in range(len(height)):
        pygame.draw.rect(win, (255, 0, 0), (x+25*i, y, width, height[i]))

while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_SPACE]:
        execute = True

    if execute == False:
        win.fill((0, 0 , 0))
        show(height)
        pygame.display.update()
    else:
        for i in range(len(height) - 1):
            for j in range(len(height) -i-1):
                if height[j] > height[j+1]:
                    t = height[j]
                    height[j] = height[j+1]
                    height[j+1] = t
                win.fill((0,0,0))
                show(height)
                pygame.time.delay(50)

                text = font.render(str(i), True, (255,255,255), (0,0,0))
                textRect = text.get_rect()
                textRect.center = (50,10)
                win.blit(text, textRect)
                pygame.display.update()
pygame.quit()

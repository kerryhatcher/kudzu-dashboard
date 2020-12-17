import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
w, h = pygame.display.get_surface().get_size()
fontsize = 500
timetext = datetime.now().strftime("%H:%M:%S")
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', fontsize)
dayfont = pygame.font.SysFont('Consolas', 300)
datefont = pygame.font.SysFont('Consolas', 300)
datetext = datetime.now().strftime("%x")
daytext = datetime.now().strftime("%A")

while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            rightnow = datetime.now()
            timetext = rightnow.strftime("%H:%M:%S")
            datetext = rightnow.strftime("%x")
            daytext = datetime.now().strftime("%A")
        if e.type == pygame.QUIT: break
    else:
        screen.fill((0, 0, 0))
        renderedtext = font.render(timetext, True, (255, 0, 0))
        rendereddaytext = dayfont.render(daytext, True, (255, 0, 0))
        rendereddatetext = datefont.render(datetext, True, (255, 0, 0))

        screen.blit(rendereddaytext, (w/2-renderedtext.get_rect().width/2,h/2-(renderedtext.get_rect().height+100)))

        screen.blit(renderedtext, (w/2-renderedtext.get_rect().width/2,h/2-renderedtext.get_rect().height/2))
        
        screen.blit(rendereddatetext, (w/2-renderedtext.get_rect().width/2,h/2+(renderedtext.get_rect().height/2)))

        pygame.display.flip()
        clock.tick(60)
        continue
    break

import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
w, h = pygame.display.get_surface().get_size()
fontsize = 400
text = datetime.now().strftime("%H:%M:%S")
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', fontsize)



while True:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            text = datetime.now().strftime("%H:%M:%S")
        if e.type == pygame.QUIT: break
    else:
        screen.fill((0, 0, 0))
        renderedtext = font.render(text, True, (255, 0, 0))
        screen.blit(renderedtext, (w/2-renderedtext.get_rect().width/2,h/2-renderedtext.get_rect().height/2))
        pygame.display.flip()
        clock.tick(60)
        continue
    break

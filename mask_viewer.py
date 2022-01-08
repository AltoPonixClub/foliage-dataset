import pygame
from pygame import K_DOWN, K_UP, K_RIGHT, K_LEFT
import os, sys
# TODO: someone needs to seriously clean this up

pygame.init()
width = 1900
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Viewer')
path = "/Users/aniketjain/Desktop/Code/AltoPonix/foliage-dataset/masks"
file_list = os.listdir(path)
photoCount = len(file_list)-1 # subtract 1 because the first file is the .gitkeep
counter = 1
alpha = 128
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 140 ,32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive


print(file_list)
# Using "for i in range" rather than "for i in file_list" so that you can decrement i to go back an image in the directory
for i in range(0, len(file_list)):
    on_image = True
    tempp = True
    img_path = os.path.join(path, file_list[i])
    try:
        print("Trying " + "imgs/" +  str(counter) + ".png")
        image = pygame.image.load("imgs/" +  str(counter) + ".png").convert()
        imageMask = pygame.image.load("masks/" +  str(counter) + "_mask.png").convert()
    except Exception as e:
        on_image = False
    while(on_image):
            screen = pygame.display.set_mode((image.get_width(), image.get_height()+32))
            pygame.display.set_caption('Viewer ' + str(counter))
            screen.blit(image, (0, 0))
            s = pygame.Surface((image.get_width(), image.get_height()))
            input_rect = pygame.Rect(0, image.get_height(), image.get_width(), 32)
            s.blit(imageMask, (0, 0))
            s.set_alpha(alpha)
            screen.blit(s, (0, 0))
            pygame.draw.rect(screen,color,input_rect)
            text_surface = base_font.render(user_text, True, (255,255,255))
            screen.blit(text_surface, (input_rect.x+5,input_rect.y+5))
            pygame.display.flip()
            while(tempp):
                keys = pygame.key.get_pressed()
                if keys[K_DOWN]:
                    alpha -= 16
                elif keys[K_UP]:
                    alpha += 16
                elif keys[K_RIGHT] and counter != photoCount:
                    on_image = False
                    alpha = 128
                    tempp = False
                elif keys[K_LEFT] and counter != 1:
                    on_image = False
                    alpha = 128
                    i = i-2
                    counter = counter-2
                    tempp = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        elif event.key != pygame.K_RIGHT and event.key != pygame.K_DOWN and event.key != pygame.K_LEFT and event.key != pygame.K_UP:
                            user_text += event.unicode
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_rect.collidepoint(event.pos):
                            color = color_active
                        else:
                            color = color_passive
                            if user_text != '' and user_text.isnumeric():
                                if (int(user_text) >= 1 and int(user_text) <= photoCount):
                                    counter = int(user_text)
                                user_text = ""
                s.blit(imageMask, (0, 0))
                s.set_alpha(alpha)
                    

    counter += 1
    if counter > photoCount:
        break
pygame.quit()

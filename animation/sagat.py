import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (50, 50, 50)
transparence = (48, 16, 0)

run = True
main_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Sagat Animation')
sprites = pygame.image.load('assets/sagat_sprite.xcf').convert_alpha()
sp = spritesheet.SpriteSheet(sprites)

standing_list = []
walking_list = []
jumping_list = []
frame_list = [5, 6, 5]
update_time = 200
frame = 0
boot_time = pygame.time.get_ticks()

for i in range(0, frame_list[0]):
    standing_list.append(sp.get_image(i, 60, 118, 2, transparence))

for i in range(4, 10):
    standing_list.append(sp.get_image(i, 60, 118, 2, transparence))

for i in range(9, frame_list[2]):
    standing_list.append(sp.get_image(i, 60, 118, 2, transparence))

def standing_animation():
    global frame
    for j in range(0, frame_list[0]):
        print(frame)
        main_screen.blit(standing_list[frame], (100, 100))
        if frame >= frame_list[0]-1:
            frame = 0

def jumping_animation():
    global frame
    for j in range(0, frame_list[2]):
        main_screen.blit(jumping_list[frame], (100, 100))
        if frame >= frame_list[2]:
            frame = 0

def walking_animation():
    global frame
    for j in range(0, frame_list[1]):
        main_screen.blit(walking_list[frame], (100, 100))
        if frame >= frame_list[1]:
            frame = 0


while run:
    main_screen.fill(BACKGROUND_COLOR)
    current_time = (pygame.time.get_ticks())
    key = pygame.key.get_pressed()
    if current_time - boot_time >= update_time:
        frame = frame + 1
        boot_time = current_time
    if key[pygame.K_RIGHT]:
        walking_animation()
    elif key[pygame.K_LEFT]:
        walking_animation()
    elif key[pygame.K_UP]:
        jumping_animation()
    else:
        if frame <= 5:
            standing_animation()
        else:
            frame = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

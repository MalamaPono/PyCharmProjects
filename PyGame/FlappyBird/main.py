import pygame
import sys
import random
import numpy as np

pygame.init()
# normal size: (576,1024)
# for my tiny macbook (576,800)
width,height = 576,800
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)

bg_surface = pygame.transform.scale(pygame.image.load('assets/background-day.png').convert(),(width,height))

floor_surface = pygame.transform.scale(pygame.image.load('assets/base.png').convert(),(width,height/7))
floor_x_pos = 0

bird_downflap = pygame.transform.scale(pygame.image.load('assets/bluebird-downflap.png').convert_alpha(),(40,30))
bird_midflap = pygame.transform.scale(pygame.image.load('assets/bluebird-midflap.png').convert_alpha(),(40,30))
bird_upflap = pygame.transform.scale(pygame.image.load('assets/bluebird-upflap.png').convert_alpha(),(40,30))
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100,height/2))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)

pipe_surface = pygame.transform.scale(pygame.image.load('assets/pipe-green.png'),(60,600-height/7))
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,800)
pipe_height = [x for x in range(250,600)]

game_over_surface = pygame.transform.scale(pygame.image.load('assets/message.png').convert_alpha(),(368,417))
game_over_rect = game_over_surface.get_rect(center = (width/2,height/2))

flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,height-height/7))
    screen.blit(floor_surface, (floor_x_pos+576,height - height/7))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700,random_pipe_pos-200))
    return bottom_pipe,top_pipe

def move_pipes(pipe_list,score):
    speeds = np.arange(3.5,5.5,0.01)
    if score >= 200:
        speed = 5.5
    else:
        speed = speeds[score]
    for pipe in pipe_list:
        pipe.centerx -= speed
    visible_pipes = [pipe for pipe in pipe_list if pipe.right > -50]
    return visible_pipes

def check_collisions(pipe_list,can_score):
    if bird_rect.top <= -100 or bird_rect.bottom >= height - height/7:
        death_sound.play()
        can_score = True
        return False
    for pipe in pipe_list:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            can_score = True
            return False

    return True

def rotate_bird(bird_surface,bird_movement):
    new_bird = pygame.transform.rotozoom(bird_surface,-bird_movement*3,1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100,bird_rect.centery))
    return new_bird,new_bird_rect

def draw_pipes(pipe_list):
    for pipe in pipe_list:
        if pipe.bottom >= height - height/7:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def update_score(score):
    high_score = 0
    with open('score.txt','r') as file:
        lines = file.readlines()
        high_score = int(lines[0].strip())
        if score > high_score:
            high_score = score
    with open('score.txt','w') as file:
        file.write(str(high_score))
    return high_score

def score_display(game_state,score,high_score):
    if game_state == 'main_game':
        score_surface = game_font.render(str(score),1,(255,255,255))
        score_rect = score_surface.get_rect(center=(width/2,100))
        screen.blit(score_surface,score_rect)

    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {score}', 1, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(width / 2, 650))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {high_score}', 1, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(width / 2, 100))
        screen.blit(high_score_surface, high_score_rect)

def pipe_score_check(pipe_list,score,can_score):
    if pipe_list:
        for pipe in pipe_list:
            if (95 < pipe.centerx < 105) and can_score:
                score += 1
                score_sound.play()
                can_score = False
            if pipe.centerx < 0:
                can_score = True
    return score,can_score

def main():
    global bird_surface, bird_rect, floor_x_pos, bird_index
    # Game Variables
    gravity = 0.2
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0
    can_score = True
    pipe_list = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 6
                    flap_sound.play()
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (100,height/2)
                    bird_movement = 0
                    score = 0
            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())
            if event.type == BIRDFLAP:
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0
                bird_surface, bird_rect = bird_animation()

        # Background
        screen.blit(bg_surface,(0,0))
        if game_active:
            # Bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface,bird_movement)
            bird_rect.centery += bird_movement
            screen.blit(rotated_bird,bird_rect)
            game_active = check_collisions(pipe_list,can_score)

            # Pipes
            pipe_list = move_pipes(pipe_list,score)
            draw_pipes(pipe_list)

            # Score
            score,can_score = pipe_score_check(pipe_list,score,can_score)
            score_display('main_game',score,high_score)
        else:
            screen.blit(game_over_surface,game_over_rect)
            high_score = update_score(score)
            score_display('game_over',score,high_score)

        # Floor
        floor_x_pos -= 1.5
        draw_floor()
        if floor_x_pos <= -576:
            floor_x_pos = 0

        pygame.display.update()
        clock.tick(120)

def main_menu():
    global floor_x_pos
    run = True
    while run:
        screen.blit(bg_surface, (0, 0))
        floor_x_pos -= 1.5
        draw_floor()
        if floor_x_pos <= -576:
            floor_x_pos = 0
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score=0)
        score_display('game_over',score=0,high_score=high_score)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

    pygame.quit()

if __name__ == '__main__':
    main_menu()
# 공 터뜨리는게임

import pygame
import os
from 풍선pang import ball
from 풍선pang import setting
dir=os.getcwd()
os.chdir(dir+"/풍선pang")


pygame.init()

# 화면 크기 설정
screen_width=setting.screen_width
screen_height=setting.screen_height
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pang")

# FPS 섷정
clock=pygame.time.Clock()
fps=30

background=pygame.image.load("background.png")

# 캐릭터 설정
character=pygame.image.load("character.png")
character_width,character_height=character.get_rect().size
character_x_pos=screen_width/2-character_width/2  #화면 가로 절반 위치-캐릭터가로 절반
character_y_pos=screen_height-character_height   # 화면 세로 가장 아래
cha_move_x=0
cha_vel=0.3       # 캐릭터 이동 속도


pang_g=setting.gravity  # 중력가속도


pang_list=[]
pang_list.append(ball.ball(0,0,1,1)) # 초기 공 생성


# 무기
weapon=pygame.image.load("pang1.png")
weapon_width,weapon_height=weapon.get_rect().size


running=True
while running:
    # 초당프레임
    dt=clock.tick(fps)

    # 이벤트 동작
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            break

        # 방향키 입력
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                cha_move_x-=cha_vel
            elif event.key==pygame.K_RIGHT:
                cha_move_x+=cha_vel
            elif event.key==pygame.K_SPACE: # 무기 발사
                pass################################
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                cha_move_x+=cha_vel
            elif event.key==pygame.K_RIGHT:
                cha_move_x-=cha_vel
    # 캐릭터 움직임
    character_x_pos+=cha_move_x*dt
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    # 캐릭터 충돌처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    # 무기 동작


    # 공 동작

    for i in range(len(pang_list)):
        # 캐릭터와 충돌
        if character_rect.colliderect(pang_list[i].ball_rect):
            print("Game Over")
            running=False
            break
        # 무기와 충돌


    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(pang[0], (pang_x_pos,pang_y_pos))




    pygame.display.update()

    


            



pygame.time.delay(1000)
pygame.quit()
# 공 터뜨리는게임
# 공을 터뜨리면 작은공 두개로 쪼개짐. 총 4단계
# 공 크기별로 max_height이 존재.
# 중력가속도 설정후 공이 땅에 닿으면 각 크기별 고정속도로 변함
# 땅에서튀어오르는 속도= sqrt(2*g*max_height)


import pygame
import random
import os
import math
dir=os.getcwd()
os.chdir(dir+"/풍선pang")

pygame.init()

# 화면 크기 설정
screen_width=640
screen_height=480
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

# 풍선 설정 (처음 생성위치, 이동방향 랜덤)
pang=[]
pang_width=[]
pang_height=[]

for i in range(4):
    pang.append(pygame.image.load(f"pang{i+1}.png"))
    w,h=pang[i].get_rect().size
    pang_width.append(w)
    pang_height.append(h)
#pang_width,pang_height=pang.get_rect().size
pang_x_pos=random.randrange(0,screen_width-pang_width[0])
pang_max_height=screen_height*1/5 # 좌표상 최대지점
pang_max=screen_height-pang_height[0]-pang_max_height # 공의 실제 최대 높이 (계산용)
pang_y_pos=pang_max_height
pang_x_vel=random.choice([-0.2,0.2])
pang_y_vel=0
pang_g=0.0004



# 무기
weapon=pygame.image.load("weapon.png")
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

    # 풍선 움직임
    pang_x_pos+=pang_x_vel*dt
    pang_y_pos+=pang_y_vel*dt
    pang_y_vel+=pang_g*dt
    #pang_y_vel=(pang_y_pos-pang_max_height)*pang_y_dir/dt/2

    if pang_x_pos<0:
        pang_x_pos=0
        pang_x_vel=-pang_x_vel
    elif pang_x_pos>screen_width-pang_width[0]:
        pang_x_pos=screen_width-pang_width[0]
        pang_x_vel=-pang_x_vel
    if pang_y_pos>screen_height-pang_height[0]:
        pang_y_pos=screen_height-pang_height[0]
        pang_y_vel=-math.sqrt(2*pang_g*pang_max)
    elif pang_y_pos<pang_max_height:
        pang_y_pos=pang_max_height
        pang_y_vel=0

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(pang[0], (pang_x_pos,pang_y_pos))




    pygame.display.update()

    


            



pygame.time.delay(1000)
pygame.quit()
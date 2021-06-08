#  보석(황금,다이아) 및 돌 생성
# 크기 랜덤, 크기별 가치
#  갈고리 회전
# 스페이스=>갈고리 발사
# 갈고리 충돌
# 보석 종류에 따른 갈고리 속도



import pygame
import os
import setting
from object import *

# 화면설정
pygame.init()
screen_width=setting.screen_width
screen_height=setting.screen_height
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Glod Miner")
fps=setting.fps

clock=pygame.time.Clock()

# 배경, 게임 이미지
current_path=os.path.dirname(__file__)
background=pygame.image.load(os.path.join(current_path, "images/background.png"))
object_claw=pygame.image.load(os.path.join(current_path,"images/claw.png"))
claw=Claw(object_claw, (screen_width//2, 50))

# 게임 구동
running=True
while running:
    dt=clock.tick(fps)
# 이벤트발생
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.blit(background,(0,0))
    object_group.draw(screen)
    claw.update()
    screen.blit(claw,claw.rect)
    pygame.display.update()




pygame.quit()




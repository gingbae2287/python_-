import pygame
import os
from setting import *
current_path=os.path.dirname(__file__)

# 색깔
RED=(255,0,0)
BLACK=(0,0,0)

# 변수
offset_of_claw=40 # 중심점으로 부터 집게 거리
LEFT=-1
RIGHT=1
STOP=0
COMEBACK=2
left_max_angle=170
right_max_angle=10

# sprite 2D 이미지들 관리
# 보석, 돌 오브젝트
class object(pygame.sprite.Sprite):
    def __init__(self,image,position):
        super().__init__()
        self.image=image
        self.rect=image.get_rect(center=position)
    def move(self, rect_distance):
        self.rect.center=(rect_distance[0], rect_distance[1])

# 집게
class Claw(pygame.sprite.Sprite):
    def __init__(self,image,position):
        super().__init__()
        self.image=image
        self.original_image=image
        self.rect=image.get_rect(center=position)
        self.line_speed=claw_speed    # 선 길이
        self.offset=pygame.math.Vector2(offset_of_claw,0) # 중심으로부터 떨어뜨리기
        self.position=position  # 위치
        self.direction=LEFT # 집게 이동방향
        self.angle_speed= claw_angle_speed  # 각속도
        self.angle=10   # 현재 각도
        self.grab=False
        self.grab_distance=0



    def update(self,dt):
        if self.direction==LEFT:
            self.angle+=self.angle_speed*dt
        elif self.direction==RIGHT:
            self.angle-=self.angle_speed*dt
        elif self.direction==STOP:
            self.offset.x+=self.line_speed*dt
            if self.grab==False:    # 물체 안잡혔을때 잡으면
                try:
                    for object in object_group:
                        if self.rect.colliderect(object.rect):  # 충돌확인
                            self.grab=True
                            self.line_speed=-claw_speed
                            self.grab_distance=self.rect.center-object.rect.center    # 두 이미지 거리차이
                            print(self.grab_distance)
                            self.grab_object=object
                            break
                except:
                    pass


                    

        if self.grab==True:
            object.move(self.grab_distance)
        if self.angle>left_max_angle:
            self.angle=left_max_angle
            self.direction=RIGHT
        elif self.angle<right_max_angle:
            self.angle=right_max_angle
            self.direction=LEFT


        elif self.rect.left<0 or self.rect.right>screen_width or self.rect.bottom > screen_height:
            self.line_speed=-claw_speed

        elif self.offset.x<offset_of_claw:
            self.offset.x=offset_of_claw
            self.line_speed=claw_speed
            self.direction=self.tmp_dir
            if self.grab==True:
                self.grab=False
                del self.object
        
        self.rotate()



        rect_center=self.position+self.offset
        # self.rect=self.image.get_rect(center=rect_center)

    # 집게 회전 함수
    def rotate(self):
        self.image=pygame.transform.rotozoom(self.original_image, -self.angle,1)
        offset_rotated=self.offset.rotate(self.angle)   # 벡터 rotate
        # 이미지 RECT 가 기존 RECT(LEFT,TOP)을 유지하고 있어서
        # new image의 center를 기존center랑 맞춰준다
        self.rect=self.image.get_rect(center=self.position+offset_rotated)
    
    def stop(self):
        if self.direction!=STOP:
            self.tmp_dir=self.direction
            self.direction=STOP
            


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen,RED,self.position,3)
        pygame.draw.line(screen,BLACK, self.position, self.rect.center, 2)
        # new image의 center까지 선 그음
    
def setup():
    small_gold=object(object_gold1,(200,300))
    object_group.add(small_gold)
    object_group.add(object(object_gold2, (300,500)))
    object_group.add(object(object_stone, (300,580)))
    object_group.add(object(object_dia, (200,500)))


object_gold1=pygame.image.load(os.path.join(current_path,"images/gold.png"))  # 작은금
object_gold2=pygame.image.load(os.path.join(current_path,"images/gold.png"))  # 큰금
object_stone=pygame.image.load(os.path.join(current_path,"images/stone.png"))
object_dia=pygame.image.load(os.path.join(current_path,"images/diamond.png"))
object_claw=pygame.image.load(os.path.join(current_path,"images/claw.png"))
claw=Claw(object_claw, (screen_width/2, 50))
# 그룹지정
object_group=pygame.sprite.Group()
setup()


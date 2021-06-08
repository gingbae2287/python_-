import pygame
import os
from setting import *
current_path=os.path.dirname(__file__)
object_gold1=pygame.image.load(os.path.join(current_path,"images/gold.png"))  # 작은금
object_gold2=pygame.image.load(os.path.join(current_path,"images/gold.png"))  # 큰금
object_stone=pygame.image.load(os.path.join(current_path,"images/stone.png"))
object_dia=pygame.image.load(os.path.join(current_path,"images/diamond.png"))


# sprite 2D 이미지들 관리
# 보석, 돌 오브젝트
class object(pygame.sprite.Sprite):
    def __init__(self,image,position):
        super().__init__()
        self.image=image
        self.rect=image.get_rect(center=position)

# 집게
class Claw(pygame.sprite.Sprite):
    def __init__(self,image,position):
        super().__init__()
        self.image=image
        self.rect=image.get_rect(center=position)
        self.offset=pygame.math.Vector2(100,0)
        self.position=position

    def update(self):
        rect_center=self.position+self.offset
        self.rect=self.image.get_rect(center=rect_center)
    
def setup():
    small_gold=object(object_gold1,(200,300))
    object_group.add(small_gold)
    object_group.add(object(object_gold2, (300,500)))
    object_group.add(object(object_stone, (300,580)))
    object_group.add(object(object_dia, (200,500)))
    
# 그룹지정
object_group=pygame.sprite.Group()
setup()


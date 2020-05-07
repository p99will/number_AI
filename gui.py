import pygame
from pygame.locals import *

class colors:
    white   = (255,255,255)
    black   = (0,0,0)
    red     = (255,0,0)
    green   = (0,255,0)
    blue    = (0,0,255)

class sprite():
    id      = None
    x       = 0
    y       = 0
    width   = 0
    height  = 0
    visible = True
    name    = ""

    def __init__(self,name,x=0,y=0,width=0,height=0,visible=True):
        self.name       = name
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height
        self.visible    = visible

    def draw(self,display):
        pass

    def tick(self):
        pass

class shape(sprite):
    thickness=0
    color=0

    def __init__(self,name,x=0,y=0,width=0,height=0,thickness=0,color=colors.white, visible=True):
        super().__init__(name,x,y,width,height,visible)
        self.thickness  = thickness
        self.color      = color

    def draw(self,display):
        pygame.draw.rect(display, self.color, (self.x,self.y,
            self.width,self.height),self.thickness)

    def tick(self):
        pass

class python_GUI():
    FPS             = 60
    WINDOW_TITLE    = ""
    WINDOW_SIZE     = (800,600)
    BG_color        = colors.black

    sprites         = []
    sprite_count    = 0

    display         = None
    fpsClock        = None

    def __init__(self,title,windowsize=(800,600),fps=60):
        self.WINDOW_TITLE   = title
        self.WINDOW_SIZE    = windowsize
        self.FPS            = fps

        pygame.init()
        pygame.font.init()

        self.fpsClock   = pygame.time.Clock()
        self.display    = pygame.display.set_mode(self.WINDOW_SIZE)

    def add_sprite(self,name='',x=0,y=0,width=0,height=0,visible=True):
        return self.__append_sprite(sprite(name,x,y,width,height,visible))

    def add_custom_sprite(self,spr):
        return self.__append_sprite(spr)

    def __append_sprite(self,spr):
        spr.id=(self.sprite_count)
        self.sprites.append(spr)
        uid=self.sprite_count
        self.sprite_count += 1
        return uid

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for i in self.sprites:
            i.tick()

    def __draw_things(self):
        self.display.fill(self.BG_color)
        for i in self.sprites:
            if i.visible:
                i.draw(self.display)

    def tick(self):
        self.__check_events()
        self.__draw_things()
        pygame.display.update()
        self.fpsClock.tick(self.FPS)

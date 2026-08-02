import pygame

from Scripts.Render import Render

class Object:
    x, y = 0.0, 0.0
    scale = 1.0
    name = ""
    color = (255, 255, 255, 255)

    def AddToBeRendered(self):
        Render.ToBeRenderedList.append(self)

    def RemoveToBeRendered(self):
        objs = 0
        for x in Render.ToBeRenderedList:
            if x.name == self.name:
                Render.ToBeRenderedList.pop(objs)
            objs += 1

    def SetColor(self, *color):
        self.color = color

    def GetColor(self):
        return self.color


class Rect(Object):
    x2, y2 = 1.0, 1.0
    shape = pygame.rect.Rect(Object.x, Object.y, x2, y2)
    type = "Rect"

    def __init__(self, name:str, x:float, y:float, x2:float, y2:float, *color):
        RectObj = Rect

        RectObj.name = name
        RectObj.color = color
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        RectObj.shape = pygame.Rect(self.x, self.y, self.x2, self.y2)

    def __call__(self):
        return self

    def GetRect(self):
        return self.shape

    def SetRect(self, Rect):
        self.shape = Rect

    def SetScale(self, value:float):
            self.scale = value
            self.x2 += self.scale
            self.y2 += self.scale
            self.UpdateShape()

    def UpdateShape(self):
        self.shape.x = int(self.x)
        self.shape.y = int(self.y)
        self.shape.width = int(self.x2)
        self.shape.height = int(self.y2)
    
    def GetScale(self):
        return self.scale
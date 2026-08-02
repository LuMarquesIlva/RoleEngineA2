import pygame

from Scripts.Core import Core

class Render:

    ToBeRenderedList = []

    @staticmethod
    def Update():
        for n in Render.ToBeRenderedList:
            match n.type:
                case "Rect":
                    pygame.draw.rect(Core.screen, n.color, n.shape)
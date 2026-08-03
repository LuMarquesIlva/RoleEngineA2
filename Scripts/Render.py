import pygame

from Scripts.Core import Core

class Render:

    ToBeRenderedList = []

    @staticmethod
    def StartRender():
        Core.screen.fill((100, 100, 120, 255))

        for n in Render.ToBeRenderedList:
            match n.type:
                case "Rect":
                    pygame.draw.rect(Core.screen, n.color, n.shape)

    @staticmethod
    def EndRender():
        Core.display.flip()
        
        Core.clock.tick(60)
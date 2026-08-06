import pygame
from PIL import Image

from Assets.Scripts.Error import Error
import Assets.Scripts.Utility as Utility

class Core:
    width, height = 800, 600
    version = "0.0.1"

    display = pygame.display
    display.set_caption(f"RoleEngineA2 - Version: {version}")
    WinIcon = None
    screen = display.set_mode((width, height), pygame.SCALED, vsync=1)
    clock = pygame.time.Clock()
    RunVar = True

    InitCompleted = False

    @staticmethod
    def quit():
        pygame.quit()

    @staticmethod
    def _GetRunVar_():
        return Core.RunVar

    @staticmethod
    def _SetRunVar_(_Var_):
        Core.RunVar = _Var_

    @staticmethod
    def LoadImageFromFile(path:str):
        return pygame.image.load(path)
  
    def __init__(self):
        pygame.init() # Initalize Pygame

        Error.RaiseTypeErrorIfNone(self.screen)
        Error.RaiseTypeErrorIfNone(self.clock)

        self.WinIcon = Core.LoadImageFromFile("Assets/Images/Icons/logo_small.svg")
        Utility.StyleControl.SetIcon(self.WinIcon)

        self.InitCompleted = True

    def __call__(self):
        return self

#from Scripts.Input import Input
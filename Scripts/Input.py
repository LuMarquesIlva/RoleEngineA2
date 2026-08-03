import pygame

from Scripts.Error import Error
from Scripts.Utility import VariableControl

class Input:
    MainEventClass = pygame.event

    def __init__(self):
        Error.RaiseTypeErrorIfNone(self.MainEventClass)

    def __call__(self):
        return self

    @staticmethod
    def Update():
        for event in Input.MainEventClass.get(pygame.QUIT):
            VariableControl.SetRunVar(False)

        Mouse.Update()
        Keyboard.Update()
        #print(Keyboard.KeysList)
    
    @staticmethod
    def GetPressedKeys():
        return Keyboard.KeysList

class Mouse:

    MouseButtons = [False, False]

    @staticmethod
    def Update():
        #print(Mouse.MouseMotionEvnt)
        for MME in Input.MainEventClass.get(pygame.MOUSEMOTION):
            #print(MME)
            for button in MME.buttons:
                pass

class Keyboard:

    KeysList = {
        "w": False,
        "a": False,
        "s": False,
        "d": False
    }

    @staticmethod
    def Update():
        for KEYDOWN in Input.MainEventClass.get(pygame.KEYDOWN):
            match KEYDOWN.key:
                case pygame.K_w:
                    Keyboard.KeysList["w"] = True
                    break
                case pygame.K_a:
                    Keyboard.KeysList["a"] = True
                    break
                case pygame.K_s:
                    Keyboard.KeysList["s"] = True
                    break
                case pygame.K_d:
                    Keyboard.KeysList["d"] = True
                    break
                case _:
                    pass

        for KEYUP in Input.MainEventClass.get(pygame.KEYUP):
            match KEYUP.key:
                case pygame.K_w:
                    Keyboard.KeysList["w"] = False
                    break
                case pygame.K_a:
                    Keyboard.KeysList["a"] = False
                    break
                case pygame.K_s:
                    Keyboard.KeysList["s"] = False
                    break
                case pygame.K_d:
                    Keyboard.KeysList["d"] = False
                    break
                case _:
                    pass

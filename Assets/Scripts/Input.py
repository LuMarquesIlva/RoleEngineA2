import pygame

from Assets.Scripts.Error import Error
from Assets.Scripts.Utility import VariableControl

class Input:
    MainEventClass = pygame.event

    LastKey = ""

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
    def GetPressedKey():
        return (Input.LastKey, Keyboard.KeysList)

    @staticmethod
    def AddValueTolist(value:str):
        Keyboard.AddValueTolist(value)

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

    KeysList = {}

    @staticmethod
    def AddValueTolist(value:str):
        Keyboard.KeysList[value] = False

    @staticmethod
    def Update():
        for KEYDOWN in Input.MainEventClass.get(pygame.KEYDOWN):
            Keyboard.KeysList[KEYDOWN.unicode] = True
            Input.LastKey = KEYDOWN.unicode

        for KEYUP in Input.MainEventClass.get(pygame.KEYUP):
            Keyboard.KeysList[KEYUP.unicode] = False
            Input.LastKey = ""

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
        for event in Input.MainEventClass.get():
            if event.type is pygame.QUIT:
                VariableControl.SetRunVar(False)

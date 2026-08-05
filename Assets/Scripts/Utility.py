import pygame

class VariableControl:
    @staticmethod
    def GetRunVar():
        from Assets.Scripts.Core import Core
        return Core.RunVar

    @staticmethod
    def SetRunVar(Var):
        from Assets.Scripts.Core import Core
        Core._SetRunVar_(Var)

class StyleControl:
    @staticmethod
    def SetIcon(icon):
        from Assets.Scripts.Core import Core
        Core.display.set_icon(icon)

import pygame

class Error:

    @staticmethod
    def RaiseTypeErrorIfNone(NoneCheck):
        if NoneCheck is None:
            raise TypeError(f"Could Not Initalize {NoneCheck.__class__.__name__}")


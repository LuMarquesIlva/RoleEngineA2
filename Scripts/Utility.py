class VariableControl:
    @staticmethod
    def GetRunVar():
        from Scripts.Core import Core
        return Core.RunVar

    @staticmethod
    def SetRunVar(Var):
        from Scripts.Core import Core
        Core._SetRunVar_(Var)
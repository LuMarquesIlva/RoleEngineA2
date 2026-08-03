from Scripts.Core import Core
from Scripts.Input import Input
from Scripts.Entity import Rect
from Scripts.Render import Render

input = Input()
core = Core()

def main():
    Player = Rect("Player", 30, 30, 80, 60, (100, 150, 200, 255))

    Player.AddToBeRendered()

    while core._GetRunVar_() is True:
        input.Update()

        try:
            match input.GetPressedKey()[0]:
                case  "w":
                    Player.shape.y -= 1
                case "a":
                    Player.shape.x -= 1
                case "s":
                    Player.shape.y += 1
                case "d":
                    Player.shape.x += 1
                case _:
                    pass
        except:
            print("Input Error")

        Render.StartRender()

        

        Render.EndRender()

    core.quit()

if __name__ == "__main__":
    main()

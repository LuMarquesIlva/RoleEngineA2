#!/usr/bin/env -S uv run --script

from Assets.Scripts.Core import Core
from Assets.Scripts.Input import Input
from Assets.Scripts.Entity import Rect, Entity
from Assets.Scripts.Render import Render

input = Input()
core = Core()

vel = 3

def main():
    Player = Entity("Player", 300, 300, core.LoadImageFromFile("Assets/Images/Sprites/Player/spryte-run.png"), True, 60)
    #Player.image = Player.CropImageSection(0, 50, 200, 300)
    print(Player.frames)
    Recto = Rect("Recto", 340, 250, 80, 80, (10, 100, 34, 100))
    Recto2 = Rect("Recto2", 640, 250, 80, 80, (10, 100, 230, 100))

    Recto2.AddToBeRendered()
    Player.AddToBeRendered()
    Recto.AddToBeRendered()

    while core._GetRunVar_() is True:
        input.Update()
        Player.UpdateImage()

        try:
            match input.GetPressedKey()[0]:
                case "w":
                    Player.shape.y -= vel
                case "a":
                    Player.shape.x -= vel
                case "s":
                    Player.shape.y += vel
                case "d":
                    Player.shape.x += vel
                case _:
                    pass
        except:
            print("Input Error")

        Render.StartRender()

        

        Render.EndRender()

    core.quit()

if __name__ == "__main__":
    main()

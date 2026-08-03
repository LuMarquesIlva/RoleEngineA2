#!/usr/bin/env -S uv run --script

from Assets.Scripts.Core import Core
from Assets.Scripts.Input import Input
from Assets.Scripts.Entity import Rect, Entity
from Assets.Scripts.Render import Render

input = Input()
core = Core()

vel = 3

def main():
    Player = Entity("Player", 150, 150, core.LoadImageFromFile("Assets/Images/Icons/AgnesPFP.jpg"))

    Player.AddToBeRendered()

    while core._GetRunVar_() is True:
        input.Update()

        try:
            match input.GetPressedKey()[0]:
                case  "w":
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

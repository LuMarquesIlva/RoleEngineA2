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

        core.screen.fill((100, 100, 150, 255))

        Render.Update()

        core.display.flip()

        core.clock.tick(60)

    core.quit()

if __name__ == "__main__":
    main()

import pygame
from PIL import Image

from Assets.Scripts.Render import Render

class Object:
    x, y = 0.0, 0.0
    scale = 1.0
    name = ""
    color = (255, 255, 255, 255)

    def AddToBeRendered(self):
        Render.ToBeRenderedList.append(self)

    def RemoveToBeRendered(self):
        objs = 0
        for x in Render.ToBeRenderedList:
            if x.name == self.name:
                Render.ToBeRenderedList.pop(objs)
            objs += 1

    def SetColor(self, *color):
        self.color = color

    def GetColor(self):
        return self.color



class Rect(Object):
    x2, y2 = 1.0, 1.0
    shape = pygame.rect.Rect(Object.x, Object.y, x2, y2)
    type = "Rect"

    def __init__(self, name:str, x:int, y:int, x2:int, y2:int, color=(255, 255, 255, 255)):

        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.shape = pygame.Rect(self.x, self.y, self.x2, self.y2)

    def __call__(self):
        return self

    def GetRect(self):
        return self.shape

    def SetRect(self, Rect):
        self.shape = Rect

    def SetScale(self, value:float):
            self.scale = value
            self.x2 += self.scale
            self.y2 += self.scale
            self.UpdateShape()

    def UpdateShape(self):
        self.shape.x = int(self.x)
        self.shape.y = int(self.y)
        self.shape.width = int(self.x2)
        self.shape.height = int(self.y2)
    
    def GetScale(self):
        return self.scale

    # TODO: FIX
    def SetPosition(self, *position):
        if position[0].type is int and position[1].type is int:
            self.x = position[0]
            self.y = position[1]
            self.UpdateShape()

    def GetPosition(self):
        return (self.x, self.y)

class Entity(pygame.sprite.Sprite):
    name = ""
    shape = pygame.rect.Rect
    type = "Entity"
    width = 0
    height = 0
    frameNumber = 0

    SpriteScale = 8

    spritesheet = None # type: ignore # type: pygame.surface.Surface | str
    if spritesheet is not None:
        SpriteArea = spritesheet.get_width() * spritesheet.get_height() #type: ignore
    frames = []

    def __init__(self, name:str, width:int, height:int, color=(255, 255, 255, 255), IsColorSpritesheet=False, SpriteScale=8):
        super().__init__()
        self.color = color
        self.name = name
        self.width = width
        self.height = height
        self.SpriteScale = SpriteScale

        # If color is a color value or image
        if color.__class__ is not pygame.surface.Surface:
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(self.color)
        elif IsColorSpritesheet is False:
            self.image = color
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = color
            self.spritesheet = pygame.transform.scale(self.image, (self.width, self.height))

        if IsColorSpritesheet is True and self.color.__class__ is pygame.surface.Surface:
            # Splits The Sprite Into Frames Using SpriteScale As The Frame Size
            for x in range(0, int(self.spritesheet.get_width()), self.SpriteScale): #type: ignore
                for y in range(0, int(self.spritesheet.get_height()), self.SpriteScale): #type: ignore
                    im = self.CropImageSection(x, y, self.SpriteScale+x, self.SpriteScale+y) # Crops The Sprite In A Section
                    self.frames.append(im) # Append It To The Frames List
            self.image = self.frames[self.frameNumber] # Makes The Default Image The First Frame

        self.shape = self.image.get_rect() # Gets the shape of the image

    def __call__(self):
        return self

    def UpdateImage(self):
        self.image = self.frames[self.frameNumber]

        # Search for the object with the same name and updates it
        for x in Render.ToBeRenderedList:
           if x.name == self.name:
               x.image = self.image

    def CropImageSection(self, x:float, y:float, x2:float, y2:float):
            image = self.spritesheet
            try: # Tries to Open the Image if string, else converts from pygame image to pillow image
                if image.__class__ is str:
                    Image.open(image).convert('RGBA') # type: ignore
                else: # Convets to Pillow Image
                    RawData = pygame.image.tostring(image, "RGBA") # type: ignore
                    PilImage = Image.frombytes("RGBA", image.get_size(), RawData) # type: ignore
            except:
                raise TypeError("Image Is Neither Pygame Image Nor Image Path")

            try:
                CroppedImage = PilImage.crop((x, y, x2, y2)) # type: ignore
            except:
                print(f"Could Not Crop The Image: Image Coordinates {x} {y} {x2} {y2}")

            try:
                # Converts Back To Pygame Image
                PygameSurfaceCropped = pygame.image.fromstring(
                    CroppedImage.tobytes(), #type: ignore
                    CroppedImage.size, #type: ignore
                    "RGBA"
                ).convert()
            except:
                print("Could Not Crop The SpriteSheet")

            try:
                return PygameSurfaceCropped # type: ignore
            except:
                return None

    def AddToBeRendered(self):
            Render.ToBeRenderedList.append(self)
    
    def RemoveToBeRendered(self):
        objs = 0

        # Search for the object with the same name and removes it
        for x in Render.ToBeRenderedList:
            if x.name == self.name:
                Render.ToBeRenderedList.pop(objs)
            objs += 1
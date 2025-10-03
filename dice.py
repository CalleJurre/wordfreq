from random import randint

class Dice:
    faces = [1, 2, 3, 4, 5, 6]
    def __init__(self, sides = 2, colour = "white"):
        self.sides = sides
        self.colour = colour
        self.face = 0
        self.point = 0
        self.pair = 0

    def roll(self):
        self.face = randint(1, self.sides)
        return self.face
        
    def get_face(self):        
        return __class__.faces[self.face-1]

    
            
        

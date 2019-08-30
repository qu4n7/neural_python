from geometry import Rectangle_mod, Cuboid_mod
    
class Cuboid(Rectangle_mod):
    def __init__ (self, width, length, height):
        Rectangle_mod.__init__(self, width, length)
        self.height = height
    
    def volume(self):
        volume = self.width * self.length * self.height
        return volume
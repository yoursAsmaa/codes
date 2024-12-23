class bird:
    def move(self):
        return "i can move"
    
class flyingBirds(bird):
    def fly(self):
        return "i can fly"
    
class nonFlyingBirds(bird):
    def walk(self):
        return"i can walk"
        
class eagle(flyingBirds):
    def fly(self):
        return "i can fly fast"
    
class pengiun(nonFlyingBirds):
    def walk(self):
        return " i can walk fast"
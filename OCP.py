class shape:
    def area(self):
        pass
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14* self.radius* self.radius
    
class square(shape):
    def __init__(self,length):
        self.length=length
        
    def area(self):
        return self.length*4
    
#extension
class rectangle(shape):
    def __init__(self, height, width):
        self.height=height
        self.width=width
        
    def area(self):
        return self.width*self.height
        
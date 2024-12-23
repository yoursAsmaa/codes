from abc import ABC, abstractmethod
class calculate_area(ABC):
    @abstractmethod
    def calc_area(self):
        pass
    
class calculate_perimeter(ABC):
    @abstractmethod
    def calc_perimeter(self):
        pass
    
class circle(calculate_area):
    def __init__(self,radius):
        self.radius=radius
        
        def calc_area(self):
            return 3.14* self.radius* self.radius
        
class rectangle(calculate_area, calculate_perimeter):
    def __init__(self, width, height):
        self.width=width
        self.height=height
        
    def calc_area(self):
        return self.width* self.height
    
    def calc_perimeter(self):
        return 2*(self.width + self.height)
    
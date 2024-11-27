'''
Milburn's Repository link - https://github.com/Milburn-Simon-Veron-Lobo/software-memory

Baahir's Repository link - https://github.com/Baahir2007/GCIS.git

Syed Rayan Repository- https://github.com/SyedRayan0/Lab 
'''

class Polygon:

    __slots__ = ["__name","__sides"]
    
    def __init__(self, polygon_name, polygon_sides ):
        """Intializing attributes such as name and sides
        """
        self.__name = polygon_name
        self.__sides = polygon_sides
    
    
    def get_name(self):
        """Getter method for the attribute name
        """
        return self.__name
    
    def get_sides(self):
        """Getter method for the attribute sides
        """
        return self.__sides
    
    def set_name(self, new_name):
        """Setter method for the attribute name
        """
        self.__name = new_name
        return self.__name
    
    def set_sides(self, new_sides):
        """Setter method for the attribute sides
        """
        self.__sides = new_sides

    
    def __eq__(self, other):
        """ Equality method that checks if the names and sides of 2 different polygons are equal 
            and returns a boolean value """
        
        if type(self) == type(other):
            return self.__name == other.__name and self.__sides == other.__sides
        return False
    
    def __ne__(self, other):
        """ Inequality method that returns a boolean value from negation of equality method """
        
        return not self.__eq__(other)
    
    def __str__(self):
        """String representation method that returns a nicely formatted string for a single polygon"""
        
        return f"{self.__name} with sides: {self.__sides}"
    
    def calculate_circumference(self): 
        '''Calculates circumference of the polygon'''
        
        total = 0
        for side in self.__sides:
            total += side
        return total

def main():
    ''' Instantiate three Polygon objects: a triangle, a square, and a hexagon '''
    triangle = Polygon("Triangle", [3.0, 4.0, 5.0])  
    square = Polygon("Square", [4.0, 4.0, 4.0, 4.0])  
    hexagon = Polygon("Hexagon", [6.0, 6.0, 6.0, 6.0, 6.0, 6.0])  
    print(f"{triangle}: Circumference = {triangle.calculate_circumference()}")
    print(f"{square}: Circumference = {square.calculate_circumference()}")
    print(f"{hexagon}: Circumference = {hexagon.calculate_circumference()}")


if __name__ == "__main__":
    main()
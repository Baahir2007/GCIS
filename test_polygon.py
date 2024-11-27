'''
Milburn's Repository link - https://github.com/Milburn-Simon-Veron-Lobo/software-memory

Baahir's Repository link - https://github.com/Baahir2007/GCIS.git

Syed Rayan Repository- https://github.com/SyedRayan0/Lab
'''

import pytest
from polygon import Polygon


#Step- 1
def test_polygon_initialization():
    '''A test that passes if the initialization function initiates the polygon object'''

    polygon1 = Polygon("Triangle", [3,3,3])
    assert polygon1.get_name() == "Triangle", "Initialization has failed --> Incorrect Name"
    assert polygon1.get_sides() == [3,3,3], "Initialization has failed--> Incorrect Sides"
    print("Initialization passed: Polygon has been Initialized correctly...")

def test_get_name():
    '''A test that passes if the getter function returns the name of the polygon object'''

    polygon2 = Polygon("Square", [4,4,4,4])
    assert polygon2.get_name() == "Square", "get_name has failed"
    print("Test for get_name passed: get_name works correctly...")

def test_set_name():
    '''A test that passes if the setter function modifies the name'''

    polygon3 = Polygon("Pentagon", [5,5,5,5,5])
    polygon3.set_name("Square")
    assert polygon3.get_name() == "Square", "set_name has failed"
    print("Test for set_name passed: set_name works correctly...")

def test_get_sides():
    '''A test that passes if the getter function returns the sides of the polygon object'''

    polygon4 = Polygon("Heptagon", [7,7,7,7,7,7,7])
    assert polygon4.get_sides() == [7,7,7,7,7,7,7], "get_sides has failed"
    print("Test for get_sides passed: get_sides works correctly...")

def test_set_sides():
    '''A test that passes if the setter function modifies the sides of the polygon object'''
    polygon5 = Polygon("Hexagon", [3,3,3,3,3,3])
    polygon5.set_sides([4,4,4,4,4,4])
    assert polygon5.get_sides() == [4,4,4,4,4,4], "set_sides has failed"
    print("Test for set_sides passed: set_sides works correctly...")


#step 2 & step 3
def test_polygon_equality():
    """A test that passes when two different polygons are equal/ have same attributes"""
    
    polygon_1 = Polygon("Triangle", [3,3,3])
    polygon_2 = Polygon("Triangle", [3,3,3])
    assert polygon_1 == polygon_2 , "Test failed..."
    print("Equality test passed successfully....")

def test_polygon_inequality():
    """A test that passes when two different polygons contain different names and sides """

    polygon_1 = Polygon("Square", [4, 4, 4, 4])
    polygon_2 = Polygon("Hexagon", [6,6,6,6,6,6])
    assert polygon_1 != polygon_2 , "Test failed..."
    print("Inequality test passed successfully....")

def test_polygon_str_():
    """A test that passes when the expected string represntation matches 
       with the actual string representation of a polygon"""
    
    polygon = Polygon("Triangle", [3, 3, 3])
    expected_str = "Triangle with sides: [3, 3, 3]"
    actual_str = str(polygon)
    assert actual_str == expected_str , "Incorrect format..."
    print("__str__ test passed successfully...")

#Step 4
def test_polygon_circumference_square():
    """Test the circumference calculation for a square"""
    polygon = Polygon("Square", [4.0, 4.0, 4.0, 4.0])  # A square with all sides 4.0
    expected_circumference = 4.0 * 4  # Sum of all sides (4 sides)
    assert polygon.calculate_circumference() == pytest.approx(expected_circumference), "Circumference calculation failed for Square"
    print("Circumference test1 passed successfully...")

def test_polygon_circumference_hexagon():
    """Test the circumference calculation for a hexagon"""
    polygon = Polygon("Hexagon", [6.0, 6.0, 6.0, 6.0, 6.0, 6.0])  
    expected_circumference = 6.0 * 6  
    assert polygon.calculate_circumference() == pytest.approx(expected_circumference), "Circumference calculation failed for Hexagon"
    print("Circumference test2 passed successfully...")

def main():
    test_polygon_circumference_square()
    test_polygon_circumference_hexagon()
    test_polygon_equality()
    test_polygon_inequality()
    test_polygon_str_()

if __name__ == "__main__":
    main()

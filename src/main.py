from typing import Union

class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numerical")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
    
    
    def add(self, x: Union[int, float], y: Union[int, float]):
        if not isinstance(x, (int, float)) or not isinstance(x, (int, float)):
            raise TypeError("Both arguments should be numerical")
        return x + y
    
    
if __name__ == "__main__":
    calculator = Calculator()
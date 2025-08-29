def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of celsius degree equivalent to fahrenheit degrees
    
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0

def above_freezing(celsius: float) -> bool:
    return celsius > 0

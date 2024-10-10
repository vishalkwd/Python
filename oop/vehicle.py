class Vehicle:
    """
    Vehicle class
    """

    def __init__(self, distance_traveled, unit="miles", **kwargs) -> None:
        """
        Initialize the class. In java we can have multiple constructors but in python this is it.
        This is why we use decorators in python - @classmethod
        """
        self.distance_traveled = distance_traveled
        self.unit = unit
    
    def description(self):
        return f"A {self.__class__.__name__} that has travelled {self.distance_traveled} {self.unit}"
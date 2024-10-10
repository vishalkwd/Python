from vehicle import Vehicle

class Bicycle(Vehicle):

    defualt_tire = "tire"

    def __init__(self, distance_traveled=0, unit="miles") -> None:
        super().__init__(distance_traveled, unit)
        if not tires:
            tires = [self.defualt_tire, self.defualt_tire]
        self.tires = tires
    
    def description(self):
        initial = super().description()
        return f"{initial} on {len(self.tires)} tires"

if __name__ == "__main__":
    bike = Bicycle()
    print(bike.description())
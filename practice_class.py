class Unit:
    def __init__(self):
        print("Unit created.")

class Flyable:
    def __init__(self):
        print("Flyable Unit created.")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # multiple inheritance: super() only calls the first parent class's __init__
        # super().__init__()

        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
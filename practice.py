class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print(f' the {self.make}{self.model} go"s Vroom Vroom')
    def Stop(self):
        print(f' the {self.make}{self.model} SKRRRRRTTT')
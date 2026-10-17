## Inheritance
## Parent class
class Car:
    def __init__(self,windows,doors,enginetype):
            self.windows=windows
            self.doors=doors
            self.enginetype=enginetype

    def drive(self):
        print(f"The person will.drive the {self.enginetype} car ")

car1=Car(4,5,"petrol")
car1.drive()

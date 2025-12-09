class Vehicle:
    def __init__(self,speed,fuel,fueleff):
        self.speed=speed
        self.fuel=fuel
        self.fueleff=fueleff 
class Car(Vehicle):
    def calculate_range(self):
        if self.speed < 50 or self.speed > 100:
            eff = self.fueleff * 0.9
        else:
            eff = self.fueleff
        return self.fueleff*eff
   
class Bike(Vehicle):
    def calculate_range(self):
        if self.speed > 80:
            eff = self.fueleff* 0.85
        else:
            eff = self.fueleff
        return self.fuel * eff
    
class Truck(Vehicle):
    def calculate_range(self):
        if self.speed > 70:
            eff = self.fueleff * 0.8
        else:
            eff = self.fueleff
        return self.fuel * eff
ob=Car(90,40,15)
print(ob.calculate_range())
ob1=Bike(85,10,50)
print(ob1.calculate_range())
ob2=Truck(75,100,5)
print(ob2.calculate_range())



#created parent class
#init function to assign objects brand and model
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
# vehicleInfo method to display comment about the vehicle's brand and name
    def vehicleInfo(self):
        msg = "We have a {} {} displayed here.".format(self.brand,self.model)
        return msg


#created child class Car
class Car(Vehicle):
    #created unique objects to child class
    Dealership = "BMW-Disney"
    Salesman = "Jackson"
    #to keep inheritance of parent __init__ we added another __init__
    def __init__(self,brand,model):
        Vehicle.__init__(self,brand,model)
    #utilized ploymorphism by calling parent mathod, but the child class will have a unique string
    def vehicleInfo(self):
        msg = "\nThe car displayed here is a  {} {}.\n We sell it at our {} dealership".format(self.brand,self.model,self.Dealership)
        return msg

    def helpCar(self):
        msg2 = "\nOur salesman {} can assist you further.".format(self.Salesman)
        return msg2



#created another child class with unique object.
class Motorcycle(Vehicle):
    Manager = "Mark"
    def __init__(self,brand,model):
        Vehicle.__init__(self,brand,model)

    def vehicleInfo(self):
        msg = "\nOur manager {} can help you learn more about the {} {} for sale.".format(self.Manager,self.brand,self.model)
        return msg

#created object to call parent class and their methods
veh1 = Vehicle("Ford","Mustang")
print(veh1.vehicleInfo())

#created object to call child class and their methods
car1 = Car("BMW","M4")
print(car1.vehicleInfo())
print(car1.helpCar())


moto1 = Motorcycle("Kawasaki","1000cc")
print(moto1.vehicleInfo())


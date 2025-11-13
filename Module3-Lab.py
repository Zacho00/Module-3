class Vehicle():
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self,vehicle_type,year,make,model,doors,roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

v_type = input('Please enter your vehicle type: ')
v_year = input('Please enter the year of your vehicle: ')
v_make = input("Please enter the make of your vehicle: ")
v_model = input('Please enter the moodel of your vehicle: ')
v_doors = input('Please enter how many doors your vehicle has: ')
v_roof = input('Please enter the type of roof your vehicle has: ')

user_vehicle = Automobile(v_type,v_year,v_make,v_model,v_doors,v_roof)

print('Vehicle Type:', user_vehicle.vehicle_type)
print('Year:', user_vehicle.year)
print('Make:', user_vehicle.make)
print('Model:', user_vehicle.model)
print('Number of Doors:', user_vehicle.doors)
print('Type of Roof:', user_vehicle.roof)


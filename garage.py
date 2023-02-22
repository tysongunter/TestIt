class vehicle:

  def SetMake (self, make):
      self.vehicle_make = make

  def SetModel (self,model):
    self.vehicle_model = model

  def displayOptions(self):
      print(f"The vehicle make is: {self.vehicle_make}")

  def displayOptions(self):
      print(f"The vehicle model is: {self.vehicle_model}") 


class car(vehicle):


    def setDoors(self, doors):
      self.vehicle_doors = doors
  

    def displayOptions(self):
      print(f"The vehicle model is: {self.vehicle_model}")
      print(f"The vehicle make is: {self.vehicle_make}")
      print(f"The amount of doors are: {self.vehicle_doors}")
      
class truck (vehicle):

  def setBedLength(self, length):
    self.bed_length = length

  def setDoors(self, doors):
      self.vehicle_doors = doors

  def displayOptions(self):
    print(f"The vehicle model is: {self.vehicle_model}")
    print(f"The vehicle make is: {self.vehicle_make}")
    print(f"The vehicles bedlength is: {self.bed_length}")
    print(f"The amount of doors are: {self.vehicle_doors}")
    



choose = input('Would you like to add a car or a truck to your garage?: ')
if choose == 'car':
  print ("Please enter the information about your car")

if choose =='truck':
  print ("Please enter the information about your truck")



input_make = input( "Please enter the make of the vehicle:")

input_model = input( "Please enter the model of the vehicle:")
input_doors = input ("Please enter the amount of doors on the vehicle: ")
input_length = input ("Please enter the bedlength, if it is a car put NA : ")


new_car = car()

new_car. setDoors (input_doors)
new_car. SetMake(input_make)
new_car. SetModel(input_model)



new_truck = truck()

new_truck. SetMake(input_make)
new_truck. SetModel(input_model)
new_truck. setBedLength(input_length)
new_truck. setDoors (input_doors)

new_truck. displayOptions()


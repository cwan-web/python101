"""
OOP: Object Oriented Programming
- A programming paradigram focusing on reusability and dry.

eg.
# Dogs: --class (blueprint of creating something)
  -color
  - weight
   -breed
eg.German Shepherd --object

  Water bottles
  -color
  -size
  -shape
  -material

  Matatus:
  -size
  -color
  -loudnessMusic

OOP:
   -Inheritance
   -Encapasulation


"""
# A bottle blueprint (plan) to create an real bottle
class Bottle:
    # attributes -characteristics
    shape = "Hour Glass"
    # methods -behaviour
    def bottleDetails(self):
        print(f"Our company bootle is of shape {self.shape}")

bottle1 = Bottle() 
bottle1.bottleDetails()  

+9

class Animal :
    # intializes the moment the animal class is called
   def __init__(self, name,breed,age,location): 
        self.name = name 
        self.breed = breed
        self.age = age
        self.location = location



# methods
def eatfood(self):
    print(f"{self.name} is a {self.breed} and is eating food!")

def talk(self):
    print(f"{self.name}")    

"""
CLASS: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
"""

class Monitor:
    # attributes b
    shape = "Rectangle"
    size = "15 inches"
    color = "Black"
    yom = 2020
    resolution ="1080p"



#  an initialize invoked when an object is created 
def __init__(self, shape, size, color, yom, resolution):
    self.shape = shape
    self.size = size
    self.color = color
    self.yom = yom
    self.resolution = resolution



    # methods -functions that reside in a class 

    def switchOnMonitor(self):
        print("turning on monitor")
    def displayInterface(self):
        print("displaying OS")

#CREATING AN OBJECT
# Object: An instance of a class. It is a specific realization of a class with actual values for the attributes defined in the class.
hpmonitor = Monitor ("Rectanglular", "15 inches", "Black", 2020, "1080p")
dellmonitor = Monitor ("Square", "17 inches", "White", 2021, "1440p")


hpmonitor.switchOnMonitor()
dellmonitor.switchOnMonitor()

print(f"===> {hpmonitor.shape}")
print(f"===> {dellmonitor.shape}")




     
     
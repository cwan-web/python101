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
hpmonitor = Monitor ("Rectangular", "15 inches", "Black", 2020, "1080p")
dellmonitor = Monitor ("Square", "17 inches", "White", 2021, "1440p")


hpmonitor.switchOnMonitor()
dellmonitor.switchOnMonitor()

print(f"====> {hpmonitor.shape}")
print(f"====> {dellmonitor.shape}")


"""
-INHERITANCE -gets the method and attributes of the parent class
-ENCAPSULATION
-POLYMORPHISM

"""
# INHERITANCE

class Vehicle:
    # attributes
    def __init__(self, make, model, color, isElectric):
        self.model = model
        self.color = color
        self.isElectric = isElectric
    # methods
    def carFeatures(self):
        print(f"This vehicle is of model {self.model}, color {self.color}, and is electric? {self.isElectric}")

    def startCar(self):
        print(f"Starting the {self.model} car")   


tesla = Vehicle("Tesla", "Model 3", "Red", True)
toyota = Vehicle("Toyota", "Corolla", "White", False)


class TukTuk(Vehicle):
    def __init__(self, model, color, isElectric, numberofWheels):
        super().__init__(model, color, isElectric)
        self.numberofWheels = numberofWheels
        




        

    def wheelNumber(self):
        print(f"This TukTuk has {self.numberofWheels} wheels")

# ENCAPSULATION

class Book:
    def __init__(self, title, author, yop, publisher):
        self.title = title
        self.author = author
        self.yearPublished = yop
        self.publisher = publisher
        self.__costofProduction = 1000 # private attribute


    def aboutBook(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.yearPublished}")
        print(f"Publisher: {self.publisher}")

    alchemist = Book("The Alchemist", "Paulo Coelho", 1988, "penguin books")  

# print("=============")         
# print(f"TITLE: {alchemist.title}")
# print(f"AUTHOR: {alchemist.author}")
# print(f"YEAR PUBLISHED: {alchemist.yearPublished}")
# print(f"PUBLISHER: {alchemist.publisher}")
# print(f"COST OF PRODUCTION: {alchemist.__costofProduction}") # this will raise an error because it is a private attribute
# print("=============")


print("=============")         
alchemist.aboutBook()
print("=============")

        
# age = 25
# name = "John"
# output = f"My name is {name} and I am {age} years old."
# print(output)








     
     
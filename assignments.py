# TASK 1: VARIABLES + CONDITIONAL STATEMENTS
name =  "Chasya"
age = 25
mark = 90.0
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")   


name =  "Grace"
age = 16
mark = 75.0
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.") 



name =  "Emmanuel"
age = 22
mark = 60.0
if age >= 18:
        print(f"{name} is an adult.")
else:
        print(f"{name} is a minor.") 

name =  "James"
age = 15
mark = 48.0
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.") 


grade = "90"
if grade >= "90":
    print("A")
elif grade >= "75":
    print("B")
elif grade >= "50":
    print("C")
else: 
    print("Fail")


    # TASK 2:Loop + Logic
#    No.1
start = 0
    
end = 30
while start <= end:
        print("=> ",start)
        if start == 1:
            print("This is the first number")
        start += 1

print("=======")   

    #  No.2
start = 0
end = 30
number = " divisible by 3"
print(f"Numbers between {0} and {30} that are {number} are: ")
if number == "divisible by 3":
    breakpoint 
while start <= end:
        if start % 3 == 0:
            print("=> ",start)
        start += 1

#         # No.3

input = 10
output = input % 3
print(output)

# TASK 3: 

# TASK 1
# 1.Class with this info
# 2.super it to avoid repitition
# 3.loop (while or if)...



input( "name: ")
input("age: ")
input("marks")

age = int("age: ")
if (age ==  18):
    print("Adult")
elif (age > 18):
    print("Adult")
else: 
    print("Minor")

if ("marks" == "90"):
    output = ("A")
elif ("marks" > "90"):
    output = ("A")
elif ("marks" == "75"):
    output = ("B")
elif ("marks" > "75"):
    output = ("B")
elif ("marks" == "50"):
    output = ("C")
elif ("marks" > "50"):
    output = ("C")
else:
    output = ("FAIL")
print( output)

#TASK 3
word = input("Enter a Word: ") 

if word.lower() == word[::-1].lower():
    print("Sting is palindrome")
else:
    print("string is not palindrome")

print(len(word)) 

def checkIfVowel(value):
    result = False
    match(value):
        case "a" :
            return True
        case "e" :
            return True
        case "i" :
            return True
        case "o" :
            return True
        case "u" :
            return True
        case _:
            return False

scores = int(True)        
print(sum(scores))


    









input( "name: ")
input("age: ")
input("marks")
marks = int("marks")
age = int("age: ")
if (age ==  18):
    print("Adult")
elif (age > 18):
    print("Adult")
else: 
    print("Minor")

if (marks == 90):
    output = ("A")
elif (marks > 90):
    output = ("A")
elif (marks == 75):
    output = ("B")
elif (marks > 75):
    output = ("B")
elif (marks == 50):
    output = ("C")
elif (marks > 50):
    output = ("C")
else:
    output = ("FAIL")
print( output)

#TASK 3
word = input("Enter a Word: ") 

if word.lower() == word[::-1].lower():
    print("Sting is palindrome")
else:
    print("string is not palindrome")

print(len(word)) 

def checkIfVowel(value):
    result = False
    match(value):
        case "a" :
            return True
        case "e" :
            return True
        case "i" :
            return True
        case "o" :
            return True
        case "u" :
            return True
        case _:
            return False

scores = int(True)      
print(sum(scores))


    







    


# TASK 4:LIST + FUNCTIONS
#  No.1
numbers = {1,2,3,4,5}
output = type(numbers)
output = numbers.add(5)
print(output)
print(numbers)

# No.2
numbers = {1,2,3,4,5}
largest = max(numbers)
print(f"The largest number in the set is: {largest}")
# No.3
numbers = {1,2,3,4,5}
numbers = sum(numbers)
max = numbers [0]

print(f"The sum of the numbers in the set is: {numbers}")



# TASK 5: DICTONARIES
# No.1

student = {
    "name": "Chasya",
    "age": 25,
    "mark": 90.0,

}
print(student)



# No.2
student["marks"] = 80.0
print(student)

student["grade"] = "B"
print(student)

for item in student:
    print(f"{item}: {student[item]}")


    #   TASK 6: OOP
    class BankAccount:
        def __init__(self, amount):
            self.amount = amount
            self._balance = amount 

        def deposit(self, amount):
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")


        def withdraw(self, amount):
            if self._balance < amount:
                print(f"Your balance is {self._balance} not enough money!")
            else:
                self._balance -= amount
                print(f"Your balance is now {self._balance}!")

        def get_balance(self):
            print(f"Your balance is {self._balance}!")


        firstAccount = BankAccount(1000)
        print("**********")
        firstAccount.get_balance()
        firstAccount.deposit(500)
        firstAccount.withdraw(200)


    print("**********")
            
        




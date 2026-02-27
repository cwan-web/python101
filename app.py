# this is a single line comment

from tkinter.font import names


name = "Chasya Wanjiru" #this is a variable
# firstName = input()# standard input
# secondName = input("Enter second name")
 

"""
Multi-line comment or string
"""


"""
DATA TYPES/STRUCTURES:
    TEXT(STRINGS) type: str
   -NUMBERS(integers ,float,complex)
   -LIST(list, tuple,dictonary,sets)
"""
# Numbers: INT
number = 89
output = number
output = type(number)


# Numbers: Float_> float()
amount = 20.5
output = amount
output = type(amount)

# Numbers: COMPLEX -> complex()
root = -2j
output = root
output = type(root)


# Text: STRING
name = "John doe"
name = "Yusmin odiche"
output = name [4]


#slicing
'''
output = name[1:3]
output = name[1:5]

output = name
output = name.replace()
'''

# OPERETATS can be grouped:
# 1.-arithmetic operators
#  SUBTRACTION
# POWER
# MODULES
# FLOOR DIVISION


# 2.Comparison operators
#    -less than(<)
#    -equal to   
#    -greater than  
#    -not equal to(!=)
#   -less than or equal to (<=)  
#   -greater than or eq (> =)




x = 10
y = 20
output = (x < y)
output = (x > y)
output = type(output)
output = (x <= y)



# LOGICAL OPERATORS(and ,or ,not)
age =17
year = 2026

output = ((2027 >=year) and (age <= 18))
output = ((2027 >year) and (age== 18))

output = not ((2027 >=year) and (age<= 18))
output = not ((2027 >=year)or (age<= 18))

#ASSIGNMENT OPERATORS:
i = 0
x = x+y
x +=y 

# i = i+1
i += 1
i *= 3
i /= 3
i *= 5
i //=3
i = 10
i %= 20
output 



# CONDITIONAL STATEMENTS:
# - if...else
# -if...elif...else
# -match
# -tenary operator

age = 18
if age > 18 :
   output = "Able to vote"

else:
   output = "Oops! You cannot vote!"
   clothing = "T-shirt"
   color = "green"

clothing = "pants"
color = "black"
shoes ="white"
socks ="happy-socks"

if (clothing == "pants")and (color =="green"):
   output = "green is good but we would black for the theme"

elif (clothing == "pants") and (color == "brown"):
     output = "The brown shoes are not part of the wedding theme"

elif (clothing == "pants")and ("offical"):
    output ="This is a good start!"

elif (clothing == "pants") and socks.startswith("happy") and (color =="black"):
    output = ""
else:
    output="we r done"


# tenary operator
x = 101
output = "ten" if (x==10) else "not ten" 

# MATCH
color = "blue"
match(color):
    case "green":
        output = "Green light!"
    case "yellow":
        output = "Get Ready!"    
    case "blue":
        output = "Time to swim"    
    

# LOOPS
# while loop

name = "Peter Parker"
for letter in  names:
   if letter == "e":
       continue
   print(letter)


    #  FUNCTIONS:
    # serves the purpose of doing a single task
    #  non-parameterized functions
    # -lamba functions



 
    
    # Lamba functions -anonymus function
        #  an initialize invoked when an object is created 
      
   x = lambda a,b : a + b
output = x(10,20)

   



















# print(name)# standard output
print("===============")
print(output)
print("===============")




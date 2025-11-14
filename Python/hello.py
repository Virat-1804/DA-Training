""" r=10
print(r)

#Formatting : if you add the cotentof the other type inside the string
a=23
b="hello"
#print("age is :",a)
print(f"My age is {a} years.")#for not doing this print("my age is ",x,end=" ") print ("years")

txt="hello world"
x=txt.capitalize() #output: Hello World
print(x)

x= txt.center(50) #this will center the string with the given width
print(x)

y= b.count("l") #this will count the number of occurence of a substring in the given string
print(y)

y=b.islower() #it will check if the string is in lowercase if it is then it will give output "true"
print(y)

print(7>4)

#Arithematic Operators
# + , - , * , / , % , // , **

f=2
g=3
print(f**g) #2*2*2=8  # ** this is used for power
print(f+g) 
print(f-g) 
print(f*g)
print(f/g)
print(f//g)
print(f%g)

#Assignment Operators : used to assign values to variables


v=12
v+=5
print(v) # v = v+5

# Comparison Operator : used to compare two values
# == , != , > , < , >= , <=

print(12 == 13)
print(12 != 13)
print(12 > 13)
print(12 < 13)
print(13 >= 12)
print(12 <= 13)

m=15
print(10 < m < 20)

#Logical Operators : used to combine conditional statements
# and , or , not

print(12 > 15 and 15 < 20)

#Bitwise Operator : used to compare binary numbers
# & , | , ^ , ~ , << , >>

k=6 # 0 1 1 0
l=3 # 0 0 1 1 
print(k & l)
print(k | l)
print(k ^ l)
print(~k)
print(k << 2)
print(k >> 2) """

#1st task
#write code on voting system where:
#if age is greater than or equal to 18 then print ("You are eligible to vote")
#else print "You are not eligible to vote"

"""a=int(input("Enter your age :"))
if a >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")"""

#2nd task(Grading system)
#write a code on grading system
#where if the grade is greater or equal to 35 then grade ic C
#if the grade is greater than or equal to 65 then grade is B
#grade is greater than 80 then grade is A
#grade is greater than 95 then grade is A++
#else fail

"""g = int(input(" enter your grade :"))
if g <= 35:
 print("your grade is c ")        
elif g >35 and g<=65:
 print("your grade is b")
elif g>65 and g<95:
 print("your grade is a")
elif g>=95:
 print(" your grade is a++")
else:
 print("Fail")"""

#List : are used to store the multiple values in the single variable

"""a= ["rachit","sachin","harsh"]
print(len(a))"""

"""a= ["rachit","sachin","harsh"]
print(type(a))"""

#Tuple : are used to store the multiple values in the single variables but tuple are immutable

"""a=(1,"chirag",True)
print(a)"""

"""a=(1,"chirag",True)
print(a[:2])"""

#Sets : are used to store the multiple values in the single variables but sets are unordered and unindexed

"""a=(1,2,2,2,5,"Oshean","bittu")
print(type(a))"""

"""a=(1,2,2,2,5,"Oshean","bittu")
b=a.count(2)
print(b)"""

"""a=(1,2,2,2,5,"Oshean","bittu")
r=list(a)
print(r)"""

#Dictionary : are used to store the multiple values in the single variable in key:value pair

"""s={"Name":"Virat","Age":18,"College":"St.Andrew"}
print(s["Name"])"""

#Loops :

#While loop :

"""i=7
while i < 8:
    print(i)
    i+=1"""

"""count=10

while count > 0:
     if count % 2 == 0:
         print(f"{count} is even")
     else:
          print(f"{count} is odd") 
     count-=5"""

"""i=0
while i<19 :
    i=i+2
    print(i)""" 

#For loop :

"""nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
    if num % 2 == 0:
        print(f"{num} is even")
    else :
        print(f"{num} is odd")"""

"""for i in range(0,9):
    print(i)"""            

"""for i in range(0,21,2):
    print(i)"""
 
#Create a code for multi student grade 
#inside array multiple students marks store
#According to their particular number marks will be decided
#Hint : use for loop and if else

"""nums=[62,75,83,23,45,55,35,88,92,100]
for num in nums:
    if num <= 35:
      print("your grade is c ")        
    elif num > 35 and num <= 65:
      print("your grade is b")
    elif num > 65 and num < 95:
      print("your grade is a")
    elif num >= 95:
       print(" your grade is a++")
    else:
       print("Fail")"""
        
"""students_marks = {"Virat":87, "Aayush":56, "Nitesh": 78,"Keshav":45, "Yash":34, "Punit": 90}
for student, mark in students_marks.items():
    if mark >= 90:
        grade = 'A'
    elif mark >= 75:
        grade = 'B'
    elif mark >= 60:
        grade = 'C'
    elif mark >= 45:
        grade = 'D'
    else:
        grade = 'F'
    print(f"{student} have scored {mark} and his grade is {grade}")"""    

#Functions

"""def abc():
    print("hello world")

abc()"""

"""def abc(name):
    print(f"My name is {name}")
abc("Virat")"""

"""def square(num):
    return num*num
result = square(10)
print("Square is",result)"""

#Task
#Write a python code on book system
#make function and store the data in dictionary atleast five books
#user call the number of book and that book need to be display
#hint : use if number (Number of book) in books (dictionary)

"""def book_system():
    books = {
        1: "to kill a mockingbird",
        2: "1984 by George",
        3: "Mahabharat",
        4: "Ramayan",
        5: "Rich Dad Poor Dad"
    }
    print("Available books")

    number = int(input("\nEnter the book number:"))

    if number in books:
        print(f"You Selected: {books[number]}")
    else:
        print("Book not found")
book_system()"""        


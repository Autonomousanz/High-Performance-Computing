#Question 1 
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
#Answer
newlist=[]
for numbers in range(2000,3201):

    if numbers%7==0 and numbers%5!=0:
        newlist.append(str(numbers))
        #print(newlist)
result=""    
    
for item in newlist :
    result+=item+","
print (result[:len(result)-1])

################################################################
#Question 2 
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:  
#8  
#Then, the output should be:  
#40320
#Answer : 
n=input("enter the value to be factorial =")

result=1
for numbers in range(1,int(n)+1):
    
    result=result*numbers
print (result)

################################################################
#Question 3 
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Answer:
n=input("enter the value to be added in dictonary =")
mydict=dict()
i=1
while i<=int(n):
    mydict[i]=i**2
    i=i+1
    
print(mydict)



################################################################
#Question 4 
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:  
#34,67,55,33,12,98  
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']  
#('34', '67', '55', '33', '12', '98')
#Answer :

values=input("enter the sequence to be added in tuple,list =")

substring=""
mylist=[]
mytup=()
for i in range(0,len(values)):
    if i==len(values)-1:
        substring+=values[i]
        mylist.append(substring)
    elif values[i]!=",":
        substring+=values[i]
         
    else :
        mylist.append(substring)
        substring=""
mytup=tuple(mylist)
print(mylist)
print(mytup)    

###############################################################
#Question 5 
#Define a class which has at least two methods:  
#getString: to get a string from console input  
#printString: to print the string in upper case.  
#Also please include simple test function to test the class methods.
#Answer
class MakeCapital():
  def _init_(self):
      self.value=""

  def getString(self):
      self.value=input("Enter a string:")
      return self.value
  
  def printString(self):
      finString=""
      for i in range(0,len(self.value)):
          z=ord(self.value[i])
          if z>=97 and z<=122:
             z=z-32
             y=chr(z)
             finString +=y
             print(y,end="")
          else :
                  y=chr(z)
                  finString +=y
                  print(y,end="")
      return finString
 
result=MakeCapital()
y=result.getString()
 
def testUpperCase():
    #y=result.getString()
    x=result.printString()
    assert x == y.upper() , "String should be upper case"
    #assert y== x, "String should be upper case"
    
testUpperCase()
 
       
################################################################
#Question 6
#Write a program that calculates and prints the value according to the given formula:  
#Q = Square root of [(2 * C * D)/H]  
#Following are the fixed values of C and H:  
#C is 50. H is 30.  
#D is the variable whose values should be input to your program in a comma-separated sequence.  
#Example:  
#Let us assume the following comma separated input sequence is given to the program:   
#100,150,180  
#The output of the program should be: 
#18,22,24

#Answer
values=input("enter the value of D =")

substring=""
resultstring=""
Q=0
for i in range(0,len(values)):
    if i==len(values)-1:
        substring+=values[i]
        Q= (2*50*int(substring)/30)**0.5
        resultstring+=str(int(Q))
        Q=0
    elif values[i]!=",":
        substring+=values[i]
         
    else :
        Q= (2*50*int(substring)/30)**0.5
        resultstring+=str(int(Q))+","
        Q=0
        substring=""
print(resultstring)     
        

################################################################
#Question 7 
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.  
#Note: i=0,1.., X-1; j=0,1,.., Y-1.  
#Example:Suppose the following inputs are given to the program:3,5  
#Then, the output of the program should be:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

values=input("enter the value for array=")
dimensions=values.split(",")

data = []

for i in range (0,int(dimensions[0])):
    column=[]
    for j in range(0,int(dimensions[1])):
        column.append(int(i*j))
    data.append(column)  
        
print (data)


  ################################################################
#Question 8 
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.    
#Suppose the following input is supplied to the program:without,hello,bag,world Then, the output should be:bag,hello,without,world


values=input("enter the sequence of words=")
#words=myseq.split(",")

substring=""
mylist=[]

for i in range(0,len(values)):
    if i==len(values)-1:
        substring+=values[i]
        mylist.append(substring)
    elif values[i]!=",":
        substring+=values[i]
         
    else :
        mylist.append(substring)
        substring=""
mylist.sort()
print(','.join(mylist))       


################################################################
#Question 9 answer
#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:  
#Hello world Practice makes perfect Then, the output should be:HELLO WORLD PRACTICE MAKES PERFECT

class MakeCapital():
  def _init_(self):
      self.value=""
  def getString(self):
      self.value=input("Enter a string:")
      
  def printString(self):
      for i in range(0,len(self.value)):
          z=ord(self.value[i])
          
            
          if z>=97 and z<=122:
             z=z-32
             y=chr(z)
             print(y,end="")
          else :
                  y=chr(z)
                  print(y,end="")
result=MakeCapital()
result.getString()
result.printString()
        


################################################################
#Question 10 

#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.  
#Suppose the following input is supplied to the program:  
#hello world and practice makes perfect and hello world again  
#Then, the output should be:  
#again and hello makes perfect practice world
#Answer
values=input("enter the sequence  =")

substring=""
mylist=[]

for i in range(0,len(values)):
    if i==len(values)-1:
        substring+=values[i]
        mylist.append(substring)
    elif values[i]!=" ":
        substring+=values[i]
         
    else :
        mylist.append(substring)
        substring=""

mylist.sort()

wordsets=set(mylist)
     
print(" ".join(sorted(wordsets)))


################################################################
#Question 11 (25)
#Define a class, which have a class parameter and have a same instance parameter.
class Student:
    # Define the class parameter "name"
    category = "Graduate"
    
    def __init__(self, category = None):
        # self.name is the instance parameter
        self.category = category

sanskruti = Student()
print("sanskruti  is %s" % (Student.category))    



################################################################
#Question 12 (35)
#Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
#Answer
def dictCreate():

    mydict=dict()
    i=1
    while i<=20:
        mydict[i]=i**2
        i=i+1
       
    for keys,values in mydict.items():
        print (values)

dictCreate()


################################################################
#Question 13(36)

#Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
#The function should just print the keys only.
#Answer
def dictCreate():

    mydict=dict()
    i=1
    while i<=20:
        mydict[i]=i**2
        i=i+1
       
    for keys,values in mydict.items():
        print (keys)

dictCreate()



################################################################
#Question 14 (37)
#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
#Answer
def dictCreate():

    mylist=[]
    i=1
    while i<=20:
        mylist.append(i**2)
        i=i+1
       
    print (mylist)

dictCreate()



################################################################
#Question 15 (43)
#Write a program to generate and print another tuple whose 
#values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
#Answer

mytuple=(1,2,3,4,5,6,7,8,9,10)
newlist=[]
result=()
for i in range(len(mytuple)):
    if(mytuple[i]%2==0):
        newlist.append(mytuple[i])
        result=tuple(newlist)
print(result)



################################################################
#Question 16 (51)

#Define a class named American and its subclass NewYorker. 

class American(object):
    def __init__(self):
        self.state = "New York"
        print(self.state)
    
class NewYorker(American):
    def __init__(self, area):
        super().__init__()
        self.area = area
        print(area, self.state)

#anAmerican = American("New York")
#print(anAmerican)

aNewYorker = NewYorker("Manhatten")
print(aNewYorker)

################################################################
#Question 17 (53)
#Define a class named Rectangle which can be constructed by a length and width.
#The Rectangle class has a method which can compute the area. 
#Answer
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(5,15)
print(aRectangle.area())



################################################################
#Question 18 (54)
#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can 
#print the area of the shape where Shape's area is 0 by default.

#Answer

class Shape(object):
     def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self)
        self.length = side

    def area(self):
        return self.length*self.length

area_square= Square(10)
print(area_square.area())


################################################################
#Question 19(56)
#Write a function to compute 5/0 and use try/except to catch the exceptions.
#Answer 
def Invalid():
    return 5/0
try:
    Invalid()
except ZeroDivisionError:
    print("trying to divide by zero!")
except :
    print("error occured!")
    

################################################################
#Question 20(94)
#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list 
#after removing all duplicate values with original order reserved.
#Answer
mylist=[12,24,35,24,88,120,155,88,120,155]
result=[]
 
for i in mylist:
    if i not in result:
        result.append(i) 
print(result)


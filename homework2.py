#Question 1 answer

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
#Question 2 answer

n=input("enter the value to be factorial =")

result=1
for numbers in range(1,int(n)+1):
    
    result=result*numbers
print (result)


################################################################
#Question 3 answer


n=input("enter the value to be added in dictonary =")
mydict=dict()
i=1
while i<=int(n):
    mydict[i]=i**2
    i=i+1
    
print(mydict)


################################################################
#Question 4 answer

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



################################################################
#Question 5 answer

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
#Question 6 answer


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
#Question 7 answer


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
#Question 8 answer

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
#Question 10 answer

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
#Question 11 answer


################################################################
#Question 12 answer



################################################################
#Question 13 answer



################################################################
#Question 14 answer


################################################################
#Question 15 answer


################################################################
#Question 16 answer



################################################################
#Question 17 answer


################################################################
#Question 18 answer



################################################################
#Question 19 answer




################################################################
#Question 20 answer


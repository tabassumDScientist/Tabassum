
#Assingment Number 1b(Question number: 2)

import sys
import time
print ("python version",sys.version)

#Assingment Number 1b(Question number: 3)
from datetime import date
today =date.today()
print("todays date is",today)

#Assingment Number 1b(Question number: 4)
r= float(input("Enter radius"))
a=3.14*r*r
print("Area of the circle",a)

#Assingment Number 1b(Question number: 5)

Fname= str(input("Enter your first name"))
Lname= str(input("Enter your Last  name"))
print("Hi"+Lname+Fname)

#Assingment Number 1b(Question number: 6)

num1= int(input("Enter first number "))
num2= int(input("Enter 2nd number "))
Add=num1+num2
print("sum two numbers :",Add)

#Assingment Number 1b(Question number: 7and Assingment A1 complete)
print(" Enter Mrks obtain in 5 sub")
subj1=int(input())
subj2=int(input())
subj3=int(input())
subj4=int(input())
subj5=int(input())
total=subj1+subj2+subj3+subj4+subj5
perc=(total/5)*300

perc =int(input())
if perc <=100 and perc >=80:
     print("this is your grade :A+")
elif  perc <=80 and perc >=70:
     print("this is your grade :A") 
    
elif  perc <=70 and perc >=65:
     print("this is your grade :B+")  

elif  perc <=64 and perc >=60:
     print("this is your grade :B") 
elif  perc <=59 and perc >=50:
     print("this is your grade :C+") 
elif  perc <=49 and perc >=40:
     print("this is your grade :D+")
elif  perc <=39 and perc >=30:
     print("this is your grade :D") 
elif perc <100 or perc <0:
     print("this is not valid")       
else:
     print("failed")







#Assingment Number 1b(Question number: 8)
num=int(input("Enter any nmber to identify the number is odd or even"))
if(num%2)==0:
    print("the number is even")
else:
    print("the number is odd")











  

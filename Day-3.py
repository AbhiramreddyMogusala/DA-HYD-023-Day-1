#Numeric datatype -->int,float,complex along with boolean

#Input formatting -->Accepting the input from the user -->input()

#Accepting integer input from the user
#by default input() accepts any input -->str
#int(input()) --> will accept only integers
'''
age = int(input('Enter the age:'))
print(age)
print(type(age))
#Float(input()) -->accepts integers,float values
age = float(input("Enter the age:"))
print(age)
print(type(age))

#Accepting string input from user

name = int(input("Enter the marks:"))
print(name)
print(type(name))

#Accept group of values

marks = int(input("Enter the marks:")).split()
print(marks)

#space separated values
a = input().split()#now you enter spaces in output
print(a)

#comma separated values
a = input("Enter the values:").split(',')
print(a)

#list of integers
marks = list(map(int,input("Enter the values").split(',')))
print(marks)

#Now we want to accept 2 values from user
age,salary = map(int,input("Enter the values").split(','))
print(age)
print(salary)

#Single input -->int(input())
#two inputs -->a,b = map(int,input().split(','))
#any number result as list -->a = list(map(int,input().split(',')))

#froup of float values
age,salary = map(float,input("Enter the values").split(','))
print(age)
print(salary)

#Accepting input from user -->int,float -->input formatting

#Operators -->Operators perform operations between values (operands)
#7 types -->Arithmatic,Assignment,Comparision (Relationship)
#Membership,Identity,Logical,Bitwise

#Arithmetic Operators -->Arithmetic operators
#+,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)#Float value
#Float Division (Integer division) -->returns quotient

#Modulus -->divisible rules -->returns remainder
print(5%3)
#power (exponential)
print(5*3)
Task -->Accept integer input as length,breadth -->find the area of rectangle
#Area = length*breadth

length,breadth=map(int,input('Enter the values:').split(','))
area=length*breadth
print(area)

#Assignment operators -->assign the values
#+,+=,-=
a = 45
print(a)
#update the value of a
a = a+5  #a+=5
print(a)
b = 35
b += a  #b=b+a
print(b)
b -=5 #b=b-5
print(b)

#Task : *=,/=,//=,%=,**= workout

#Comparision Operators -->we compare the values -->boolean
#== (equal to), !=(not equal to), <(less than), >(greater than)
#<= (less than or equal to), >=(greater than or equal to)

age=25
print(age==25)#returns boolean output
print(age!=35)
print(age<25)
print(age>25)
print(age<=35)
print(age>=35)

print(-5<-1)

#Membership Operators -->in,not in
#it checks for the existance of an object in a collection

marks = [56,65,72,90]
print(56 in marks)
#print(35 in 355)#TypeError

print(25 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$frg')

#Logical Operators -->logical decision making -->and,or,not
#and -->all conditions to be satisfied
#or -->any one condition to be satisfied

a=(25 in [25,55,65]) and 45<50
print(a)
b=55>56 or 25<=55
print(b)
c = not(True)
print(c)

#Identity Operators -->check for identity of an object -->id()

a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)
b = [1,3,4,2,5]
print(id(b))



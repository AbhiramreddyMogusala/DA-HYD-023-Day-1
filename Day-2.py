'''
Tokens -->Variables,Punctuators

Variables -->Named memory location, its a plachholder for data
#Rules are to be folled

#MultiAssignment of Variables

name,age,place='Abhiram',22,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='----->')

#a,b = 2,4,5 #ValueError as too many values to unpack
#Reassigning values

name="Abhiram"
a,b = 45,1.6
print(a,b)
a,b=b,a
print(a,b,sep=',')

a,b=b,c #NameError as c is not defined
print(a,b)

#Deleting the variables -->
#del a
#print(a)
del a,b
print(a,b)

#Punctuators -->[](lists),()(tuples),{}(Dict,sets)
name = "Abhiram";age = 22;course = 'Data_Analytics'
print(name,age,couse)

#Datatypes -->Numeric (int,float,complex),boolean,None
#--->Sequences --->Lists,Tuples,Sets,Strings,Frozensets,mappinga(dict)

#Numeric type -->int,float,complex

#int datatype --.quantity,age..
age=22
print(age)
print(type(age)) #type --> returns the datatype of object

print(type(245))

#quantity = 03 #it is not allowed
#print(quantity)

#float datatype --->temp,salary,price
prive = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imaginary
i2 = 4
data = 5+i2
print(data)

data = 5+2j #j is imaginary representation
print(data)
print(type(data))

#Boolean --> True/False

valid = True
print(type(valid))

error = False
print(type(error))


#TypeCasting -->Converting one type to another type
#Python by default follows Implict Type (we need not to mention the datatype)

#We will go for Explict Conversion

#Every built-in datatype is a built-in function
int,float,complex,bool

#TypeCasting -->int -->float,complex,bool

age =22
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(b)
c = complex(age)
print(c)
d = bool(age) #returns True for existing data
print(d)
e = bool(0)
print(e)

#Float -->Typecasting -->int,complex,bool

price = 22.8
print(type(price))
d = int(price)
print(d)
print(type(d))
e = complex(price)
print(e)
print(type(e))
f = bool(price)
print(f)   #bool of anything is true

e = int(float(bool(45)))

print(e)
'''
f = 45+ 2.5+2+3j +False
print(f)





























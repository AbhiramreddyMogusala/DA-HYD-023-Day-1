'''
#Student marks and grade analyzer (if-else)
90-100 --> 'A'
80-89 --> 'B'
70-79 --> 'C'
60-69 --> 'D'
<60 -->Fail
#also -ve cases should not be allowed and marks shouldn't be greater than 100

marks = int(input("Enter the marks(1-100):"))
if marks >0 and marks <=100:
    if marks>=90:
        print("User has secured grade A")
    if marks>=80 and marks<=89:
        print("User has secured grade B")
    if marks>=70 and marks<=79:
        print("User has secured grade C")
    if marks>=60 and marks<=69:
        print("User has secured grade D")
    if marks<60:
        print("User has failed, study again")
else:
    print("Enter only +ve values greater than 0 and less than 100")
'''
#elif keyword -->if-else-if
'''
if<condition1>:
   statement(s)......
elif<condition2>:
   statement(s)......
elif<condition3>:
   statement(s)......
    .........
else:
    statement(s)...
    ......

marks = int(input("Enter the Student marks:"))
if marks>=100:
    print("Entered values should be greater than 1 and less than 100")
elif marks>=90 and marks<=100:
        print("User has secured grade A")
elif marks>=80 and marks<=89:
        print("User has secured grade B")
elif marks>=70 and marks<=79:
        print("User has secured grade C")
elif marks>=60 and marks<=69:
        print("User has secured grade D")
elif marks<60 and marks>=0:
        print("User has failed, study again")
else:
    print("No negative values")

#Task -->Same usecase try with if-elif-else usage in another way

#Voter Eligibility checkcase -->make sure to satisfy all possible conditions
#>=18 and 100 -->Access
#<18 -->no of years eligibility should tell
#negative values -->not acceptable

age = int(input("Enter the age"))
if age>=18 and age <=100:
    print('-----User has Vote Eligibility -----')
    print('-----Access Granted-----')
elif age<18 and age>0:
    print('-----User still need to get Vote Eligibility -----')
    print('-----User need to wait for more',(18-age), 'year(s)-----')
else:
    print('-----Only +ve values and less than 100 Acceptable-----')

#prefer if-else-else....

#Output Formatting -->old style formatting (using commas)
#% usage (%f,%d), .format() usage, fstring notation
a,b = 7,9
print(a)
print(b)
print(a,b)
name = "Codegnan"; batch = "DataAnalytics"
print(name,batch)#by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='----->')
#end='\n', \t -->tabe space
print(name,batch,end='\t')
print(a,b,end='')
print('Hyderabad')

name = 'Codegnan'; batch = 'DA-023';place='Hyderabad'
#Usage of commas
print(batch, 'is in', name)#variables and msg to be separated by comma
print(name,'is in', place, 'age is', age, 'years')
#Old style formatting --->%d--->integer,%s--->string,%f-->float
salary = 25000
 '''   




















   

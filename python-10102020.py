print("hello world")
print("hello world in much fun")
x=10
print(x)
print(type(x))
s = "python is fun"
print(type(s))
print("value of x is:",x)
# print("value of y is:",y)
cars =100
drivers = 80
print("there are cars ", cars, "and drivers ", drivers)
print ("car pool cpacity is ", drivers*4)
print("theer sre {} cars and {} drivers".format(cars,drivers))
print(f"theer sre {cars} cars and {drivers} drivers")
print("theer sre %d cars and %d drivers"%(cars,drivers))
x=100**123
print(x)
x+7635
print(x)
x=10
y=20
print(x+7-y)
print(x*6)
y=6.8
print(type(y))
print(x+y)
# built-in functions -- print, type, str/int, help, dir
print(x+19)
print(3.9+y)
print(s + "5")
print(str(x))
print(type(str(x)))
s = "string"
print(2*s)
salary = '6580'
salary = int(salary)
print(salary * 1.2)
print('welcome')
salary = 7800
print('salary after 10% hike is', salary*1.1)
print('end of program')
salary = '20000'
print(salary*2)
s1 = 'python is fun'
s2 = "python is fun"
s3 ='''python is fun'''
s4="""python is fun """
print(s1 + "\n"+ s2 + "\n" + s3 + "\n" + s4)
s = """python is fun
thanks you
we all learning python fro data scrince"""
print(s)
print('hi\n how are you')
print('/localtion/of/new/file/file.txt')
print('c:\location\of\new\file\file.txt')
print('c:\\location\\of\\new\\file\\file.txt')
print('hi\nhow are you')
print('hi\\nhow are you')
print(r'c:\location\of\new\file\file.txt')
# number = input("give me a number:")
# print(type(number))
# print(number)
# number = int(input('enter a number:'))
# print(number + 5)
# import keyword
import math as m
import os as o
print(m.sqrt(9))
print(o.getcwd())
print(m.pi)
print(m.factorial(6))
import builtins
print(builtins.all)
import random as r
print(r.randint(1,100))
import numpy as numpy
# print(numpy.amax(10,20))
# print(m.)
print(dir(m))
# print(help(m.sqrt))
print('hi how are you'.capitalize())
salary = '$7600'
print(salary.strip('$'))
salary = '$' + str(int(salary.strip('$')) * 1.3)
print(salary)
s='python is fun'
print(s.capitalize())
print(s.strip())
# HOMEWORK - explore string functions
print(s.format())
print('today is {} and {} is sunday'.format('first','second'))
print(s[0])
print(s[-1])
print(s[-2])
print(s[-4])
print(s[-5] == s[8])
print(s[0] == 'P')
print(s[2:5])
print(s[1:9:2])
print(s[:4])
print(s[1:7])
print(len(s)-1)
print(s[6:2:-1])
print(s[::-1])
s='dad'
print(s[::-1] == s) #palendine string
x = 10
if x == 10:
    print('x is TEN')
    print('end of if block')
print('outside if block')

investment = 100
income = 120
if investment > income:
    print('loss making business')
    print('end of if block')
elif investment == income:
    print('break even')
else:
    print('profitable business')
    print('end of else block')


# take input from user(an integer)
# check if number is odd/even

# number = int(input('enter a number:'))
# if(number % 2) == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')

for i in range(10):
    print(i, end =' ')

print('is' in 'python is fun')
print('py' in 'python is fun')

# for i in range(1,10,2):
#     print(i, end =' ')

for i in range(1,20,2):
    print(i,end =' ')

num = int(input('Enter a number:'))
fact = 1
for i in range(1, num+1):
    fact = fact * i
    print(fact)
print(m.factorial(9))

no_vaccine = True
while no_vaccine:
    print('take precaution')
    print('avoid public places')
    check = input('is vaccine available(yes/no)?:')
    if check == 'yes':
        print('hurrey')
        no_vaccine=False
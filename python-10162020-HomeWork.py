# def add_student():
#     name = input('Enter your name:')
#     roll_no = int(input('Enter your roll number:'))
#     ph = input('Enter your phone number:')
#     rec = {'name':name, 'phone':ph}
#     data[roll_no] = rec

# def update():
#     who = int(input('enter roll number to update:'))
#     rec = data[who]
#     for key, value in rec.items():
#         new = input(f'{key} ({value}):')
#         data[who][key] = value if new =='' else new

# def delete():
#     pass

# def display():
#     print(data)

# data = {}
# while True:
#     print('1. Add student')
#     print('2. update student details')
#     print('3. delete student')
#     print('4. display student details')
#     ch = int(input('enter your choice[1-5]: '))
#     if ch == 1:
#         add_student()
#     elif ch==2:
#         update()
#     elif ch==3:
#         delete()
#     elif ch==4:
#         display()
#     elif ch==5:
#         save_to_file()
#     else:
#         break

# data = {'id':{'name':'Akash','age':25}}



# 1. add add_student
# 2. update student details
#
#
# 1. white a program to find if a given number is prime or not
# 2. write a function to get the factorial of a number 1*2*3*4*5....*n
# 3. Days of the week are represented as
# ('mon','tue','wed','thu','fri','sat','sun')
# write a function which takes a day (string) and a number (k) as arguments and return a day of the week that is k days later
# e.g. s='wed' and k = 2 --> function should return 'fri'

# day = input('Enter the day:')
# ahead_num = int(input('Enter the ahead number:'))
# print(f'{day}  {ahead_num}')
# week_days = ['mon','tue','wed','thu','fri','sat','sun']
# print( ahead_num % 7)
# print()
# def isPrime(number):
#     if number > 1:
#        for i in range(2, number):
#            if (number % i) == 0:
#                print(number, "is not a prime number")
#                break
#        else:
#            print(number, "is a prime number")
#     else:
#        print(number, "is not a prime number")
#
# prime = int(input('Enter a number to check for prime:'))
# isPrime(prime)




# def my_factorial(x):
#     fact = 1
#     for i in range(1,x+1):
#         fact = fact * i
#     return fact
# factorial = int(input('Enter a number to check for factorial:'))
# print (f'The factorial of {factorial} is : {my_factorial(factorial)} ')

# import math
# print(math.factorial(9))


# map function
map(int, ['34','6','12','9'])
print([int(x) for x in ['34','6','12','9']])
print(list(map(int, ['34','6','12','9'])))

def validate(x):
    if int(x)<0:
        return 0
    else:
        return int(x)

print(list(map(validate,['34','6','12','9','-1'])))
print(list(map(str.upper,['python','is','fun'])))


fh = open('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10172020/sample.txt')
contents = fh.read()
print(contents)
fh.close()

with open('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10172020/sample.txt') as fh:
    # fh.writelines("sudhir tomar last line")
    contents = fh.read()
    print(contents)
    print(type(contents))
    contents = fh.readline()
    print(contents)
    contents = fh.readline()
    print(contents)
    print(dir(fh))
    print('**' * 20)
    print(fh.read())
    print('**' * 20)

# with open('/Volume/MacData/Data/NSE-INFY.csv') as infy:
#     contents = infy.read()

with open('/Users/stomar-n/001_sudhir_2020_nmac/cognexia_training_python/10172020/sample2.txt','w+') as fh:
    fh.write(100*'python is fun1\n')
    fh.writelines(['line 1', 'line 2'])

# k = 10
# print('hello')
# try:
#     num = int(input('enter a number:'))
#     print(k/num)
# except ZeroDivisionError:
#     print('Exception is handled')
#     num = int(input('enter a number:'))
#     print(k/num)
# except ValueError:
#     print('value error')
# except Exception:
#     print('Generic handling error')
#
# print('important stuff here')
# print('end of program')

radius = 4.2
name ='A'
color = 'red'
circle2_radius = 5.3
circle2_name = 'B'

circle3_radius = 5.3
circle3_name = 'B'

# from math import pi
# class Circle:
#     radius = 3.1
#     name ='A'
#     def calc_area(self):
#         print(pi*self.radius**2)
# c1 = Circle()
# print(c1.radius)
# print(c1.calc_area())

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = 'A'
    def calc_area(self):
        print(pi*self.radius**2)
        return pi*self.radius**2

c1 = Circle(4.2)
c2 = Circle(5.1)
print(c1.calc_area())
print(c2.calc_area())

from math import factorial
from math import factorial, sqrt
import math as m

from math import pi
class Circle:
    def __init__(self,r,name):
        self.name=name
        self.radius = r
    def calc_area(self):
        print(pi*radius**2)
        return pi*radius**2

c1 = Circle(4.3,'A')
print(c1.name)
print(c1.radius)
c1.color='red'
print(c1.color)
print(c1.calc_area())

lst = [2,3,5]
print(lst * 2)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.__version__)
print(arr)
print(10*'*')
arr = np.array(42)
print(arr)
print(10*'*')
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(10*'*')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)
a = np.arange(20)
print(a)
print(100*'*')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0, 1, 2])
print(100*'*')
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
print('Last element from 2nd dim: ', arr[1, -1])
print(100*'*')
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr)
print(arr[1:5:2])
print(100*'*')
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)
print(arr[0:2, 1:4])
a=np.arange(100)
print(a)
print(a/3)
print(a.reshape(10,10))
a2 = np.arange(100).reshape(10,10)
print(a2)
print(a2[0])
a3 = np.arange(9).reshape(3,3)
print(a3)
print(np.arange(100).reshape(5,20))
print(a2.sum())
print(a2[0].sum())
print(a2.sum(axis=0))
print(a2.sum(axis=1))
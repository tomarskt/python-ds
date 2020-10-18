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




def my_factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact
factorial = int(input('Enter a number to check for factorial:'))
print (f'The factorial of {factorial} is : {my_factorial(factorial)} ')

import math
print(math.factorial(9))

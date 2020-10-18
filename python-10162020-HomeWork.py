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

# -*- coding: utf-8 -*-
"""

@author: Hemant Rathore
"""


### NumPy Arrays

# Creating NP Array using list




import numpy as np


my_list = [1,2,3]



np_arr=np.array(my_list)



print(np_arr)

type(np_arr)

print(np_arr.dtype)



my_list = ['a','b','c']


np_arr=np.array(my_list)

print(np_arr)

print(np_arr.dtype.name)



# Creating Matrix using Numpy


my_new_list= [[1,2,3],[4,5,6],[7,8,9]]


np_mat = np.array(my_new_list)

print(np_mat)



## some inbuilt numpy utilities

# numpy.arange() - to Generate array of sequences



np_seq = np.arange(0,10)

print(np_seq)

# using custom sequences


np.arange(0,50,3)


np.arange(0.1,5,0.1)




# linspaces() - to devide the range into given number of equal intervals


np.arange(0,9)


np.linspace(0,9,100)



# full() - Creating np array using given constant


np.full(10,1)

np.full((5,5),0)

np.full((2,5,5),1)




# Analyzing the Array Structure


a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])



print(len(a))

print(a.shape)

print(a.size)




# Subsetting & Slicing operations

a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])


a[1,1]


a[3,2]


a[0]


a[0,:]

a[:,0]

a[0:2,1:3]



# with skipping

a=np.array([1,3,2,2,2,4,7,5,8,11,12,9,10,6,1])

a[1:10:2]



# Locate Indices

np.where(a==20)



## Array Manipulation

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])


a.shape

12 - 2x6, 6x2, 3x4, 4x3

# Reshape array

new_array = a.reshape(3,4)

print(new_array)

print(new_array.shape)

new_array = a.reshape(3,4,order='F')

print(new_array)

print(new_array.shape)


# Transpose Array

a=np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])

a.shape

print(a)


print(np.transpose(a))


print(a.T)



# Insert new element at given index

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

#(array,index,element)

a=np.insert(a,1,13)

a=np.insert(a,13,[14,15,16])

a

# Delete the element

a

a=np.delete(a,5)

a

# Append array

a

b=np.array([13,14,15,16])

a=np.append(a,b)

a


# Copy Array

a

b=a

b

a[0]=100

a

b

c= a.copy()

c

a[0]=1

a

b

c



np.unique(a, return_counts=True)



# Sorting

np.sort(a)


-np.sort(-a)

np.sort(a)[::-1]




# using Matrices and their operations

a=np.array([(1,2,3),(4,5,6)])

a

print(a.sum())

# col sum

print(a.sum(axis=0))

# row sum

print(a.sum(axis=1))



# Arithmetic Operations on Array

a=np.array([(1,2,3),(4,5,6)])

b=np.array([(10,20,30),(40,50,60)])

a

b

# addition

print(a+b)

# substraction

print(a-b)

# multiplication

print(a*b)

# division

print(a/b)



# Matrix Multiplication

a=np.array([(1,2,3),(4,5,6)])

b=np.array([(1,2,3),(4,5,6)])

b=np.array([(1,2,3),(4,5,6),(7,8,9)])


a.shape

b.shape


a*b

np.matmul(a,b)



# Read and Wrtie from/to file

b= np.loadtxt("array.csv",delimiter="|",dtype=int)

np.savetxt("array.csv", b, delimiter=";",fmt='%d')




### Control Structures in Python

## If Else Control Structure


var1,var2 = 200,50


if (var1 >200 and var2 <= 100)
than {

print(var1)
print("Hello")
}




if var1 > 200 and var2 <= 100:
    print(var1)
    print("Hello, i am inside the scope")
print("i am out of scope")




# if else



if var1 >200 and var2 <= 100:
    print(var1)

else:

    print(var2)



# else-if

var1 = 200
var2 = 50

if var1 >200:
    print(var1)

elif var2<=50:
    print(var2)

else:
    print("nothing")




## Loops

# for loop


num = list(range(10))


for i in num:

    print(i)





# using Continue to skip sequence

num = list(range(10))

for i in num:
    if i == 5:
        continue
    print(num[i])




# while loop


count = 10


while count > 1:

    print(count)
    count -= 1 # count = count -1

    # count += 1 # count = count +1




# using break

count = 10

while count > 1:
    if count==5:
        break
    print(count)
    count -= 1





### Creating Custom Functions



def my_fun(name = 'Ram',s_name = 'Singh'):


    print("Hello, My name is",name,s_name)





my_fun('John','Sheena')



my_fun()



my_fun('John')


a = my_fun(s_name='Sheena')

a

# function with return

def my_fun1(name = 'Ram',s_name = 'Singh'):

    return( "Hello, My name is "+ name + " " + s_name)




out = my_fun1()

print(out)





# Exception Handling


def simple_fun(n):
    print(n)



simple_fun(1)


l0 = [1, 2, 3, 4, 5]


for i in range(20):
    simple_fun(l0[i])




for i in range(20):
   try:

        simple_fun(l0[i])

   except IndexError: # Raised when accessing a non-existing index of a list
        simple_fun(0)

        print("Index Error-exception for i =",i)

   finally:
       print("done!")




# Some exception examples are ArithmeticError, OverflowError, ZeroDivisionError etc.

# For handling all type of exceptions


for i in range(20):
   try:
        simple_fun(l0[i])

   except Exception as e: # Raised in case of all the exceptions
        simple_fun(0)
        print("Faced Exceptione - "+str(e)+", for i =",i)

   finally:
       print("Done!")

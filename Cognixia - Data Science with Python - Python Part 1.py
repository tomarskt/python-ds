
# -*- coding: utf-8 -*-
"""
@author: Hemant Rathore
"""


print("Hello World!!")



### Introduction to Python - 
## 1. Using Python in Interactive Mode




import sys


# Know your python installation path

sys.executable


## know & set your working directory

import os

os.getcwd()


os.chdir("D:\Data Science Training\Data")


os.getcwd()



import sys




# Interactive Python Mode


1+2


2*4




# Using Variables



x = 0.75

a = 3/4


a



print(a)



b = a+2



 
print(b)



a = 100
b = 200.5
c = 300.45


a,b,c = 100,200.5,300.45


print(a,b,c)





##### 2. Data Structures in Python


#### 2.1 List - Array type structure, it supports different datatype in 1 single list

## to create list use []


# [1,2,3,4,5,6,7,8,9]


# ['adfds','bddsfsd','c']

# [] for List



a = [1,2,3,4,5]

a

print(a)

type(a)


b = ['a','b','c','d']


print(b)

# OR

b = ["a","b","c","d"]



c = [1.2,2.3,3.4,4.5]



# different datatypes

d = ['a',1,2.345,1+2.34j]

d


## Accessing List elements


range(1,100)


l1 = list(range(1,100))


print(l1)


# In Python indexes start with 0



l1[0]


l1[4]


len(l1)

l1[98]


# Using negative indexes

l1[-3]


# Using : for accessing range

l1[1:5] # staring from start position upto (n-1)th position


l1[50:]


l1[:50]


l1[-5:]




# List Concatenation



l2 = ['a','b','c','d']


l1+l2


l1 +l1

# list Replication
 
l2*4




# Updaing list elements


l2[3] = 'x'

l2

# Adding new element




l2.extend([10,11,12,13])

Or

l2 = l2 + [10,11]



# Inserting at specific index (index,value)


l2.insert(2,100)

l2

# Deleting element

del(l2[2])

l2




# Copying list - assignment is not copy, it creates reference to the same object


l3 = l2


l3


l2[2] = 200

l2

l3

# correct way to copy

l4 = l2.copy()

l2[2] = 300

l2

l3

l4




#### 2.2 tuple - immutable list - read only

## to create tuple use ()

t1 = (1,2,3,4)

t1

print(t1)

type(t1)

t1[1]

t1[1:3]

t1[-1]

# assignment not possible

t1[3] = 5



# tuple concatenation



t1 = t1 + (5,)

print(t1)



# multiplication

t2=t1*2




#### 2.3 dictionary - hash table type structure, contains key-value pairs

## to create dictionary use {} 

[............'Raj','9874464646'.............]



l1 = ["9874464646"]

d1 = {"Raj":"9874464646"}



d1['Raj']


d1 = {"Raj":"9874464646","Raju":"9874464647","Rajesh":"9874464648"}




# accessing dict. elements

d1[0]

d1["Raj"]

d1["Raju"]


d1.keys()

d1.values()


# add new element


d1.update({"Raja" :"7965548722"})

d1

# Update existing element

d1.update({"Raj" :"23242423"})


# deleting elements

del(d1["Raj"])

d1
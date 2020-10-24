print("10232020 - Classes")
import numpy as np
import pandas as pd
# import panda as pd
# import panda as pd
a = np.arange(100).reshape(10,10)
print(a)
# a[0],a[1]
# a[-1],a[-2],
# a[1:5], a[-4:]
# a[1:6,2:5]
# a[start_index:stop_index, start_index:stop_index]
# a[start_index:stop_index:step, start_index:stop_index:step]
print(a[0])
print(a[1:6,2:5])
print(a[1:6,2:5])
print(a[2:7,1:8])
print(a[4:7,0:3])
print(a[1:2,0:3])
print(np.linspace(0,30,11)) #linearly spaced number
print(np.linspace(0,30,20))
# [0,3,6] - integers
#[ 0.,3.,6.] - > allfloats
print(np.random.randint(10,100))
print(np.linspace(0,30,11,dtype=int))
print(np.random.randint(10,100,size=100))
print(np.random.randint(10,100,size=100).reshape(10,10))
a = np.random.randint(10,100,size=100).reshape(10,10)
print(a)
print(a[0,:])
print(a[0,:].mean())
print(a[0:4,:])
print(a[0:4,:].mean(axis=1))
print(a[0:4,:].mean(axis=1).min())
print(a[0:4,:].mean(axis=1).max())
print(a[0:4,:].mean(axis=1).sum(axis=0))
print(a[0:4,:].mean(axis=1).mean(axis=0))
lst1= [1,2,3]
lst2=[4,5,6]
print([x+y for x,y in zip(lst1,lst2)])
import time
SIZE = 10000000
lst1 = list(range(SIZE))
lst2 = list(range(SIZE))
t0 = time.time()
res = [x+y for x,y in zip(lst1,lst2)]
# print([x+y for x,y in zip(lst1,lst2)])
print(f'Time taken for addition of ywo lists: {(time.time() - t0)}')
a1 = np.arange(10).reshape(5,2)
a2 = np.random.randint(0,100,size=10).reshape(5,2)
print(a1)
print(a2)
a1[2]=a2[2]
print(a1)
print(np.insert(a1,2,np.array([0,0]),axis=0))
print(a1.flatten())

# import numpy as np
# array1 = np.array([2, 2, 2, 0, 2, 0, 2])
# print np.where(array1==0, 1, array1) 
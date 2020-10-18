# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:27:35 2020

@author: Hemant Rathore
"""

import numpy as np


# Random number generation from uniform distribution (btw 0-1)


np.random.rand(1)

np.random.rand(100)

np.random.rand(5,5)

np.random.randint(1,9,size=(5,5))



## Statistical Summary functions

a=np.random.rand(1000)



# max
np.max(a)

# min
np.min(a)

# sum
np.sum(a)

# mean
np.mean(a)

# median
np.median(a)

# variance
np.var(a)

# Std. Dev.
np.std(a)

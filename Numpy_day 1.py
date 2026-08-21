
#<<<<<<<<<<<<<<<20 AUGUST 2026 >>>>>>>>>>>>>>>>>>

# TO CHECK NUMPY VERSION 

import numpy as np
print (np. __version__)

# Numpy ND ARRATY OBJECT

import numpy as np
x = np.array([1,2,3,4,5,6]) 
print (x)
print(type(x))


# A LIST TUPLE OR ARRAY LIKRE OBJECT WITH ARRAY() AND ITS WILL GET CONVERTED TO ND ARRAY 

import numpy as np 
y = ((1,2,3,4,5,6,))
print(y)
print(type(y))

# TYPES OF ARRAY
#0-D ARRAY
# 1-D ARRAY 
# 2-D ARRAY 
# 3-D ARRAY 

###########(............0-----D ARRAY--------------)#################

import numpy as np 
z = np.array(42)
print(z) 


###########(............1-----D ARRAY--------------)#################

import numpy as np 
k = np.array([1,2,3,4,5,6,7,8])
print(k) 

###########(............2-----D ARRAY--------------)#################


import numpy as np 
p = np.array([[1,2,3,4,5], [2,3,4,5,7]])
print(p) 


###########(............3-----D ARRAY--------------)#################

import numpy as np 
o= np.array([[[1,2,3,4,],[1,2,3,4,],[1,2,3,4],[1,2,3,4]]])
print(o) 

###########(CHECK HOW MANY DIMENSION ARRAY IS )#################

import numpy as np 
a=np.array(42)
b= np.array([1,2,3,4,5,6,7,8])
c=np.array([[1,2,3,4,5], [2,3,4,5,7]])
d=np.array([[[1,2,3,4,],[1,2,3,4,],[1,2,3,4],[1,2,3,4]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#_____________________5 D ARRAY__________________________#

import numpy as np 
n= np.array ([1,2,3,4,5], ndmin=5)
print(n)
print('number of dimension :',n.ndim)
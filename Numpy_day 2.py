#<<<<<<<<<<<<<<21 August 2026>>>>>>>>>>>>>>>>>>>>>>


# ARRAY INDEXING IS THE SAME AS ACCESSINDING AN ARRAY ELEMENT ....
#>>>>>>>>>>>>INDEXING STARSTS WITH 0<<<<<<<<<<<<<<<<<<<<<

import numpy as np 
s=np.array ([1,2,3,4])
print(s[0])

#>>>>>>>>>>>>>>WE CAN ADD ELEMENTS BY USING INDEXING <<<<<<<<<<<<

import numpy as np 
d=np.array([1,2,3,4])
print(d[2] + d[3])

#>>>>>>>>>>>>>>>>>ACESSING THE 2-D ELEMENTS>>>>>>>>>>>>>>>>

import numpy as np 
f=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(" 2nd element in 1st row ",f[0,1])
print(" 5th element in 2nd  row ",f[1,4])


# ACCESSING THE 3-D 
import numpy as np
g=np.array ([[[1,2,3,],[4,5,6],[7,8,9],[10,11,12]]])
print(g[0,1,2])


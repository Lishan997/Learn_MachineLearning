#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


a = np.array(2)
a.ndim


# <h1>Scalors</h1>
# 
# Scalor does not have dimensions - 0 dimension<br>
# above "a" is scalor it has no dimension

# In[5]:


b = np.array([1,2,3])
b


# In[6]:


b.ndim


# <h1>Vectors</h1>
# 
# above "b" is a 1D Tensor(1D array)<br>
# "b" is made of combinations of scalors there for it is vector<br>
# "b" vector has 3 dimensions(x,y,z)<br><br>
# <b>Table</b>
# ![image-4.png](attachment:image-4.png)
# 
# <b>row vector</b>
# ![image-5.png](attachment:image-5.png)
# 
# <b>column vector</b>
# ![image-3.png](attachment:image-3.png)
# 
# <b>above row vector has 3 dimensions</b>
# ![image-6.png](attachment:image-6.png)
# 
# <u><b>important</b></u>
# <ul style="list-style-type:disc;">
#   <li> axis = rank = dimension </li>
#   <li>Sometimes the number of dimensions in a vector in data sets can be more than 3, then it may be difficult for us to represent graphically, in such cases we may have to reduce the number of dimensions in the vector that is how "Dimensionality reduction” come to the picture</li>
# </ul>

# In[8]:


c = np.array([[1,2,3], [4,5,6], [7,8,9]])
c.ndim


# <h1>Metrices(2D Tensors)</h1>
# 
# above "C" is a 2D Tensor(2D array)<br>
# "c" is made of combinations of vectors there for it is matrics<br>
# "c" tensor has 2 dimensions(x,y)<br>
# "c" tensor has 3 vectors(each vector has 3 dimension)
# Table of dat is matrics
# 
# ![image.png](attachment:image.png)

# In[16]:


d = np.array([
    [[1,2,3], [4,5,6], [7,8,9]], #<--- 2D Tensor/Metrics
    [[-1,-2,-3], [-4,-5,-6], [-7,-8,-9]],#<--- 2D Tensor/Metrics
    [[-10,-20,-30], [-40,-50,-60], [-70,-80,-90]]#<--- 2D Tensor/Metrics
])


# <h1>3D Tensors</h1>
# 
# above "d" is a 3D Tensor(3D array)<br>
# "d" is made of combinations of metrices there for it is 3D Tensor<br>
# "d" has 3 dimensions(x,y,z)<br>
# "d" has 3 Metrics(each Metrics has 3 dimension / 3 vectors)<br>
# each vector has 3 dimension  
# 
# ![image.png](attachment:image.png)

# In[17]:


# above each sentences store as below

sentences = np.array(
    [
        [[1,0,0,0,0],[0,1,0,0,0]], # <-- Hi Onara
        [[1,0,0,0,0],[0,0,1,0,0]], # <-- Hi Danuja
        [[1,0,0,0,0],[0,0,0,1,0]], # <-- Hi Deen
        [[1,0,0,0,0],[0,0,0,0,1]], # <-- Hi Dewmini
    ]
)


# <h1>Shape and Size</h1>
# 
# <p>How many item can be stored in a datastructure</p>
# 
# <p> shape of c matrics is (3,3) </p>
# <p> size of c matrics is 3*3 = 9 (Numberof elemnts) </p>
# 
# <p> shape of d tensor is (3,3,3) / (number of 2D tensors, number of 1D tensors{vectors}, number of 0D tensors{scalors}) </p>
# <p> size of d tensor is 3*3*3 = 27 (Numberof elemnts) </p>

# <b>nD Tensors = Combination of (n-1)D tensors</b>

# ![image.png](attachment:image.png)
# ![image-2.png](attachment:image-2.png)

# In[ ]:





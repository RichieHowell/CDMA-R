#Part 5_1

# 1 - did this by just doing 'ipython'in cmd
# 2 - did this with 'import pandas', 'import numpy' and 'import matplotlib'

# 3 - looked up 5 commands in np by np.diag*? and got np.diag, np.diag_indices, np.diag_indices_from, np.diagflat, np.diagonal

# 4 - used ctrl l to clear screen, then up arrow to get a previous command, used down arrow to go back to my empty prompt, looked at the input on line 3 of a file using _i3 and the output of that line using _3

#5 - used %run to run a program, %paste to paste a code into cmd, %quickref to get a lot of information, %timeit to get the average time of execution of a piece of code, %hist to see everything i have done,%pwd to see my current directory, %cd to change my directory, and %ls to see all the files in the directory i just moved to

#6 - ran a few lines of inclass4_3 part 1 by copying them from notepadd++ and using %paste

#7 - found information on %xdel by running %xdel?, str.split with str.split?, imported re then found information on it with re?, and i found out that matplotlib.pylab does not exist with matplotlib.pylab?

#8 - started pylab with 'pylab', built the plot by doing a = numpy.random.randn(100) and plot(a.cumsum()) and a line graph showed up on my screen, found information on random and i see randn genereates uniformly distributed values

#9 - cumsum returns the cumulative sum of the elements along a given axis, found by running cumsum?

#10 - 100 numbers = 100000 loops with 4.58microseconds per loop so .458 seconds, 1000 number = 10000 loops with 38.7 microseconds per loop so .387 seconds, 1000 loops with 347 microseconds per loop so .347 seconds. I found out that the more numbers you generate, the less time it seems to take.
#found this information by running %timeit numpy.random.randn(100), %timeit numpy.random.randn(1000), %timeit numpy.random.randn(10000)
#-------------------------------------

#Part 5_2

#-------------------------------------
# coding: utf-8

# In[19]:

import numpy as np;


# In[20]:

#create the arrays
arr1 = np.array([1,2,3,4,5]);
arr2 = np.array([2,3,4,5,6]);


# In[21]:

#prints the shape of the arrays
print arr1.shape;
print arr2.shape;
#prints the type of the dimensions
print arr1.dtype;
print arr2.dtype;


# In[22]:

#element-wise summation
print arr1 + arr2;


# In[23]:

#element-wise multiplication
print arr1 * arr2;


# In[24]:

#creates a 6x6 identity matrix
imatrixSix = np.eye(6);


# In[25]:

#changes the third row to be all fives
imatrixSix[2] = np.array([5,5,5,5,5,5]);


# In[26]:

#change all none zero elements to 6
imatrixSix[imatrixSix != 0] = 6;


# In[35]:

#create an empty 3 dimensional array, and change it's type to integer
arr3 = np.empty((2,3,4));
arr3 = arr3.astype('int64');


# In[36]:

#print its dimensions, shape, and size
print arr3.shape;
print arr3.dtype;
print arr3.ndim;


# In[37]:

#set the array position
arr3[1][2][2] = 5;


# In[50]:

#create an array of 20 random values between 0 and 1
randArr = np.random.rand(20);


# In[47]:

#get the min, max, sum, mean, and standard deviation of the random array
print randArr.min()
print randArr.max()
print randArr.sum()
print randArr.mean()
print randArr.std()


# In[55]:

#changes all the numbers less than .5 to 0, and the rest to 1
randArr = np.where(randArr < .5, 0,1)


# In[56]:

#sorts the array
randArr.sort()


# In[58]:

#finds all the unique values
randArr = np.unique(randArr)


# In[ ]:
#-----------------------------------------------------

#Part 5_3

#----------------------------------------------
# coding: utf-8

# In[1]:

#imports 
import numpy as np
import pandas as pd
import Quandl


# In[2]:

#get the bitcoin exchange rate venues
bitStamp = Quandl.get("BCHARTS/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="8jxkNH7xjx8xy8pRyWQ8")
bitFinex = Quandl.get("BCHARTS/BITFINEXUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="8jxkNH7xjx8xy8pRyWQ8")
bitLake = Quandl.get("BCHARTS/LAKEUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="8jxkNH7xjx8xy8pRyWQ8")


# In[5]:

bitStamp.head()
#column names are date, open, high, low, close, volume(BTC), volume(currency), and weighted price
#the frequency of the data is daily


# In[15]:

#create the index objects
ind1 = bitStamp.index;
ind2 = bitFinex.index;
ind3 = bitLake.index;


# In[16]:

#print the index objects
print ind1
print ind2
print ind3
#ind1 and ind2 have 273 elements, ind3 has 214 elements


# In[21]:

print ind1.values
print ind2.values
print ind3.values
#the time of object being displayed is a datetime, and the dtype is datetime64[ns]


# In[26]:

print bitStamp.columns
print bitFinex.columns
print bitLake.columns
#in each we have 7 columns


# In[28]:

#drops the volume (BTC) column from each dataframe
bitStamp.drop('Volume (BTC)', 1)
bitFinex.drop('Volume (BTC)', 1)
bitLake.drop('Volume (BTC)', 1)


# In[ ]:







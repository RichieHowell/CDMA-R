
# coding: utf-8

# In[1]:

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:

#get the project dataframe
projectDF = pd.read_csv('cars93.csv', index_col = 0)


# In[3]:

#gets numerical summaries for the data
projectDF.describe()


# In[4]:

#fills in all the NAN's with 0's
projectDF.fillna(0)


# In[5]:

#data reshaping
#cylinders are all integers except for rotary which says "rotary" so we change rotary to be 0
projectDF['Cylinders'] = projectDF['Cylinders'].map({'rotary':0, '3':3, '4':4,'5':5,'6':6,'8':8})


# In[6]:

#replace origin values of non-USA with 0 and USA with 1
projectDF['Origin'] = projectDF['Origin'].map({'non-USA':0, 'USA':1})


# In[10]:

#3 visualizations that are meaningful
#visualization 1 : scatterplot showing RPM to horsepower
scatter = projectDF.plot(kind = 'scatter', x='RPM', y='Horsepower')
plt.title('Scatter plot using the variables RPM (x) and Horsepower(y)')
scatterFig = scatter.get_figure()
scatterFig.savefig('hw4Scatter.png')
plt.clf()


# In[9]:

#visualization 2 : denisty plot of the weight variable
dens = projectDF['Weight'].plot(kind = 'density')
plt.title('density plot of the weight variable')
densFig = dens.get_figure()
densFig.savefig('hw4Density.png')
plt.clf()


# In[11]:

#visualization 3 : histogram of the passengers variable
hist = projectDF['Passengers'].hist(bins = 7)
plt.title('histogram of the price variable')
histFig = hist.get_figure()
histFig.savefig('hw4Hist.png')
plt.clf()


# In[12]:

#create a pickle for the project Data frame
projectDF.to_pickle('Project_Pickle')


# In[ ]:




#Inclass 7 Part 1


# coding: utf-8

# In[1]:

#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:

#get the project dataframe
projectDF = pd.read_csv('cars93.csv', index_col = 0)
projectDF


# In[3]:

#creates a histogram of the price variable with 8 bins
hist = projectDF['Price'].hist(bins = 8)
plt.title('histogram of the price variable')
histFig = hist.get_figure()
histFig.savefig('projectHist.png')
plt.clf()


# In[4]:

#creates a denisty plot of the min price variable
dens = projectDF['Price'].plot(kind = 'density')
plt.title('density plot of the price variable')
densFig = dens.get_figure()
densFig.savefig('projectDensity.png')
plt.clf()


# In[5]:

#creates a bar chart of the Passengers variable
bar = projectDF['Passengers'].plot(kind = 'bar')
plt.title('Bar graph of the passengers variable')
barFig = bar.get_figure()
barFig.savefig('projectBar.png')
plt.clf()


# In[6]:

#creates a horizontal stacked bar chart with categories summing to 1 using the weight variable 
barh = projectDF['Weight'].div(projectDF['Weight'].sum(1).astype(float), axis = 0).plot(kind = 'barh',stacked = True)
plt.title('Horizontal bar chart with categories summing to 1 of the weight variable')
barhFig = barh.get_figure()
barhFig.savefig('projectBarHorizontal.png')
plt.clf()


# In[7]:

#creates a scatter plot of the price variable and weight variable
scatter = projectDF.plot(kind = 'scatter', x='Price', y='Weight')
plt.title('Scatter plot using the variables Price (x) and Weight(y)')
scatterFig = scatter.get_figure()
scatterFig.savefig('projectScatter.png')
plt.clf()


# In[ ]:



#Inclass 7 part 2

# coding: utf-8

# In[20]:

import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import sklearn as sk


# In[12]:

#reads the medical csv
medicalDF = pd.read_csv('medical.csv')


# In[30]:

#gets the features age and HgA1c
X = np.array(medicalDF[['Age','HgA1C']])
#gets the array of literacy
literacyTypes = {'HIGH':1, 'LOW':0}
y = np.array(medicalDF['A Literacy Category'].map(literacyTypes))


# In[31]:

#set up the training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.25, random_state=33)


# In[32]:

#scale the sets
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[34]:

#create the classifier
from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, y_train)
#prints out the equation
print clf.coef_
print clf.intercept_
#the equation is 27.65 - 5.08968882 * x1 + 16.81823155 * x2 = 0


# In[35]:

#get the accuracy on the training set
from sklearn import metrics
y_train_pred = clf.predict(X_train)
print metrics.accuracy_score(y_train, y_train_pred)
#it scored 89.2% right


# In[39]:

#get the accuracy on the testing set
y_pred = clf.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)
#it scored at 100%


# In[40]:

#gets the confusion matrix
print metrics.confusion_matrix(y_test, y_pred)
#we only had 1 number meaning that the testing matrix only
#had a sample from the people with High litracy, and it correctly
#guessed that they all had high literacy

#the classifier was not so useful since our sample only took
#people withe High litracy.


# In[ ]:



#Inclass 7 part 3



# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[2]:

import sklearn as sk
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
#answer to number 2 : 0,1,4,6 are easily seperated while 5,8, and 9 might be confounded


## Principal Components Analysis

#### Dimensionality Reduction and Visualization

####### #Get the digits data

# In[3]:

from sklearn.datasets import load_digits
digits = load_digits()


####### #What does the digits dataset contain?

# In[4]:

print digits.keys()


####### #Each row of data in X_digits corresponds to one of the following digits:

# In[5]:

digits.target_names


# In[6]:

X_digits, y_digits = digits.data, digits.target


####### #What does the X matrix look like?

# In[7]:

X_digits.shape


####### #Get the first 10 principal components of the X_digits matrix

# In[8]:

from sklearn.decomposition import PCA

estimator = PCA(n_components=10)
X_pca = estimator.fit_transform(X_digits)


####### #What does the PCA matrix looks like

# In[9]:

X_pca.shape


# In[10]:

X_pca


####### #Visualize our data using the first two principal components in a scatterplot

# In[12]:

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 7][y_digits == i]
    py = X_pca[:, 8][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('Eighth Principal Component')
plt.ylabel('Ninth Principal Component')
#answer to number 4 : this new graph shows all the digits are confounded together and it would be hard to distinguish between them


# In[ ]:




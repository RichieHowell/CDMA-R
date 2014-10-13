#Inclass 6 PART 1
#-------------------------------------------
# coding: utf-8

# In[1]:

#normal imports
import pandas as pd
import numpy as np


# In[2]:

#creates the data frames for work_comma, work_tab and 
commaDF = pd.read_csv('work_comma.csv');
tabDF = pd.read_table('work_tab.txt',index_col = False);
stressDF = pd.read_table('stress2_1.txt',skiprows = 19, header=None, delimiter = '\s+');


# In[3]:

#gets the github events api and turns it into a data frame with 4 columns 
import json
import requests
request = requests.get('https://api.github.com/events')
temp = request.json()
fields = ['id', 'created_at','public', 'type']
githubDF = pd.DataFrame(temp, columns = fields)


# In[4]:

#creates the pickle for the github data frame
githubDF.to_pickle('GH_pickle')
#loads the pickle into githubDF2 which is not a copy of githubDF
githubDF2 = pd.read_pickle('GH_pickle')


# In[5]:

#saves the data in HDF5 form
storage = pd.HDFStore('GHData.h5')
#stores the data in the storage area
storage['GH'] = githubDF
#accesses the stored data frame
storage['GH']


#PART 2
#-----------------------------------------------------------------

# coding: utf-8

# In[1]:

#normal imports
import pandas as pd
import numpy as np


# In[2]:

#create the project data frame using the pandas read_csv method
projectDF = pd.read_csv('cars93.csv', index_col = 0)


# In[3]:

#describes the projectDF dataframe
projectDF.describe()


# In[4]:

#turn a nurmerical column into a categorical variable
#first create the bins, i created these based on the min, 25%, 50%, 75% and max values, i used 1 under the min
#since it is not inclusive on the bottom end
bins = [14,18,21,25,46];
#these bins will cut the numerical column into 4 evenly distrubuted categories
projectDF['MPG.city'] = pd.cut(projectDF['MPG.city'],bins);


# In[5]:

#gets the frequences of the categorical column we just made
pd.value_counts(projectDF['MPG.city'])
#those frequencies are 26 for (21-25], 25 for (14,18], 25 for (18,21], and 18 for (25,46]


# In[6]:

#create the types of MPG variable, anything above average is good, anything below is bad
MPGtypes = {'(21, 25]':'Good', '(25, 46]':'Good', '(14, 18]':'Bad', '(18, 21]':'Bad'}
MPGcomparison = projectDF['MPG.city'].map(MPGtypes);


# In[7]:

#renames 2 columns
projectDF = projectDF.rename(columns = {'MPG.city':'cityMPG', 'MPG.highway':'highwayMPG'})


# In[8]:

#get random row numbers
sample = np.random.permutation(93);
#takes 47(half rounded up) random rows from the project data frame
training_set = projectDF.take(sample[:47]);
#time to do it again
sample2 = np.random.permutation(93);
training_set2 = projectDF.take(sample2[:47]);


# In[12]:

#combines the training sets
training_set_combine = pd.merge(training_set, training_set2);
training_set_combine.describe();
#drops the duplicate rows, merge already did this, but just to be safe
training_set_combine.drop_duplicates();
#to see how many we have left
training_set_combine.describe();
#we have 28 left which is 30%




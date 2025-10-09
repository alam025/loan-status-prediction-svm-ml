#!/usr/bin/env python
# coding: utf-8

# # Importing the Dependencies

# In[2]:
# Importing the Dependencies

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score



# #Data Collection and Processing

# In[4]:

# Data Collection and Processing
#loading the dataset to pandas Dataframe
#loading the dataset to pandas Dataframe
loan_dataset = pd.read_csv('loan.csv')


# In[5]:

#printing the first five rows of the dataframe
#printing the first five rows of the dataframe
loan_dataset.head()


# In[6]:

# Add shape analysis
# number of rows and columns
loan_dataset.shape


# In[8]:

# Add statistical analysis
# statistical measures
loan_dataset.describe()


# In[9]:

# Add missing value check
#number of missing values in  each column
loan_dataset.isnull().sum()


# In[10]:

# Add dropna()
# dropping the missing values
loan_dataset = loan_dataset.dropna()


# In[11]:


#number of missing values in  each column
loan_dataset.isnull().sum()


# In[13]:

# Add loan status encoding
#label encoding
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)


# In[14]:


#printing the first five rows of the dataframe
loan_dataset.head()


# In[15]:

# Add dependents analysis
#Dependent column values
loan_dataset['Dependents'].value_counts()


# In[16]:

# Replace 3+ with 4
#replacing the value of #+ to 4
loan_dataset = loan_dataset.replace(to_replace='3+',value=4)


# In[17]:


#dependent values
loan_dataset['Dependents'].value_counts()


# #Data Visualization

# In[18]:

# Add education countplot
#Education and loan status
sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)


# In[19]:

# Add marital status countplot

# marital status & Loan Status
sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)


# In[22]:

# Add all categorical encoding
#convert categorical columns to numerical values
loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},
                      'Self_Employed':{'No':0,'Yes':1},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)


# In[23]:


loan_dataset.head()


# In[25]:


#separating the data and label

X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_dataset['Loan_Status']


# In[26]:


print(X)
print(Y)


# #Train Test Split
# 

# In[27]:

# Add X, Y separation
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)


# In[28]:


print(X.shape,X_train.shape,X_test.shape)


# Training the model:
# Support Vector Machine Model

# In[30]:
# Add SVM initialization

classifier = svm.SVC(kernel='linear')


# In[31]:

# Add model training
#training the support Vector Machine Model 
classifier.fit(X_train,Y_train)


# #Model Evaluation

# In[32]:


#Accuracy score on training data

X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)


# In[33]:


print('Accuracy on training data: ',training_data_accuracy)


# In[34]:

# Add testing prediction
#Accuracy score on test data

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)


# In[35]:


print('Accuracy on test data: ',test_data_accuracy)


# #Making a predicitve system
# 

# In[ ]:





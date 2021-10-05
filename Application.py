#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st


# In[5]:


import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# In[6]:


dataset=load_iris()


# In[7]:


x=pd.DataFrame(dataset.data, columns=dataset.feature_names)
y=pd.Series(dataset.target)


# In[8]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y)


# In[16]:


class application:
    def __init__(self):
        self.model=LogisticRegression()
        
    def traindata(self):
        self.model.fit(x_train, y_train)
        return self.model
    def container(Self):
        st.title("Iris dataset classification Web Application")
        sepal_l=st.number_input("Enter the sepal length in cm")
        sepal_w=st.number_input("Enter the sepal width in cm")
        petal_l=st.number_input("Enter the petal length in cm")
        petal_w=st.number_input("Enter the petal width in cm")
        values=[sepal_l,sepal_w,petal_l,petal_w]
        return values
    def main_app(self):
        self.traindata()
        values=self.container()
        values_for_prediction=np.array(values).reshape(1, -1)
        pred=self.model.predict(values_for_prediction)
        res=dataset.target_names[pred[0]]
        probability=self.model.predict_proba(values_for_prediction)
        st.markdown('<p class="header"> Results</p>',unsafe_allow_html=True)
        col1, col2=st.columns(2)
        col1.markdown(f'<p class="font" style="border:5px">The Predicted plant is</p>',unsafe_allow_html=True)
        col2.markdown(f"{res}")
        col2.write(f"{probability[0][pred[0]]}")
        
        col1.write('<p>Its probability value is </p>',unsafe_allow_html=True)
        
       
        return self
op=application()
op.main_app()
        


# In[ ]:





import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

def priority_assigner(df,train_data):

  x_train.y_train,x_test,y_test=train_test_split(train_data,df['priority'],test_size=0.2,random_state=0)  
  #Has to be completed yet
  
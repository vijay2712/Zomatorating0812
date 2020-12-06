import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('deploy_df')
df.drop('Unnamed: 0',axis=1,inplace=True)
print(df.head())
x=df.drop('rate',axis=1)
y=df['rate']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=10)

#Building a Model

from sklearn.ensemble import ExtraTreesRegressor
ET_Model=ExtraTreesRegressor(n_estimators=120)
ET_Model.fit(x_train,y_train)

y_predict=ET_Model.predict(x_test)
print(y_predict)

#Lets save the model using Pickle
import pickle
pickle.dump(ET_Model,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

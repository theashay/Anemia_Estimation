import seaborn as sns
import tkinter as tk
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.naive_bayes import GaussianNB

import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from mlxtend.preprocessing import minmax_scaling
import os

        
df = pd.read_csv('E:/anemia_estimation/anemia_estimation/anemia_estimation/Anemia.csv')
df.head(10)
df.corr()

cor_mat=df.corr()
fig,ax=plt.subplots(figsize=(10,7))
sns.heatmap(cor_mat,annot=True,linewidths=0.5,fmt=".3f")
df.isnull()
df.isna().sum()
df.replace('Hemoglobin','111',inplace=True)
df.replace('MCH','222',inplace=True)
df.replace('MCHC','333',inplace=True)
df.replace('MCV','444',inplace=True)
df.head(10)

X = df.drop('IDENTIFICATION',axis=1).values
y = df['IDENTIFICATION'].values

original_data = np.random.exponential(size=1000)

# mix-max scale the data between 0 and 1
scaled_data = minmax_scaling(original_data, columns=[0])

# plot both together to compare
fig, ax = plt.subplots(1,2)
sns.distplot(original_data, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")

x = df.drop('IDENTIFICATION',axis=1).values
y = df['IDENTIFICATION'].values

from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.9, random_state = 0)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=1)

from sklearn.svm import SVC
svcclassifier = SVC(kernel='linear', C = 1.0 , gamma = 'scale')
svcclassifier.fit(x_train, y_train)

y_pred = svcclassifier.predict(x_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
ACC = (accuracy_score(y_test, y_pred) * 100)
repo = (classification_report(y_test, y_pred))
    
    #label4 = tk.Label(root,text =str(repo),width=40,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    #label4.place(x=205,y=100)
    
# label5 = tk.Label(root,text ="Model Traning is Completed \nModel anemia_MODEL.joblib",width=40,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
# label5.place(x=300,y=200)
from joblib import dump
dump (svcclassifier,"anemia_MODEL.joblib")
print("Model Traning is Completed \n Model saved as anemia_MODEL.joblib")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


df=pd.read_csv('loan-train.csv')

df=df.dropna()

#df['Loan_Status']=(df['Loan_Status']=='Y').astype(int)
catagarical_features = [feature for feature in df.columns if df[feature].dtypes == 'O']

catg_2_features=[]
for feature in catagarical_features:
    if len(df[feature].unique())==2:
        catg_2_features.append(feature)
for feature in catg_2_features:
    df[feature]=(df[feature]==df[feature].value_counts().keys()[0]).astype(int)

dependents = pd.get_dummies(df['Dependents'])

area = pd.get_dummies(df['Property_Area'])

area_dep_merged = pd.concat([df,area,dependents],axis='columns')

df =area_dep_merged.drop(['Property_Area','Semiurban','Dependents','0'], axis='columns')

c_matrix=df.corr()

strong_relation_features=[]
for feature in c_matrix['Loan_Status'].sort_values(ascending=False).keys():
    if c_matrix['Loan_Status'][feature]>=0.04 or c_matrix['Loan_Status'][feature]<=-0.04:
        strong_relation_features.append(feature)
strong_relation_features.remove('Loan_Status')


X=df[strong_relation_features]

X=X.rename(columns={"2": "two_dependant", "1": "one_dependant"})

y=df['Loan_Status']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train,y_train)

print(model.score(X_test,y_test))

pickle.dump(model, open('model_Loan_eligibility_predictions.pkl','wb'))

model_ = pickle.load(open('model_Loan_eligibility_predictions.pkl','rb'))

print(model_.predict([[1,1,1,0,1,1,3273,1820,1,81,0]]))



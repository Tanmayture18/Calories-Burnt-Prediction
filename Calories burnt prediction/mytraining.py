import pandas as pd
import numpy as np
import pickle


if __name__=="__main__":
    df1=pd.read_csv('exercise.csv')
    df2=pd.read_csv('calories.csv')
    df2.drop('User_ID',axis=1,inplace=True)
    df=pd.concat([df1,df2],axis=1)
    df.drop('User_ID',axis=1,inplace=True)
    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    df['Gender']=le.fit_transform(df['Gender'])
    X=df.drop('Calories',axis=1)
    y=df.Calories
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    from sklearn.preprocessing import StandardScaler
    sc=StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.fit_transform(X_test)
    #Algorithm
    from sklearn.ensemble import RandomForestRegressor
    rr=RandomForestRegressor()
    rr.fit(X_train,y_train)

    #Pickle
    file=open('model.pk1','wb')
    pickle.dump(rr,file)   
    file.close() 

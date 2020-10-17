# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:18:41 2020

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from datetime import datetime as dt
import seaborn as sns

df=pd.read_csv("data.csv")
df.shape
df.describe()
#converting to date time object
df["Year"]=pd.to_datetime(df["Year"],format="%Y")
df.dtypes
df.describe()

#filling missing values
df["Gender"].value_counts()
df.isnull().sum()
df["Gender"].fillna(st.mode(df.Gender),inplace=True)

#removing where states is null
df.State.unique()
df=df.loc[df.State.notnull(),:]

#accesing the year
df["Year"].dt.year
#finding the topper of each year
def toppers():
    for i in df["Year"].dt.year.unique():
        participants=df.loc[df["Year"].dt.year==i,"Gender"].count()
        df_2=df.loc[df["Year"].dt.year==i,"Gender"]
        df_2=pd.DataFrame(df_2)
        print(" {} Gender has more people in top 10 in year {}.".format(st.mode(df_2.Gender),i))
        male=df_2.loc[df_2["Gender"]=="M",:]
        male_cnt,gender=male.shape
        female=df_2.loc[df_2["Gender"]=="F"]
        female_cnt,gendr=female.shape
        if male_cnt==female_cnt:
            print("Both gender scored equal in top {}".format(participants))
        elif male_cnt>female_cnt:
            print("In the year {} , {} gender dominated the top {} with {} members".format(i,"male",participants,male_cnt))
        else:
            print("In the year {} , {} gender dominated the top {} with {} members".format(i,"female",participants,female_cnt))

toppers()

#too see which gender dominates the top 10 for past 4 years
male_cnt=df.loc[df["Gender"]=="M","Rank"].count()
tot=df.loc[:,"Rank"].count()
female_cnt=tot-male_cnt
print("In past 4 years {} have been males and {} have been females , out of {} toppers".format(male_cnt,female_cnt,tot))

#plot to see which gender performs better in top 10 past 4 years
df["Gender"].value_counts().plot.bar()
#which state performs better in the top 10 in past 4 years
df["State"].value_counts().plot.bar()

#converting actegorical to interger
#only LabelEncoding since there are only 
# two genders 0 and 1 are good enough
#1s rank has more importance than 2nd,...,10th rank so OneHotEncoder is not requires
from sklearn.preprocessing import LabelEncoder
df2=df.copy()
st_enc=LabelEncoder()
df2.State=st_enc.fit_transform(df2.State)
gen_enc=LabelEncoder()
df2.Gender=gen_enc.fit_transform(df2.Gender)

#heatmap shows no relationship of Rank with either State or Gender
sns.heatmap(df2.corr(),annot=True)

#Rank is not effected by State or Gender 
#need more data









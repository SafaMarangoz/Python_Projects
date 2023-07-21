## PANDASTA SECIM ISLEMLERI (SELECTION IN PANDAS)
######################################################
##VERI MANIPULASYONU VE ANALISTI DIYINCE AKLIMIZA SECIM ISLEMLERI  GELIR
######################################################

import pandas as pd
import seaborn as sns
df=sns.load_dataset("titanic")
df.head()
df.index
df[0:25]
##INDEXLERDE SILME ISLEMI

df.drop(0,axis=0).head()
delete_indexes=[1,3,5,7]
df.drop(delete_indexes,axis=0).head(10)

###KALICI OLARAK SILMEK
#df=df.drop(delete_indexes,axis=0)
#df.drop(delete_indexes,axis=0,inplace=True)

##########################################
##DEGISKENI INDEXE CEVIRMEK
##########################################

df["age"].head()
df.age.head()

df.index=df["age"]
df.drop("age",axis=1).head()

###KALICI SEKILDE YAPMA
df.drop("age",axis=1,inplace=True)
df.head()

####################################################
#### INDEXI DEGISKENE CEVIRME
####################################################
##1.yol)
df.index
df["age"]
##eror verdi cünkü sildik
##degıskeni ekleyelim
df["age"]=df.index
df.head()
##2.yol)
df.drop("age",axis=1,inplace=True)
df=df.reset_index().head()
df.head()
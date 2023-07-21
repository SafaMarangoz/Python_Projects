#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################
import pandas as pd
import seaborn as sns

df=sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe()
df.describe().T
df.isnull().values.
##BİR NUMPY ARRAY DÖNDÜ.SERİLERDE OLDUĞU GİBİ PANDAS DATAFRAMELERİNDE DE VALUES IFADESI KULLANIRSAK :
# SÜTUN VE SATIR İNDEKSI (DEĞİŞKENLERDEN ) ARINDIĞINDAN DOLAYI VERİ BUNU NUMPY ARRAYE DÖNÜŞTÜRDÜ.
#SONRA ANY KULLANIYORUZ.
df.isnull().values.any()
####################################################################
#HANGI DEGISKENDE KAC EKSIK DEGER VAR
#####################################################################
df.isnull().sum()
df.sum()
####################################################################
#KATEGORIK DEGISKENI SECMEK
####################################################################
df.["sex"]
df.["sex"].head()
df["sex"].value_counts()
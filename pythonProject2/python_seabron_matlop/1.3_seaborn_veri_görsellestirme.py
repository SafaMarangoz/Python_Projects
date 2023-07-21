import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df=sns.load_dataset("tips")
df.head()

#KATEGORIK DEGISKENLER:SÜTUN

df["sex"].value_counts()
sns.countplot(x=df['sex'],data=df)
plt.show()

#MATPLOTTA NASIL YAPIYORDUK
df["sex"].value_counts().plot(kind="bar")
plt.show()

######################################################
##SAYISAL DEGISKEN GOSTERME:HISTOGRAM VEYA KUTU GRAFİK
#######################################################

##BOXPLOT
sns.boxplot(x=df["total_bill"])
plt.show()

##SEABORN
df["total_bill"].hist()
plt.show()

####3 TEMEL YAKLASIM VAR
##value.counts ve count.plot
##Hıstogram
##Boxplot

#soru çözüm
#3
#df.plot.barh()
#yatay bar grafiği
#5
#Bir değişkende 'outlier' olup olmadığını grafikten bakarak tespit etmek istiyorsak aşağıdakilerden hangisi en uygun grafik çeşididir?
#BOXPLOT
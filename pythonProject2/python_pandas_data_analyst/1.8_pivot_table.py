#######################
# Pivot table
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()
##PIVOT TABLE ON TANIMLI DEGERI ORTALAMADIR
##BURADA CINSIYET SATIRLARDA EMBARKED SÜTUNLARDA YER ALIR.SURVIVED ISE KESISIM DEGERLERIDIR.

df.pivot_table("survived", "sex", "embarked")
##ON TANIMLI DEGERI STANDART SAPMA YAPALIM.
df.pivot_table("survived", "sex", "embarked",aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.head()

#HEM CINSIYET HEM LOKASYON YA DA YASLARA GORE KILIRIM
#YAS DEGISKENINI NASIL EKLEYEBILIRIM(SAYISAL DEGISKENI KATEGORIK YAPMA)
#PD.CUT FONKISOYNU VEQ.CUT FONKSIYONU SAYISAL DEGISKENI KATEROGRIK YAPAR
#QCUT OTOMATIK OLARAK KUCUKTEN BUYUĞE SIRALAR VE YÜZDELİK ÇEYREK DEGERLERE BÖRE KATEGOİELRE BÖLER

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
df.head()

##ALTTAKI FONKSIYONU ACIKLIYORUM
df.pivot_table("survived", "sex", "new_age",)
##KESISIMIZ SURVIVED , SATIR CINSIYET , SÜTUNLAR ISE BELIRLEDIGIMIZ YASLAR VE CLASS
df.pivot_table("survived", "sex", ["new_age", "class"])

##CIKTILARIN GORUNTU AYARI (HEP BERABER GOZUKMESI ICIN)
pd.set_option('display.width', 500)






pd.set_option('display.width', 500)
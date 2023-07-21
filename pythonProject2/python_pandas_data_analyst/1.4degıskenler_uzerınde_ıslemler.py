#######################
# Değişkenler Üzerinde İşlemler
#######################
import pandas as pd
import seaborn as sns
##TUM CIKTILARI GOSTER
pd.set_option('display.max_columns', None)
###################################
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())
#####################################################################################################
##BİR DEĞİŞKEN SEÇERKEN SONUCU SERI VEYA DATAFRAME OLARAK ALABİLİRİZ.KOSELI PARANTEZDE BOZULMAZ
##BURADA TYPE PANDAS SERİSİ BU YÜZDEN;

##SECIM ISLEMI YAPARKEN KOSELI PARANTEZ GIRERSEK DATAFRAME OLARAK KALIR.
df[["age"]].head()
type(df[["age"]].head())
######################################################################################################
##BİRDEN FAZLA DEGISKEN SECMEK ICIN ;
df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

df["age2"] = df["age"]**2
df.head()
df["age3"] = df["age"] / df["age2"]
###############################################
#SILMEK ISTERSEK
##############################################
df.drop("age3", axis=1).head()
###############################################
#KALICI YAPMAK ISTERSEK
###############################################
df.drop("age3",axis=1,inplace=True)
##TÜM SÜTUNLARI SILME
df.drop(col_names, axis=1).head()
##TUM AGE IFADELERINE ERISMEK ISTIYORUM

df.loc[:, df.columns.str.contains("age")].head()

#AGE DISINDAKILERI SECMEK ISTIYORUM
df.loc[:, ~df.columns.str.contains("age")].head()
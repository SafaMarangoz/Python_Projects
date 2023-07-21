#############################################
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

##SINIF SAYILARI
df["survived"].value_counts()
##UNIQ DEGERLERI
df["sex"].unique()
#KAC UNIQ  DEGERI
df["class"].nunique()
#KATEGORIK DEGISKEN YAKALAYACAGIZ
#YANI NUMERİC OLAN KATEGORIK DEGISKENLERIDE BULMAMIZ GEREKIYOR.
#HEM TİP BİLGİSİNE BAKICAZ,HEMDE NUMERİC OLAN AMA KATEGORIK OLAN DEGISKENLERI GORECEGIZ

#col for col in df.columns (SÜTUNLARDA GEZIYORUM)

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

#TİPİ INT VEYA FLOAT OLANLARI BUL.BUNLARIN EŞSİZ SINIF SAYISINA BAK.(CINSIYET,HAYATTA KALANLAR)

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

#ÖLCUM DEGERI TASIMAYACAK KADAR (BİLGİ TAŞIMAYACAK KADAR SINIF SAYISI COK OLAN KATEORIK DEGISKEN)
#OLCULEBILIR DEGGISKEN DEGILDIR.BUNU BUL.(ESSIZ SINIF SAYISI 20DEN FAZLA ISE  )

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

#CAT COLSLARDA GEZ EGER CAT_BUT_CARLARDA YOKSA BUNU CALISTIR.

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols]

df[cat_cols].nunique()

## CATEGORIK OLMAYANLARI BULMA
[col for col in df.columns if col not in cat_cols]


df["survived"].value_counts()
##100DELIK KARSILIGI

100 * df["survived"].value_counts() / len(df)

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex")

##HEPSINE TEK TEK AZ ONCE UYGULADIGIMIZ FONKSIYONU UYGULA
for col in cat_cols:
    cat_summary(df, col)
##############################################################################################################################
##PART2:
##############################################################################################################

for col in cat_cols:
    cat_summary(df, col)

####GRAFIK OLUSTURMA

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)
###############################################################################################################################
##BOOL TIPINDEYSE YAZDIR
## DEGILSE CALISMAYI SURDUR

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("sdfsdfsdfsdfsdfsd")
    else:
        cat_summary(df, col, plot=True)

##BOOL TİPİ DEGISTIRMEK ISTEDIGIMIZI VARSAYALIM.

df["adult_male"]
##TRUE GORDUGU YERE 1 FALSE 0 YAZDIRDIK
df["adult_male"].astype(int)

##KALICI YAPMA

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)

    else:
        cat_summary(df, col, plot=True)

##BOOL TIPTE DONUSUMUNU YAP
## ELIMIZDE CAT SUMMARY FONKSIYONU VAR.BU FONKSIYONUN GOREVI ÖZETLEMEK
##BUNDAN DOLAYI DÖNGÜ YAZRAK FONSKIYON GIRIYORUZ

def cat_summary(dataframe, col_name, plot=False):

    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

cat_summary(df, "adult_male", plot=True)





def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex")

def cat_summary
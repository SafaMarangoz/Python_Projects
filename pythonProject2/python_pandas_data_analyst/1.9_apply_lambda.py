#############################################
# Apply ve Lambda
#############################################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

##APPLY:SATIR VE SÜTUNLARA FOKSIYON CALISTABILIRIZ
##LAMBDA:FONKSIYON TANIMLAMADAN KULLAN AT MANTIĞIYLA ÇALIŞIR.

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

##DONGUYLE YAZALIM
##for col in df.columns:BU DTFRAMELERIN DEGISKENLERINDE GEZ
##if "age" in col:EĞER BUNLARI ICERIYORSA YAZDIR.

for col in df.columns:
    if "age" in col:
        print(col)

 ##ICERSINDE YAS IFADESI VARSA O IFADEYI SEC VE 10A BÖL


for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

## BUNU KAYDETMEK ICIN

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

        df.head()

##lambda KULLANIMI

    df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()
#:==TÜM SATIRLARI SEÇ
#df.columns.str.contains("age"):age sütunları içeren sütunları filtrelere
#x:ler degıskenlerı gösterir
    df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

#daha karısık
    #ıcersınde age barındıranları sec:
    # yas-yasın ortalaması /standart sapma diyoruz
    df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

#SIMDIYE KADAR FONKSIYON TANIMLAMADAN YAPMAK ISTEDIK



#def ile yapma
## apply ile lambda kullanıyorduk .klasik fonksıyonlarıda kullanabiliyoruz.
    def standart_scaler(col_name):
        return (col_name - col_name.mean()) / col_name.std()

##appyle fonksıyonu satır veya sütunlarda elimizdeki fonksıyonu uygulamayı sağlar.
##lambda da kullan at fonksıyonu

    df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

    # df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

    df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

    df.head()

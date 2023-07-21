#############################################################
#MATPLOTLIB:LOW LEVEL,SEABORNE GORE UĞRAŞIRIZ
#############################################################

#ELIMIZDE KATEGORIK DEGISKEN VARSA BUNU :SUTUN GRAFIK,PASTA GRAFİĞİ  ILE GORSELLESTIRIRIZ
#SEABORN ICERSIINDEKI .COUNTPLOT YA DA MATPLOT ICERSIINDEKI ...

##ELIMIZDE SAYISAL DEGISKEN VARSA BUNU:HISTOGRAM,BOXPLOT

#PYTHON VERİ GORSELLESTIRME ICIN ÇOK DA UYGUN DEGILDIR.
#BI IS ZEKASI ARACLARIDIR I
#POWER BI,TABLEU,CLICKWIEW

#VERI TABANLARINDA OLACAKTIR VERİ
#BI ARACLARI RAPORLARİGRAFIKLER,DASHBOARD HAZIRLAMAK ICIN KULLANILIR.

#######################################################
##KATEGORIK DEGISKEN GORSELLESTIRME
#######################################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#max sütun ıcın
pd.set_option("display.max_columns",None)
#SÜTUNLAR ASAGI KAYMAMASI ICIN
pd.set_option("display.width",500)
df=sns.load_dataset("titanic")
df.head()

#cok onemli kateroik degısken kullanırken sayıdırır önemlidf["sex"].value_counts()

df["sex"].value_counts().plot(kind="bar")
plt.show()
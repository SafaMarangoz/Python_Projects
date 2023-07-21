#############################################
# PANDAS
#############################################

# Pandas Series
#TEK BOYUTLUDUR .OTOMATIK INDEX BİLGISINE SAHIPTIR.
#MAT ISTATISTIK INDEX ISLEMLERINI YAPABILECEĞİMİZ ALANDIR
### VERI MANIPULASYONU VE ANALISTI DIYINCE AKLIMIZA SECIM ISLEMLERI  GELIR

import pandas as pd
s=pd.Series([10,77,12,4,5])
type(s)
s.index
s.dtype
##ELEMAN SAYISI
s.size
##BOYUT SAYISI
s.ndim
##ICINDEKI DEGERLERI GORME
s.values
##SADECE DEGERLERI GORMEK ISTEDIGIMIZINXDEX BILGISIYLE ILGILENMIYORUM DEDIGIMIZ ICIN BU YUZDEN TYPEI NUMPY ÇIKTI.
type(s.values)
s.head(3)
s.tail(3)
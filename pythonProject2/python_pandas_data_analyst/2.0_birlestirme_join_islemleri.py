#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

##Concat Sürekli Kulllanılır

pd.concat([df1, df2])

##INDEXLERI SIFIRLAMAK ICIN ;

pd.concat([df1, df2], ignore_index=True)

#######################
# Merge ile Birleştirme İşlemleri
# DETAYLU
#######################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)
##QUİZ PANDAS
#1
df.columns
#2
import pandas as pd
series=pd.Series([1,2,3])
series**2
series.dtype
#3
import pandas as pd
dict={"Paris":[10],"Berlin":[20]}
pd.DataFrame(dict)
#4
import pandas as pd
import numpy as np
df=pd.DataFrame(data=np.random.randint(1,10,size=2,3)),
columns=["var1","var2","var3"]
df[(df.var1<=5)][["var2","var3"]]
#CEVAP MUADİLİ
df.loc[(df.var1 <= 5), ["var2", "var3"]]
#5
df.index()

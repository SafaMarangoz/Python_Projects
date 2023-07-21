number=input()
>? 6
type(number)


def calc(wage,hour):
    print(wage*hour)
    calc(10,40)-200



students = ["Denise", "Arsen", "Tony", "Audrey"]
low = lambda x: x[0].lower()
print(list(map(low, students)))


names={"Demise":"French","Jean":"French",
       "John":"American","Sarah":"American"}
new_names=["FR_"+name if names[name]=="French" else
           "US_"+name for name in names.keys()]
new_names


names=["denise","jean","fleur"]
ages=[20,32,45]
cities=["lyon","lille","nantes"]
list(zip(names,ages,cities))


#Bir fonksiyon, sınıf, metod ya da modülde kodun belirli bir bölümünü açıklamak/belgelemek için kullanılan yorum benzeri yapılar ...olarak adlandırılır.” Cümlesinde boş kalan yere aşağıdakilerden hangisi getirilmelidir.
#DOCSTRING

import numpy as np
from functools import reduce
num_list=np.arange(10)
filter_list=list(filter(lambda x:x %3==0,num_list))
final_list=reduce(lambda x,y:x*y,filter_list)
final_list




#Aşağıdaki işlem ile yapılmak istenen aşağıdakilerden hangisidir?
import numpy as np
serie=np.arange(1,10)
x=[3,4,5]
serie[x]
#Fancy index yardımı ile ilgili indexte yer alan verileri çağırma

#Bir Pandas DataFrame’inde isminde “a” harfi içeren değişkenler aşağıdaki hangi kod yardımı ile seçilebilir?
#D
#df.loc[:, df.columns.str.contains('a')]

import seaborn as sns
df=sns.load_dataset("titanic")
df[["sex","survived"]].groupby("sex")
#groupby işlemine toplulaştırma argümanı verilmediği için çıktı oluşmaz


import seaborn as sns
titanic=sns.load_dataset("titanic")
sns.countplot(x="class",data=titanic)
plt.show()
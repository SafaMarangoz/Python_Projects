#######################
# Koşullu Seçim (Conditional Selection)
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50].count()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

##IKI KOSULU GIRME
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
## 3 KOSUL GIRME
df.loc[(df["age"] > 50) & (df["sex"] == "male"), & ((df["embark_town"] == "Cherbourg")["age", "class","embark_town"]].head()
## SINIFLARINA BAKMA

df["embark_town"].value_counts()
##YA DA
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()
####################################
## STRING METHODS
####################################

dir(str)
#####################
##LEN
#####################

name="Safa"
type(name)
type(len)
len(name)
len("machinelearning")
##FONKSIYONLAR VE METHODLAR GOREVLERI AYRIDIR ANCAK;
##FONKSIYONLAR BAGIMSIZ METHODLAR İSE CLASSLAR ICINDE TANIMLANMIŞ OLMASIDIR.

#####################
# #upper(),lower():
#####################
"safa".upper()
"POWER".lower()
type(upper())

##################
#REPLACE:KARAKTER DEGISIMI
###################

hi="safa marangoz"
hi.replace("s","k")
##########################
#split:böler
##########################
"SAFA MARANGOZ DATA ANALYST".split()

##########################
#strip():böler
##########################
" pekipeki ".strip()
"pekipeki".strip("p")

##########################
#capitalize=ilk harfi büyütür
##########################
"machinelearning".capitalize()

dir(str)
dir("foo")
"foo".startswith("f")

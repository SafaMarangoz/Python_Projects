######################################
##NEDEN NUMPY?
##VERIMLI VERI SAKLAR.HIZ
##DAHA AZ CABA DAHA COK ISLEM (DAHA FONKSIYONEL DAHA VEKTOREL)
######################################

import numpy as np
a=[1,2,3,4]
b=[2,3,4,5]

##DONGUYLE 2 LIST ÇARPMA
ab=[]
for i in range(0,len(a)):
    ab.append(a[i]*b[i])

#NUMPY ILE CARPMA
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
a*b
ab
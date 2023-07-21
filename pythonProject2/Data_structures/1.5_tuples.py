###############################################
# Demet (Tuple)
###############################################

# - Değiştirilemez.###
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("monster", "samsung", 9, 6)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99

###TUPLEDAN  LISTEYE GECİS
t = list(t)
t=tuple(t)
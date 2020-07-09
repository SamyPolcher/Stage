import uproot as ut
import numpy as np
from matplotlib import pyplot as plt

data = ut.open('/users/LHCb/polcherrafael/Data/Select_sig_veto_vars.root')["t"]
file = ut.recreate('/users/LHCb/polcherrafael/Data/Select_sig_veto_Lb_vars.root')

#Filtre sur Lambdastar
Lambdastar_M = data["Lambdastar_M"].array()
mask = (Lambdastar_M > 1470) & (Lambdastar_M < 1570)

#création du fichier root
dico_newtree = {}
dico_extend = {}
k = 0

#recopier les valeurs de data dans le nouveau en appliquant le filtre
for i in data.keys():
    x = data[i].array()
    if len(np.shape(x)) != 1 :
        print('coucou')
        continue
    x = x[mask]
    dico_newtree[i] = np.float64
    dico_extend[i] = x
    print(k)
    k = k+1

file["t"] = ut.newtree(dico_newtree)
file["t"].extend(dico_extend)

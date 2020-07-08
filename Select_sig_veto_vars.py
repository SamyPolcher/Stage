
import uproot as ut
import numpy as np
from matplotlib import pyplot as plt

data = ut.open('/users/LHCb/polcherrafael/Data/Select_sig_veto.root')["t"]
file = ut.recreate('/users/LHCb/polcherrafael/Data/Select_sig_veto_vars.root')

class particule :
    def __init__(self,name,PE,PX,PY,PZ) :
        self.PE = PE
        self.PX = PX
        self.PY = PY
        self.PZ = PZ
        self.name = name
        self.masse = np.sqrt(self.PE ** 2 - self.PX ** 2 - self.PY ** 2 - self.PZ ** 2)

    def sum(self,a,name):
        somme = particule(name , self.PE + a.PE , self.PX + a.PX , self.PY + a.PY , self.PZ + a.PZ )
        return somme


def allocation (name) :
    PE, PX, PY, PZ = data[name+'_PE'].array(), data[name+'_PX'].array(), data[name+'_PY'].array(), data[name+'_PZ'].array()
    return particule(name,PE,PX,PY,PZ)


#Filtre sur Lambdastar
Lambdastar_M = data["Lambdastar_M"].array()
mask =  (1470 < Lambdastar_M) & (Lambdastar_M < 1570) 

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
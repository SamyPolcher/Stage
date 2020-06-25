# Script pour seletioner le bruit
import uproot as ut
import numpy as np

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


#Objet conntenant les valeurs réeles
data = ut.open('/sps/lhcb/marin/RpK-fullr1r2/2017/data/LeptonU_MagDown.root')["tuple_mmLine;1"]['DecayTree;1']
file = ut.recreate('Data_Bruit.root')


L1 = allocation("L1")
L2 = allocation("L2")

#Création de filtres "masks" pour sélectionner un beau bruit
Lambdastar_M = data["Lambdastar_M"].array()
Lb_M = data["Lb_M"].array()


q = L1.sum(L2,"Dimuon")

mask_masse_Lb = Lb_M > 6500
mask_mase_pK = Lambdastar_M < 1600
mask_q2 = (q.masse**2 > 100000) & (q.masse**2 < 8860000) #Gev carre passés en Mev carre
#mask_q2_inf = q.masse**2 < 8860 #Gev care passés en Mev carre

mask = mask_q2 & mask_masse_Lb & mask_mase_pK
dico_newtree = {}
dico_extend = {}
k = 0

for i in data.keys():
    x = data[i].array()
    if len(np.shape(x)) != 1 :
        print('coucou')
        continue
    x = x[mask]
    #print('apres ',np.shape(x))
    dico_newtree[i] = np.float64
    dico_extend[i] = x
    print(k)
    k = k+1


file["t"] = ut.newtree(dico_newtree)
file["t"].extend(dico_extend)
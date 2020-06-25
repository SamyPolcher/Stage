# Script pour seletioner les evenements donnant des masses de pkmumu proches de celle de Lb

import uproot as ut
import numpy as np
from matplotlib import pyplot as plt

data = ut.open('/sps/lhcb/marin/RpK-fullr1r2/2017/data/LeptonU_MagDown.root')["tuple_mmLine;1"]['DecayTree;1']
#file = ut.recreate('/users/LHCb/polcherrafael/Data/Select_Lb.root')

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

    def hist(self):
        name = self.name
        plt.figure(figsize=(15, 10))
        #plt.suptitle('Vecteur quantite de mouvement ' + name, size=30)
        plt.subplot(221)
        plt.hist(self.PE, 1000)
        plt.title(name + '_PE')

        plt.subplot(222)
        plt.hist(self.PX, 1000, color='r')
        plt.title(name + '_PX')

        plt.subplot(223)
        plt.hist(self.PY, 1000, color='y')
        plt.title(name + '_PY')

        plt.subplot(224)
        plt.hist(self.PZ, 1000, color='g')
        plt.title(name + '_PZ')

        plt.tight_layout()
        #pdf = PdfPages('Quadrivecteur_' + name + '.pdf')
        #pdf.savefig()
        plt.savefig('Quadrivecteur_'+ name +'.png' )
        #plt.show()
        plt.close()
        #pdf.close()


def allocation (name) :
    PE, PX, PY, PZ = data[name+'_PE'].array(), data[name+'_PX'].array(), data[name+'_PY'].array(), data[name+'_PZ'].array()
    return particule(name,PE,PX,PY,PZ)


#Particules en jeu et liste de valeurs

L1 = allocation('L1')
L2 = allocation('L2')
q = L1.sum(L2,'Dimuon')
Lambdastar_M = data["Lambdastar_M"].array()
Lb_M = data["Lb_M"].array()


#Filtres

mask_proche_masse_Lb = (Lb_M < 6124) & (Lb_M > 5124)
mask_masse_pK = Lambdastar_M < 1600
mask = mask_proche_masse_Lb & mask_masse_pK

Lb_M_filtre = Lb_M[mask]
Lambdastar_filtre = Lambdastar_M[mask]
q2_filtre = (q.masse**2)[mask]


#Graphes

plt.figure(figsize=(15,10))

plt.subplot(221)
plt.title('Masse de pKmumu filtrée')
plt.hist(Lb_M_filtre,1000, color='gold')
plt.legend(['mu = '+str(round(np.mean(Lb_M_filtre),3))+'\nsigma = '+str(round(np.std(Lb_M_filtre)))],fontsize='15')
plt.xlabel('Masse en MeV/C²',fontsize='15')

plt.subplot(222)
plt.title('Masse de Lambda* filtrée')
plt.hist(Lb_M_filtre,1000, color='b')
plt.legend(['mu = '+str(round(np.mean(Lambdastar_filtre),3))+'\nsigma = '+str(round(np.std(Lambdastar_filtre)))],fontsize='15')
plt.xlabel('Masse en MeV/C²',fontsize='15')

plt.subplot(223)
plt.title('q² filtré')
plt.hist(q2_filtre,1000,color='r')
plt.legend(['mu = '+str(round(np.mean(q2_filtre),3))+'\nsigma = '+str(round(np.std(q2_filtre)))],fontsize='15')
plt.xlabel('Masse en MeV²/C⁴',fontsize='15')

plt.savefig('blabla.png' )
plt.close()
    

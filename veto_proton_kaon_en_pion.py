import uproot as ut
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
from matplotlib.backends.backend_pdf import PdfPages


data = ut.open('/sps/lhcb/marin/RpK-fullr1r2/2017/data/LeptonU_MagDown.root')["tuple_mmLine;1"]['DecayTree;1']

#print(data.keys())
print(len(data.keys()))
#index = data['__index__'].array()
#print(index)

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

    def ajust(self, condition1 = None, condition2 = None):
        indice = list(np.where(self.PE > lim_PE)[0]) + list(np.where(condition1)[0]) + list(np.where(condition2)[0])
        for i in indice:
            #print('i',i)
            self.PE[i] = np.nan
            self.PX[i] = np.nan
            self.PY[i] = np.nan
            self.PZ[i] = np.nan
            self.masse[i] = np.nan

    def rmv_nan(self,a) :
        #np.delete(self.PE, indice)
        self.PE = self.PE[~np.isnan(self.PE)]
        self.PX = self.PX[~np.isnan(self.PX)]
        self.PY = self.PY[~np.isnan(self.PY)]
        self.PZ = self.PZ[~np.isnan(self.PZ)]
        self.masse = self.masse[~np.isnan(self.masse)]

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


L1 = allocation('L1')
L2 = allocation('L2')
K = allocation('Kaon')
P = allocation('Proton')
K_Pion = allocation('Kaon')
P_Pion = allocation('Proton')

##Kaon en Pion
#K_Pion.PE = np.multiply(np.divide(P.masse, K.masse),K.PE)
m_pion = 134.9766 #en MeV/c^2
K_Pion.PE = np.sqrt(numpy.square(K.PX) + numpy.square(K.PY) + numpy.square(K.PZ) + m_pion)

Lambdastar1 = K_Pion.sum(P,'Lstar')
Lb1 = ( L1.sum(L2,'Dimuon') ).sum(Lambdastar1,'Lb')

# Graphes
plt.figure(figsize=(15,10))
plt.suptitle('VETO : Kaon --> Pion', size=30)

plt.subplot(121)
plt.title('Masse de Lambda* m(ppion)')
plt.hist(Lambdastar1.masse,1000)
plt.legend(['mu = '+str(round(np.mean(Lambdastar1.masse),3))+'\nsigma = '+str(round(np.std(Lambdastar1.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C2')

plt.subplot(122)
plt.title('Masse de Lambdab m(llppion)')
plt.hist(Lb1.masse,1000,color='r')
plt.legend(['mu = '+str(round(np.mean(Lb1.masse),3))+'\nsigma = '+str(round(np.std(Lb1.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C2')

plt.savefig('Veto_Kaon_en_Pion.png')
plt.close()

##Proton en Pion
m_pion = 134.9766 #en MeV/c^2
P_Pion.PE = np.sqrt(numpy.square(P.PX) + numpy.square(P.PY) + numpy.square(P.PZ) + m_pion)

Lambdastar2 = K.sum(P_Pion,'Lstar')
Lb2 = ( L1.sum(L2,'Dimuon') ).sum(Lambdastar2,'Lb')

# Graphes
plt.figure(figsize=(15,10))
plt.suptitle('VETO : Kaon --> Pion', size=30)

plt.subplot(121)
plt.title('Masse de Lambda* m(ppion)')
plt.hist(Lambdastar2.masse,1000)
plt.legend(['mu = '+str(round(np.mean(Lambdastar2.masse),3))+'\nsigma = '+str(round(np.std(Lambdastar2.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C2')

plt.subplot(122)
plt.title('Masse de Lambdab m(llppion)')
plt.hist(Lb2.masse,1000,color='r')
plt.legend(['mu = '+str(round(np.mean(Lb2.masse),3))+'\nsigma = '+str(round(np.std(Lb2.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C2')

plt.savefig('Veto_Proton_en_Pion.png')
plt.close()

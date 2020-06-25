import uproot as ut
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
from matplotlib.backends.backend_pdf import PdfPages


#data = ut.open('/sps/lhcb/marin/RpK-fullr1r2/2017/data/LeptonU_MagDown.root')["tuple_mmLine;1"]['DecayTree;1']
data = ut.open('/users/LHCb/polcherrafael/Data/Data_Bruit.root')["t"]

#print(data.keys())
#print(len(data.keys()))
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


# Produits finaux
L1 = allocation('L1')
L2 = allocation('L2')
K = allocation('Kaon')
P = allocation('Proton')

#  P des produits intermediaires
Lstar = K.sum(P,'Lstar')
q = L1.sum(L2,'Dimuon')


# Lambdab
Lb = q.sum(Lstar,'Lb')


#pour les comparaisons avec les masses calculées 
Lambdastar_M = data['Lambdastar_M'].array()
Lb_M = data['Lb_M'].array()

'''
#comparaison L* calculée et L*_M
plt.figure(figsize=(15,10))
#plt.suptitle('Masses calculees', size=30)
plt.subplot(121)
plt.title('Masse de Lambda* Lambdastar_M')
plt.hist(Lambdastar_M,1000)
plt.legend(['mu = '+str(round(np.mean(Lambdastar_M),3))+'\nsigma = '+str(round(np.std(Lambdastar_M)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(122)
plt.title('Masse de Lambda* calculée')
plt.hist(Lstar.masse,1000,color='r')
plt.legend(['mu = '+str(round(np.mean(Lstar.masse),3))+'\nsigma = '+str(round(np.std(Lstar.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

#pdf = PdfPages('Masses_calcule.pdf')
#pdf.savefig()
plt.savefig('Lambdastar_diff.png')
#plt.show()
plt.close()
#pdf.close()

# Histogrammes des masses calculees
plt.figure(figsize=(15,10))
#plt.suptitle('Masses calculees', size=30)
plt.subplot(121)
plt.title('Masse de Lambda*')
plt.hist(Lstar.masse,1000)
plt.legend(['mu = '+str(round(np.mean(Lstar.masse),3))+'\nsigma = '+str(round(np.std(Lstar.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(122)
plt.title('q carré')
plt.hist(q.masse**2,1000,color='r')
plt.legend(['mu = '+str(round(np.mean(q.masse**2),3))+'\nsigma = '+str(round(np.std(q.masse**2)))],fontsize='12')
plt.xlabel('Masse en MeV²/C⁴',fontsize='12')

#pdf = PdfPages('Masses_calcule.pdf')
#pdf.savefig()
plt.savefig('Masses_intermediares.png')
#plt.show()
plt.close()
#pdf.close()


# Histogrammes des masses produit finaux
plt.figure(figsize=(15,10))
#plt.suptitle('Masses des produits finaux', size=30)

plt.subplot(221)
plt.title('Masse de L1')
plt.hist(L1.masse , 1000,log=True)
plt.legend(['mu = '+str(round(np.mean(L1.masse),3))+'\nsigma = '+str(round(np.std(L1.masse)*10**9,3))+'e-09'],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(222)
plt.title('Masse de L2')
plt.hist(L2.masse,1000,color='r',log=True)
plt.legend(['mu = '+str(round(np.mean(L2.masse),3))+'\nsigma = '+str(round(np.std(L2.masse)*10**9,3))+'e-09'],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(223)
plt.title('Masse du Proton')
plt.hist(K.masse,1000,color='y',log=True)
plt.legend(['mu = '+str(round(np.mean(P.masse),3))+'\nsigma = '+str(round(np.std(P.masse)*10**10,3))+'e-10'],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(224)
plt.title('Masse du Kaon')
plt.hist(K.masse,1000,color='g',log=True)
plt.legend(['mu = '+str(round(np.mean(K.masse),3))+'\nsigma = '+str(round(np.std(K.masse)*10**10,3))+'e-10'],fontsize='12')
plt.xlabel('Masse en MeV/C2',fontsize='12')

plt.tight_layout()
#pdf = PdfPages('Masses_produits.pdf')
#pdf.savefig()
plt.savefig('Masses_produits.png')
#plt.show()
plt.close()
#pdf.close()

#comparaison Lb calculée et Lb_M
plt.figure(figsize=(15,10))

plt.subplot(121)
plt.title('Masse de Lambdab Lb_M')
plt.hist(Lb_M,1000)
plt.legend(['mu = '+str(round(np.mean(Lb_M),3))+'\nsigma = '+str(round(np.std(Lb_M)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(122)
plt.title('Masse de Lambdab calculée')
plt.hist(Lb.masse,1000,color='r')
plt.legend(['mu = '+str(round(np.mean(Lb.masse),3))+'\nsigma = '+str(round(np.std(Lb.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

#pdf = PdfPages('Masses_calcule.pdf')
#pdf.savefig()
plt.savefig('Lb_diff.png')
#plt.show()
plt.close()
#pdf.close()'''

# Histogrammes bruit sur les valeurs coupées
plt.figure(figsize=(15,10))
#plt.suptitle('Masses calculees', size=30)
plt.subplot(221)
plt.title('Masse de Lambda* (bruit)')
plt.hist(Lstar.masse,1000, color='b')
plt.legend(['mu = '+str(round(np.mean(Lstar.masse),3))+'\nsigma = '+str(round(np.std(Lstar.masse)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(222)
plt.title('Masse de Lambdab (bruit)')
plt.hist(Lb_M,1000, color='gold')
plt.legend(['mu = '+str(round(np.mean(Lb_M),3))+'\nsigma = '+str(round(np.std(Lb_M)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(223)
plt.title('q carré (bruit)')
plt.hist(q.masse**2,1000,color='r')
plt.legend(['mu = '+str(round(np.mean(q.masse**2),3))+'\nsigma = '+str(round(np.std(q.masse**2)))],fontsize='12')
plt.xlabel('Masse en MeV²/C⁴',fontsize='12')

#pdf = PdfPages('Masses_calcule.pdf')
#pdf.savefig()
plt.savefig('Masses_bruit.png')
#plt.show()
plt.close()
#pdf.close()
import uproot as ut
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
from matplotlib.backends.backend_pdf import PdfPages


sig = ut.open('/users/LHCb/polcherrafael/MC/MC_BKGCAT10.root')["t"]
bkg = ut.open('/users/LHCb/polcherrafael/Data/Data_Bruit.root')["t"]

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
        plt.savefig('Quadrivecteur_'+ name +'.png' )
        plt.close()



def allocation (name) :
    PE, PX, PY, PZ = data[name+'_PE'].array(), data[name+'_PX'].array(), data[name+'_PY'].array(), data[name+'_PZ'].array()
    return particule(name,PE,PX,PY,PZ)




# Impulsion transverse

Proton_PT_bkg = bkg['Proton_PT'].array()
Proton_PT_sig = sig['Proton_PT'].array()
Kaon_PT_bkg = bkg['Kaon_PT'].array()
Kaon_PT_sig = sig['Kaon_PT'].array()

 
plt.figure(figsize=(15,10))

plt.subplot(221)
plt.title('Impulsion transverse proton (bkg)')
plt.hist(Proton_PT_bkg ,1000 , color='b')
plt.legend(['mu = '+str(round(np.mean(Proton_PT_bkg),3))+'\nsigma = '+str(round(np.std(Proton_PT_bkg)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(222)
plt.title('Impulsion transverse proton (sig)')
plt.hist(Proton_PT_sig ,1000 , color='gold')
plt.legend(['mu = '+str(round(np.mean(Proton_PT_sig),3))+'\nsigma = '+str(round(np.std(Proton_PT_sig)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(223)
plt.title('Impulsion transverse kaon (bkg)')
plt.hist(Kaon_PT_bkg ,1000 , color='b')
plt.legend(['mu = '+str(round(np.mean(Kaon_PT_bkg),3))+'\nsigma = '+str(round(np.std(Kaon_PT_bkg)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.subplot(224)
plt.title('Impulsion transverse kaon (sig)')
plt.hist(Kaon_PT_sig ,1000 , color='gold')
plt.legend(['mu = '+str(round(np.mean(Kaon_PT_sig),3))+'\nsigma = '+str(round(np.std(Kaon_PT_sig)))],fontsize='12')
plt.xlabel('Masse en MeV/C²',fontsize='12')

plt.savefig('Impulsions_trans_comparaison.png')
plt.close()

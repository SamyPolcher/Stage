import uproot as ut
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
from matplotlib.backends.backend_pdf import PdfPages


sig = ut.open('/users/LHCb/polcherrafael/MC/MC_BKGCAT10.root')["t"]
bkg = ut.open('/users/LHCb/polcherrafael/Data/Data_Bruit.root')["t"]


## Impulsion transverse proton
Proton_PT_bkg = bkg['Proton_PT'].array()
Proton_PT_sig = sig['Proton_PT'].array()
Kaon_PT_bkg = bkg['Kaon_PT'].array()
Kaon_PT_sig = sig['Kaon_PT'].array()


plt.figure(figsize=(15,10))

plt.subplot(221)
plt.title('Impulsion transverse proton (bkg)')
plt.hist(Proton_PT_bkg ,1000 , color='b')
plt.legend(['mu = '+str(round(np.mean(Proton_PT_bkg),3))+'\nsigma = '+str(round(np.std(Proton_PT_bkg)))],fontsize='12')

plt.subplot(222)
plt.title('Impulsion transverse proton (sig)')
plt.hist(Proton_PT_sig ,1000 , color='gold')
plt.legend(['mu = '+str(round(np.mean(Proton_PT_sig),3))+'\nsigma = '+str(round(np.std(Proton_PT_sig)))],fontsize='12')

plt.subplot(223)
plt.title('Impulsion transverse kaon (bkg)')
plt.hist(Kaon_PT_bkg ,1000 , color='b')
plt.legend(['mu = '+str(round(np.mean(Kaon_PT_bkg),3))+'\nsigma = '+str(round(np.std(Kaon_PT_bkg)))],fontsize='12')

plt.subplot(224)
plt.title('Impulsion transverse kaon (sig)')
plt.hist(Kaon_PT_sig ,1000 , color='gold')
plt.legend(['mu = '+str(round(np.mean(Kaon_PT_sig),3))+'\nsigma = '+str(round(np.std(Kaon_PT_sig)))],fontsize='12')

plt.savefig('Proton_Kaon_PT.png')
plt.close()

## Impulsion transverse kaon
L1_PT_bkg = bkg['L1_PT'].array()
L1_PT_sig = sig['L1_PT'].array()
L2_PT_bkg = bkg['L2_PT'].array()
L2_PT_sig = sig['L2_PT'].array()

plt.figure(figsize=(15,10))

plt.subplot(221)
plt.title('Impulsion transverse L1 (bkg)')
plt.hist(L1_PT_bkg ,1000 , color='b')
plt.legend(['mu = '+str(round(np.mean(L1_PT_bkg),3))+'\nsigma = '+str(round(np.std(L1_PT_bkg)))],fontsize='12')

plt.subplot(222)
plt.title('Impulsion transverse L1 (sig)')
plt.hist(L1_PT_sig ,1000 , color='gold')
plt.legend(['mu = '+str(round(np.mean(L1_PT_sig),3))+'\nsigma = '+str(round(np.std(L1_PT_sig)))],fontsize='12')

plt.subplot(223)
plt.title('Impulsion transverse kaon (bkg)')
plt.hist(L2_PT_bkg ,1000 , color='b')
plt.legend(['mu = '+str(round(np.mean(L2_PT_bkg),3))+'\nsigma = '+str(round(np.std(L2_PT_bkg)))],fontsize='12')

plt.subplot(224)
plt.title('Impulsion transverse kaon (sig)')
plt.hist(L2_PT_sig ,1000 , color='gold')
plt.legend(['mu = '+str(round(np.mean(L2_PT_sig),3))+'\nsigma = '+str(round(np.std(L2_PT_sig)))],fontsize='12')



plt.savefig('Leptons_PT.png')
plt.close()






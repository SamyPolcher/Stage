import uproot as ut
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
from matplotlib.backends.backend_pdf import PdfPages
import math

Bruit = ut.open('/users/LHCb/polcherrafael/Data/Data_Bruit.root')["t"]
Signal = ut.open('/users/LHCb/polcherrafael/MC/MC_BKGCAT10.root')["t"]
#data = ut.open('/users/LHCb/polcherrafael/Data/Select_sig.root')["t"]

minHadron_IPCHI2 = np.minimum(Proton_IPCHI2_OWNPV,Kaon_IPCHI2_OWNPV)
minHadron_PT = np.minimum(Proton_PT,Kaon_PT)
sumHadron_PT = np.sum(Proton_PT,Kaon_PT)
sumHadron_IPCHI2 = np.sum(Proton_IPCHI2_OWNPV,Kaon_IPCHI2_OWNPV)
minLepton_PT = np.min(L1_PT,L2_PT)
maxLepton_IPCHI2 = np.max(L1_IPCHI2_OWNPV, L2_IPCHI2_OWNPV)
minLepton_IPCHI2 = np.min(L1_IPCHI2_OWNPV, L2_IPCHI2_OWNPV)
sumLJ_PT = np.sum(Lambdastar_PT,Jpsi_PT)
Hsum_ETA = np.sum(Proton_ETA,Kaon_ETA)


list_vars = ["Log_Lb_PT", "Log_Lb_IPCHI2_OWNPV", 'Log_Lb_DIRA_OWNPV', "Lb_DIRA_OWNPV", 
"Log_Lb_FDCHI2_OWNPV", "Log_Lb_LOKI_DTF_CHI2NDOF", "Log_Lb_ENDVERTEX_CHI2", 
"Log_Jpsi_FDCHI2_OWNPV", "Log_Lambdastar_PT", "Log_Lambdastar_IPCHI2_OWNPV", "Log_Lambdastar_ENDVERTEX_CHI2", 
"minHadron_PT", "minHadron_IPCHI2", "sumHadron_PT","sumHadron_IPCHI2", "minLepton_PT", "maxLepton_IPCHI2", "minLepton_IPCHI2","sumLJ_PT", 
"Log_Proton_P","Hsum_ETA"]

def plot_vars(list_vars) :
    page = math.ceil(len(list_vars)/6)
    pdf = PdfPages('Variables_entrainement.pdf')

    for n in range(page) :
        plt.figure(figsize = (8.3, 11.7))
        k = 1
        for i in list_vars[n*6 : (n+1)*6] :
            plt.subplot(3,2,k)
            plt.title(i, fontsize = 15)
            plt.hist(Bruit[i[4:]].array(), 10, linewidth=1.2, edgecolor = 'b', color='b', alpha=0.5, density = True, log = True)
            plt.hist(Signal[i[4:]].array(),10, linewidth=1.2, edgecolor = 'r', color='r', alpha=0.5, density = True, log = True)
            k += 1
        plt.tight_layout()
        pdf.savefig()
        plt.close()
    pdf.close()

plot_vars(list_vars)

import uproot as ut
import numpy as np
from matplotlib import pyplot as plt
import scipy.integrate as integrate
from matplotlib.backends.backend_pdf import PdfPages


data = ut.open('/sps/lhcb/marin/RpK-fullr1r2/2017/MC/15114000/LeptonU_MagDown.root')["tuple_mmLine;1"]['DecayTree;1']
file = ut.recreate('/users/LHCb/polcherrafael/MC/MC_BKGCAT10.root')


Lb_BKGCAT = data["Lb_BKGCAT"].array()

mask_BKGCAT = Lb_BKGCAT == 10

dico_newtree = {}
dico_extend = {}

for i in data.keys():
    x = data[i].arrays()
    if len(np.shape(x)) != 1 :
        print('coucou')
        continue
    x = x[mask_BKGCAT]
    #print('apres ',np.shape(x))
    dico_newtree[i] = np.float64
    dico_extend[i] = x


file["t"] = ut.newtree(dico_newtree)
file["t"].extend(dico_extend)






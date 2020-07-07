import uproot as ut
import numpy as np

#Objet contenant les valeurs réeles
data = ut.open('/users/LHCb/polcherrafael/MC/MC_BKGCAT10.root')['t']
file = ut.recreate('/users/LHCb/polcherrafael/MC/MC_BKGCAT10_vars.root')

#data = ut.open(/users/LHCb/polcherrafael/Data/Data_Bruit.root)['t']
#file = ut.recreate('/users/LHCb/polcherrafael/Data/Data_Signal_vars.root')

dico_newtree = {}
dico_extend = {}
k = 0

for i in data.keys():
    x = data[i].array()
    if len(np.shape(x)) != 1 :
        print('coucou')
        continue
    #print('apres ',np.shape(x))
    dico_newtree[i] = np.float64
    dico_extend[i] = x
    print(k)
    k = k+1

Jpsi_P = data['Jpsi_P'].array()
Proton_P = data['Proton_P'].array()
Kaon_P = data['Kaon_P'].array()

L1_PT = data['L1_PT'].array()
L2_PT = data['L2_PT'].array()
Proton_PT = data['Proton_PT'].array()
Kaon_PT = data['Kaon_PT'].array()
Lambdastar_PT = data['Lambdastar_PT'].array()
Jpsi_PT = data['Jpsi_PT'].array()

Proton_IPCHI2_OWNPV= data['Proton_IPCHI2_OWNPV'].array()
Kaon_IPCHI2_OWNPV= data['Kaon_IPCHI2_OWNPV'].array()
L1_IPCHI2_OWNPV = data['L1_IPCHI2_OWNPV'].array()
L2_IPCHI2_OWNPV= data['L2_IPCHI2_OWNPV'].array()

Proton_ETA= data['Proton_ETA'].array()
Kaon_ETA= data['Kaon_ETA'].array()



dico_newtree["beta"] = np.float64
dico_extend["beta"] = np.divide( Jpsi_P - Proton_P - Kaon_P ,  Jpsi_P + Proton_P + Kaon_P )

dico_newtree["minHadron_IPCHI2"] = np.float64
dico_extend["minHadron_IPCHI2"] = np.minimum(Proton_IPCHI2_OWNPV,Kaon_IPCHI2_OWNPV)

dico_newtree["minHadron_PT"] = np.float64
dico_extend["minHadron_PT"] = np.minimum(Proton_PT,Kaon_PT)

dico_newtree["sumHadron_PT"] = np.float64
dico_extend["sumHadron_PT"] = Proton_PT + Kaon_PT

dico_newtree["sumHadron_IPCHI2"] = np.float64
dico_extend["sumHadron_IPCHI2"] = Proton_IPCHI2_OWNPV + Kaon_IPCHI2_OWNPV

dico_newtree["minLepton_PT"] = np.float64
dico_extend["minLepton_PT"] =np.minimum(L1_PT,L2_PT)

dico_newtree["maxLepton_IPCHI2"] = np.float64
dico_extend["maxLepton_IPCHI2"] = np.maximum(L1_IPCHI2_OWNPV,L2_IPCHI2_OWNPV)

dico_newtree["minLepton_IPCHI2"] = np.float64
dico_extend["minLepton_IPCHI2"] = np.minimum(L1_IPCHI2_OWNPV,L2_IPCHI2_OWNPV)

dico_newtree["sumLJ_PT"] = np.float64
dico_extend["sumLJ_PT"] = Lambdastar_PT + Jpsi_PT

dico_newtree["Hsum_ETA"] = np.float64
dico_extend["Hsum_ETA"] = Proton_ETA + Kaon_ETA

file["t"] = ut.newtree(dico_newtree)
file["t"].extend(dico_extend)

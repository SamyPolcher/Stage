import uproot as ut
import numpy as np
import matplotlib.pyplot as plt
import xgboost

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from matplotlib import pyplot as plt

sig = ut.open('/users/LHCb/polcherrafael/MC/MC_BKGCAT10_rare_vars.root'')["t"]
bkg = ut.open('/users/LHCb/polcherrafael/Data/Data_Bruit_vars.root')["t"]
data = ut.open('/users/LHCb/polcherrafael/Data/Select_rare_Filtre.root')["t"]

file = ut.recreate('/users/LHCb/polcherrafael/Data/Select_rare_Filtre.root')

vars = ["beta", "Lb_PT", "Lb_IPCHI2_OWNPV", 'Lb_DIRA_OWNPV', "Lb_DIRA_OWNPV", 
"Lb_FDCHI2_OWNPV", "Lb_LOKI_DTF_CHI2NDOF", "Lb_ENDVERTEX_CHI2", 
"Jpsi_FDCHI2_OWNPV", "Lambdastar_PT", "Lambdastar_IPCHI2_OWNPV", "Lambdastar_ENDVERTEX_CHI2", 
"minHadron_PT", "minHadron_IPCHI2", "sumHadron_PT","sumHadron_IPCHI2", "minLepton_PT", "maxLepton_IPCHI2", "minLepton_IPCHI2","sumLJ_PT", 
"Proton_P","Hsum_ETA"]

# create a pandas data frame with these variables only
sig_array = sig.pandas.df(vars).to_numpy()
bkg_array = bkg.pandas.df(vars).to_numpy()
data_array = data.pandas.df(vars).to_numpy()

print("Signal shape:", sig_array.shape)
print("Backgr shape:", bkg_array.shape)
print("Data shape:", data_array.shape)

# merge and define signal and background labels
X = np.concatenate((sig_array, bkg_array))
y = np.concatenate((np.ones(sig_array.shape[0]),# 1 is signal
                    np.zeros(bkg_array.shape[0]))) # 0 is background

# split data in train and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
print("Train size:", X_train.shape[0])
print("Test size: ", X_test.shape[0])

# define a model, example: xgboost
params_dict = {
    "n_estimators": 200,
    "learning_rate": 0.3,
    "max_depth": 3,
    }
model = xgboost.XGBClassifier(**params_dict)

# train it
model.fit(X_train, y_train)
print("Model has been trained")
    
# make predictions
y_prob_train = model.predict_proba(X_train)    
y_prob_test  = model.predict_proba(X_test)
y_prob_data = model.predict_proba(data_array)

#création du mask
y_prob_data_transpose = np.transpose(y_prob_data)
mask = y_prob_data_transpose[0] > 0.8

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
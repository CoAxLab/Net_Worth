
# coding: utf-8

# In[ ]:

def run_exp3mod1(id):
    """ Pure drift-rate to task params model
    """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model1 = hddm.HDDM(data,depends_on={'v':['rwd_prob','stableVar']},p_outlier=0.05)
    exp3model1.find_starting_values()
    exp3model1.sample(1500, burn=250, dbname='exp3mod1%i.db'%id,db='pickle')
    return exp3model1


# In[ ]:

def run_exp3mod2(id):
    """ Bias: task params model
    """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model2 = hddm.HDDM(data,depends_on={'z':['rwd_prob','stableVar']}, include='z'
                           , p_outlier=0.05)
    exp3model2.find_starting_values()
    exp3model2.sample(1500, burn=250, dbname='exp3mod2%i.db'%id,db='pickle')
    return exp3model2


# In[ ]:

def run_exp3mod3(id):
    """ Drift-rate: rwd prob, bias: stable target variance model
    """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model3 = hddm.HDDM(data,depends_on={'v':'rwd_prob','z':'stableVar'}, include='z'
                           , p_outlier=0.05)
    exp3model3.find_starting_values()
    exp3model3.sample(1500, burn=250, dbname='exp3mod3%i.db'%id,db='pickle')
    return exp3model3


# In[ ]:

def run_exp3mod4(id):
    """ Drift-rate stable target variance, bias: rwd prob model
    """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model4 = hddm.HDDM(data,depends_on={'v':'stableVar','z':'rwd_prob'}, include='z'
                           , p_outlier=0.05)
    exp3model4.find_starting_values()
    exp3model4.sample(1500, burn=250, dbname='exp3mod4%i.db'%id,db='pickle')
    return exp3model4

# In[ ]:

def run_exp3mod5(id):
    """ drift-rate: stable target variance model """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model5 = hddm.HDDM(data, depends_on={'v':'stableVar'}, p_outlier=0.05)
    exp3model5.find_starting_values()
    exp3model5.sample(1500, burn=250, dbname='exp3mod5_%i.db'%id, db='pickle')
    return exp3model5

# In[ ]:

def run_exp3mod6(id):
    """ drift-rate: rwd prob model """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model6 = hddm.HDDM(data, depends_on={'v':'rwd_prob'}, p_outlier=0.05)
    exp3model6.find_starting_values()
    exp3model6.sample(1500, burn=250, dbname='exp3mod6_%i.db'%id, db='pickle')
    return exp3model6


# In[ ]:

def run_exp3mod7(id):
    """ bias: stable target variance model """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model7 = hddm.HDDM(data, depends_on={'z':'stableVar'}, include='z'
                           , p_outlier=0.05)
    exp3model7.find_starting_values()
    exp3model7.sample(1500, burn=250, dbname='exp3mod7_%i.db'%id, db='pickle')
    return exp3model7


# In[ ]:

def run_exp3mod8(id):
    """ bias: rwd prob model """
    import hddm
    data = hddm.load_csv(
        'C:/Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp3model8 = hddm.HDDM(data, depends_on={'z':'rwd_prob'}, include='z'
                           , p_outlier=0.05)
    exp3model8.find_starting_values()
    exp3model8.sample(1500, burn=250, dbname='exp3mod8_%i.db'%id, db='pickle')
    return exp3model8

# In[ ]:

def run_exp3mod9(id):
    """ drift-rate: task params with free bias model """
    #imports
    import hddm
    data = hddm.load_csv(
        'C://Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    #build model
    exp3model9 = hddm.HDDM(data,depends_on={'v':['stableVar','rwd_prob']}, include='z'
                           , p_outlier=0.05)
    exp3model9.find_starting_values()
    exp3model9.sample(1500, burn=250, dbname='exp3mod9_%i.db'%id,db='pickle')
    return exp3model9

# In[ ]:

def run_exp3mod10(id):
    """ drift-rate: stable target variance with free bias model """
    #imports
    import hddm
    data = hddm.load_csv(
        'C://Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    #build model
    exp3model10 = hddm.HDDM(data,depends_on={'v':'stableVar'}, include='z'
                           , p_outlier=0.05)
    exp3model10.find_starting_values()
    exp3model10.sample(1500, burn=250, dbname='exp3mod10_%i.db'%id,db='pickle')
    return exp3model10

# In[ ]:

def run_exp3mod11(id):
    """ drift-rate: rwd_prob with free bias model """
    #imports
    import hddm
    data = hddm.load_csv(
        'C://Users/Rory/Dropbox/Net_Worth/Pub_Code/Data/Experiment3/Model/Exp3ModelData.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    #build model
    exp3model11 = hddm.HDDM(data,depends_on={'v':'rwd_prob'}, include='z'
                           , p_outlier=0.05)
    exp3model11.find_starting_values()
    exp3model11.sample(1500, burn=250, dbname='exp3mod11_%i.db'%id,db='pickle')
    return exp3model11
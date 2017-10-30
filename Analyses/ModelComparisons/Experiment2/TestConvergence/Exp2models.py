
# coding: utf-8

# In[ ]:

def run_exp2mod1(id):
    """
    Pure drift-rate: task params model
    """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model1 = hddm.HDDM(data,depends_on={'v':['rwd_pen','rwd_prob']}, p_outlier=0.05)
    exp2model1.find_starting_values()
    exp2model1.sample(3000, burn=1500, dbname='exp2mod1%i.db'%id,db='pickle')
    return exp2model1


# In[ ]:

def run_exp2mod2(id):
    """
    Bias: task params model
    """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model2 = hddm.HDDM(data,depends_on={'z':['rwd_pen','rwd_prob']}, include='z'
                           , p_outlier=0.05)
    exp2model2.find_starting_values()
    exp2model2.sample(1500, burn=500, dbname='exp2mod2%i.db'%id,db='pickle')
    return exp2model2


# In[ ]:

def run_exp2mod3(id):
    """
    Drift-rate: rwd/pen tradeoff, bias: rwd prob model
    """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model3 = hddm.HDDM(data,depends_on={'v':'rwd_pen','z':'rwd_prob'}, include='z'
                           , p_outlier=0.05)
    exp2model3.find_starting_values()
    exp2model3.sample(1500, burn=500, dbname='exp2mod3%i.db'%id,db='pickle')
    return exp2model3


# In[ ]:

def run_exp2mod4(id):
    """
    Drift-rate: rwd prob, bias: rwd/pen tradeoff model
    """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model4 = hddm.HDDM(data,depends_on={'v':'rwd_prob','z':'rwd_pen'}, include='z'
                           , p_outlier=0.05)
    exp2model4.find_starting_values()
    exp2model4.sample(1500, burn=500, dbname='exp2mod4%i.db'%id,db='pickle')
    return exp2model4

# In[ ]:

def run_exp2mod5(id):
    """ drift-rate: rwd/pen tradeoff  model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model5 = hddm.HDDM(data, depends_on={'v':'rwd_pen'}, p_outlier=0.05)
    exp2model5.find_starting_values()
    exp2model5.sample(1500, burn=500, dbname='exp2mod5_%i.db'%id, db='pickle')
    return exp2model5

# In[ ]:

def run_exp2mod6(id):
    """ drift-rate: rwd prob model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model6 = hddm.HDDM(data, depends_on={'v':'rwd_prob'}, p_outlier=0.05)
    exp2model6.find_starting_values()
    exp2model6.sample(1500, burn=500, dbname='exp2mod6_%i.db'%id, db='pickle')
    return exp2model6


# In[ ]:

def run_exp2mod7(id):
    """ bias: rwd/pen tradeoff model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model7 = hddm.HDDM(data, depends_on={'z':'rwd_pen'}, include='z'
                           , p_outlier=0.05)
    exp2model7.find_starting_values()
    exp2model7.sample(1500, burn=500, dbname='exp2mod7_%i.db'%id, db='pickle')
    return exp2model7


# In[ ]:

def run_exp2mod8(id):
    """ bias: rwd prob model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    exp2model8 = hddm.HDDM(data, depends_on={'z':'rwd_prob'}, include='z'
                           , p_outlier=0.05)
    exp2model8.find_starting_values()
    exp2model8.sample(1500, burn=500, dbname='exp2mod8_%i.db'%id, db='pickle')
    return exp2model8

# In[ ]:

def run_exp2mod9(id):
    """ drift-rate: task params with free bias model """
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    #build model
    exp2model9 = hddm.HDDM(data,depends_on={'v':['rwd_pen','rwd_prob']}, include='z'
                           , p_outlier=0.05)
    exp2model9.find_starting_values()
    exp2model9.sample(1500, burn=500, dbname='exp2mod9_%i.db'%id,db='pickle')
    return exp2model9

# In[ ]:

def run_exp2mod10(id):
    """ drift-rate: rwd/pen tradeoff with free bias model """
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    #build model
    exp2model10 = hddm.HDDM(data,depends_on={'v':'rwd_pen'}, include='z'
                           , p_outlier=0.05)
    exp2model10.find_starting_values()
    exp2model10.sample(1500, burn=500, dbname='exp2mod10_%i.db'%id,db='pickle')
    return exp2model10

# In[ ]:

def run_exp2mod11(id):
    """ drift-rate: rwd_prob with free bias model """
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp2data.csv')
    #data grooming, remove fast outliers
    #rtSig = data.rt.std()
    #rtMu = data.rt.mean()
    #cutoff =  rtMu - rtSig
    #data = data[data.rt>cutoff]
    #data.reset_index(drop=True, inplace=True)
    #build model
    exp2model11 = hddm.HDDM(data,depends_on={'v':'rwd_prob'}, include='z'
                           , p_outlier=0.05)
    exp2model11.find_starting_values()
    exp2model11.sample(1500, burn=500, dbname='exp2mod11_%i.db'%id,db='pickle')
    return exp2model11
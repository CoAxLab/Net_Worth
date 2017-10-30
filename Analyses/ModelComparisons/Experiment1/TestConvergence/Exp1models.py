
# coding: utf-8

# In[ ]: # This file contains the model definitions for all HDDMs tested on Experiment 1 data.

# In[ ]:

def run_exp1mod1(id):
    """ pure drift-rate:task params model """
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model1 = hddm.HDDM(data,depends_on={'v':['rwd_pen','stableVar']}, p_outlier=0.05)
    exp1model1.find_starting_values()
    exp1model1.sample(3000, burn=1500, dbname='exp1mod1_%i.db'%id,db='pickle')
    return exp1model1


# In[ ]:

def run_exp1mod2(id):
    """ bias:task params model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    exp1model2 = hddm.HDDM(data, depends_on={'z':['rwd_pen','stableVar']}, include='z'
                           , p_outlier=0.05)
    exp1model2.find_starting_values()
    exp1model2.sample(1500, burn=500, dbname='exp1mod2_%i.db'%id, db='pickle')
    return exp1model2


# In[ ]:

def run_exp1mod3(id):
    """ drift-rate: rwd/pen tradeoff, bias: stable target variance model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    exp1model3 = hddm.HDDM(data, depends_on={'v':'rwd_pen','z':'stableVar'}, include='z'
                           , p_outlier=0.05)
    exp1model3.find_starting_values()
    exp1model3.sample(1500, burn=500, dbname='exp1mod3_%i.db'%id, db='pickle')
    return exp1model3


# In[ ]:

def run_exp1mod4(id):
    """bias: rwd/pen tradeoff, drift-rate: stable target variance model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    exp1model4 = hddm.HDDM(data, depends_on={'v':'stableVar','z':'rwd_pen'}, include='z'
                           , p_outlier=0.05)
    exp1model4.find_starting_values()
    exp1model4.sample(1500, burn=500, dbname='exp1mod4_%i.db'%id, db='pickle')
    return exp1model4


# In[ ]:

def run_exp1mod5(id):
    """ drift-rate: rwd/pen tradeoff  model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    exp1model5 = hddm.HDDM(data, depends_on={'v':'rwd_pen'}, p_outlier=0.05)
    exp1model5.find_starting_values()
    exp1model5.sample(1500, burn=500, dbname='exp1mod5_%i.db'%id, db='pickle')
    return exp1model5


# In[ ]:

def run_exp1mod6(id):
    """ drift-rate: stable target variance model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    exp1model6 = hddm.HDDM(data, depends_on={'v':'stableVar'}, p_outlier=0.05)
    exp1model6.find_starting_values()
    exp1model6.sample(1500, burn=500, dbname='exp1mod6_%i.db'%id, db='pickle')
    return exp1model6


# In[ ]:

def run_exp1mod7(id):
    """ bias: rwd/pen tradeoff model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    exp1model7 = hddm.HDDM(data, depends_on={'z':'rwd_pen'}, include='z'
                           , p_outlier=0.05)
    exp1model7.find_starting_values()
    exp1model7.sample(1500, burn=500, dbname='exp1mod7_%i.db'%id, db='pickle')
    return exp1model7


# In[ ]:

def run_exp1mod8(id):
    """ bias: stable target variance model """
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    exp1model8 = hddm.HDDM(data, depends_on={'z':'stableVar'}, include='z'
                           , p_outlier=0.05)
    exp1model8.find_starting_values()
    exp1model8.sample(6000, burn=3000, dbname='exp1mod8_%i.db'%id, db='pickle')
    return exp1model8

# In[ ]:

def run_exp1mod9(id):
    """ drift-rate: task params with free bias model """
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model9 = hddm.HDDM(data,depends_on={'v':['rwd_pen','stableVar']}, include='z'
                           , p_outlier=0.05)
    exp1model9.find_starting_values()
    exp1model9.sample(3000, burn=1500, dbname='exp1mod9_%i.db'%id,db='pickle')
    return exp1model9

# In[ ]:

def run_exp1mod10(id):
    """ drift-rate: rwd/pen tradeoff with free bias model """
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model10 = hddm.HDDM(data,depends_on={'v':'rwd_pen'}, bias=True, include=['v','a','t','z']
                           , p_outlier=0.05)
    exp1model10.find_starting_values()
    exp1model10.sample(1500, burn=500, dbname='exp1mod10_%i.db'%id,db='pickle')
    return exp1model100
    
# In[ ]:

def run_exp1mod11(id):
    """ drift-rate: stable target variance with free bias model """
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model11 = hddm.HDDM(data,depends_on={'v':'stableVar'}, bias=True, include=['v','a','t','z']
                           , p_outlier=0.05)
    exp1model11.find_starting_values()
    exp1model11.sample(3000, burn=1500, dbname='exp1mod11_%i.db'%id,db='pickle')
    return exp1model11
    
# In[ ]:

def run_exp1mod12(id):
    """ drift-rate: stable target variance, rwd/pen tradeoff
        bias : stable target variance model"""
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model12 = hddm.HDDM(data,depends_on={'v':['rwd_pen','stableVar'],'z':'stableVar'}, bias=True,
                            include=['v','a','t','z'], p_outlier=0.05)
    exp1model12.find_starting_values()
    exp1model12.sample(3000, burn=1000, dbname='exp1mod12_%i.db'%id,db='pickle')
    return exp1model12
    
# In[ ]:

def run_exp1mod13(id):
    """ drift-rate: stable target variance, rwd/pen tradeoff
        bias : rwd/pen tradeoff model"""
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model13 = hddm.HDDM(data,depends_on={'v':['rwd_pen','stableVar'],'z':'rwd_pen'}, bias=True,
                            include=['v','a','t','z'], p_outlier=0.05)
    exp1model13.find_starting_values()
    exp1model13.sample(3000, burn=1000, dbname='exp1mod13_%i.db'%id,db='pickle')
    return exp1model13

# In[ ]:
def run_exp1mod14(id):
    """ drift-rate: rwd/pen tradeoff
        bias : rwd/pen tradeoff, stable target variance model"""
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model14 = hddm.HDDM(data,depends_on={'v':['rwd_pen'],'z':['rwd_pen','stabelVar']}, bias=True,
                            include=['v','a','t','z'], p_outlier=0.05)
    exp1model14.find_starting_values()
    exp1model14.sample(3000, burn=1000, dbname='exp1mod14_%i.db'%id,db='pickle')
    return exp1model14

# In[ ]:

def run_exp1mod15(id):
    """ drift-rate: stable target variance model
        bias : rwd/pen tradeoff, stable target variance model"""
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model15 = hddm.HDDM(data,depends_on={'v':['stableVar'],'z':['rwd_pen','stabelVar']}, bias=True,
                            include=['v','a','t','z'], p_outlier=0.05)
    exp1model15.find_starting_values()
    exp1model15.sample(3000, burn=1000, dbname='exp1mod15_%i.db'%id,db='pickle')
    return exp1model15

# In[ ]:

def run_exp1mod16(id):
    """ drift-rate: rwd/pen tradeoff, stable target variance model
        bias : rwd/pen tradeoff, stable target variance model"""
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    exp1model16 = hddm.HDDM(data,depends_on={'v':['rwd_pen','stableVar'],'z':['rwd_pen','stabelVar']},
                            bias=True, include=['v','a','t','z'], p_outlier=0.05)
    exp1model16.find_starting_values()
    exp1model16.sample(3000, burn=1000, dbname='exp1mod16_%i.db'%id,db='pickle')
    return exp1model16

# In[ ]:

def run_testmod(id):
    #imports
    import hddm
    data = hddm.load_csv('~/Pub_Code_master/Data/exp1data.csv')
    #data grooming, remove fast outliers
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    #build model
    testmod = hddm.HDDM(data)
    testmod.sample(200,burn=20,dbname='testmod_%i.db'%id, db='pickle')
    return testmod

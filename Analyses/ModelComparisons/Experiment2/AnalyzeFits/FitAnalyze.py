
# coding: utf-8

# In[ ]:

def fit_and_analyze(experiment=1, depends_on={}, bias=False, include=['v', 't', 'a', 'z'], nsample=1000, nburn=20, p_outlier=.05, mname='myModel', saveplots=False, stats=False):
    """ fits a hierarchical model to <data> with any dependencies specified 
        by <depends_on> dict. Saves the MCMC traces to current wk dir by default. 
        Traces are then loaded into collapsed into an average_model which is then 
        used to visualize the avg. posterior_quantile and posterior_predictive model fits 
    
    ::Arguments::
        data (DataFrame):
            df passed to model 
        depends_on (dict): 
            dict with parameters (keys) and dependencies on exp. conditions (values)
        include (list):
            list of parameters to include in model
        bias (bool):
            fit starting-point (z) parameter if True
        nsample (int):
            number of MCMC samples
        nburn (int):
            size of burn-in
        p_outlier (int):
            values [0,1], includes uniform probability of outliers
        mname (str): 			
            arbitrary name of model being fit
        figsize (tuple):
            width, height of average_model posterior pred/quant plots
        saveplots (bool):
            saves png file of average_model fit results to working dir
        stats (bool):
            saves csv of average model stats

    ::Returns::
        m (HDDM model): 
            optimized hierarchical model
    """
    # Imports
    import hddm
    import numpy as np
    get_ipython().magic('matplotlib inline')
    
    # Logistics
    tracesName = '_'.join([mname, 'traces.db'])
    if 'z' in list(depends_on):
        bias = True

    if 'z' not in include and bias:
        include.append('z')
    
    # Data
    data = hddm.load_csv('~/Pub_Code_master/Data/exp%idata.csv'%experiment) # select data for chosen experiment
    
    # data grooming, remove fast outliers, only present in exp1
    #if experiment == 1:
    rtSig = data.rt.std()
    rtMu = data.rt.mean()
    cutoff =  rtMu - rtSig
    data = data[data.rt>cutoff]
    data.reset_index(drop=True, inplace=True)
    
    # Model
    m=hddm.HDDM(data, depends_on=depends_on, bias=bias, include=include, p_outlier=p_outlier)
    m.find_starting_values()
    m.sample(nsample, burn=nburn, dbname=tracesName, db='pickle')

    # get model fit stats
    if stats:
        statsname = '_'.join([mname,'stats.csv'])
        stats = m.print_stats(statsname)
        m.print_stats()
        
    # gen. average model with traces loaded
    avgm = get_avg_model(m, tracesName)
                     
    # set sensible xlim of RT density plots
    valRange = np.linspace(-2, 2, 100)

    # plot RT density
    avgm.plot_posterior_predictive(save=saveplots, value_range=valRange)
    
    # plot posteriors
    avgm.plot_posteriors(save=saveplots)
    
    return avgm

def get_avg_model(model, tracesName):
    """ gen average_model from <model> and loads hier. traces from wk dir 
    """
    avgm=model.get_average_model()
    return avgm.load_db(tracesName, db='pickle')


# In[ ]:

#from jupyterthemes import jtplot
#jtplot.style('oceans16')
#test = fit_and_analyze(experiment=2, depends_on={}, bias=False, include=['v', 't', 'a', 'z'], nsample=200, nburn=20, p_outlier=.05, mname='test', figsize=(12, 10), saveplots=False)


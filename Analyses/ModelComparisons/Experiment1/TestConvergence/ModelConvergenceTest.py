
# coding: utf-8

# In[ ]:

def test_convergence(run_model, chains, saveplots=False):
    """
    Uses ipyparallel client to run <chains> model fits, then runs r-hat (gelman-rubin) statistic
    on the resulting traces. Finally, the models are concatenated and their posteriors are plotted for assessing
    convergence.
    """
    from ipyparallel import Client
    c = Client()[:] # create the ipython client
    jobs = c.map(run_model, range(chains)) # c.map(function, number of CPUs)
    models = jobs.get() # run the jobs
    
    # Calculate convergence statistics
    from kabuki.analyze import gelman_rubin
    rhat = gelman_rubin(models)
    
    # Create a new model that contains all traces concatenated from the individual models
    from kabuki.utils import concat_models
    combined_model = concat_models(models)
    
    # Plot posteriors
    combined_model.plot_posteriors(save=saveplots)
    return rhat
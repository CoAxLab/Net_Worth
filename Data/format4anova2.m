%format4anova2.m
% Formats the subject data for rmanova2.m
clear

load('exp2data.mat');

% For each subject, take the mean of the measures
subs = unique(subj_idx);

% Define output vectors
mean_response = zeros(length(subs)*8,1);

mean_rt_risky = zeros(length(subs)*8, 1);
mean_rt_safe = zeros(length(subs)*8, 1);

mean_slxn_err_risky = zeros(length(subs)*8, 1);
mean_slxn_err_safe = zeros(length(subs)*8, 1);

mean_peak_V_risky = zeros(length(subs)*8, 1);
mean_peak_V_safe = zeros(length(subs)*8, 1);

subj_labels = sort(repmat(subs,8,1));
rp_labels = zeros(length(subs)*8,1);
rprob_labels = zeros(length(subs)*8,1);

probs = sort(unique(rwd_prob));
loc = 1; % output location index

% Next, we need to remove subjects who don't select the risky target ever
% in one of the conditions for the psychophysics info.
for i = 1:length(subs)
    sub = subs(i); % This subject
    mask = find(subj_idx == sub); % Indices of data points for this subj
    
    % pull out decisions for that subj
    ch = response(mask);
    
    rp = rwd_pen(mask);
    rprob = rwd_prob(mask);
    
    % create mask for risky/safe selections for this subj
    risky = find(ch == 1);
    safe = find(ch == 0);
    
    % get the psychophysics & task condition for each target slxn
    pVr = peakV(risky);
    pVs = peakV(safe);
    
    slr = slxn_err(risky);
    sls = slxn_err(safe);
    
    tr = rt(risky);
    ts = rt(safe);
    
    rpr = rwd_pen(risky);
    rps = rwd_pen(safe);
    
    rprobr = rwd_prob(risky);
    rprobs = rwd_prob(safe);
    
    % Take means for each conditional combination
    
    for r = 1:4
        for s = 1:2
            % Decisions
            cmask = find( (rp == s) & (rprob == probs(r))); % cond mask general
            mean_response(loc) = nanmean(ch(cmask));
            
            % Psychophysics
            rmask = find( (rpr == s) & (rprobr == probs(r))); % cond mask risky
            smask = find( (rps == s) & (rprobs == probs(r))); % cond mask safe
            if ~isempty(rmask)
                mean_peak_V_risky(loc) = nanmean(pVr(rmask));
                mean_slxn_err_risky(loc) = nanmean(slr(rmask));
                mean_rt_risky(loc) = nanmean(tr(rmask));
                mean_peak_V_safe(loc) = nanmean(pVs(smask));
                mean_slxn_err_safe(loc) = nanmean(sls(smask));
                mean_rt_safe(loc) = nanmean(ts(smask));
            end

            % Condition Labels
            rp_labels(loc) = s;
            rprob_labels(loc) = r;
            
            loc = loc + 1; %update output location for next iteration
        end
    end
end
mask = [];
for i = 1:length(subj_labels)
    if mean_peak_V_risky(i) == 0 || mean_peak_V_safe(i) == 0 || isnan(mean_peak_V_safe(i)) 
        rm_sub = subj_labels(i);
        mask = [mask; find(subj_labels == rm_sub)];
    end
end

mean_rt_risky(mask) = [];
mean_rt_safe(mask) = [];

mean_slxn_err_risky(mask) = [];
mean_slxn_err_safe(mask) = [];

mean_peak_V_risky(mask) = [];
mean_peak_V_safe(mask) = [];

subj_labels2 = subj_labels; % Second set of labels are for the psychophysics
rp_labels2 = rp_labels; % While the first set are for the decisions (responses)
rprob_labels2 = rprob_labels;

subj_labels2(mask) = [];
rp_labels2(mask) = [];
rprob_labels2(mask) = [];

% Differences between targets
pv_diff = mean_peak_V_risky - mean_peak_V_safe;
rt_diff = mean_rt_risky - mean_rt_safe;
sl_diff = mean_slxn_err_risky - mean_slxn_err_safe;

save('exp2_anova_data.mat', 'subj_labels','rp_labels','rprob_labels',...
    'subj_labels2','rp_labels2','rprob_labels2',...
    'mean_response','mean_peak_V_risky','mean_peak_V_safe','mean_slxn_err_risky',...
    'mean_slxn_err_safe','mean_rt_risky','mean_rt_safe');


% Do the ANOVAs
responses = rm_anova2(mean_response,subj_labels,rp_labels,rprob_labels,{'rp','prob'})

sl_risky = rm_anova2(mean_slxn_err_risky,subj_labels2,rp_labels2,rprob_labels2,{'rp','prob'})
sl_safe = rm_anova2(mean_slxn_err_safe,subj_labels2,rp_labels2,rprob_labels2,{'rp','prob'})

rt_risky = rm_anova2(mean_rt_risky,subj_labels2,rp_labels2,rprob_labels2,{'rp','prob'})
rt_safe = rm_anova2(mean_rt_safe,subj_labels2,rp_labels2,rprob_labels2,{'rp','prob'})

pV_risky = rm_anova2(mean_peak_V_risky,subj_labels2,rp_labels2,rprob_labels2,{'rp','prob'})
pV_safe = rm_anova2(mean_peak_V_safe,subj_labels2,rp_labels2,rprob_labels2,{'rp','prob'})

diff_pV = rm_anova2(pv_diff, subj_labels2, rp_labels2, rprob_labels2, {'rp','prob'})
diff_rt = rm_anova2(rt_diff, subj_labels2, rp_labels2, rprob_labels2, {'rp','prob'})
diff_sl = rm_anova2(sl_diff, subj_labels2, rp_labels2, rprob_labels2, {'rp','prob'})

save('exp2_anova_results.mat', 'responses','sl_risky','sl_safe','rt_risky','rt_safe'...
    ,'pV_risky','pV_safe','diff_pV','diff_rt','diff_sl');
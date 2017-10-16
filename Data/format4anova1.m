%format4anova1.m
% Formats the subject data for rmanova2.m

% Load data & remove subj 9 with this script:
remove_subj9;

% For each subject, take the mean of the measures
subs = unique(subj_idx);

% Define output vectors
mean_response = zeros(length(subs)*16,1);

mean_rt_risky = zeros(length(subs)*16, 1);
mean_rt_safe = zeros(length(subs)*16, 1);

mean_slxn_err_risky = zeros(length(subs)*16, 1);
mean_slxn_err_safe = zeros(length(subs)*16, 1);

mean_peak_V_risky = zeros(length(subs)*16, 1);
mean_peak_V_safe = zeros(length(subs)*16, 1);

subj_labels = sort(repmat(subs,16,1));
rp_labels = zeros(length(subs)*16,1);
sv_labels = zeros(length(subs)*16,1);

loc = 1; % output location index

% Next, we need to remove subjects who don't select the risky target ever
% in one of the conditions for the psychophysics info.
for i = 1:length(subs)
    sub = subs(i); % This subject
    mask = find(subj_idx == sub); % Indices of data points for this subj
    
    % pull out decisions for that subj
    ch = response(mask);
    
    rp = rwd_pen(mask);
    sv = stableVar(mask);
    
    % create mask for risky/safe selections for this subj
    risky = find(ch == 1);
    safe = find(ch == 0);
    
    % get the psychophysics & task condition for each target slxn
    pVr = peak_V(risky);
    pVs = peak_V(safe);
    
    slr = slxn_err(risky);
    sls = slxn_err(safe);
    
    tr = rt(risky);
    ts = rt(safe);
    
    rpr = rwd_pen(risky);
    rps = rwd_pen(safe);
    
    svr = stableVar(risky);
    svs = stableVar(safe);
    
    % Take means for each conditional combination
    for r = 1:4
        for s = 1:4
            % Decisions
            cmask = find( (rp == r - 1) & (sv == s - 1)); % cond mask general
            mean_response(loc) = nanmean(ch(cmask));
            
            % Psychophysics
            rmask = find( (rpr == r - 1) & (svr == s - 1)); % cond mask risky
            smask = find( (rps == r - 1) & (svs == s - 1)); % cond mask safe
            if ~isempty(rmask)
                mean_peak_V_risky(loc) = nanmean(pVr(rmask));
                mean_slxn_err_risky(loc) = nanmean(slr(rmask));
                mean_rt_risky(loc) = nanmean(tr(rmask));
                mean_peak_V_safe(loc) = nanmean(pVs(smask));
                mean_slxn_err_safe(loc) = nanmean(sls(smask));
                mean_rt_safe(loc) = nanmean(ts(smask));
            end

            % Condition Labels
            rp_labels(loc) = r;
            sv_labels(loc) = s;
            
            loc = loc + 1; %update output location for next iteration
        end
    end
end
mask = [];
for i = 1:length(subj_labels)
    if mean_peak_V_risky(i) == 0
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
sv_labels2 = sv_labels;

subj_labels2(mask) = [];
rp_labels2(mask) = [];
sv_labels2(mask) = [];

% Differences between targets
pv_diff = mean_peak_V_risky - mean_peak_V_safe;
rt_diff = mean_rt_risky - mean_rt_safe;
sl_diff = mean_slxn_err_risky - mean_slxn_err_safe;

save('exp1_anova_data.mat', 'subj_labels','rp_labels','sv_labels',...
    'subj_labels2','rp_labels2','sv_labels2',...
    'mean_response','mean_peak_V_risky','mean_peak_V_safe','mean_slxn_err_risky',...
    'mean_slxn_err_safe','mean_rt_risky','mean_rt_safe');

% Do the ANOVAs
responses = rm_anova2(mean_response,subj_labels,rp_labels,sv_labels,{'rp','sv'})

sl_risky = rm_anova2(mean_slxn_err_risky,subj_labels2,rp_labels2,sv_labels2,{'rp','sv'})
sl_safe = rm_anova2(mean_slxn_err_safe,subj_labels2,rp_labels2,sv_labels2,{'rp','sv'})

rt_risky = rm_anova2(mean_rt_risky,subj_labels2,rp_labels2,sv_labels2,{'rp','sv'})
rt_safe = rm_anova2(mean_rt_safe,subj_labels2,rp_labels2,sv_labels2,{'rp','sv'})

pV_risky = rm_anova2(mean_peak_V_risky,subj_labels2,rp_labels2,sv_labels2,{'rp','sv'})
pV_safe = rm_anova2(mean_peak_V_safe,subj_labels2,rp_labels2,sv_labels2,{'rp','sv'})

diff_pV = rm_anova2(pv_diff, subj_labels2, rp_labels2, sv_labels2, {'rp','sv'})
diff_rt = rm_anova2(rt_diff, subj_labels2, rp_labels2, sv_labels2, {'rp','sv'})
diff_sl = rm_anova2(sl_diff, subj_labels2, rp_labels2, sv_labels2, {'rp','sv'})

save('exp1_anova_results.mat', 'responses','sl_risky','sl_safe','rt_risky','rt_safe'...
    ,'pV_risky','pV_safe','diff_pV','diff_rt','diff_sl');
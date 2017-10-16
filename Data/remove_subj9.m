%remove_subj9.mat

% Removes subject #9 pre-ANOVA analyses due to apparent lack of candid
% participation (peak velocities extremely unreasonable for human
% participant in aiming experiment).

load('exp1data.mat');

subj9_indices = find(subj_idx == 9);

% Since all of the data is already sorted in ascending order by subj_idx,
% we can just remove these indices by redefining the vectors as the
% elements before and after the min/max of these indices

% Get the start/end of subj 9's data
s = min(subj9_indices);
e = max(subj9_indices);

% Redefine vectors
peak_V = split_vector(peak_V,s,e);
response = split_vector(response,s,e);
rt = split_vector(rt,s,e);
rwd_pen = split_vector(rwd_pen,s,e);
stableVar = split_vector(stableVar,s,e);
slxn_err = split_vector(slxn_err,s,e);
subj_idx = split_vector(subj_idx,s,e);

clear subj9_indices s e
function out_vect =  split_vector(vect,start_split, end_split)
out_vect = [vect(1:start_split-1, 1) ; vect(end_split+1:end, 1)];
end


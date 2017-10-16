function [ Eligible, PercentMT ] = EligibleMT( MTs )
%EligibleMT takes an input of a vector of subject movement times in each 
%trial ofa task and returns a binary value for the eligibility of a subject 
%with respect to movement time criteria. This function is based off of the 
%idea that MTs of 0 are not valid selections since subjects are not conducting
%motor selections. Therefore, any subject with more than 5% of MTs of 0 is
%not participating in the task enough to meet eligbility for inclusion in
%behavioral analysis.

GoodSelections = find(MTs); %Finds movement times that are not 0
SelectionCriteria = 0.95; % This will be the minimal percent good selections allowed to meet eligibility
PercentMT = numel(GoodSelections)/length(MTs); %Percentage of trials on which subjects moved the cursor
if numel(GoodSelections) < length(MTs) * SelectionCriteria;
    Eligible = 0;
else
    Eligible = 1;
end
end


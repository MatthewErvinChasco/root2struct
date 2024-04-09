%% Import ROOT Ntuples into MATLAB as Structure of Tables
% Copyright 2024 The Mathworks, Inc.
% 
% Path management

orig = pwd;
parserPath = orig+"\NtupleParserCode.py";
rootfilePath = orig+"\py-hsimple2.root";
rootfilePath = "'"+replace(rootfilePath,"\","/")+"'";
%% 
% Navigate into root bin folder, run thisroot.bat, then run PyROOT code.

cd('C:\root_v6.30.04\bin\')
try
S = struct;
!thisroot.bat
%% 
% Collect Keys from ROOT file and list only the Ntuples

[Keys,isfolder]=pyrunfile(orig+"\CollectNtuples.py "+rootfilePath,["KeyNameList","IsFolderList"]);
Keys = replace(string(char(Keys)),"'",'"');
eval("Keys="+Keys)
isfolder = logical(isfolder);
Keys = Keys(isfolder);
%% 
% Loop over Ntuples to grab leaf data and names. Save Ntuple content to a MATLAB 
% Table. Save Tables to Structure.

for j=1:length(Keys)
    [Values,leafNames]=pyrunfile(parserPath+" "+rootfilePath+" "+Keys(j),["NtupleVars","leafNames"]);
    Values = double(Values).';
    leaves = replace(string(char(leafNames)),"'",'"');
    eval("leaves="+leaves)
    T = array2table(Values);
    T.Properties.VariableNames = leaves;
    S.(Keys(j)) = T;
end

catch Merr
    disp(Merr.message)
end
cd(orig)
save("structFromROOT","S")
%% Generate a ROOT file to work with

try
    [status,cmdout] = system("C:\root_v6.30.04\bin\thisroot.bat & py -3.8 ./hsimple2.py","-echo")
catch Merr
    disp(Merr.message)
end
%% Run main file to import ROOT file data into MATLAB

root2struct
%% Perform analysis

histogram(S.ntuple.px)
histogram(S.ntuple2.mt)
scatter(S.ntuple.px,S.ntuple.pz)
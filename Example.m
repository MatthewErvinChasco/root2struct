%% Generate a ROOT file to work with

orig = pwd
cd('C:\root_v6.30.04\bin\')
try
    !thisroot.bat
    pyrunfile(orig+"\hsimple2.py")
catch Merr
    disp(Merr.message)
end
cd(orig)
%% Run main file to import ROOT file data into MATLAB

root2struct
%% Perform analysis

histogram(S.ntuple.px)
histogram(S.ntuple2.mt)
scatter(S.ntuple.px,S.ntuple.pz)
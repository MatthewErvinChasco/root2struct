import ROOT
from ROOT import gROOT, TCanvas,TH1D,TH2D,TFile,TStyle,TLegend,TPave,TPaveStats,TPad,TPaveLabel,gStyle,gPad,TPaletteAxis,TLine
import numpy
import sys

filepath = sys.argv[1]
ntupleInFile = sys.argv[2]
f = ROOT.TFile.Open(filepath,'READ')
tree = f.Get(ntupleInFile)
listofleaves = tree.GetListOfLeaves()
# print(listofleaves)

leafNames = []
for atree in listofleaves:
    print(atree.GetName())
    leafNames.append(atree.GetName())

NtupleVars = []
for atree in listofleaves:
    #n=0
    Physvars = []

    for entry in tree:
        physvar = entry.GetLeaf(atree.GetName()).GetValue()
        #n = n+1
        Physvars.append(physvar)

    Physvars = numpy.array(Physvars)
    Physvars = Physvars.reshape(-1,1)
    # print(numpy.shape(NtupleVars))
    NtupleVars.append(Physvars)
NtupleVars = numpy.array(NtupleVars)
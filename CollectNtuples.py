import ROOT
from ROOT import gROOT, TCanvas,TH1D,TH2D,TFile,TStyle,TLegend,TPave,TPaveStats,TPad,TPaveLabel,gStyle,gPad,TPaletteAxis,TLine
import numpy
import sys

filepath = sys.argv[1]
f = ROOT.TFile.Open(filepath,'READ')
trees = f.GetListOfKeys()
# print(trees)
KeyNameList = []
IsFolderList = []
for x in trees:
    # print(x.GetName())
    # print(x.IsFolder())
    KeyNameList.append(x.GetName())
    IsFolderList.append(x.IsFolder())
IsFolderList = numpy.array(IsFolderList)
    

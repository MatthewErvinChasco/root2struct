##  This program creates :
##    - a memory-resident ntuple
##
##  These objects are filled with some random numbers and saved on a file.
##
## \author Wim Lavrijsen, Enric Tejedor
##  modified by Matt Chasco

from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import ctypes
import math

# Create a new ROOT binary machine independent file.
# Note that this file may contain any kind of ROOT objects, histograms, etc
# This file is now becoming the current directory.

hfile = gROOT.FindObject( 'py-hsimple2.root' )
if hfile:
   hfile.Close()
hfile = TFile( 'py-hsimple2.root', 'RECREATE', 'Demo ROOT file with histograms' )

# Create ntuples
ntuple = TNtuple( 'ntuple', 'Demo ntuple', 'px:py:pz:random:i' )
ntuple2 = TNtuple( 'ntuple2', 'Demo ntuple', 'm:mt' )

# Initialize random number generator.
gRandom.SetSeed()
rannor, rndm = gRandom.Rannor, gRandom.Rndm

# Fill histograms randomly.
px_ref, py_ref = ctypes.c_double(), ctypes.c_double()

for i in range( 25000 ):
 # Generate random values. Use ctypes to pass doubles by reference
   rannor( px_ref, py_ref)
 # Retrieve the generated values
   px = px_ref.value
   py = py_ref.value
   
   pz = px*px + py*py
   random = rndm(1)

   m = rndm(2)
   mt = math.sqrt(1-m*m)

 # Fill ntuples.
   ntuple.Fill( px, py, pz, random, i )
   if i < 5000:
    ntuple2.Fill( m, mt )

# Save all objects in this file.
hfile.Write()

# Note that the file is automatically closed when application terminates
# or when the file destructor is called.
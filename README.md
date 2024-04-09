The MATLAB code runs Python to use PyROOT for extracting data from a ROOT file.
Running this package requires the compatibility of three platforms: MATLAB, Python, and ROOT.

MATLAB version R2021b

Python version 3.8

ROOT version 6.30.04

Begin by creating a Python environment from within a MATLAB session with the command:
*pyenv(Version=pathtoPython)*
You will also need to know the path to your ROOT installation to execute the thisroot.bat script.

The main entry point is the MATLAB script *root2struct.mlx*
View the *Example.mlx* file for context.
The code file ".m" counterparts are included here for visibility.

The Python scripts *CollectNtuples.py* and *NtupleParserCode.py* are helper files used in *root2struct.mlx*, taking advantage of PyROOT.

The Python script *hsimple2.py* generates the *py-hsimple2.root* file used in the example. It is modified from the file found in the PyROOT tutorial: https://root.cern.ch/doc/master/group__tutorial__pyroot.html

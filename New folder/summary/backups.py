# The list of all the working exercises along with the basic guide to plotting histograms


# excercise 5.3: to have a graph of only positively charged electrons: do not edit
lepchargecut = " lep_charge[{0}] == 1 && lep_type[{0}]=={1} "  # this has to be a string, so "..."
chargecut = "(" + lepchargecut.format(0, 11) + ")"
# t.setalias("meanpt","sum$(lep_pt)/length$(lep_pt)") # define meanpt
t.draw("lep_pt >> h_lep_pt_mean(500,0,140e3)", weighting + "*" + chargecut)  # plot meanpt
h_lep_pt_mean = r.gdirectory.get("h_lep_pt_mean")
h_lep_pt_mean.write()

# exercise 6.4: invariant mass histogram of mll by running your code on the z -> mu mu data
# first run on the zmumu plot
# second run on the 2lep plot
inv_mass = "sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]- lep_eta[1])- cos(lep_phi[0]-lep_phi[1])))"
lepchargecut = "lep_charge[0] * lep_charge[1] == 1 && lep_type[{0}]=={1} && lep_n==2 "
chargecut = "(" + lepchargecut.format(0, 11) + "&&" + lepchargecut.format(1, 11) + ")"
t.SetAlias("inv_mass", inv_mass)
t.Draw("inv_mass >> h_lep_pt_mean(100,0,140e3)", weighting + "*" + chargeCut)
h_lep_pt_mean = r.gDirectory.Get("h_lep_pt_mean")
h_lep_pt_mean.Write()

# EXERCISE 6.7: plotting cone data from the calorimeter
# opposite flavour cut - when one is different flavour
lepchargeCut = " lep_charge[0] * lep_charge[1] == +1 && (lep_type[{0}]== 11 || lep_type[{0}]== 13) && lep_type[0]!=lep_type[1] && lep_n==2 "
chargeCut = "(" + lepchargeCut.format(0) + " || " + lepchargeCut.format(1) + ")"

# same flavour
lepchargeCut = " lep_charge[0] * lep_charge[1] == -1 && lep_n==2 && lep_type[{0}] == lep_type[{1}] && (lep_type[{0}]== 11 || lep_type[{0}]== 13 || lep_type[{0}]== 15)"
chargeCut = "(" + lepchargeCut.format(0, 1) + ")"

# same flavour for ptcone30
lepchargeCut = "lep_charge[0] * lep_charge[1] == 1 && lep_type[{0}]=={1} && lep_n==2 "
chargeCut = "(" + lepchargeCut.format(0, 13) + " && " + lepchargeCut.format(1, 13) + ")"
t.Draw("lep_ptcone30 >> lep_ptcone30(100,0,10e3)", weighting + "*" + chargeCut)
lep_ptcone30 = r.gDirectory.Get("lep_ptcone30")
lep_ptcone30.Write()

# same flavour for etcone20
lepchargeCut = "lep_charge[0] * lep_charge[1] == -1 && lep_type[{0}]=={1} && lep_n==2 "
chargeCut = "(" + lepchargeCut.format(0, 13) + "&&" + lepchargeCut.format(1, 13) + ")"
t.Draw("lep_etcone20 >> lep_etcone20(500,0,10e3)", weighting + "*" + chargeCut)
lep_etcone20 = r.gDirectory.Get("lep_etcone20")
lep_etcone20.Write()

# the part taken from the notebook
# The required header for every cell
import ROOT as r
from ROOT import *
import os

histFile = r.TFile.Open("out/Zmumu_fast.root", "READ")
histFile2 = r.TFile.Open("out/2lep_fast.root", "READ")
histFile2 = r.TFile.Open("out/2lep_fast.root", "READ")
# then read in the histograms. Exercise 6.4 will be used as an example


# Drawing hisitograms the basics - according to the initial file
# Format is t.Draw("variable_to_plot >> histogram_name (number_of_bins, x_axis_minimum, x_axis_maximum"),weighting)

# A couple of simple examples:
# 1) Draw a histogram of number of leptons per event.
# t.Draw("lep_n >> h_lep_n(10, -0.5, 9.5)", weighting)
# 2) Draw a histogram of the "lepton type" of every lepton in every event.
# t.Draw("lep_type >> h_lep_type(10, 7.5, 17.5)", weighting)
# Note: lepton type takes the value 11 for electrons and 13 for muons


# Selection cuts can be used to plot only data that pass certain "selection cuts".
# For second argument in t.Draw() use (weighting + "* (selection_cuts)")

# For example, plotting transverse momentum of leptons only for events with 3 or more leptons:
# t.Draw("lep_pt >> h_3lep_pt(200,0,140e3)", weighting + "* (lep_n >= 3)")


# For example, plotting the average transverse momenta of leptons in each event:
# t.SetAlias("meanPt","Sum$(lep_pt)/Length$(lep_pt)") # define meanPt
# t.Draw("meanPt >> h_lep_pt_mean(200,0,140e3)", weighting + "*" + chargeCut) # plot meanPt
# For more information see https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45


# It can be useful to define selection cuts that can take input arguments - here is an example
# Define selection cuts for each lepton
# lepCut = "lep_pt[{0}] > 20e3  && lep_type[{0}]=={1} "
# Note: here "{0}" and "{1}" are dummy arguments that take the values specified when the function is used, as given below

# Require that both leptons [0] and [1] satisfy the specified selection cuts
# selCutsE = "(" + lepCut.format(0,11) + "&&" + lepCut.format(1,11) + ")"
# For events containing two electrons satisfying the specified selection cuts plot the average of the pseudorapidity of the  two electrons
# t.Draw("(lep_eta[0]+lep_eta[1])/2.0 >> h_electron_eta_average(100,-3.0,3.0)", weighting + "*" + selCutsE)

# Retrieve the results of drawing the histograms.
# This needs to be done for each histogram.
# h_lep_n = r.gDirectory.Get("h_lep_n")
# h_lep_type = r.gDirectory.Get("h_lep_type")
# h_3lep_pt = r.gDirectory.Get("h_3lep_pt")
# h_lep_pt_mean = r.gDirectory.Get("h_lep_pt_mean")
# h_electron_eta_average = r.gDirectory.Get("h_electron_eta_average")

# Set style of lep_n  histogram.
# h_lep_n.GetXaxis().SetTitle("Number of leptons per event") # label x axis
# h_lep_n.GetYaxis().SetTitle("Number of entries/bin") # label y axis
# h_lep_n.SetTitle("Number of leptons per event")
# h_lep_n.SetLineColor(r.kRed) # set the line colour to red
# For more information on histogram styling see https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html
# Note useful trick to get selection cuts used in making a particular histogram written out as a "title" for the histogram
# h_electron_eta_average.SetTitle(selCutsE)


# Write histograms to the output file.
# This needs to be done for each histogram.
# h_lep_n.Write()
# h_lep_type.Write()
# h_3lep_pt.Write()
# h_lep_pt_mean.Write()
# h_electron_eta_average.Write()


hist2.SetLineColor(r.kGreen + 1)
# hist2.SetFillColor(r.kGreen+1)
hist2.SetFillColorAlpha(r.kGreen + 1, 1)
hist3.SetLineColor(r.kOrange)
# hist3.SetFillColor(r.kOrange)
hist3.SetFillColorAlpha(r.kOrange, 1)
hist4.SetLineColor(r.kOrange)
# hist4.SetFillColor(r.kOrange)
hist4.SetFillColorAlpha(r.kOrange, 1)
hist5.SetLineColor(r.kYellow)
# hist5.SetFillColor(r.kYellow)
hist5.SetFillColorAlpha(r.kYellow, 1)
hist6.SetLineColor(r.kTeal)
# hist6.SetFillColor(r.kTeal)
hist6.SetFillColorAlpha(r.kTeal, 1)
hist7.SetLineColor(r.kBlue - 2)
# hist7.SetFillColor(r.kBlue-2)
hist7.SetFillColorAlpha(r.kBlue, 1)

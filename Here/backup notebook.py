# Cell for plotting single graphs

# Allow 'integral' value to be shown in statistics box of all histograms
gStyle.SetOptStat(1111111)


# This next block of code is used to display one histogram - its style must be repeated for every histogram you want to plot.

# FIRST HISTOGRAM

# Make the first canvas
# For simplicity the variable referring to the canvas should be the same as its name (given by the argument of "TCanvas()")
canvas1 = r.TCanvas("canvas1")

# Draw out the first histogram of your choice onto the canvas
hist_W.Draw("HIST")

#hist_lep_ptcone30.Draw()
#hist_lep_ptcone30_2.Draw()
#hist_lep_ptcone30_3.Draw()
#hist_lep_etcone20.Draw()
#hist_lep_etcone20_2.Draw()
#hist_lep_etcone20_3.Draw()

# Show historgram by displaying the canvas
canvas1.Draw()

hist_W.SetTitle("this one")
hist_W.GetXaxis().SetTitle("invariant mass (MeV)")
hist_W.GetYaxis().SetTitle("Number of entries/bin")

#hist_lep_ptcone30_2.SetTitle("2lep-13 ptcone30 (sc sf)")
#hist_lep_ptcone30_2.GetXaxis().SetTitle("Momentum (MeV)")
#hist_lep_ptcone30_2.GetYaxis().SetTitle("Number of entries/bin")
#hist_lep_ptcone30_2.GetYaxis().SetRangeUser(0,80)



# SECOND HISTOGRAM

# Make a second canvas
canvas2 = r.TCanvas("canvas2")

#To remove the stats box
hist_2lep_pt.SetStats(0)

# Draw out the second histogram onto this new canvas
hist_2lep_pt.Draw()

#hist_lep_etcone20.Draw()
#hist_lep_ptcone30.Draw()

# Show historgram by displaying this new canvas
canvas2.Draw()

#add axis labels
hist_2lep_pt.SetTitle("Invariant Mass using 2lep-13 data (dc df)")
hist_2lep_pt.GetXaxis().SetTitle("invariant mass (MeV)")
hist_2lep_pt.GetYaxis().SetTitle("Number of entries/bin")

#hist_lep_etcone20_2.GetXaxis().SetTitle("Energy (MeV)")
#hist_lep_etcone20_2.GetYaxis().SetTitle("Number of entries/bin")
#hist_lep_etcone20_2.SetTitle(" 2lep-13 etcone20 ")

#hist_lep_ptcone30.SetTitle("Zmumu ptcone30 (sc sf)")
#hist_lep_ptcone30.GetXaxis().SetTitle("Momentum (MeV)")
#hist_lep_ptcone30.GetYaxis().SetTitle("Number of entries/bin")
#hist_lep_ptcone30.GetYaxis().SetRangeUser(0,14)

# THIRD HISTOGRAM

# Make a third canvas
#canvas3 = r.TCanvas("canvas3")
#hist_lep_ptcone30_3.Draw()
#canvas3.Draw()
#hist_lep_ptcone30_3.SetTitle("Zee ptcone30 (sc sf)")
#hist_lep_ptcone30_3.GetXaxis().SetTitle("Momentum (MeV)")
#hist_lep_ptcone30_3.GetYaxis().SetTitle("Number of entries/bin")
#hist_lep_ptcone30_3.GetYaxis().SetRangeUser(0,14)





#canvas2.SetLogy()
#canvas2.SetLogx()







# cell for plotting multiple graphs

# Opening files up
histFile_2lep = r.TFile.Open("out/2lep_fast.root","READ")
#histFile_Zmumu = r.TFile.Open("out/Zmumu_fast.root","READ")
histFile_Zee = r.TFile.Open("out/Zee_fast.root","READ")
#histFile_Ztautau = r.TFile.Open("out/Ztautau_fast.root","READ")

histFile1 = r.TFile.Open("out/2lep_fast.root","READ")
histFile2 = r.TFile.Open("out/ttbar_lep_fast.root","READ")
histFile3 = r.TFile.Open("out/Zmumu_fast.root","READ") # same colour
histFile4 = r.TFile.Open("out/Zee_fast.root","READ")  # same colour
histFile5 = r.TFile.Open("out/Ztautau_lep_fast.root","READ")
histFile6 = r.TFile.Open("out/Wplus_2lep_fast.root","READ")
histFile7 = r.TFile.Open("out/Wminus_2lep_fast.root","READ")




# Get histograms
dataHist = histFile_2lep.Get("h_lep_pt_mean")
#mcHist_Zmumu = histFile_Zmumu.Get("h_lep_pt_mean")
mcHist_Zee = histFile_Zee.Get("h_lep_pt_mean")
#mcHist_Ztautau = histFile_Ztautau.Get("h_lep_pt_mean")

# Change the histograms directory once read in so that they do not get delected when files close
dataHist.SetDirectory(0)
#mcHist_Zmumu.SetDirectory(0)
mcHist_Zee.SetDirectory(0)
#mcHist_Ztautau.SetDirectory(0)

# Close the files
histFile_2lep.Close()
#histFile_Zmumu.Close()
histFile_Zee.Close()
#histFile_Ztautau.Close()

# MAKING A STACKED PLOT - ALL MC CONTRIBUTIONS STACKED ON TOP OF EACH OTHER, COMPARED WITH DATA

# Make a canvas
canvasstack = r.TCanvas("canvasstack")

# Make a stacked histogram
hs = r.THStack("hs","Stacked plot")

# Configure and plot the 2lep data
dataHist.SetTitle("Stacked plot of MC contributions compared with data corresponding to invariant mass")
dataHist.GetXaxis().SetTitle("Invariant Mass (MeV)")
dataHist.GetYaxis().SetTitle("Number of entries/bin")
dataHist.SetStats(0)
dataHist.SetLineColor(r.kBlack)
dataHist.SetLineWidth(1)
dataHist.SetMarkerColor(r.kBlack)
dataHist.SetMarkerStyle(21)
dataHist.SetMarkerSize(0.5)
dataHist.Draw("e")

# Add MC contributions to the stacked histogram
mcHist_Zee.SetLineColor(r.kBlue)
mcHist_Zee.SetFillColor(r.kBlue)
hs.Add(mcHist_Zee,"h")
#mcHist_Zmumu.SetLineColor(r.kGreen)
#mcHist_Zmumu.SetFillColor(r.kGreen)
#hs.Add(mcHist_Zmumu,"h")
#mcHist_Ztautau.SetLineColor(r.kRed)
#mcHist_Ztautau.SetFillColor(r.kRed)
#hs.Add(mcHist_Ztautau,"h")

# Draw the stacked plot onto the canvas
hs.Draw("same,hist")

# Draw the data on the same canvas
#dataHist.Draw("e,same")

# Edit the x axis range of both stacked plot and data
hs.GetXaxis().SetRangeUser(0,40e3)
#dataHist.GetXaxis().SetRangeUser(0,120e3)

# Add a legend to the plot
legend = r.TLegend(0.7,0.45,0.9,0.85)
legend.AddEntry(mcHist_Zee,"Zee, MC")
#legend.AddEntry(mcHist_Zmumu,"Zmumu MC")
#legend.AddEntry(mcHist_Ztautau,"Ztautau MC")
legend.AddEntry(dataHist,"2lep Data")
legend.SetLineWidth(0)
legend.Draw("same")

# Plot the canvas
canvasstack.Draw()
canvasstack.SetLogy()

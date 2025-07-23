import ROOT
import sys
import matplotlib.pyplot as plt
import numpy as np
import mplhep
mplhep.set_style("CMS")
import pandas as pd

plt.rcParams["figure.figsize"] = (10,8)

def rebin(n, edges, nbins):
  assert len(n) % nbins == 0
  centers = (edges[:-1] + edges[1:]) / 2
  new_n, new_edges = np.histogram(centers, bins=nbins, range=(edges[0], edges[-1]), weights=n)
  return new_n, new_edges 

poisson_ci = pd.read_csv("poisson_interval_68.csv")
poisson_ci.set_index("N", inplace=True)
poisson_ci = poisson_ci.to_numpy()

def poissonError(n):
  errors = []
  for i in range(len(n)):
    if n[i] > 1000:
      errors.append([np.sqrt(n[i]), np.sqrt(n[i])])
    else:
      errors.append(poisson_ci[int(n[i])])
  return np.array(errors)

def convert(label):
  name, order = label[:-1], label[-1]

  conversion_dict = {
    "exppoly": "ExpPoly",
    "lau": "Laurent",
    "pow": "Power Law",
    "exp": "Exponential",
    "bern": "Bernstein",
    "hmdijet": "Dijet"
  }
  new_name = conversion_dict[name]
  return f"{new_name} ({order})"

def getPlotLabel():
  mx = sys.argv[1].split("mx")[1].split("my")[0]
  my = sys.argv[1].split("my")[1].split("cat")[0]
  cat = sys.argv[1].split("cat")[1].split("_")[0]

  return f"$(m_X, m_Y) = ({mx}, {my})\,GeV$\nCategory {cat}"

f = ROOT.TFile(sys.argv[1])

w = f.Get("multipdf")

datas = [d for d in w.allData()]
assert len(datas) == 1
data = datas[0]

if isinstance(data, ROOT.RooDataSet):
  datahist = data.binnedClone("datahist", "datahist")
else:
  datahist = data

n, edges = datahist.to_numpy()
n = np.array(n)
edges = np.array(edges[0])

#print(n, edges)
n, edges = rebin(n, edges, 300)
#print(n, edges)
centers = (edges[:-1] + edges[1:]) / 2

bin_width = edges[1] - edges[0]
uncert = poissonError(n)
#blinded_region = [115, 135]
blinded_region = [68, 87]
s = (centers < blinded_region[0]) | (centers > blinded_region[1])
s = s & (n > 0)


#plt.errorbar(centers[s], n[s], xerr=bin_width/2, yerr=uncert[s].T, capsize=2, fmt='k.', label="Data")

plt.xlabel(r"$m_{\gamma\gamma}$ [GeV]")
plt.ylabel(f"Events / ( {bin_width:.2g} GeV )")

x = w.var("CMS_hgg_mass")

for pdf in w.allPdfs():
  if "_bkgshape" in pdf.GetName():
    multipdf = pdf

for cat in w.allCats():
  if "pdfindex" in cat.GetName():
    index = cat

for pdf in w.allPdfs():
  if hasattr(pdf, "fixCoefNormalization"):
    pdf.fixCoefNormalization([x])

for i in range(len(index)):
  index.setIndex(i)
  multipdf_val = []
  for c in centers:
    x.setVal(c)
    multipdf_val.append(multipdf.getVal()*sum(n))

  multipdf_val = np.array(multipdf_val)
  multipdf_val *= sum(n) / sum(multipdf_val)
  plt.plot(centers, multipdf_val, label=convert(multipdf.getPdf(i).GetName().split("_")[-1]), linewidth=3)

plt.errorbar(centers[s], n[s], yerr=uncert[s].T, capsize=2, fmt='ko', label="Data")

handles, labels = plt.gca().get_legend_handles_labels()
handles = handles[::-1] # flip
labels = labels[::-1] # flip

#plt.ylim(bottom=0)
#plt.xlim(edges[0], edges[-1])
plt.ylim(top=plt.ylim()[1]*1.2)
plt.text(0.05, 0.95, getPlotLabel(), horizontalalignment='left',
     verticalalignment='top', transform=plt.gca().transAxes, fontsize=20)

mplhep.cms.label(data=True, lumi=sys.argv[2])
plt.legend(handles, labels, ncol=1)

name = sys.argv[1].split("multipdf_")[1].split("_combined")[0]
plt.savefig(f"bkgmodel_pdfs_{name}.pdf")
plt.yscale("log")

plt.ylim(1e-1, 5e4)
plt.savefig(f"bkgmodel_pdfs_{name}_log.pdf")


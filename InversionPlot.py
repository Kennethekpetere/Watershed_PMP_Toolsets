import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt #This is the main plotting library used in python
import pandas as pd #This is a nice libarary for working with data
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import sem



#make plots appear clean
mpl.rcParams['font.size'] = 12
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['figure.titlesize'] = 'medium'
mpl.rcParams['lines.linewidth'] = 2.0 


## Load Datasets

dfP= pd.read_csv('./ImageStat/InversionDoc.csv')
print(dfP)

## ## Declare Array
xarP = dfP.to_xarray()

Duration = xarP['Duration']
NOAA = xarP['NOAA']
IMERG_UNJ = xarP['IMERG_UNJ']
IMERG_AJ1 = xarP['IMERG_AJ1']
IMERG_AJ2 = xarP['IMERG_AJ2']

plt.figure(figsize=(12,6))
plt.plot(Duration, NOAA, linewidth=1.2, linestyle='-', color='red', marker='o', markerfacecolor="black", markersize=2, label = "NOAA Derived PMP") 
plt.plot(Duration, IMERG_UNJ,  linewidth=1.2, linestyle='-', color='blue', marker='o', markerfacecolor="black", markersize=2, label = "Undjusted IMERG PMP") 
# plt.plot(Duration, IMERG_AJ1,  linewidth=1.2, linestyle='-', color='brown', marker='o', markerfacecolor="black", markersize=2, label = "After First IMERG Adjustment")
plt.plot(Duration, IMERG_AJ2,  linewidth=1.2, linestyle='-', color='green', marker='o', markerfacecolor="black", markersize=2, label = "Adjustment IMERG PMP") #After Second IMERG Adjustment
plt.xlabel('Durations (hrs)', fontweight='bold', fontsize=14)
plt.ylabel('PMP (mm)', fontweight='bold', fontsize=14)
# plt.grid(True, alpha=0.2)
plt.title('Inversion in IMERG', fontweight='bold', fontsize=16)
plt.legend(loc=2, fontsize=10)
#plt.xaxis.grid(True)
plt.savefig("Plots/Inversion_IMERG.png")
plt.show()
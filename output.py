import incermental_analysis
import input
import injector
import math
import scipy
import numpy as np
import matplotlib.pyplot as plt
import burnrate as br




xpoints = br.burn_time_array
ypoints = incermental_analysis.mass_flux
plt.plot(xpoints, ypoints)
plt.show()

xpoints = br.burn_time_array
ypoints = incermental_analysis.vol_array
plt.plot(xpoints, ypoints)
plt.show()

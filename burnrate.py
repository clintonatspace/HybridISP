import incermental_analysis
import input
import injector
import math
import scipy
import numpy as np

burn_rate_array=input.a_co*(incermental_analysis.mass_flux**input.n_expo)
#burn_rate_array is in m/s
burn_time_array=(incermental_analysis.burn_incerment_array)/burn_rate_array

#burn_time_array is in sec
burn_a_array=np.delete(incermental_analysis.mass_of_grain_array,(input.data_points-2))
burn_b_array=np.delete(incermental_analysis.mass_of_grain_array,0)
#first value - second value in burn time array is burn c arrary of mass
burn_c_array=(burn_a_array-burn_b_array)

#first value - second value in mass of grain array  is mass c arrary
time_a_array=np.delete(burn_time_array,0)
time_b_array=np.delete(burn_time_array,(input.data_points-2))
time_c_array=time_a_array-time_b_array

mass_flow_rate_fuel_array=burn_c_array/time_c_array
total_mass_flow_rate_array=mass_flow_rate_fuel_array+injector.oxi_mass_flow_rate
max_total_mass_flow=np.max(total_mass_flow_rate_array)

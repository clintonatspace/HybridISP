from array import array
from email.errors import MissingHeaderBodySeparatorDefect
from unittest import result
import numpy as np
import input
import math
import injector
#data_sn=list(range(int(input.data_points)))
sn_data_array =np.arange(1,int(input.data_points),1)
burn_incerment_array=sn_data_array*input.dx
#burning area cal
burn_area_array=((2*math.pi)*((burn_incerment_array)+(input.grain_inner_radius/1000))*(input.grain_length/1000))
vol_a=((input.grain_or**2)-((burn_incerment_array+input.grain_in)**2))
vol_array=vol_a*math.pi*input.grain_l
#mass of the grain 
mass_of_grain_array=vol_array*input.fuel_density
port_radius_evlo_array=burn_incerment_array+input.grain_in
mass_flux=(injector.oxi_mass_flow_rate/(math.pi*((port_radius_evlo_array)**2)))


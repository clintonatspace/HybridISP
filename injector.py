from cmath import sqrt
from math import pi
import input
orifice_area=(((pi/4)*(input.orifice_dia**2))/1000000)
# orifice area in m2
a2=(sqrt(2*input.oxi_density*(input.feed_pressure_pa-input.chamber_pressure_pa)))
oxi_mass_flow_rate=orifice_area*input.cd*a2
#mass_flow _rate in kg/s
injection_velocity=(a2/input.oxi_density)*orifice_area
#injection velocity in m/s
velocity_at_orifice=sqrt(((input.gamma*input.R*input.T)/input.M))
mach_at_orifice=(injection_velocity/velocity_at_orifice)
required_fuel_mass_flow = (a2/input.Of)
# fuel_mass_flow_rate in kg/s 

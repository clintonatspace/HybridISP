from asyncio import constants
import incermental_analysis
import input
import injector
import math
from scipy import constants
import numpy as np
import burnrate as br



#Pressure at Throat of nozzle
nozzle_throat_pressure=(input.nozzle_design_pressure*(((((1+(input.gamma-1)/2))**((-input.gamma)/(input.gamma-1))))))
#in pa
nozzle_throat_temp=input.chamber_tem/(1+(((input.gamma-1/2))))
# in k
a=(br.max_total_mass_flow/(nozzle_throat_pressure))    
nozzle_throat_area =  a *math.sqrt((input.R*nozzle_throat_temp)/(input.M*input.gamma))
                      
nozzle_throat_dia=(math.sqrt((4 * nozzle_throat_area)/(math.pi)))
#in m
nozzle_throat_dia_mm=nozzle_throat_dia*1000
#in mm
#mach_number_exits

a=(2/(input.gamma-1))
b=(input.chamber_pressure_pa/input.amb_pressure_pa)
c=(input.gamma-1)/input.gamma
nm2=a*((b**c) -1)
exit_mach=math.sqrt(nm2)
# exit area
e=(nozzle_throat_area/exit_mach)
f=(((input.gamma-1)/2)*(nm2)+1)
g=((input.gamma+1)/2)
h=((input.gamma+1)/(2*(input.gamma-1)))
exit_area=(e*((f/g)**h))
#in m2
exit_dia=math.sqrt((4*exit_area)/math.pi)
#in m
expansion_ratio=exit_area/nozzle_throat_area

nozzle_con_length=math.sqrt((((math.pi/4)*(input.nozzle_inlet_dia**2))/math.pi)*((1/math.tan(math.radians(input.nozzle_con_angle)))))

nozzle_div_length=math.sqrt((((exit_area))/math.pi)*((1/math.tan(math.radians(input.nozzle_con_angle)))))
print(nozzle_div_length)


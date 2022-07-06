from tkinter import W
from scipy import constants


print("PRESSURE INPUTS")
tank_pressure=float(1500)
tank_pressure_pa=(constants.psi)*tank_pressure
feed_pressure =float(500)
feed_pressure_pa=(constants.psi)*feed_pressure
chamber_pressure =float(200)
chamber_pressure_pa=(constants.psi)*chamber_pressure
amb_pressure=float(14.6959)
amb_pressure_pa=amb_pressure*(constants.psi)
print(amb_pressure_pa)
print ("PROPELLANT INPUTS")
fuel=("ABS")
fuel_density=float(998)
oxi=("OXYGEN")
oxi_density=float(1.331)
Of=float(2.5)   
a_co=0.00016
n_expo=0.31 
print("INJECTOR INPUTS")
cd=float(0.8)
orifice_dia=(float(5))
print("THERMODYNAMICAL INPUT")
gamma=float(1.1266)
R =float((8314.46))
M=float(26.01)
T=float(3483.81)   
print("GRAIN INPUT")
grain_outer_radius=float(33.1)
grain_or=grain_outer_radius/1000
grain_inner_radius=float(20)
grain_in=grain_inner_radius/1000
webthickness=((grain_outer_radius-grain_inner_radius)/1000)
grain_length=float(300)
grain_l=grain_length/1000
grain_outer_diameter=grain_outer_radius*2
grain_inner_diameter =grain_inner_radius*2
data_points=float(100)
dx=webthickness/data_points
#NOZZLE 
nozzle_design_pressure=(150)*constants.psi
nozzle_inlet_dia=(23/1000)
nozzle_con_angle=30
nozzle_div_angle=12
#in psi
chamber_tem=3529
#in k
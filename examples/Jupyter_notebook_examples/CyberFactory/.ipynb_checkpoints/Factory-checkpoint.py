import os
import sys 
sys.path.insert(0, os.path.abspath('..\..\..\..\sysmpy'))  
from sysmpy import * 
from sysmpy.gui.mxgraph.tornado_gui_server import * 

#=== Factory Code ===

p = Process('Process')
PS, IF, HT, HR, SP, CR, AL, PL, FR, SL, IL = p.And('Production Start', 'Induction Furnace', 'Heater', 'Hot Rolling Mill', 'Scalper', 
                    'Cold Rolling Mill', 'Annealing Line', 'Pickling Line', 'Finish Rolling Mill','Slitting Line', 'Inspection Line')

IF.Property('Speed', range=Normal(300, 10))
IF.Property('Temperature', range=Normal(1000, 10))
HT.Property('Speed', range=Normal(300, 10))
HT.Property('Temperature', range=Normal(1200, 10))

# Hot Rolling Mill #######################################
HR.Property('RG', range=Normal(10, 0.1))
HR.Property('RF', range=Normal(400, 10))

SP.Property('Gap', range=Normal(900, 10))
CR.Property('RG', range=Normal(5, 0.1))
CR.Property('RF', range=Normal(200, 10))
AL.Property('Speed', range=Normal(300, 10))
AL.Property('Temperature', range=Normal(90, 10))
PL.Property('Speed', range=Normal(300, 10))
FR.Property('RG', range=Normal(2, 0.1))
FR.Property('RF', range=Normal(50, 3))
SL.Property('Speed', range=Normal(300, 10)) 
IL.Property('Speed', range=Normal(300, 10)) 


PS_a = PS.Action('Supplying')
IF_a = IF.Action('Casting and Cutting')
HT_a = HT.Action('Heating')

# Hot Rolling #######################################
HR_a = HR.Action('Hot Rolling')

SP_a = SP.Action('Scalping')
CR_a = CR.Action('Cold Rolling')
AL_a = AL.Action('Annealing')
PL_a = PL.Action('Pickling')
FR_a = FR.Action('Finish Rolling')
SL_a = SL.Action('Slitting')
IL_a = IL.Action('Inspection')

CTH = Item('Copper Cathode')
CTH.Property('Thickness', range=Normal(900, 10))
CTH.Property('Width', range=Normal(1100, 10))
CTH.Property('Length', range=Normal(1000, 10))
CTH.Property('Temperature', range=Normal(25, 5))
SLB = Item('Slab')
SLB.Property('Thickness', range=Normal(250, 10))
SLB.Property('Width', range=Normal(650, 10))
SLB.Property('Length', range=Normal(6000, 10))
SLB.Property('Temperature', range=Normal(600, 30))

# Heated Slab #######################################
HSL = Item('Heated Slab')
HSL.Property('Thickness', range=Normal(250, 10))
HSL.Property('Width', range=Normal(650, 10))
HSL.Property('Length', range=Normal(6000, 10))
HSL.Property('Temperature', range=Normal(1200, 30))
HSL.Property('Goal_Thickness', range=Normal(10, 5))
 
# Hot Strip Coil #######################################
HSC = Item('Hot Strip Coil')
HSC.Property('Thickness', range=Normal(10, 5))
HSC.Property('Width', range=Normal(600, 5))
HSC.Property('Length', range=Normal(150000, 5))
HSC.Property('Temperature', range=Normal(900, 5))

SSC = Item('Scalped Strip Coil')
SSC.Property('Thickness', range=Normal(9, 1))
SSC.Property('Width', range=Normal(600, 1))
SSC.Property('Length', range=Normal(166666, 1))
SSC.Property('Temperature', range=Normal(50, 10))
CSC = Item('Cold Strip Coil')
CSC.Property('Thickness', range=Normal(5, 1))
CSC.Property('Width', range=Normal(600, 1))
CSC.Property('Length', range=Normal(166770, 1))
CSC.Property('Temperature', range=Normal(30, 10))
ASC = Item('Annealed Strip Coil')
ASC.Property('Thickness', range=Normal(5, 0.1))
ASC.Property('Width', range=Normal(600, 0.1))
ASC.Property('Length', range=Normal(166770, 0.1))
ASC.Property('Temperature', range=Normal(100, 10))
LSC = Item('Cleaned Strip Coil')
LSC.Property('Thickness', range=Normal(5, 0.1))
LSC.Property('Width', range=Normal(600, 0.1))
LSC.Property('Length', range=Normal(166770, 0.1))
LSC.Property('Temperature', range=Normal(100, 5))
FSC = Item('Finished Strip Coil')
FSC.Property('Thickness', range=Normal(2, 0.1))
FSC.Property('Width', range=Normal(600, 0.1))
FSC.Property('Length', range=Normal(168880, 0.1))
FSC.Property('Temperature', range=Normal(25, 1))
TSC = Item('Slitting Strip Coil')
TSC.Property('Thickness', range=Normal(2, 0.1))
TSC.Property('Width', range=Normal(200, 0.1))
TSC.Property('Length', range=Normal(168880, 0.1))
TSC.Property('Temperature', range=Normal(25, 1))
NSC = Item('Final Strip Coil')
NSC.Property('Quality', range=Normal(90, 1)) 

PS_a.sends(CTH)
IF_a.sends(SLB)
HT_a.sends(HSL)
HR_a.sends(HSC)
SP_a.sends(SSC)
CR_a.sends(CSC)
AL_a.sends(ASC)
PL_a.sends(LSC)
FR_a.sends(FSC)
SL_a.sends(TSC)
IL_a.sends(NSC)

IF_a.triggered(CTH) 
HT_a.triggered(SLB)
HR_a.triggered(HSL)
SP_a.triggered(HSC)
CR_a.triggered(SSC)
AL_a.triggered(CSC)
PL_a.triggered(ASC)
FR_a.triggered(LSC)
SL_a.triggered(FSC)
IL_a.triggered(TSC) 

# Function Script #######################################
def rm_function(io):
	Thickness_1 = io.get("Heated Slab.Thickness")
	Width_1 = io.get("Heated Slab.Width")
	Length_1 = io.get("Heated Slab.Length")
	Temperature_1 = io.get("Heated Slab.Temperature")
	Goal_Thickness_1 = io.get("Heated Slab.Goal_Thickness")

	Thickness_2 = io.get("Hot Strip Coil.Thickness")
	Width_2 = io.get("Hot Strip Coil.Width")
	Length_2 = io.get("Hot Strip Coil.Length")
	Temperature_2 = io.get("Hot Strip Coil.Temperature")

	# Use AGC-AI to predict the roll gab
	from examples.Jupyter_notebook_examples.CyberFactory.AGC_AI import agc_ai
	roll_gab = agc_ai.run(Thickness_1.value, Goal_Thickness_1.value)
	Thickness_2.value = roll_gab
	Width_2.value = Width_1.value
	Length_2.value = Length_1.value
	Temperature_2.value = Temperature_1.value
# 	print(roll_gab, Width_2.value)

# Hot Rolling
HR_a.func(rm_function)

# 2 run simulation
# asyncio.run(p.sim(print_out=True))

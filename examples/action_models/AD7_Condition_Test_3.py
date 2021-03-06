from sysmpy import *
import asyncio

"""
                            +---------------+
                            |               |
                            |     start     |
                            |               |
                            +---------------+
                                    | process
                                    |
                            +---------------+
                            |               |
                            |   Condition1  |
                            |               |
                            +---------------+
                                |       |                                    
                        +--------       --------+
                        | process 1             | process 2
                        |   90%                 |  10%           
                +---------------+       +---------------+   
                |               |       |               |   
                |    Action1    |       |    Action2    |   
                |               |       |               |   
                +---------------+       +---------------+   
                        |                       |           
                        |                       |                        
                        +---------(OR)----------+
                                    |
                            +---------------+
                            |               |
                            |      End      |
                            |               |
                            +---------------+
"""
print('AD7_Condition_Test_3')

###############################################
# 1 Define a model
p = Process("process0")

p_con = p.Condition("Condition 1")

p1 = p_con.Process("process 1")
p2 = p_con.Process("process 2")
p_act1 = p1.Action("Action 1")
p_act2 = p2.Action("Action 2")

# Condition Script ######################################
def function1(io):
    import random
    # outputs
    o1, o2 = io.get('process 1'), io.get('process 2')

    if random.random() < 0.9:
        return o1
    else:
        return o2

# Script end ##################################

p_con.func(function1)

###############################################
# 2 Run a simulation
asyncio.run(p.sim(print_out=True))
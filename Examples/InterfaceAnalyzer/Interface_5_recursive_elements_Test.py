from entity import *
import asyncio

""" 
                +---------------+
                |               |
      +-------->|    Action1    |---------+
      |         |               |         | 
      |         +---------------+         | 
   (Item1)              |              (Item1)
      |                 |                 |
      |         +---------------+         |
      |         |               |         |
      +---------|    Action2    |<--------+
                |               |        
                +---------------+  
"""
###############################################
# 1 Define actions
p = Process("process 1")
act1 = p.Action("Action1")
act2 = p.Action("Action2")

i1 = Item("Item1")
act1.sends(i1)
act2.receives(i1)

act2.sends(i1)
act1.receives(i1)

###############################################
# 2 run interface analyzer
p.evaluate_interfaces()



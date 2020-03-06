import asyncio
"""
                            +---------------+        /   +---------------+
                            |               |       /    |               |
                            |     start     |      /     |     start     |
                            |               |     /      |               |
                            +---------------+    /       +---------------+
                                    | process1  /                | process1.1
                                    |          /                 | 
                            +---------------+            +---------------+    
                            |               |            |               |    
                            |    Action1    |            |   Action1.1   |    
                            |             |||            |               |    
                            +---------------+            +---------------+    
                                    |          \                 |          
                                    |           \                |
                            +---------------+    \       +---------------+
                            |               |     \      |               |
                            |    Action2    |      \     |      End      |
                            |               |       \    |               |
                            +---------------+        \   +---------------+
                                    |
                                    |
                            +---------------+
                            |               |
                            |      End      |
                            |               |
                            +---------------+ 
"""
from examples.ActionModels import AD9_SubActions_Test_2 as super

###############################################
# 1 Define actions
p1_1 = super.act1.Process("process1.1")
act1_1 = p1_1.Action("Action1.1")

###############################################
# 2 run simulation
asyncio.run(super.p.sim())


from sysmpy import *

"""
    LIFECYCLE MODELING LANGUAGE (LML)
    Document URL: http://www.lifecyclemodeling.org/spec/1.1
    December 1, 2015
"""
#======================================================================================#
#                                                                                      #
#                                  LML Entities                                        #
#                                                                                      #
#======================================================================================#
#=======================================================================#
#                                 LML Artifact                          #
#=======================================================================#
class Artifact(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Asset                             #
#=======================================================================#
class Asset(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Statement                         #
#=======================================================================#
class Statement(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Characteristic                    #
#=======================================================================#
class Characteristic(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Connection                        #
#=======================================================================#
class Connection(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Conduit                           #
#=======================================================================#
class Conduit(Connection):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Cost                              #
#=======================================================================#
class Cost(StaticEntity):
    def __init__(self, name):
        pass
#=======================================================================#
#                                 LML Decision                          #
#=======================================================================#
class Decision(Action):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Input/Output                      #
#=======================================================================#
class Input_Output(Item):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Location                          #
#=======================================================================#
class Location(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Logical                           #
#=======================================================================#
class Logical(Connection):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Measure                           #
#=======================================================================#
class Measure(Characteristic):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Orbital                           #
#=======================================================================#
class Orbital(Location):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Physical                          #
#=======================================================================#
class Physical(Location):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Requirement                       #
#=======================================================================#
class Requirement(Statement):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Resource                          #
#=======================================================================#
class Resource(Asset):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Risk                              #
#=======================================================================#
class Risk(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Time                              #
#=======================================================================#
class Time(StaticEntity):
    def __init__(self, name):
        pass

#=======================================================================#
#                                 LML Virtual                           #
#=======================================================================#
class Virtual(Location):
    def __init__(self, name):
        pass


#======================================================================================#
#                                                                                      #
#                                     LML Relationships                                #
#                                                                                      #
#======================================================================================#
#=======================================================================#
#                            LML Alternative Of                         #
#=======================================================================#
class AlternativeOf(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Causes                                 #
#=======================================================================#
class Causes(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Consumed By                            #
#=======================================================================#
class ConsumedBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Decided By                             #
#=======================================================================#
class DecidedBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Decomposed By                          #
#=======================================================================#
class DecomposedBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Decomposes                             #
#=======================================================================#
class Decomposes(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Enables                                #
#=======================================================================#
class Enables(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Incurs                                 #
#=======================================================================#
class Incurs(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Located At                             #
#=======================================================================#
class LocatedAt(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Locates                                #
#=======================================================================#
class Locates(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Mitigates                              #
#=======================================================================#
class Mitigates(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Occurred By                            #
#=======================================================================#
class OccurredBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Produced By                            #
#=======================================================================#
class ProducedBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Related To                             #
#=======================================================================#
class RelatedTo(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Relates                               #
#=======================================================================#
class Relates(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Resolves                               #
#=======================================================================#
class Resolves(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Results In                             #
#=======================================================================#
class ResultsIn(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Seized By                              #
#=======================================================================#
class SeizedBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Sourced By                             #
#=======================================================================#
class SourcedBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Specified By                           #
#=======================================================================#
class SpecifiedBy(Relationship):
    def __init__(self, name):
        pass

#=======================================================================#
#                            LML Traced To                              #
#=======================================================================#
class TracedTo(Relationship):
    def __init__(self, name):
        pass


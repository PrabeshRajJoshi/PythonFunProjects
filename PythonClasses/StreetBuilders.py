# Python module containing creator functions and relevant classes to build objects within a street
import numpy as np

class StreetObjectCategories:
    '''
    class containing information on the various categories of objects found in a street 
    '''
    def __init__(self):
        self._Buildings = ["House", "School", "Shopping Mall", "Office"]
        self._NonBulidings = ["Park", "Empty", "Parking Lot", "Farm Land"]
    
    def AddBuilding(self, CategoryName):
        if CategoryName not in self._Buildings:
            self._Buildings.append(CategoryName)

    def AddNonBuilding(self, CategoryName):
        if CategoryName not in self._NonBulidings:
            self._NonBulidings.append(CategoryName)

    def GetBuildings(self):
        return self._Buildings

    def GetNonBuildings(self):
        return self._NonBulidings
    
    def GetAll(self):
        return self._Buildings + self._NonBulidings
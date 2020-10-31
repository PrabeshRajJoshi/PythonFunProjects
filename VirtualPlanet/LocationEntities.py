# Python module containing classes for various location entities
#   Location heirarchy: Planet -> ... -> Country -> ... -> houses/parks -> apartments -> people
'''
Street as a class with name, houses, and other details.
House as a class with house number and apartments.
Apartment as a class with apartment number and number of residents.
Use methods to get total houses in the street, total apartments in a house, ...
'''

import numpy as np

from StreetBuilders import StreetObjectCategories

# Planet: Class for a planet entity containing SuperNations
class Planet:
    def __init__(self, Name=None, Type=None):
        self.Name = Name
        self.Type = Type
        # Initialize a list of SuperNation objects
        self.SuperNationList = []
    
    def SpawnSuperNations(self):
        pass
    
    def GetStreets(self):
        '''
        Method to receive a list of streets
        '''
        StreetsInPlanet = []
        # Create a simple list of street objects in all the cities within
        for supernation in self.SuperNationList:
            StreetsInPlanet.extend(supernation.GetStreets())
        return StreetsInPlanet
    
    def GetBuildings(self):
        '''
        Method to receive a list of buildings
        '''
        BuildingsInPlanet = []
        # Use the list of streets to get the buildings
        for street in self.GetStreets():
            BuildingsInPlanet.extend(street.GetBuildings())
        return BuildingsInPlanet

    def GetApartments(self):
        '''
        Method to receive a list of apartments
        '''
        ApartmentsInPlanet = []
        # Use the list of buildings to get the apartments
        for building in self.GetBuildings():
            ApartmentsInPlanet.extend(building.GetApartments())
        return ApartmentsInPlanet

# SuperNation: Class for international entities containing Nations. 
#   e.g. Continents, United Nations, European Union, African Union, SAARC, Oceans, Seas,...
class SuperNation:
    def __init__(self, Name=None, Type=None):
        self.Name = Name
        self.Type = Type
        # Initialize a list of Nation objects
        self.NationList = []
    
    def SpawnNations(self):
        pass

    def GetStreets(self):
        StreetsInSuperNation = []
        # Create a simple list of street objects in all the cities within
        for nation in self.NationList:
            StreetsInSuperNation.extend(nation.GetStreets())
        return StreetsInSuperNation
    
    def GetBuildings(self):
        '''
        Method to receive a list of buildings
        '''
        BuildingsInSuperNation = []
        for street in self.GetStreets():
            BuildingsInSuperNation.extend(street.GetBuildings())
        return BuildingsInSuperNation
    
    def GetApartments(self):
        '''
        Method to receive a list of apartments
        '''
        ApartmentsInSuperNation = []
        for building in self.GetBuildings():
            ApartmentsInSuperNation.extend(building.GetApartments())
        return ApartmentsInSuperNation

# Nation: Class for a national level entities containing States
class Nation:
    def __init__(self, Name=None, Type=None):
        self.Name = Name
        self.Type = Type
        # Initialize a list of State objects
        self.StateList = []
    
    def SpawnStates(self):
        pass

    def GetStreets(self):
        StreetsInNation = []
        # Create a simple list of street objects in all the cities within
        for state in self.StateList:
            StreetsInNation.extend(state.GetStreets())
        return StreetsInNation

    def GetBuildings(self):
        '''
        Method to receive a list of buildings
        '''
        BuildingsInNation = []
        for street in self.GetStreets():
            BuildingsInNation.extend(street.GetBuildings())
        return BuildingsInNation
    
    def GetApartments(self):
        '''
        Method to receive a list of apartments in a city
        '''
        ApartmentsInNation = []
        for building in self.GetBuildings():
            ApartmentsInNation.extend(building.GetApartments())
        return ApartmentsInNation

# State: Class for a sub-national level entities (e.g. state/district/zone) containing Cities
class State:
    def __init__(self, Name=None, Type=None):
        self.Name = Name
        self.Type = Type
        # Initialize a list of City objects
        self.CityList = []
    
    def SpawnCities(self):
        pass
    
    def GetStreets(self):
        StreetsInState = []
        # Create a simple list of street objects in all the cities within
        for city in self.CityList:
            StreetsInState.extend(city.GetStreets())
        return StreetsInState

    def GetBuildings(self):
        '''
        Method to receive a list of buildings
        '''
        BuildingsInState = []
        for street in self.GetStreets():
            BuildingsInState.extend(street.GetBuildings())
        return BuildingsInState
    
    def GetApartments(self):
        '''
        Method to receive a list of apartments in a city
        '''
        ApartmentsInState = []
        for building in self.GetBuildings():
            ApartmentsInState.extend(building.GetApartments())
        return ApartmentsInState

# City: Class for a city/town/village containing Streets
class City:
    def __init__(self, Name=None, Type=None):
        self.Name = Name
        self.Type = Type
        # Initialize a list of Street objects
        self.StreetList = []
    
    def SpawnStreets(self):
        pass
    
    def GetStreets(self):
        return self.StreetList
    
    def GetBuildings(self):
        '''
        Method to receive a list of buildings
        '''
        BuildingsInCity = []
        for street in self.GetStreets():
            BuildingsInCity.extend(street.GetBuildings())
        return BuildingsInCity
    
    def GetApartments(self):
        '''
        Method to receive a list of apartments in a city
        '''
        ApartmentsInCity = []
        for building in self.GetBuildings():
            ApartmentsInCity.extend(building.GetApartments())
        return ApartmentsInCity


# Street: Class for a street containing 
#   - buildings(houses, businesses, schools,...) and 
#   - spaces(parks, parking lots, empty land, ...)
class Street:
    # Default class attributes ("is a" components), that can be inherited from parent classes
    # instance attributes ("has a" components), unique for each Street instance
    def __init__(self, Name=None, Type=None, Location=None, State=None, Country=None, Capacity=None):
        self.Name = Name
        self.Type = Type
        self.Location = Location
        self.State = State
        self.Country = Country

        # Define minimum and maximum objects allowed in a street
        StreetCapacityMin = 5
        StreetCapacityMax = 20
        self.Capacity = np.random.randint(StreetCapacityMin, StreetCapacityMax)

        # Define a list of objects for the Street ("has a" component)
        self.StreetObjects = []
    
    def SpawnStreetObjects(self,categories_list):
        '''
        Method to create a list of objects in a Street: \n
        \t use random elements from categories_list, and
        \t ensure total objects = Street.Capacity
        '''
        for id in range(self.Capacity):
            # choose a random element from categories_list
            StreetObjectID = np.random.randint(0, len(categories_list))
            category = categories_list[StreetObjectID]
            # add it to the list of objects in the street
            self.StreetObjects.append(StreetObject(category, id+1))
    
    def AddBuildingObject(self, Type=None, NumApartments=None, NumResidents=None):
        '''
        Method to add a new Building Object to the Street at some later point \n
        \t NumApartments = maximum number of apartments allowed, and
        \t NumResidents = maximum number of residents per apartment
        '''
        print("Adding new StreetObject to %s..."%self.Name)
        NewObject = StreetObject(Type, len(self.StreetObjects)+1)
        NewObject.SpawnApartments(NumApartments)
        if NewObject.ApartmentList:
            for MyApartment in NewObject.ApartmentList:
                MyApartment.SpawnResidents(NumResidents)
        
        self.StreetObjects.append(NewObject)
        # self.print_info()
    
    def AddNonBuildingObject(self, Type=None):
        '''
        Method to add a new Non-Building Object to the Street at some later point
        '''
        print("Adding new StreetObject to %s..."%self.Name)
        NewObject = StreetObject(Type, len(self.StreetObjects)+1)
        self.StreetObjects.append(NewObject)
        # self.print_info()

    def GetBuildings(self):
        '''
        Method to receive a list of Building objects in a street.
        '''
        BuildingsInStreet = []

        Categories = StreetObjectCategories()
        for item in self.StreetObjects:
            # Check if the item is a Building
            if item.Category in Categories.GetBuildings():
                BuildingsInStreet.append(item)
        return BuildingsInStreet

    def GetApartments(self):
        '''
        Method to receive a list of apartments in a street
        '''
        ApartmentsInStreet = []
        for item in self.GetBuildings():
            ApartmentsInStreet.extend(item.GetApartments())
        return ApartmentsInStreet

    
    def print_info(self):
        '''
        Method to print some info about the Street object
        '''
        print("%s is a %s street with %i Objects."
              % (self.Name, self.Type, len(self.StreetObjects)))


# StreetObject: Class for an object in a street
class StreetObject:    
    # instance attributes
    def __init__(self, CategoryName, ObjectNumber):
        # Object category, e.g. House, School, Shopping Mall, Office, ...
        self.Category = CategoryName
        # Number assigned to the object in the street
        self.Number = ObjectNumber

        # initialize number of apartments in a building object
        self.NumApartments = 0
        # define a list of apartments in a building object
        self.ApartmentList = []
    
    def SpawnApartments(self, NumApartments):
        '''
        Method to create apartments (up to NumApartments) in a StreetObject if it is a building.
        '''
        # check if the StreetObject is a building
        Categories = StreetObjectCategories()
        if self.Category in Categories.GetBuildings():
            self.NumApartments = NumApartments
            # Create a list of Apartment objects
            self.ApartmentList = [Apartment(val+1) for val in range(self.NumApartments)]
            # print("Created %i Apartment objects in the building."%NumApartments)
        # else:
            # print("This building category does not support Apartments.")

    def GetApartments(self):
        return self.ApartmentList
    
    def print_info(self):
        '''
        Method to print some information about an instance of the class StreetObject
        '''
        print("It is a %s located at number %i in the Street." %(self.Category,self.Number))
        if self.ApartmentList:
            print("It contains %i Apartment objects."%self.NumApartments)



# Apartment: Class for apartments/compartments in a building
class Apartment:
    # instance attributes
    def __init__(self, AptNumber=None, Capacity=None):
        # Number assigned to the apartment in a building
        self.Number = AptNumber
        self.Capacity = Capacity
        # Define the number of residents in the apartment
        self.NumResidents = 0
        self.ResidentsList = []
        self.NumRooms = 0
        
    def SpawnResidents(self,NumResidents):
        '''
        Method to initialize residents in an apartment.
        '''
        self.NumResidents = NumResidents
        self.ResidentsList = [Resident(Number=val+1) for val in range(NumResidents)]
    
    def CreateRooms(self,NumRooms):
        '''
        Method to initialize rooms in an apartment.
        '''
        self.NumRooms = NumRooms
        self.RoomsList = [Room(Number=val+1) for val in range(NumRooms)]

    def print_info(self):
        print("Apartment %i contains %i residents" %
              (self.Number, self.NumResidents))

# Room: Class for room of an apartment/house/building
class Room:
    def __init__(self,Number=None,Type=None):
        self.Number = Number
        self.Type = Type

# Resident: Class for resident of an apartment/house/building
class Resident:
    #instance attributes
    def __init__(self,Number=None,Name=None,Age=None,Gender=None):
        self.Number = Number
        self.Name = Name
        self.Age = Age
        self.Gender = Gender


# Code to get intuition about classes

'''
Scenario: set up appropriate classes for
    Planet -> ... -> Country -> ... -> houses/parks -> apartments -> people
Goal: Given the details of an apartment, determine if this apartment is available in a given planet/country/....

Street as a class with name, houses, and other details.
House as a class with house number and apartments.
Apartment as a class with apartment number and number of residents.
Use methods to get total houses in the street, total apartments in a house, ...
'''
## for some number operations
import numpy as np
#np.random.seed(1)

# Class for planet
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
        # Create a simple list of street objects in all the cities
        for supernation in self.SuperNationList:
            StreetsInPlanet.extend(supernation.GetStreets())
        return StreetsInPlanet
    
    def GetBuildings(self):
        '''
        Method to receive a list of buildings
        '''
        BuildingsInPlanet = []
        for street in self.GetStreets():
            BuildingsInPlanet.extend(street.GetBuildings())
        return BuildingsInPlanet

    def GetApartments(self):
        '''
        Method to receive a list of apartments
        '''
        ApartmentsInPlanet = []
        for building in self.GetBuildings():
            ApartmentsInPlanet.extend(building.GetApartments())
        return ApartmentsInPlanet

# Class for international entities. 
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
        # Create a simple list of street objects in all the cities
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

# Class for a national level entities containing states, e.g. country/nation
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
        # Create a simple list of street objects in all the cities
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

# Class for a sub-national level entities containing cities, e.g. state/district/zone
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
        # Create a simple list of street objects in all the cities
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

# Class for a city/town/village containing streets
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


# Class for street containing buildings(houses, businesses, schools,...) and spaces(parks, parking lots, empty land, ...)
class Street:
    # Default class attributes ("is a" components), that can be inherited from parent classes
    # instance attributes ("has a" components), unique for each Street instance
    def __init__(self, Name=None, Type=None, Location=None, State=None, Country=None):
        self.Name = Name
        self.Type = Type
        self.Location = Location
        self.State = State
        self.Country = Country

        # Define a list of objects for the Street ("has a" component)
        self.StreetObjects = []
    
    def SpawnStreetObjects(self,StreetObjectCategories, StreetCapacity):
        '''
        Method to create a list of objects in a Street using: \n
        \t random elements from StreetObjectCategories, and
        \t total objects = StreetCapacity.
        '''
        for id in range(StreetCapacity):
            # choose a random element from StreetObjectCategories
            StreetObjectID = np.random.randint(0, len(StreetObjectCategories))
            StreetObjectCategory = StreetObjectCategories[StreetObjectID]
            # add it to the list of objects in the street
            self.StreetObjects.append(StreetObject(StreetObjectCategory, id+1))
    
    def AddBuildingObject(self, Type=None, NumApartments=None, NumResidents=None):
        '''
        Method to add a new Building Object to the Street at some later point
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
        for item in self.StreetObjects:
            if item.Category in BuildingCategories:
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


# Class for an object in a street
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
        Method to create apartments (up to NumApartments)in a StreetObject if it is a building.
        '''
        # use global variable BuildingCategories to check if the StreetObject is a building
        if self.Category in BuildingCategories:
            self.NumApartments = NumApartments
            # Create a list of Apartment objects with random population/capacity
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



# Class for apartments/compartments in a building
class Apartment:
    # instance attributes
    def __init__(self, Number):
        # Number assigned to the apartment in a building
        self.Number = Number
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

# Class for resident of an apartment/house/building
class Resident:
    #instance attributes
    def __init__(self,Number=None,Name=None,Age=None,Gender=None):
        self.Number = Number
        self.Name = Name
        self.Age = Age
        self.Gender = Gender

# Class for room of an apartment/house/building
class Room:
    def __init__(self,Number=None,Type=None):
        self.Number = Number
        self.Type = Type


def SearchInStreet(StreetContainer,AptNumber=None,AptResidents=None):
    '''
    Function to search for a certain apartment ...
    \t StreetContainer : any object with GetStreets() method
    \t AptNumber       : apartment number to search for
    \t AptResidents    : number of residents in the apartment
    '''
    for street in StreetContainer.GetStreets():
        found_in_houses = []
        for house in street.StreetObjects:
            if house.NumApartments >= AptNumber:
                for apt in house.ApartmentList:
                    if apt.Number==AptNumber and apt.NumResidents == AptResidents:
                        found_in_houses.append(house.Number)

        if not found_in_houses:
            print("Description not matched in %s."%street.Name)
        else:
            print("Description matched in following houses in %s."%street.Name)
            print(found_in_houses)


# Create a planet
Earth = Planet(Name="Earth",Type="Habitable")
# Create a supernation entity
Europe = SuperNation(Name="Europe", Type="Continent")
Pacific = SuperNation(Name="Pacific", Type="Ocean")
# Create a nation entity
Germany = Nation(Name="Germany",Type="Country")
# Create a sub-national entity
NorthRheinWestf = State(Name="NRW", Type="State")
BerlinState = State(Name="Berlin", Type="State")
# Create a city entity
Dusseldorf = City(Name="Duesseldorf", Type="City")
Cologne = City(Name="Cologne",Type="City")
Berlin = City(Name="Berlin", Type="CapitalCity")
# A special type of city containing moving Aircraft Carriers of each nation
USAirCarriers = City(Name="USAirCarriers", Type="Special")

# Create a street entity
Glockenstrasse = Street(Name="Glockenstrasse", Type="City")
Merheimerstrasse = Street(Name="Merheimerstrasse", Type="City")
FrankfurterAllee = Street(Name="Frankfurter Allee", Type="City")
USAirCarrier1 = Street(Name="USAirCarrier1", Type="Ship")

# Begin to build cities with streets
Dusseldorf.StreetList.append(Glockenstrasse)
Cologne.StreetList.append(Merheimerstrasse)
Berlin.StreetList.append(FrankfurterAllee)
USAirCarriers.StreetList.append(USAirCarrier1)

# Build states
NorthRheinWestf.CityList.extend((Dusseldorf,Cologne))
BerlinState.CityList.append(Berlin)

# Build nation
Germany.StateList.extend((NorthRheinWestf,BerlinState))

# Build supernation
Europe.NationList.append(Germany)
Pacific.NationList.append(USAirCarriers)

# Build planet
Earth.SuperNationList.extend((Europe,Pacific))


# Set up categories of objects to include in the street
BuildingCategories = ["House", "School", "Shopping Mall", "Office"]
OtherCategories = ["Park", "Empty", "Parking Lot", "Farm Land"]
StreetObjectCategoryList = BuildingCategories + OtherCategories

# Define minimum and maximum objects allowed in a street
StreetCapacityMin = 5
StreetCapacityMax = 20
# Define minimum and maximum apartments allowed in a building
BuildingCapacityMin = 1
BuildingCapacityMax = 30
#Define minimum and maximum residents in an apartment
ApartmentCapacityMin = 1
ApartmentCapacityMax = 6

def CreateStreetObjects(StreetContainer):
    '''
    Function to create random StreetObject in all streets found in StreetContainer
    '''
    StreetList = StreetContainer.GetStreets()
    print("Creating street objects in %i streets of %s ..."%(len(StreetList),StreetContainer.Name))

    for street in StreetList:
        street.SpawnStreetObjects(StreetObjectCategoryList, 
                                np.random.randint(StreetCapacityMin, StreetCapacityMax))
        street.print_info()

def CreateApartments(BuildingsContainer):
    '''
    Function to create random Apartments in all buildings found in BuildingsContainer
    '''
    BuildingsList = BuildingsContainer.GetBuildings()
    print("Creating apartment objects in %i buildings in %s ..."%(len(BuildingsList),BuildingsContainer.Name))
    # Create apartments in buildings
    for building in BuildingsList:
        building.SpawnApartments(np.random.randint(BuildingCapacityMin, BuildingCapacityMax))

def CreateResidents(ApartmentsContainer):
    '''
    Function to create random Residents in all apartments found in ApartmentsContainer
    '''
    ApartmentsList = ApartmentsContainer.GetApartments()
    print("Populating %i apartments in %s ..."%(len(ApartmentsList),ApartmentsContainer.Name))
    # Create residents in apartments
    for apartment in ApartmentsList:
        apartment.SpawnResidents(np.random.randint(ApartmentCapacityMin, ApartmentCapacityMax))

# Create objects in the streets
CreateStreetObjects(Earth)
# Create apartments in the buildings
CreateApartments(Earth)
# Create residents in the apartments
CreateResidents(Earth)
# Add new StreetObjects to a Street
Glockenstrasse.AddNonBuildingObject(Type="Empty")
Merheimerstrasse.AddBuildingObject(Type="House",NumApartments=5,NumResidents=2)

# StreetList = Earth.GetStreets()
# print("List of all the streets on Earth:")
# print([street.Name for street in StreetList])
# # Create objects in the streets
# for MyStreet in StreetList:
#     MyStreet.CreateObjects(StreetObjectCategoryList,np.random.randint(StreetCapacityMin,StreetCapacityMax))
#     MyStreet.print_info()
#     # Create apartments in buildings
#     for MyStreetObject in MyStreet.StreetObjects:
#         MyStreetObject.CreateApartments(np.random.randint(BuildingCapacityMin,BuildingCapacityMax))
#         # Create residents in apartments
#         for MyApartment in MyStreetObject.ApartmentList:
#             MyApartment.CreateResidents(np.random.randint(ApartmentCapacityMin,ApartmentCapacityMax))

# # Add new StreetObjects to a Street
# StreetList[0].AddNonBuildingObject(Type="Empty")
# StreetList[1].AddBuildingObject(Type="House",NumApartments=5,NumResidents=2)



# Find if the details given by a user is matched in any of the streets
user_apartment_num = 5
user_apartment_residents = 2

SearchInStreet(Earth,AptNumber=user_apartment_num,AptResidents=user_apartment_residents)


# pjoshi, 08.2020
# python code to create and populate virtual planet-like entities

'''
Scenario: set up appropriate classes for
    Planet -> ... -> Country -> ... -> houses/parks -> apartments -> people
Goal: Given the details of an apartment, determine if such an apartment is available in a given planet/country/....

Street as a class with name, houses, and other details.
House as a class with house number and apartments.
Apartment as a class with apartment number and number of residents.
Use methods to get total houses in the street, total apartments in a house, ...
'''
## For some number operations
import numpy as np
#np.random.seed(1)

## import objects from custom module to create entities such as planets, cities, ...
import LocationEntities as LE

## import creator functions from custom module
import StreetBuilders

## import searching functions from custom module
import EntitySearchers

# For clear separation of outputs from this script
print("\n")

# Create a planet
Earth = LE.Planet(Name="Earth", Type="Habitable")
# Create a supernation entity
Europe = LE.SuperNation(Name="Europe", Type="Continent")
Pacific = LE.SuperNation(Name="Pacific", Type="Ocean")
# Create a nation entity
Germany = LE.Nation(Name="Germany", Type="Country")
# Create a sub-national entity
NorthRheinWestf = LE.State(Name="NRW", Type="State")
BerlinState = LE.State(Name="Berlin", Type="State")
# Create a city entity
Dusseldorf = LE.City(Name="Duesseldorf", Type="City")
Cologne = LE.City(Name="Cologne", Type="City")
Berlin = LE.City(Name="Berlin", Type="CapitalCity")
# A special type of city containing moving Aircraft Carriers of a nation
USAirCarriers = LE.City(Name="USAirCarriers", Type="Special")

# Define minimum and maximum objects allowed in a street
StreetCapacityMin = 5
StreetCapacityMax = 20

# Create a street entity, specify the type and capacity of the street
Glockenstrasse = LE.Street(Name="Glockenstrasse", Type="City" )
Merheimerstrasse = LE.Street(Name="Merheimerstrasse", Type="City" )
FrankfurterAllee = LE.Street(Name="Frankfurter Allee", Type="City" )
USAirCarrier1 = LE.Street(Name="USAirCarrier1", Type="Ship" )

# Begin to build cities with streets
Dusseldorf.StreetList.append(Glockenstrasse)
Cologne.StreetList.append(Merheimerstrasse)
Berlin.StreetList.append(FrankfurterAllee)
USAirCarriers.StreetList.append(USAirCarrier1)

# Build states
NorthRheinWestf.CityList.extend((Dusseldorf, Cologne))
BerlinState.CityList.append(Berlin)

# Build nation
Germany.StateList.extend((NorthRheinWestf, BerlinState))

# Build supernation
Europe.NationList.append(Germany)
Pacific.NationList.append(USAirCarriers)

# Build planet
Earth.SuperNationList.extend((Europe, Pacific))



# Specify a list of various categories of objects to be created in streets
DefaultCategories = StreetBuilders.StreetObjectCategories()

# Create objects in the streets
StreetBuilders.CreateStreetObjects(Earth, DefaultCategories.GetAll() )
# Create apartments in the buildings
StreetBuilders.CreateApartments(Earth)
# Create residents in the apartments
StreetBuilders.CreateResidents(Earth)
# Add new StreetObjects to some Street entities
Glockenstrasse.AddNonBuildingObject(Type="Empty")
Merheimerstrasse.AddBuildingObject(Type="House",NumApartments=5,NumResidents=2)







# Find if the details given by a user is matched in any of the streets
user_apartment_num = 5
user_apartment_residents = 2

EntitySearchers.SearchInStreet(Earth,AptNumber=user_apartment_num,AptResidents=user_apartment_residents)

# For clear separation of outputs from this script
print("\n")

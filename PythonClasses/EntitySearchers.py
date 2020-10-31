# Python module containing searcher functions

def SearchInStreet(StreetContainer, AptNumber=None, AptResidents=None):
    '''
    Function to search for a certain apartment ...
    \t StreetContainer : any object with GetStreets() method
    \t AptNumber       : apartment number to search for
    \t AptResidents    : number of residents in the apartment
    '''

    # Indicate that all initialization is complete before searching and printing results
    print("\nInitialization complete. Beginning search...\n")

    for street in StreetContainer.GetStreets():
        found_in_houses = []
        for house in street.StreetObjects:
            if house.NumApartments >= AptNumber:
                for apt in house.ApartmentList:
                    if apt.Number == AptNumber and apt.NumResidents == AptResidents:
                        found_in_houses.append(house.Number)

        if not found_in_houses:
            print("Description not matched in %s." % street.Name)
        else:
            print("Description matched in following houses in %s." % street.Name)
            print(found_in_houses)
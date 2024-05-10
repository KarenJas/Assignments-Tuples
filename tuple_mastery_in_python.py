#1. Tuple Mastery in Python

#Function that takes a list of tuples as an argument
def flight_itineraries(itineraries):
    #Initializing an empty string
    return_itinerary = ''
    #Iterating through each itinerary
    for i, itinerary in enumerate(itineraries,start=1):
        #Unpack the tuple
        traveler_name, origin, destination = itinerary
        #Create formated string
        return_itinerary += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return return_itinerary

#Test
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(flight_itineraries(itineraries))



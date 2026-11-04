# Labeeb Farooqi
# HPO267
# 11432366

def calculate_trip_cost(flight_cost, room_cost, travelers, nights):
    """Calculates the total travel costs of a group of people by calculating and adding up airfare and hotel costs

        Parameters:
            flight_cost (float or int):  Cost of flight per person
            room_cost (float or int): Cost of room
            travelers (int): Number of people traveling
            nights (int): Number of nights spent in hotel

        Returns:
                float: Total cost of the trip rounded to 2 decimal places if necessary
    """

    # Rounds up to the next room if number of travelers is odd
    rooms_needed = travelers//2 if travelers % 2 == 0 else travelers//2 + 1
    # Uses travel rates to determine total costs
    total_flight_cost = flight_cost * travelers
    total_room_cost = room_cost * rooms_needed * nights

    # Converts value into a float
    return round(float(total_flight_cost + total_room_cost), 2)

#Assigns values in their respected
print("Family/Group Trip Travel Expenses Calculator:")
user_flight_cost = float(input("Enter the cost of the flight per person ($): "))
user_room_cost = float(input("Enter the hotel room cost per night ($): "))
user_traveler_count = int(input("Enter the number of travelers on the trip: "))
user_night = int(input("Enter the number of nights spent in the hotel:"))
print("The total group cost for the trip is $" + str(calculate_trip_cost(user_flight_cost, user_room_cost, user_traveler_count, user_night)))

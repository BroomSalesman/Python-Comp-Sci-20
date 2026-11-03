# Labeeb Farooqi
# HPO267
# 11432366

def calculate_trip_cost(flight_cost, room_cost, travelers, nights):
    """Calculates the total cost of the family trip by calculating and adding up airfare and hotel costs

        flight_cost (float):  Cost of flight per person
        room_cost (float): Cost of room
        travelers (int): Number of people traveling
        nights (int): Number of nights spent in hotel
    """
    # Rounds up to the next room if number of travelers is odd
    rooms_needed = travelers/2 if travelers % 2 == 0 else travelers//2 + 1
    # Uses travel rates to determine total costs of
    total_flight_cost = flight_cost * travelers
    total_room_cost = room_cost * rooms_needed * nights


    return total_flight_cost + total_room_cost







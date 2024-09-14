def checkio(array: list[int]) -> int:
    # If there are zero items in array (the list), return 0
    if len(array) == 0:
        return 0

    # If the last number in array is 0, return 0, since x * 0 = 0
    elif array[-1] == 0:
        return 0

    # If there is only one item in array, the item is multiplied by itself
    elif len(array) == 1:
        return array[0] * array[-1] # Both values are the same, since there is only one item in list, the first and last

    else:
        last_array_value = array[-1] # The last item in list that is used to multiply the sum of even index items
        indexes = []
        even_index_values = []

        #adds only even indexes to indexes list
        for i in range(len(array)):
            if i % 2 == 0:
                indexes.append(i)

        for i in indexes:
            even_index_values.append(array[i])

        sum_values = sum(even_index_values)

        return sum_values * last_array_value

checkio([0, 1, 2, 3, 4, 5])

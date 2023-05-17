numbers = {17, 4, 7, 10, 11, 121}
num_list = list(numbers)
target = 14

def foo(values, one):
    iterations_list = []
    nums = list(values)
    while not len(iterations_list) == len(nums):
        for i in nums:
            iterations = 0
            if i == one:

                return one
                break

            elif i < one:
                while i < one:
                    i += 1
                    iterations += 1
                iterations_list.append(iterations)

            elif i > one:
                while i > one:
                    i -= 1
                    iterations += 1
                iterations_list.append(iterations)


    min_iter_values = []
    min_values_index = []
    min_values = []

    # going to add first value, will be used to check for dupes and index of dupes
    min_iter = min(iterations_list) # gets the first smallest value in iterations list
    min_iter_values.append(min_iter)

    min_iter_index = iterations_list.index(min_iter) # get the index of the first smallest iteration value
    min_values_index.append(min_iter_index) # added the index of the the min iteration and added to a list

    min_values.append(nums[min_iter_index]) # Got the number related to the iterations, added to a list for the closest values to the target number
    del nums[min_iter_index]


    # Now check for reoccurences of the same min value (the first one)
    for i in iterations_list:
        if i == min_iter:
            min_iter_values.append(i)  # add the value to the min_values list, dont remove yet, need index
            min_values_index.append(iterations_list.index(i))
            min_values.append(nums[iterations_list.index(i)])
            del nums[iterations_list.index(i)]
            del iterations_list[iterations_list.index(i)]


    return min(min_values)
print(foo({4, 7, 10, 11, 12, 17}, 30))

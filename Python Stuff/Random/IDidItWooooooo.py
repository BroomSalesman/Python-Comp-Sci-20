def nearest_value(values: set[int], one: int) -> int:
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
    check_for_dupes_list = []
    dupe_detected = False
    for i in iterations_list:
        if i not in check_for_dupes_list:
            check_for_dupes_list.append(i)
        else:
            dupe_detected = True
            break

    if dupe_detected == True:
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
    else:
        min_iter = min(iterations_list)
        min_iter_index = iterations_list.index(min_iter)

        return nums[min_iter_index]


print("Example:")
print("nearest_value({4, 7, 10, 11, 12, 17}, 9)")

print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5

print("assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10")
print("assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7")
print("assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8")
print("assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9")
print("assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4")
print("assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17")
print("assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8")
print("assert nearest_value({2, 3, -1}, 0) == -1")
print("assert nearest_value({5}, 5) == 5")
print("assert nearest_value({5}, 7) == 5")

print(assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10)
print(assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7)
print(assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8)
print(assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9)
print(assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4)
print(assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17)
print(assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8)
print(assert nearest_value({2, 3, -1}, 0) == -1)
print(assert nearest_value({5}, 5) == 5)
print(assert nearest_value({5}, 7) == 5)





print("The mission is done! Click 'Check Solution' to earn rewards!")

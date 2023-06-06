def my_count(a_list, target):
    counter = 0
    for item in a_list:
        counter += 1 if item == target else 0
    return counter

list = ["hello", "hi", "greetings", "hola", "hello", "hola", "hello", "hola"]

def my_in(collection, target):
    for item in collection:
        if item == target:
            return True
    return False

def my_reverse(list):
    reversed_list = []
    for i in list:

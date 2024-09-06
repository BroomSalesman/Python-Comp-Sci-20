def even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


this_shalt_be_the_number = 0
while even_or_odd(this_shalt_be_the_number):
    this_shalt_be_the_number = input("What shalt be the number?  ")
    this_shalt_be_the_number = int(this_shalt_be_the_number)
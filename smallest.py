def find_smallest_number(numbers):
    smallest_numbers = 888
    for num in numbers:
        if num < smallest_numbers:
            smallest_numbers = num
    return smallest_numbers
    
final = find_smallest_number([1, 2, 3, 4, 5])
print (final)
def find_largest_number(numbers):
    largest_number = 0
    for num in numbers:
        if num > largest_number:
            largest_number = num
    return largest_number
    
final = find_largest_number([1, 2, 3, 4, 5])
print (final)
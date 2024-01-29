def local_min(numbers_list):
   return min(numbers_list)

def local_max(numbers_list):
    return max(numbers_list)

numbers_list = [1, 2, 3]

min_number = local_min(numbers_list)
max_number = local_max(numbers_list)

print(f"The minimum number is: {min_number}")
print(f"The maximum number is: {max_number}")
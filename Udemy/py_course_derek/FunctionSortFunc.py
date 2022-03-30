def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    odd_list = []
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list


list_of_nums = range(1, 90, 3)
print("List of Numbers:", list_of_nums)

odd_list = change_list(list_of_nums, is_it_odd)
print(f"\nOdd Numbers: ", odd_list)

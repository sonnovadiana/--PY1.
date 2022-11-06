import random

def get_unique_list_numbers():
    list_random_number = []
    while len(list_random_number) != 15:
        ran_num = random.randint(-10, 10)
        if ran_num not in list_random_number:
            list_random_number.append(ran_num)
    return list_random_number

print(get_unique_list_numbers())

    

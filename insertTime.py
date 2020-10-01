import time, random

def timer(func):
    '''Timer function, code borrowed from CS 162 assignment #8.'''
    def wrapper(*args, **kwargs):
        beginning_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - beginning_time

    return wrapper

@timer
def insertion_sort(number_list):
    '''insertion sort the integers in list in ascending order'''
    for j in range(1, len(number_list)):
        # current_value and prior index
        value = number_list[j]
        prior_index = j - 1
        # loop backwards and sort any numbers not in ascending order.
        while prior_index >= 0 and number_list[prior_index] > value:
            number_list[prior_index + 1] = number_list[prior_index]
            prior_index -= 1
        number_list[prior_index + 1] = value

    # return the sorted list in descending order.
    return number_list


def main():
    '''run insertion sort with n starting from 5000 to 35,0000'''

    # starting number of integers to sort and list to hold dict of {n, time}
    n = 5000
    data_list = []
    print('Running insertion sort with 5000, 10000, 15000, 20000, 25000, 30000 and 35000')
    # loop until 35k
    while n <= 35000:
        # list with n amount of random integers
        number_list = [random.randint(0, 10000) for x in range(n)]
        # append data into list and increment n
        time = insertion_sort(number_list)
        data_list.append({'n': n, 'time': round(time, 2)})
        n += 5000

    print(data_list)

if __name__ == '__main__':    main()

import time, random

def timer(func):
    '''Timer function, code borrowed from CS 162 assignment #8.'''
    def wrapper(*args, **kwargs):
        beginning_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - beginning_time

    return wrapper

def merge_sort(number_list):
    '''Merge sort the list of integers in descending order
    merge sort influenced from https://www.geeksforgeeks.org/merge-sort/'''
   
    if len(number_list) > 1:
        # get midpoint of number list
        mid = len(number_list) // 2
        # get left & right of mid point
        left_sub_array = number_list[:mid]
        right_sub_array = number_list[mid:]

        # recurse the left and right 
        left = merge_sort(left_sub_array)
        right = merge_sort(right_sub_array)

        number_list = []

        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                number_list.append(left[0])
                left.pop(0)
            else:
                number_list.append(right[0])
                right.pop(0)

        for i in left:
            number_list.append(i)

        for i in right:
            number_list.append(i)

    return number_list

def main():
    '''run merge sort with n starting from 5000 to 35,0000'''

    # starting number of integers to sort and list to hold dict of {n, time}
    n = 5000
    data_list = []
    print('Running merge sort with 5000, 10000, 15000, 20000, 25000, 30000 and 35000')
    # loop until 35K
    while n <= 35000:
        # list with n amount of random integers
        numb_list = [random.randint(0, 10000) for x in range(n)]

        # set begin & end time for merge sort
        beginning_time = time.perf_counter()
        merge_sort(numb_list)
        end_time = time.perf_counter()

        # append data into list and increment n
        data_list.append({'n': n, 'time': round(end_time - beginning_time, 2)})
        n += 5000

    print(data_list)

if __name__ == '__main__':    main()
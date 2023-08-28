import random


def swap(left_index, right_index, array):
    tmp = array[left_index]
    array[left_index] = array[right_index]
    array[right_index] = tmp


def partition(from_index, to_index, arr):
    left_index = from_index
    right_index = to_index

    random_index = random.randrange(from_index, to_index)
    random_element = arr[random_index]
    while right_index >= left_index:

        while arr[left_index] < random_element:
            left_index += 1

        while arr[right_index] > random_element:
            right_index -= 1

        if left_index <= right_index:
            swap(left_index, right_index, arr)
            left_index += 1
            right_index -= 1

    return left_index


def sort(from_index, to_index, arr):
    if to_index <= from_index:
        return

    divide_index = partition(from_index, to_index, arr)
    sort(from_index, divide_index - 1, arr)
    sort(divide_index, to_index, arr)


def quick_sort(arr):
    sort(0, len(arr) - 1, arr)

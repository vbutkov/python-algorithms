import qsort

if __name__ == '__main__':
    array = [2, 5, 1, 9, 5, 6, 0, 9, 8, 3]
    print(f"Массив до сортировки: {array}")
    qsort.quick_sort(array)
    print(f"Массив после сортировки: {array}")

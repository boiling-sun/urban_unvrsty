"""
Insertion sort iterates, consuming one input element each repetition, and grows a sorted output list. 
At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list, and inserts it there. 
It repeats until no input elements remain.
"""


def insertion_sort(array):
    sorted_array = []
    for i in range(len(array)):
        element = array[i]
        inserted = False
        for j in range(len(sorted_array)):
            if element < sorted_array[j]:
                sorted_array.insert(j, element)
                inserted = True
                break
        if not inserted:
            sorted_array.append(element)

    return sorted_array


def main():
    list_ = [3, 5, 4, 1, 9, 0] 
    print(insertion_sort(list_))

if __name__ == '__main__':
    main()
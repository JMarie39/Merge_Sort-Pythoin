"""
Name: AGULTO, JULIANA MARIE B.
Language: PYTHON
Paradigm: FUNCTIONAL
"""

import copy


# The function is used to merge the left and right list.
def merge(left, right):
    result = []         # To store the sorted list
    left_pointer = right_pointer = 0

    # While it still have items to put into the result list
    while not (left_pointer >= len(left) and right_pointer >= len(right)):
        # If the left pointer is at the end of the left list
        if left_pointer == len(left):
            result.append(right[right_pointer])
            right_pointer += 1       
        
        # If the right pointer is at the end of the right list
        elif right_pointer == len(right):
            result.append(left[left_pointer])
            left_pointer += 1
        
        # Compares the values being pointed
        elif left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    
    return result

# This function is used to sort the array.
# start = start index
# last = last index
def merge_sort(array, start, last):
    
    if len(array) > 1:
        mid = len(array) // 2       # To get the midpoint

        # If there are two (even) elements left in the array
        if len(array) % 2 == 0:
            mid -=  1

        # Splits the array (list) into left and right (lists)
        left, right = array[ : mid + 1], array[mid + 1 : ]

        # Divide & Conquer
        left, right = merge_sort(left, start, start + len(left) - 1), merge_sort(right, start + len(left), start + len(array) - 1)

        # To merge the list
        array = merge(left, right)
        
        # Prints the global array_copy
        print_copy(array, start, last + 1)

    return array

# This function is used to print the elements in the array.
def print_list(array):
    for arr in array: 
        print(str(arr) + " ", end="")
    print()

# This function is used to show the steps.
def print_copy(array, start, last):
    global array_copy
    for i in range(start, last, 1):
        array_copy[i] = array[i - start]
    print_list(array_copy)


array_copy = []
def main():
    global array_copy
    num_elements = int(input("Input the number of elements: ").strip(" "))      # To get the number of elements the user wants to sort.
    array = list(int(input().rstrip()) for i in range(num_elements))          # To get the list of elements.
    array_copy = copy.deepcopy(array)   # Copies the array (list)
    
    print("Sorting...")
    array_sorted = merge_sort(array, 0, len(array) - 1)

    print("\nSorted Array")
    print_list(array_sorted)

if __name__ == "__main__":
    main()
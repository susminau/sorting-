def bubbleSort(insertion_sort):
    n = len(insertion_sort)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if insertion_sort[j] > insertion_sort[j + 1]:
                insertion_sort[j], insertion_sort[j + 1] = insertion_sort[j + 1], insertion_sort[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


# Driver code to test above
insertion_sort = [5,2,4,3,10,7,1,9,6,8]

bubbleSort(insertion_sort)

#print (insertion_sort)

print("Sorted array :")
for i in range(len(insertion_sort)):
    print("%d" % insertion_sort[i], end=" ")
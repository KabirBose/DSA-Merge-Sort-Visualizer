# Kabir Bose: 100862410
# merge sort algorithm

import os
file = "swap-sound.mp3"

def merge_sort(arr):
    # only perform sorting if the array is > than 1 || return
    if len(arr) > 1:
        # find the middle index of the array
        mid = len(arr) // 2

        # Use substring function to divide the array elements into 2 parts (left and right of middle index)
        l = arr[:mid]
        r = arr[mid:]

        print('----------------------------------------------')
        print(f"Array: {arr}\nLeft side: {l}\nRight side: {r}")
        print('----------------------------------------------')

        # play a sound after each swap
        os.system("afplay " + file)

        # sort the left side
        merge_sort(l)

        # sort the right side
        merge_sort(r)

        # assign all counter values to 0
        i = j = k = 0

        # after both sides are sorted, merge them
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        # check if any element was left in l
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        # check if any element was left in r
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    # return the sorted array            
    return arr

# the og array
arr = [11,1,30,2,51,6,29,7,67,15,118,4,89,23]

# a copy of the og array
to_sort = arr.copy()

print(f"\nOld Result: {arr}\nFinal result: {merge_sort(to_sort)}\n")
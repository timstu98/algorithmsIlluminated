def mergeSort(arr):
    """mergeSort algorithm
    recursive algo
    performs a marge sort on the input array.

    Args:
        arr (list of int): The array to be sorted

    Returns:
        list of int: The sorted array
    """

    if len(arr)==1: # can improve, no need to work with arr1, arr2
        return arr

    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]

    left = mergeSort(arr1)
    right = mergeSort(arr2)

    merged=[]
    j=k=0
    while j<len(left) and k<len(right):
        if left[j]<right[k]:
            merged.append(left[j])
            j+=1
        else:
            merged.append(right[k])
            k+=1
    merged.extend(left[j:])
    merged.extend(right[k:])

    return merged

print(mergeSort([5,4,1,8,7,2,6,3]))

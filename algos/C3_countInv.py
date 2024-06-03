from C1_mergeSort import mergeSort

def sortCountInversions(array,numberInversions):
    """Counts the number of inversions in an array using divide-and-conquer.

    Args:
        array (list of int): Array for which number of inversions are to be counted.

    Returns:
        int: Number of inversions in array
    """
    n=len(array)
    if n==0 or n==1:
        return array,numberInversions
    l=array[:(n//2)]
    r=array[(n//2):]

    lSorted,lInversions = sortCountInversions(l,numberInversions)
    rSorted,rInversions = sortCountInversions(r,numberInversions)
    sortedArray,splitInversions = mergeCountSplitInversions(lSorted,rSorted)
    # print("--------------------------------------")
    # print(array,sortedArray,lInversions+rInversions+splitInversions)
    # print(l,lSorted,lInversions)
    # print(r,rSorted,rInversions)

    return sortedArray,lInversions+rInversions+splitInversions

    
def mergeCountSplitInversions(lSorted,rSorted):

    sortedArray=[]
    j=k=numberSplitInversions=0
    while j<len(lSorted) and k<len(rSorted):
        if lSorted[j]<=rSorted[k]:
            sortedArray.append(lSorted[j])
            j+=1
        else:
            sortedArray.append(rSorted[k])
            k+=1
            numberSplitInversions+=len(lSorted[j:])
    # numberSplitInversions+=len(lSorted[j:])
    sortedArray.extend(lSorted[j:])
    sortedArray.extend(rSorted[k:])

    return sortedArray,numberSplitInversions




sortedArray1,numInversions1=sortCountInversions([0,1,2,3,5,4,6,7],0)
print(sortedArray1)
print(numInversions1)
sortedArray2,numInversions2=sortCountInversions([7,5,3,1,-1,-3,-5,-5],0)
print(sortedArray2)
print(numInversions2)

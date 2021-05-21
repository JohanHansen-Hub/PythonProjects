ex_list = [5,3,8,1,9,2]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
    
        i = j = k = 0
        while i < len(left) and j < len(right):
            # Vi sammenligner left i med right j:
            # Den minste verdien blir plassert i arr sin k plassering -> som vi øker med 1 for hver iterasjon.
            if left[i] < right[j]:
                arr[k]  = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

print(mergeSort(ex_list))
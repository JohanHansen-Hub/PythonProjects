ex_list = [5,3,8,1,9,2]

def selectionSort(arr):
    index_lengde = [i for i in range(0, len(arr) - 1)]
    # Vi itererer gjennom listen og leter etter den minste verdien:
    for i in index_lengde:
        min_val = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j
        # Bytter possisjonen til den minste verdien:
        if min_val != i:
            arr[min_val], arr[i] = arr[i], arr[min_val]
    return arr

print(selectionSort(ex_list))
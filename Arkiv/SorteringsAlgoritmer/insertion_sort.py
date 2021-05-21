ex_list = [5,3,8,1,9,2]

def insertionSort(arr):
    index_lengde = [i for i in range(1, len(arr))]
    # Vi itererer gjennom listen:
    for i in index_lengde:
        sorting_val = arr[i]
        # Dersom verdien til venstre er større enn verdien til høyre -> vi switcher verdiene
        while arr[i-1] > sorting_val and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr

print(insertionSort(ex_list))
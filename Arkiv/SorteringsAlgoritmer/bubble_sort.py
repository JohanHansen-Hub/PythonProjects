ex_list = [5,3,8,1,9,2]

def bubbleSort(arr):
    index_lengde = len(arr) - 1
    # Vi lager en løkke som fortsetter intill listen er sortert (sorter = False)
    sorter = True
    while sorter:
        sorter = False
        # Begynner fra starten og sammenligner verdien med nabo-verdien (i vs. i+1)
        for i in range(0, index_lengde):
            # Dersom verdien til venstre er større en verdien til høyre -> flipp rundt på elementene
            if arr[i] > arr[i+1]:
                sorter = True # Vi trenger en ny while gjennomgang for å sikre at alle verdiene er på riktig plass.
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubbleSort(ex_list))
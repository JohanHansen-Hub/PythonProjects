
eksamplelist = [5,3,8,1,9,2]

def quickSort(the_list):
    if len(the_list) <= 1:
        return the_list
    else:
        pivot = the_list.pop()

    larger_items = []
    smaller_items = []
    # Vi må sammenligne alle elementene i listen og sortere:
    for i in the_list:
        if i > pivot:
            larger_items.append(i)
        else:
            smaller_items.append(i)
    return quickSort(smaller_items) + [pivot] + quickSort(larger_items)

print(quickSort(eksamplelist))
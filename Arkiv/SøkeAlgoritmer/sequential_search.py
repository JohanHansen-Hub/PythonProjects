
eksamplelist = [5,3,8,1,9,2]

def sequentialSearch(the_list, item):
    position = 0
    found = False
    while position < len(the_list) and not found:
        if the_list[position] == item:
            found == True
        else:
            position += 1
    return found

print(sequentialSearch(eksamplelist, 9))
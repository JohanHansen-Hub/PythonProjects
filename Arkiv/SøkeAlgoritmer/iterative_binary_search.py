
eksamplelist = [5,3,8,1,9,2]

def iterativeBinarySearch(the_list, item):
    start = 0
    end = 0
    found = 0
    while start <= end and not found:
        mid = (start + end) // 2
        if the_list[mid] > item:
            end = mid - 1
        elif the_list[mid] < item:
            end = mid - 1
        else:
            found = True
    return found


print(iterativeBinarySearch(eksamplelist.sort(), 9))
eksamplelist = [5,3,8,1,9,2]

def recursiveBinarySearch(the_list, item):
    if len(the_list) == 0:
        return False
    else:
        mid = len(the_list) // 2
        if the_list[mid] > item:
            return recursiveBinarySearch(the_list[:mid], item)
        elif the_list[mid] < item:
            return recursiveBinarySearch(the_list[mid + 1:], item)
        else:
            return True


print(recursiveBinarySearch(eksamplelist.sort(), 9))
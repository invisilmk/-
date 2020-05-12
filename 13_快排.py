def quick_sort(alist,first,last):
    mid_value = alist[first]
    if first>= last:
        return
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        #low += 1
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        #high -= 1
    alist[low] = mid_value
    #you
    quick_sort(alist,first,low-1)
    #zuo
    quick_sort(alist,low+1,last)


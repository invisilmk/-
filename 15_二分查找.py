def binary_search(alist,item):
    n = len(alist)
    if n>0:
        mid = n/2
        if alist[mid] ==item:
            return True
        elif item< alist[mid]:
            binary_search(alist[:mid],item)
        else:
            binary_search(alist[mid+1:],item)
    return False

def binary_search_2(alist,item):
    n = len(alist)
    first = 0
    last = n - 1
    while first<= last:
        mid = (first+last)//2
        if alist[mid]==item:
            return True
        elif alist[mid]>item:
            last = mid-1
        elif alist[mid]<item:
            first = mid+1
    return False



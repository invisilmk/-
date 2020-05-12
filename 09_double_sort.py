


def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        for i in range(0,n-j-1):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
        



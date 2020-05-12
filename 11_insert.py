def insort_sort(alist):
    n = len(alist)
    for j in range(1,n):
        i = j
        while i >0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            else:
                break

if __name__ == '__main__':
    li = [1,4,2,7,5,9,6]
    print(li)
    print(insort_sort(li))
    print(li)

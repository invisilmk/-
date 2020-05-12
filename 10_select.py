

def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]

if __name__ == '__main__':
    li = [1,4,2,7,5,9,6]
    print(li)
    print(select_sort(li))
    print(li)


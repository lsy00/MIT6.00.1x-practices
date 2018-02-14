def mergesort(left,right):
    '''
    sort and merge two list
    '''
    result = []
    i,j = 0,0
    while i<len(left) and j < len(right): #do until one of them becomes empty
        if left[i]>right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    while j < len(right): #left is empty
        result.append(right[j])
        j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
#linear
'''
用改变index的办法而非slice list的方法来避免复制list
也可见于bisection search的两种办法
'''

def mergesort_recur_divide(L):
    '''
    divide the list
    '''
    if len(L) < 2:
        return L[:] #base case
    else:
        middle = len(L)//2
        left = mergesort_recur_divide(L[:middle])
        right = mergesort_recur_divide(L[(middle+1):])
        return mergesort(left,right)

#overall complexity: O(nlog(n))

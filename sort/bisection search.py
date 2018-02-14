def bisection_search_1(L,e):
    if L == []:
        return False
    
    elif len(L) == 1:
        return e == L[0]

    else:
        middle = len(L)//2
        if L[middle]>e:
            return bisection_search_1(L[:middle],e)
        elif L[middle] < e:
            return bisection_search_1(L[middle:],e)

def bisection_search_2(L,e):
    def bisection_helper(L,e,high,low):
        if high == low: #only 1 element
            return L[0]==e
        middle = (high+low)//2
        if L[middle] == e:
            return True
        elif L[middle] > e:
            if middle == high:
                return False
            else:
                return bisection_helper(L,e,low,middle-1)
        else:
            return bisection_helper(L,e,middle+1,high)
    

    if L == []:
        return False
    else:
        return bisection_helper(L,e,0,len(L)-1)

    
#use helper function to keep complexity constant

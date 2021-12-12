from math import floor
from operator import __lt__, __gt__, __eq__

def mergeSort(lst:list, key=None, reverse = False):
    
    oper = __lt__
    if reverse:
        oper = __gt__


    if key == None:
        n = len(lst)
        pivot = n//2
        

        if n > 2:

            #if the length is greater than 2, i will split the arrays
            lst[:pivot] = mergeSort(lst[:pivot], key=key, reverse=reverse)
            lst[pivot:] = mergeSort(lst[pivot:], key=key, reverse=reverse) 

            #then merge the lists
            l1 = 0
            l2 = pivot
            ans = []
            while l1 < pivot and l2 < n:
                if oper(lst[l1], lst[l2]):
                    ans.append(lst[l1])
                    l1 += 1

                else:
                    ans.append(lst[l2])
                    l2 += 1
            
            if l2 < n:
                for i in range(l2, n):
                    ans.append(lst[l2])
            
            if l1 < pivot:
                for i in range(l1, pivot):
                    ans.append(lst[l1])


            return ans
            
        elif len(lst) == 2:
            if oper(lst[1], lst[0]):
                lst[0], lst[1] = lst[1], lst[0]
        
            return lst
            
        
        
    else:
        lst = list(tuple(ooo, key(ooo)) for ooo in lst)
        n = len(lst)
        
        pivot = n//2

        if(n > 2):
            #if the length is greater than 2, i will split the arrays
            lst[:pivot] = mergeSort(lst[:pivot][1], key=key, reverse=reverse)
            lst[pivot:] = mergeSort(lst[pivot:][1], key=key, reverse=reverse) 

            l1 = 0
            l2 = pivot
            ans = []
            while l1 < pivot and l2 < n:
                if oper(lst[l1][1], lst[l2][1]):
                    ans.append(lst[l1])
                    l1 += 1

                else:
                    ans.append(lst[l2])
                    l2 += 1
            
            if l2 < n:
                for i in range(l2, n):
                    ans.append(lst[l2])
            
            if l1 < pivot:
                for i in range(l1, pivot):
                    ans.append(lst[l1])


            return ans

        elif len(lst) == 2:
            if oper(lst[1][1], lst[0][1]):
                lst[0], lst[1] = lst[1], lst[0]
            
        return list(a[0] for a in lst)

def bingoSort(lst:list, key=None, reverse=False):
    #un selection sort mai special
    oper = __lt__
    if reverse:
        oper = __gt__


    if key == None:
        n = len(lst)
        
        for i in range(0, n):
            indexes = []
            value = lst[i]
            for j  in range(i+1, n):
               
                if oper(lst[j],value):
                    indexes.clear()
                    indexes.append(j)
                    value = lst[j]

                elif lst[j] == value:
                    indexes.append(j)
            
            for ind in indexes:
                lst[i], lst[ind] = lst[ind], lst[i]
            
             # doublecheck the same element
            
    else:
        lst = list(tuple(ooo, key(ooo)) for ooo in lst)

        n = len(lst)

        for i in range(0, n):
            indexes = []
            value = lst[i]
            for j  in range(i+1, n):
               
                if oper(lst[j][1],value):
                    indexes.clear()
                    indexes.append(j)
                    value = lst[j][1]

                elif lst[j][1] == value:
                    indexes.append(j)
            
            for ind in indexes:
                lst[i], lst[ind] = lst[ind], lst[i]

            # doublecheck the same element
        
    return lst

def key(a):
    return a[1]

a = [
    [100, 1],
    [100, 123],
    [100, 1241235],
    [100, 35345],
    [100, 2134]
]
a = bingoSort(a)
print(a)

    
from math import floor
from operator import __lt__, __gt__, __eq__
from typing import Type

def mergeSort(lst:list, key=None, reverse = False, cmp = None):
    # be aware of the way key and cmp are declared!!!!!


    oper = __lt__
    if reverse:
        oper = __gt__

    if cmp != None:
        oper = cmp
        if reverse:
            oper = lambda a,b: not cmp(a,b)

    if key == None:
        n = len(lst)
        pivot = n//2
        

        if n > 2:

            #if the length is greater than 2, i will split the arrays
            lst[:pivot] = mergeSort(lst[:pivot], key=key, reverse=reverse, cmp=cmp)
            lst[pivot:] = mergeSort(lst[pivot:], key=key, reverse=reverse, cmp=cmp) 

            #then merge the lists
            l1 = 0
            l2 = pivot
            ans = []
            #repun concomitent elementele din ambele jumatati
            while l1 < pivot and l2 < n:
                if oper(lst[l1], lst[l2]):
                    ans.append(lst[l1])
                    l1 += 1

                else:
                    ans.append(lst[l2])
                    l2 += 1
                
            #pun elementele ramase 
            if l2 < n:
                for i in range(l2, n):
                    ans.append(lst[i])
            
            if l1 < pivot:
                for i in range(l1, pivot):
                    ans.append(lst[i])


            return ans
            
        elif len(lst) == 2:
            #daca am doar doua elemente, pur si simplu le compar
            if oper(lst[1], lst[0]):
                lst[0], lst[1] = lst[1], lst[0]
        
            return lst
            
        
        
    elif key != None and cmp == None:
        lst = list((ooo, key(ooo)) for ooo in lst)
        n = len(lst)
        
        pivot = n//2

        if(n > 2):
            #if the length is greater than 2, i will split the arrays
            lst[:pivot] = mergeSort(list(a[0] for a in lst[:pivot]), key=key, reverse=reverse, cmp=cmp)
            lst[pivot:] = mergeSort(list(a[0] for a in lst[pivot:]), key=key, reverse=reverse, cmp=cmp) 
            lst = list((ooo, key(ooo)) for ooo in lst)

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
                    ans.append(lst[i])
            
            if l1 < pivot:
                for i in range(l1, pivot):
                    ans.append(lst[i])


            return list(a[0] for a in ans)

        elif len(lst) == 2:
            if oper(lst[1][1], lst[0][1]):
                lst[0], lst[1] = lst[1], lst[0]
            
        return list(a[0] for a in lst)
    
    else:
        return TypeError("Key and cmp are both declared, witch is not allowed.")



def bingoSort(lst:list, key=None, reverse=False, cmp = None):
    #un selection sort mai special
    
    #treat the reverse case
    oper = __lt__
    if reverse:
        oper = __gt__

    if cmp != None:
        oper = cmp
        if reverse:
            oper = lambda a,b : not cmp(a,b)

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
        return lst
            
    elif key!=None and cmp == None:
        lst = list((ooo, key(ooo)) for ooo in lst)

        n = len(lst)

        for i in range(0, n):
            indexes = []
            value = lst[i][1]
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
        
        return list(a[0] for a in lst)
    
    else:
        return TypeError("Key and cmp are both declared, witch is not allowed.")


if __name__ == "__main__":
    def key(a):
        return a[1]

    def cmp(a,b):
        return a[1] ^ -1 < b[1] ^ -1

    a = [
        [100, 1],
        [100, 123],
        [100, 123],
        [100, 35345],
        [100, 2134]
    ]
    a = bingoSort(a, cmp = cmp)
    print(a)

    
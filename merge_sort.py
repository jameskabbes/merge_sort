

def merge_sort( a: list ):
    
    if len(a) == 1:
        return a

    middle_index = len(a) // 2
    l1 = merge_sort( a[ :middle_index ] )
    l2 = merge_sort( a[ middle_index: ] )

    l_merged = []
    l1_index = 0
    l2_index = 0
    len_l1, len_l2 = len(l1), len(l2)
    
    while ( l1_index < len_l1 ) or ( l2_index < len_l2 ):

        # list 1 is add the end, just use the rest of l2
        if l1_index == len_l1:
            for i in range( l2_index, len_l2 ):
                l_merged.append( l2[ i ] )
            break

        # list 2 is add the end, just use the rest of l1
        if l2_index == len_l2:
            for i in range( l1_index, len_l1 ):
                l_merged.append( l1[ i ] )
            break

        if l2[ l2_index ] > l1[ l1_index ]:
            l_merged.append( l1[l1_index] )
            l1_index += 1
        else:
            l_merged.append( l2[l2_index] ) 
            l2_index += 1

    return l_merged


import random

a = list(range(100))
random.shuffle( a )

print (a)
print ()

print ( merge_sort( a ) )



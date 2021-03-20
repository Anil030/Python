def cap(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd
lst = [10,13,12,5,4,6,22,3]

even, odd = cap(lst)
print("Even : {} and odd :{}".format(even,odd))
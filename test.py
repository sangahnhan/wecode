def even(): 
    even_list=[]
    for i in range(1,51):
        if i % 2 == 1:
            continue
        even_list.append(i)
    return even_list
    
def merge(arr_1,arr_2):
    merged_array = []
    while(len(arr_1) > 0 and len(arr_2) > 0): 
        if(arr_1[0] >= arr_2[0]):
            merged_array.append(arr_1.pop(0))
        else:
            merged_array.append(arr_2.pop(0))
    if(len(arr_1) == 0):
        merged_array.extend(arr_2)    
    else:
        merged_array.extend(arr_1)
    return merged_array

a = [8,2,1]
b = [12,9,0]

print(a)
print(merge(a,b))
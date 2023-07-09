# computing minimal absolute difference in an array

def min_abs_diff(a):
    a.sort()
    min_ = abs(a[len(a)-1]-a[0])+1
    for i in range(len(a)-1):
        if a[i+1]-a[i] < min_:
            min_ = a[i+1]-a[i] 
    return min_

a = [1,8,10,-14,-12,16]

print(min_abs_diff(a))
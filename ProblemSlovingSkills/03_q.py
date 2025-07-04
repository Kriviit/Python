#replace element 4 with 100
arr=(1,2,3,1,4)
arr=list(arr)
arr[-1]=100
arr=tuple(arr)
print(arr)
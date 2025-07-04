#find elemet with the maximum count 
a=[1,2,1,3,1,12,1,3,1,1,1,2,2,4,2,3,3,4,4,5,5,5,6,6,7,6,8,8,6,9,9,3]
# def find_max_ele(arr):
#     s=set(arr)
#     m=0
#     c=0
#     for i in s:
#         if c<arr.count(i):
#             c=arr.count(i)
#             m=i
#         return m
from collections import Counter
print(Counter(a))
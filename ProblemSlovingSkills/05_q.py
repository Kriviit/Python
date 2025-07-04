#remove dublicates
# all the values will be pos+
a=[1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7,9, 9, 12,8, 8]

b=set()
i=0
for x in a:
    if x not in b:
        b.add(x)
        a[i]=x
        i+=1
del a[i:]
print(b)

#collection 


prev=a[0]
for i in range(1,len(a)):
    if a[i]!=prev :
        prev=a[i]
    elif a[i-1]==-1 or a[i]==a[i-1]:
        a[i]=-1


# for i in a:
#     if i!=-1:
#         print(i,end=" ")



















# result=[1,2,3,4,5,6,7,9,12,8]
# r=[]
# r.append(a[0])
# for i in range(1,len(a)):
#     if a[i]!=a[i-1]:
#         r.append(a[i])
# print(r)
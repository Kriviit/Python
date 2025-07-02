# a=[1,2,3,4]
# b=[2,3,4,5,6]
# # print(a.append(20))#method is it updating orginal or return new list ### return none
# # print(a)
# # # b.append(-20)
# # # print(a)
# # # print(b)
# a.clear()# no return Nne
# print(a.clear())

# a=[1,2,3,3,3,1,2,2,3,2,1,2,2,3,3,1,2,3,2,4,45,5,6,200]
# print(a.count(3))
# print(a)



# a=[1,2,3,4,5]
# b=[1,2,3]
# # a=[1,2,3,4,5,[1,2,3]] or a=[1,2,3,4,5,1,2,3] 
# a.extend(b)
# print(a)
# print(a.index(3))


# a=[1,2,3]
# a.insert(0,20)
# print(a)

# a=[1,2,3,3,4,5]
# print(a.pop(2))
# print(a)



# a=[1,2,3,3,4,5]
# a.remove(3)
# print(a)


# print(a.reverse())
# print(a)
a=[1,2,3,4,5]
b=a.copy()
a[4]=100
print(b)
print(a)
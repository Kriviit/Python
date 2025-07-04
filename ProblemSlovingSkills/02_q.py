# all multiples of 2 and 3 in between 200 to 1000

def mult_2_3(start,stop):
    result=[]
    for i in range(start,stop+1):
        if i%2==0 and i%3==0:
            result.append(i)
    return result
print(mult_2_3(100,200))
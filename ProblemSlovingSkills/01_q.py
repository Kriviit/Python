# # seperate all the elemensts from the list and make them sublist

arr=[1,2,3,"True",[1,2,3],False,True,(1,2,3,4),22.3,22.5]

def sep_data(arr):
    INT=[]
    FLOAT=[]
    LIST=[]
    TUPLE=[]
    STR=[]
    BOOL=[]
    for i in arr:
        if type(i)==int:
            INT.append(i)
        elif type(i)==float:
            FLOAT.append(i)
        elif type(i)==list:
            LIST.append(i)
        elif type(i)==tuple:
            TUPLE.append(i)
        elif type(i)==bool:
            BOOL.append(i)
        elif type(i)==str:
            STR.append(i)
    return INT,FLOAT,TUPLE,BOOL,STR

INT,FLOAT,TUPLE,BOOL,STR=sep_data(arr)
l=list(sep_data(arr))







#tuple unpacking

# a=[1,2,3,4]
# c,d,e,d=a
# print(c)
# print(d)
# print(e)




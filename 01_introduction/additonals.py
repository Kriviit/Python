# a=20
# b="python"
# c=True
# print(a+False)

from demo import a
# a=10 # global
                                                                    
def outter():
        # a=30 #outter function view -> local  innerfunction-enclouser

        def inner():
            # a=50
            return a
        
        return inner()
        #legb l=local e-encloser g -global b -stands builtin

print(outter())  





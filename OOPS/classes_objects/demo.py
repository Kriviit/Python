class Student:
    university="VBIT" # static or class varable
    def __init__(self,name,age,rollno,cgpa,branch):# instance method
        self.name=name #instance varable
        self.age=age
        self.rollno=rollno
        self.cgpa=cgpa
        self.branch=branch
    def intance_method(self):
        return self.name

pavan=Student("Pavan",26,"b01",8.6,"IT")
venkat=Student("Venkat",30,"b01",9.6,"CSE")

print(pavan.age)
print(venkat.age)
print(pavan.intance_method())
print(venkat.intance_method())
# pavan=Student("Pavan",26,"b01",8.6,"IT")
# 類別以及物件
 
from Animal import Animal

class People(Animal):
    def __init__(self,name,sex,id) -> None:
        self.Name = name
        self.Sex =sex
        self.Id =id

    def IsBoy(self):
        if self.Sex==True:
            return "1"
        else:
            return "2"

    def yell(self,say): 
        print(say)
     
people1= People("Alex",True,"A001")
people2= People("Bennett",True,"A002")

print(people1.Name)
print(people2.Id)

isboy =people2.IsBoy()

print(isboy)


    
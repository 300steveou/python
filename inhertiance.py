from Animal import Animal
from classObject import People

people1= People("Clock",True,"1430")
# people1.yellString("叫什麼叫")

people1.yell("yell what?")

# People是否為Animal的子類別
print(issubclass(People,Animal))


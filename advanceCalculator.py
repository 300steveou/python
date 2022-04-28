# 建立一個計算機可以相增,相減,相乘,相除

inputOne = float(input("Please input Number1:"))
operator = input("Please input Operator:")
inputTwo = float(input("Please input Number2:"))

# 相加

if (operator=="+"):
    print(inputOne+inputTwo)
elif(operator=="-"):
    print(inputOne-inputTwo)
elif(operator=="*"):
    print(inputOne*inputTwo)
elif(operator=="/"):
    print(inputOne/inputTwo)
else:
    print("please input corrct operator")
# for迴圈練習

# for para in list

for letter in "abcdefgh":
    print(letter)

for num in [0,1,2,3,4]:
    print(num)

# range apply 
for num in range(5):
    print(num)

# 2,3,4,5,6
for num in range(2,7):
    print(num)


firstNum = int(input("Please input first Num:"))
secondNum = int(input("Please input second Num:"))
 
def powTest(firstNum,secondNum):
    result = firstNum
    for index in range(secondNum-1):
        result = result*firstNum
    return result

print(powTest(firstNum,secondNum))
# 條件判斷式

a=1
b=1

if a== 2:
    print("True")
else:
    print("False")


# 多條件判斷式

# 判斷其一
score = 90
if score==100:
    print("滿分")
elif score>80:
    print("高標")
elif score>60:
    print("及格")

mathScore = 80

# and 條件
if score==100 and mathScore==100:
    print("滿分")
elif score>80 and mathScore>=80:
    print("高標")
elif score>60:
    print("及格")

# OR條件式
mathScore =100
score =70

if score==100 or mathScore==100:
    print("滿分")
elif score>80 or mathScore>=80:
    print("高標")
elif score>60:
    print("及格")

# 組合
def maxNum(num1,num2,num3):
    if(num1> num2 and num1> num3):
        return num1
    elif (num2> num1 and num2> num3):
        return num2
    elif (num3> num1 and num3> num2):
        return num3

x= maxNum(88,66,777)
print(x)
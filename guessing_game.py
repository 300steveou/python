# 猜數字 終極密碼
secretNum =66
guessNum = None

firstNum =1
secondeNum = 100

while (secretNum!=guessNum):
    
    guessNum =int(input("Please Guess" +str(firstNum)+"~"+str(secondeNum)+":")) 

    if(guessNum>secretNum):
        secondeNum = guessNum   
    elif(guessNum<secretNum):
        firstNum = guessNum
            
print("Bingo")

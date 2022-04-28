from question import Quenstion
# from Question import Quenstion

test = [
    "2+8=?\n (a)10 (b)11 (c)12\n",
    "2+6=?\n (a)9 (b)8 (c)5\n",
    "2+15=?\n (a)9 (b)10 (c)17\n",
]

print(test[0])

questions = [
    Quenstion(test[0],"a"),
    Quenstion(test[1],"b"),
    Quenstion(test[2],"c")
]

print(questions)

def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if(answer==question.answer):
            score +=1
    print(str(score))

runTest(questions)
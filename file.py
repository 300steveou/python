# file read and write
 # open("檔案路徑",mode="開啟模式")

# 絕對路徑
# 相對路徑

# mode
# r 讀取
# w 複寫
# a 在原先的地方寫東西

# open word.txt
file=open("word.txt",mode="r")
# print(file.read()) 
# print(file.readline())

for line in file:
    print(line)

# close resource
file.close()

# rewrite 
file=open("word.txt",mode="w")
file.write("hello")
file.close()

# file=open("word.txt",mode="a",encoding="utf-8")
# file.write("寫")

# using
with open("word.txt",mode="a",encoding="utf-8") as file:
    file.write("寫123")


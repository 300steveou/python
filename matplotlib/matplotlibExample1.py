# pyplot繪圖
# 第三方外部引用,pip套件管理工具下載
#  
from cProfile import label
import matplotlib.pyplot as mpt

month =['6/6','6/7','6/8','6/9','6/10']
month2=['6/6','6/7','6/8','6/9','6/10']
sales =[16605.96,16512.88,16670.51,16621.34,16460.12]
sales2 =[535,540,544,541,530]

for index,value in enumerate(sales2):
 sales2[index] =sales2[index]*30
 print (sales2[index])

# plot lw=2 粗細程度
mpt.plot(month,sales,lw=5,label="taiwan")
mpt.plot(month2,sales2,lw=2,label="2330*30")

mpt.xlabel('day')
mpt.ylabel('point')
mpt.legend()
mpt.title('point between 2330 and taiwan')
mpt.show()

# mpt.plot([1,2,3,4],[1,40,9,16])
# mpt.show()
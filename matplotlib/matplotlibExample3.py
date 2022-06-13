# pyplot繪圖
# 第三方外部引用,pip套件管理工具下載
# example 虛線;矩形;綠色三角形
# r--紅色虛線
# bs藍色矩形
# g^綠色三角形
# numpy 矩陣運算
 
import matplotlib.pyplot as mpt
import numpy as np

# 從0到5 ,每個0.2步
t= np.arange(0.0, 5.0, 0.2)

for index in t :
 print(index)

mpt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
mpt.show()
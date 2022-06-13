# pyplot繪圖
# 第三方外部引用,pip套件管理工具下載
# example 點點,及x軸y軸

from cProfile import label
import matplotlib.pyplot as mpt

xRowValues =[1,2,3,4]
yRowValues=[1,4,9,16]

mpt.plot(xRowValues,yRowValues,'ro')
mpt.axis([0,5,0,25])
mpt.show()
 
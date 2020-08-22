from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")


x =[1,2,3,4]
y =[4,5,6,7]


#设置图形大小
#plt.figure(figsize=(5,5),dpi=80)

# 绘制散点图
# plt.scatter(x,y)



# a=["战狼","速度与激情","功夫瑜伽"]
# b=[56,24,34]
# #柱状图
# plt.bar(range(len(a)),b,width=0.5)  #竖着的柱状图
# #plt.barh(range(len(a)),b,height=0.3)    横着的柱状图
# #plt.yticks(range(len(a)),a,fontproperties=my_font,rotation=45)
#  plt.xticks(range(len(a)),a,fontproperties=my_font,rotation=45)



#绘制直方图
plt.hist()


plt.show()

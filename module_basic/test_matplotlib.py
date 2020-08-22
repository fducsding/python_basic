from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")

x=range(2,26,2)
y=[15,13,14.5,17,20,25,26,26,27,22,18,15]

#设置图片大小
plt.figure(figsize=(5,5),dpi=80)


#绘图
plt.plot(x,y)


#设置x的刻度
plt.xticks(range(2,25))
plt.yticks(y)


#保存
plt.savefig("./t1.png")    #.表示当前目录的意思



#添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)   #matplotlib不会显示中文，
                                                                 # 所以还需要再引入font_manager

#展示图形
plt.show()

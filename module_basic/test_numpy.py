import numpy as np
import random


#使用numpy生成数组，得到ndarray数据类型
# t1=np.array([1,2,3])
# print(t1)
# print(type(t1))
#
#
# # t3=np.arange(10)  #等价于np.array(range(10))
# t3=np.arange(4,10,2)
# print(t3)







# #numpy中的数据类型
# t4=np.array(range(1,4),dtype="float32")
# print(t4)
# print(t4.dtype)
#
# #调整数据类型
# t5=t4.astype("int8")
# print(t5)
# print(t5.dtype)





# #numpy中的小数
# t7=np.array([random.random() for i in range(10)])
# print(t7)
# print(t7.dtype)
#
# t8=np.round(t7,2) #用round取两位小数
# print(t8)






# #取行操作
# tt=np.arange(50).reshape(10,5)
# print(tt)

# #取行
# print(tt[1])
# #连续取多行
# print(tt[5:])
# #取不连续的多行
# print(tt[[2,8,9]])


# #取第一列
# print(tt[:,0])  #逗号前面表示取行的
# #取连续的多列
# print(tt[:,2:])
# #取不连续的多列
# print(tt[:,[0,2]])
#
#
# #取第三行第四列的值
# print(tt[2,3])
# #取第三行到第五行，第二列到第四列的结果
# print(tt[2:5,1:4])       #    ：后的一个值取不到
# #取多个不相邻的点
# print(tt[[0,2],[0,1]])     #取的就是(0,0)(2,1)这两个值







#numpy中数值的修改

# tt[tt<5]=3   #tt中小于5的值改为3
# print(tt)

# tt=np.where(tt<10,0,10)    #tt<10就赋值为0，否则赋值为10
# print(tt)
# tt=tt.clip(10,18)    #clip裁剪  小于10的为10，大于18的为18
# print(tt)







# #数组的拼接
# t1=np.arange(10).reshape(2,5)
# t2=np.arange(11,21).reshape(2,5)

# #竖直拼接
# t1=np.vstack((t1,t2))
# print(t1)

# #水平拼接
# t1=np.hstack((t1,t2))
# print(t1)







#数组的行列交换
# tt[[1,2],:]=tt[[2,1],:]       #行交换
# tt[:,[1,2]]=tt[:[2,1]]        #列交换


# #创建一个全为0或1的数组
# print(np.zeros((2,3)))   #创建一个两行3列的数组全是0
# print(np.ones((2,3)))

# #创建一个对角线为1的正方形数组
# print(np.eye(3))


#获取最大值最小值的位置
# tt=np.arange(25).reshape(5,5)
# print(tt)
# print(np.argmax(tt,axis=0))    #axis代表轴的意思 0表示按列的意思























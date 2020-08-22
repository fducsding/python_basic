import pandas as pd
import numpy as np


#Series 表示一维，带标签的数组
# t1=pd.Series([1,23,2,5,3],index=list("abcde"))
# t1=pd.Series([1,23,2,5,3])
# print(t1)

# temp_dict={"name":"xiaohong","age":18,"tel":10083}
# t2=pd.Series(temp_dict)
# print(pd.Series(temp_dict))
# print(t2["age"])
# print(t2[0])
# print(t2[[0,1]])
# print(t2[["name","age"]])





#DataFrame对象既有行索引，又有列索引，是二维的
#横向索引叫index，0轴，axis=0
#纵向索引叫columns,1轴，axis=1
# tt=pd.DataFrame(np.arange(12).reshape(3,4))
# tt=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("qwer"))
# print(tt)

# d1={"name":["xiao","dfsa"],"age":[20,18],"tel":[100,200]}
# t1=pd.DataFrame(d1)
# print(t1)




#DataFrame中排序的方法
# df=pd.read_csv("文件名")
# df=df.sort_values(by="")



#pandas取行或列的注意点
# -- 方括号写数组，表示取行，对行进行操作
# -- 方括号写字符串，表示队列进行索引，对列进行操作


#pandas.loc通过标签索引行数据
#pandas.iloc通过位置获取行数据
t3=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(t3.loc["a",:])
print(t3.iloc[1,:])











import xlwt


'''
wookbook =xlwt.Workbook(encoding="utf-8")  #创建这个对象
wooksheet = wookbook.add_sheet("sheet1")   #创建工作表
wooksheet.write(0,0,"hello")  #写入数据，第一行参数是行，第二行是列，第三个参数是内容
wookbook.save("student.xls")
'''


wookbook =xlwt.Workbook(encoding="utf-8")  #创建这个对象
wooksheet = wookbook.add_sheet("sheet1")   #创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        wooksheet.write(i,j,"%d * %d = %d" %(i+1,j+1,(i+1)*(j+1)))


wookbook.save("student1.xls")

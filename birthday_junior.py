import xlrd
file_path=r'D:\pandownloader\初三2班身份证信息核对.xlsx'
data = xlrd.open_workbook(file_path)
table = data.sheet_by_name('Sheet1')
rows=1
birthday=[]
name=[]
for item in range(1,51):
    cell_value = table.cell(rows, 4).value
    cell_birth=cell_value[6:14:1]
    birthday.append(cell_birth)
    cell_name=str(table.cell(rows,2))
    cell_name_1=cell_name[6:9]
    whether=cell_name_1.find('\\')
    if whether==2:
        cell_name_1=cell_name_1[0:2]
    name.append(cell_name_1)
    rows+=1

with open('birthday.txt','w') as f:
    number=0
    for item in range(1,51):
        name_1=name[number]
        birthday_1=birthday[number]
        f.write(name_1+'   生日是'+birthday_1+'  \n')
        number+=1
# 1、xlwt 模块的初级使用
'''import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet# 创建一个workbook 设置编码
worksheet = workbook.add_sheet('My Worksheet')  # 表名
# 写入excel
# 参数对应 行, 列, 值
#worksheet.write(0, 0, label='姓名')
#worksheet.write(0, 1, label='生日')
rows_2=2
for item_1 in name:
    worksheet.write(rows_2, 0, label=item_1)
#for item_2 in birthday:
    #worksheet.write(rows_2, 1, label=item_2)
# 保存
workbook.save('.birthday.xls')'''
import xlwt

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(0, 0, label='姓名')
worksheet.write(0, 1, label='生日')
rows_2=1
for item in name:
    worksheet.write(rows_2, 0, label=item)
    rows_2+=1
rows_3=1
for item in birthday:
    worksheet.write(rows_3, 1, label=item)
    rows_3+=1
# 保存
workbook.save('junior_birthday.xls')


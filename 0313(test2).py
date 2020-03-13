# 统计字符串内元素类型的个数
intCount, strCount, otherCount = 0, 0, 0
strIn = input('输入任意字符串：')
# 将输入的语句切片变成列表操作
listIn = strIn.split()
# 遍历列表，分支判断统计数量
for i in listIn:
    if i.isalpha():
        strCount += 1
    elif i.isdigit():
        intCount += 1
    else:
        otherCount += 1
print('int型的个数是%d，str型的个数是%d，其他类型的个数是%d'
      % (intCount, strCount, otherCount))

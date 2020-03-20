# 简单的好友通讯录管理程序
# 保存已有通讯录，名字为键值（key），values为电话与地址组成的列表
dict1 = {'小明': ['001', '广州'],
         '小红': ['002', '深圳'],
         '小王': ['003', '北京'], }
print('1:添加 ， 2:删除 ， 3:查找 ， 4:修改 ')
# 在循环中等待输入操作
while 1:
    in_num = input('请输入你要进行的操作：')
    if in_num == '1':
        str1 = input('请输入添加的好友信息：')
        list1 = str1.split()
        dict1[list1[0]] =[list1[1], list1[2]]
        print(dict1)
    elif in_num == '2':
        str2 = input('请输入要删除的人员的名字：')
        del dict1[str2]
        print(dict1)
    elif in_num == '3':
        str3 = input('请输入要查找人的名字：')
        print('他的通讯信息是：', end='')
        print(dict1[str3])
    elif in_num == '4':
        str4 = input('请输入修改人的名字：')
        info = input('请重新填写修改人的信息：')
        list2 = info.split()
        dict1[str4] = [list2[0],list2[1]]
        print(dict1)


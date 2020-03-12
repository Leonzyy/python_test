# test1

# 提示字符串
str1 = '''
1.水瓶座 1.20-2.8
2.双鱼座 2.19-3.20
3.白羊座 3.21-4-19
4.金牛座 4.20-5.20
5.双子座 5.21-6.21
6.巨蟹座 6.22-7.22
7.狮子座 7.23-8.22
8.处女座 8.23-9.22'''

# 保存输入的姓名和星座序号
name = input('请输入您的名字：')
print(str1)
cons = int(input('请根据如上提示选择对应编号：'))
cons_act = ''

# 确认对应星座,python无switch语句，用字典和lambda实现
switch = {
    1: lambda: '水瓶座',
    2: lambda: '双鱼座',
    3: lambda: '白羊座',
    4: lambda: '金牛座',
    5: lambda: '双子座',
    6: lambda: '巨蟹座',
    7: lambda: '狮子座',
    8: lambda: '处女座',
}
cons_act=switch[cons]()

# 输出结果
print("%s,您好！%s的您星座分析结果为：结果。"%(name,cons_act))
# 对给定的两个数进行最大最大公约数最小公倍数的分析
str1 = input('请输入给定的两个数字：')
list_num = str1.split()
n = 0
for i in list_num:
    list_num[n] = int(i)
    n += 1
# 求最大公约数
A = set()
B = set()
for x in range(1, list_num[0]+1):
    if list_num[0]%x == 0:
        A.add(x)
for x in range(1, list_num[1]+1):
    if list_num[1]%x == 0:
        B.add(x)
print('最大公约数是：%d' % max(A & B))
# 求最小公倍数
a = set()
b = set()
for x in range (5):
    a.add(list_num[0]*(x+1))
    b.add(list_num[1]*(x+1))
print('最小公倍数是：%d' % min(a & b))



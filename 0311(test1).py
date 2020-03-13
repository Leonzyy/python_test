# 计算斐波那契数列前两项给定长度的数列，并删除重复项和追加数列各项之和为新项
# 新建数列，给定前两项
fib_list = [0, 1]
# 给定数列长度
size = input('请输入期望数列的长度:')
# 第一步：先得出原始的fib数列
i = 2
while i < int(size):
    fib_list.append(fib_list[i-1]+fib_list[i-2])
    i += 1
print('得到的Fib数列是：', end='')
print(fib_list)
# 移除第三项重复项，数列求和追加到尾部
fib_list.pop(2)
fib_list.append(sum(fib_list))
print('得到的新数列是：', end='')
print(fib_list)


# 使用lambda表达式实现对列表中的元素求平方
list_in = input('请输入要处理的列表：').split()
n = 0
# 将输入列表中的字符串变成数字
for i in list_in:
    list_in[n] = int(i)
    n += 1
# 调用map()函数，第二个参数为操作的列表，第一个参数为对列表操作的函数
# python3 map()返回一个迭代器，需要对其list()操作得到新的列表
print(list(map(lambda x: x ** 2, list_in)))



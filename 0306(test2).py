# test2

# m为个数，u为均值，σ2为方差，σ为标准差
m = s = σ2 = σ = 0

# 将输入函数返回的值赋予字符串，用split函数对字符串进行处理分割出数字
str_in = input("请输入任意个数值，用英文逗号(,)进行分隔:")
# .split()返回一个列表
str_num = str_in.split(",")

# 先求均值
for i in str_num:
    m += 1
    s += int(i)
u = s/m
s = 0

# 再求方差和标准差
for i in str_num:
    s += (int(i)-u) **2
σ2 = s/m
σ = pow(σ2,0.5)

print('均值为: %.1f \n方差为: %.1f \n标准差为: %.1f' % (u, σ2, σ))

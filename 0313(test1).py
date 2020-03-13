# 猜数字游戏，输出猜数次数
import random
number = random.randint(0,100)
guess = 0
your_num = int(input('请输入你猜的数字：'))
# 循环分支完成猜数游戏并输出猜数次数
while 1:
    if your_num > number:
        print('你猜的数大了，重新输入：', end='')
        your_num = int(input())
        guess += 1
        continue
    elif your_num < number:
        print('你猜的数小了，重新输入：', end='')
        your_num = int(input())
        guess += 1
        continue
    else:
        print('你猜对了！')
        break
print('正确的数字是%d,你猜了%d次' % (number, guess))


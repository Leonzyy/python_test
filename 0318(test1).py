# 构建一个计算列表中位数的函数
def calculate(*args):
    # 奇数个元素
    if len(args)%2 != 0:
        new_tuple = sorted(args)
    # 取排序后的中间位置的数取法：下标为对个数除2向下取整为中间的数
        print('计算的结果为：', end='')
        print(new_tuple[int(len(new_tuple) / 2)])
    # 偶数个元素
    else:
        new_tuple = sorted(args)
    # 排序后中间位置取法：下标为个数除2，以及个数除2-1
        print('计算的结果为：', end='')
        print((new_tuple[int(len(new_tuple)/2)]+
              new_tuple[int(len(new_tuple)/2)-1])/2)


calculate(6, 4, 3, 5, 1, 2)


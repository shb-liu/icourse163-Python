#ex601_CalStatisticsV1.py
def getNum():  # 获取用户不定长度的输入
    numbers = []    #本地可以实现，但是网页不能实现。
    number = input()    #在此确认原题：：获取以逗号分隔的多个数据输入（输入为一行）
    while number != "":
        numbers.append(eval(number))
        number = input()
    return numbers

def mean(numbers):  # 计算平均值
    sum = 0.0
    for number in numbers:
        sum += number
    return sum/len(numbers)

def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)

def median(numbers):  # 计算中位数
    #sorted(numbers)
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        med = (numbers[length//2] + numbers[length//2 - 1])/2
    else:
        med = numbers[length//2]
    return med

n = getNum()  # 主体函数
m = mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n,m), median(n)))
#ex_301_Workday.py
factorA = 0.01
powerA = pow((1 + factorA), 365)
def workdayPower(ft):
    powerB = 1  #属于该def内部参数，在内部定义。
    for i in range (365):
        if i % 7 in [6, 0]:
            powerB *= (1 - 0.01)
        else:
            powerB *= 1 + ft
    return powerB   #必须要返回一个值。
factorB = 0.01
while workdayPower(factorB) < powerA:
    factorB += 0.001
print('工作日的努力参数是: {:.3f}'.format(factorB))
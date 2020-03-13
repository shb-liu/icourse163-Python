#ex_401_CalBMI.py
h, w = eval(input())
bmi = w / (h ** 2)
if bmi < 18.5:
    gj, gn = "偏瘦", "偏瘦"
elif bmi < 24:
    gj, gn = "正常", "正常"
elif bmi < 25:
    gj, gn = "正常", "偏胖"
elif bmi < 28:
    gj, gn = "偏胖", "偏胖"
elif bmi < 30:
    gj, gn = "偏胖", "肥胖"
else:
    gj, gn = "肥胖", "肥胖"
print("BMI数值为:{:.2f}".format(bmi))
print("BMI指标为:国际'{}',国内'{}'".format(gj, gn))
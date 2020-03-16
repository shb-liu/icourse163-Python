t = input()
ori = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cod = "DEFGHIJKLMNOPQRSTUVWXYZABC"
oriL = ori.lower()
codL = cod.lower()
nT = ""
for i in t:
    if i in ori:
        nT += cod[ori.find(i)]
    elif i in oriL:
        nT += cod.lower()[ori.lower().find(i)]
    else:
        nT += i
print(nT)
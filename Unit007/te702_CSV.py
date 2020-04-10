#te702_CSV.py
f = open("data.csv")
t = f.readlines()
t = t[::-1]
for i in t:
    i = i.strip("\n")
    i = i.replace(" ","")
    ii = i.split(",")
    ii = ii[::-1]
    print(";".join(ii))
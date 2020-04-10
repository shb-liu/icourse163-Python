#ex705_CSVcl_BP.py
f = open("data.csv")
s = f.read()
s = s.replace(" ","")
print(s)
f.close()
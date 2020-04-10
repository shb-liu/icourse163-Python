#ex705_CSVcl.py
f = open("data.csv")
for line in f:
    print(line.replace(" ", "").replace("\n", ""))

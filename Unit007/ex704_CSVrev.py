#ex704_CSVrev.py
t = open("data.csv", "r")
for l in t:
    l = l.replace("\n", "")
    ll = l.split(",")
    print(",".join(ll[::-1]))

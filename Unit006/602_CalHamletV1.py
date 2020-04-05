#602_CalHamletV1.py
def getText():
    text = open("hamlet.txt", "r").read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        text = text.replace("ch", " ")
    return text

hamletText = getText()
words = hamletText.split()
counts = {} #创建字典
for word in words:
    counts[word] = counts.get(word,0) + 1   #以word为key，为其赋值
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
#try701.py
tf = open("f.txt", "rt")
print(tf.readline())
tf.close()

bf = open("f.txt", "rb")
print(bf.readline())
bf.close()
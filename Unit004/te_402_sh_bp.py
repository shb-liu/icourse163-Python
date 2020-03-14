#Prime
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
sum = 0
for i in range(2,1000):
    if is_prime(i):
        sum += i
print(sum)
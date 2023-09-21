def is_prime(n):
     avval = True
     for i in range(2, int(n**0.5) + 1):
          if n % i==0:
               avval = False
               break
     return avval


prime_count=0
last=0
for i in range(1, 1000001):
     if is_prime(i):
          last=i
          prime_count+=1

print(last)

sum=0
def zarib3or5(n):
    if n%3 ==0 or n%5 == 0:
        return True
    else:
        return False


for i in range(1, 1000 ):
    print ('checking', i)
    if zarib3or5(i) :
        sum = sum + i;


print('jam mazarebe 3 , 5  ta 10 mishe', sum)
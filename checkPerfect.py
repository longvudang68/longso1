def isPerfect(number):
    sum = 0
    for i in range (1,number):
        if number%i==0:
            sum+=i
        return sum==n
def checkAstrong(number):
    sum = 0
    m = number
    n = len(str(number)
    while number!=0:
        sum+=number%10**n
        number // = 10
    return sum==m 


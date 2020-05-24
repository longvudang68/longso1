def countUpper(string):
    uppercase = 0
    for letter in string:
        if letter.isupper():
            uppercase+=1
    return uppercase
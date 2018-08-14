def uppercase_lowercase(string):
    d={'upper':0,'lower':0}
    for x in string:
        if x.isupper():
            d['upper']+=1
        elif x.islower():
            d['lower']+=1
        else:
            pass
    print('the number of uppercase letters are',d['upper'])
    print('the number of lowercase letters are',d['lower'])

uppercase_lowercase('IIUHTFYGYT gstyssysy')                   

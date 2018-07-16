def char_occurence(string):
    dict={}
    for n in string:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_occurence(input("Enter a string")))

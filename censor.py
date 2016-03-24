def censor(text, word):
    text = text.split(" ")
    censor = word
    print censor
    censor = list(censor)
    newStr = []
    for i in range(0,len(censor)):
        censor[i - 1] = "*"
    censor =  "".join(censor)
    for i in text:
        if(i == word):
            newStr.append(censor)
        else:
            newStr.append(i)
            
    return " ".join(newStr)
    
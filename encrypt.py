import random
import string

#----------------------------------------------------
arr=[]
len_old=0
strink=''
after_dec=''
#----------------------------------------------------

def Encode(isss):
    #--------------------generating_lang----------------------
    language=[]
    newlanguage=[]
    for i in range(30) :
        language.append(random.choice(string.ascii_letters))
    for s in range(40) :
        language.append(random.choice(string.punctuation))
    for j in range(30):
        language.append(j)
    random.shuffle(language)
    #--------------------------------------------------------
    arr = list(isss)

    for i in range(len(arr)):
        newlanguage.append(language[i])
        language[i]=arr[i]
    len_old = len(newlanguage)
    new_en=''
    for j in range(len(newlanguage)):
        new_en= new_en + str(newlanguage[j])
    
    return new_en, language, len_old

def Decode(st,arr,len_old):
    back=[]
    new_de=''

    for i in range(len_old):
        back.append(arr[i])
    
    for j in range(len(back)):
        if j < len(back):
            new_de= new_de + str(back[j])

    return new_de 



strink,arr, len_old = Decode("how it")
# print(arr)
# print(strink)
# print('----after dec----')
after_dec = Decode(strink,arr,len_old)

# print(strink)
# print(after_dec)



#тест выражения с убратыми пробелами

#teststring="asFGFGFT asdf Affga"
def string_register(teststring):
    newstring = ""
    for letter in teststring:
        if letter.isupper():
            newstring+=letter.lower()
        else:
            newstring+=letter
    return(newstring)


text=input("фраза для теста на палиндром: ")

def reverse(text):
    b=string_register(text)
    a=b.replace(" ", "")
    if a==a[::-1]:
        print(text,"- это да, это палиндром")
    else:
        print(text," - это не палиндром")
reverse(text)






"""text="abcba" #test word
text1="oloo"
def reverse(text):
    if text==text[::-1]:
        print(text,"palyndrome")
    else:
        print(text,"nope")
reverse(text)
reverse(text1)"""





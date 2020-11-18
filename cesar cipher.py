def encrypt(input , shift):
    
    Capitals=["A","B","C","D","E","F","G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


    smalls=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    
    encrText=""
    for ch in input:
        if ch not in Capitals and ch not in smalls:
            encrText = encrText + ch
        elif ch.isupper():
            charIndex=Capitals.index(ch)
            newindex=(charIndex+shift)%26
            encrText=encrText+Capitals[newIndex]
        else:
            charIndex=smalls.index(ch)
            newIndex=(charIndex+shift)%26
            encrText=encrText+smalls[newIndex]


    return encrText


text= input("enter text: ")
s=int(input("enter shift number: "))
print("orignal text: ", text)
encryptedText=encrypt(text,s)

print("encrypted text:",encryptedText)
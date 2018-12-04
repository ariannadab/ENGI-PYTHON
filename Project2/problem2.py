def piggify(w):
    index=0
    wordadd=""

    w = w.lower()
    vowels='aeiou'
    if w[0] in vowels:
        return(print(w + "yay"))
    else:
        while w[index] not in vowels:
            wordadd+=w[index]
            index+=1
        return(print(w[index:len(w)]+wordadd+"ay"))
        
word=input("Enter a word to convert to pig latin: ")     
while(word[0]!="."):
      piggify(word)
      word=input("Enter a word to convert to pig latin: ")
exit()
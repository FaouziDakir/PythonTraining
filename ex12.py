alphabet = "abcdefghijklmnopqrstuvwxyz"
atbash = "zyxwvutsrqponmlkjihgfedcba"
sentence = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
encrypted = ""

for char in sentence:
    if char != " ": 
        index = alphabet.index(char)
        encrypted += atbash[index]
    else :
        encrypted += " "
    
print(encrypted)
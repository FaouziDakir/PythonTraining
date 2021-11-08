def pangram(arg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in arg.lower():
            return False
    return True

sentence = 'Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre'
if(pangram(sentence)):
    print("Your sentence is a pangram")
else:
    print("Your sentence is not a pangram")
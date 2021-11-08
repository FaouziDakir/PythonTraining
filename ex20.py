vowels = ('a','e','i','o','u','A','E','I','O','U')

sentence = "Long time no see"
pigSentence = ""
pigWord = ""

def first_vowel(s):
    for index, char in enumerate(s):
        if char in 'aeiouAEIOU':
            return index

for word in sentence.split():
    if word.startswith(vowels):
        pigWord = word + 'ay '
        pigSentence += pigWord
        pigSentence = pigSentence.lower()
    else:
        index = first_vowel(word)
        pigSentence += word[index:] + '-' + word[:index] + 'ay '
        pigSentence = pigSentence.lower()


print(pigSentence)

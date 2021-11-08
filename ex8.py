def anagram(list, word):
    counts = []
    for each in list:
        anagram = False
        if sorted(each) == sorted(word):
            anagram = True
        counts.append(anagram)
    return counts

list = ['enlists ','google', 'inlets', 'banana', 'silent']
listBoolean = anagram(list, 'listen')
booleanIndexes = [i for i, x in enumerate(listBoolean) if x]

for each in booleanIndexes:
    print(str(list[each]))
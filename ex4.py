test_string = 'free olly olly in come olly in free'
words = test_string.split()

wordsAndCount = dict((i, words.count(i)) for i in words)

for key, val in wordsAndCount.items():
    print(str(key) + " : " + str(val))
# Python code for run length encoding
from collections import OrderedDict

def encode(data):

	# Generate ordered dictionary of all lower
	# case alphabets, its output will be
	# dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0}
	dict=OrderedDict.fromkeys(data, 0)

	# Now iterate through input string to calculate
	# frequency of each character, its output will be
	# dict = {'w':4,'a':3,'d':1,'e':1,'x':6}
	for ch in data:
		dict[ch] += 1

	# now iterate through dictionary to make
	# output string from (key,value) pairs
	output = ''
	for key,value in dict.items():
		output = output + str(value) + key
	return output

def decode(data):
    output = ''
    for key,value in enumerate(data):
        if value.isdigit():
            char = data[key+1]
            for i in range(int(value)):
                output += char
    return output


    

data="wwwwaaadexxxxxx"
encodedData = "4w3a1d1e6x"
print(encode(data))
print(decode(encodedData))
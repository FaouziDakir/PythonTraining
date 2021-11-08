digits = "49142"
serie = 3

if serie > len(digits):
    print("Error you are asking for a serie bigger than the length of the number itself")
else:
    for i,e in enumerate(digits):
        if len(digits[i:i+serie]) == serie:
            print(digits[i:i+serie])
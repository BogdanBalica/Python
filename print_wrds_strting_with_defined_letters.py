quote = "Wheresoever you go, go with all your heart world"
word = ''
for letter in quote:
    if letter.isalpha():
        word += letter
    elif word.lower() >= 'h':
        print(word.upper())
        word = ''
    else:
        word = ''
if word.lower() >= 'h':
    print(word.upper())
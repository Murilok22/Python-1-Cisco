word_without_vowels = ""
user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

for vogal in user_word:
    if vogal == "A":
        continue
    elif vogal == "E":
        continue
    elif vogal == "I":
        continue
    elif vogal == "O":
        continue
    elif vogal == "U":
        continue
    else:
        word_without_vowels = word_without_vowels+vogal
# Imprima a palavra atribuída a word_without_vowels.
print(word_without_vowels)

text = [character for character in input()]

vowels = ['a', 'o', 'u', 'e', 'i']

text_without_vowels = [character for character in text
                       if character.lower() not in vowels]

print("".join(text_without_vowels))

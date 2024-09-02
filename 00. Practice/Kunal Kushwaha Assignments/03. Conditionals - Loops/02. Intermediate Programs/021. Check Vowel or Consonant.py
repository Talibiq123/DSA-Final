def check_vowel_or_consonant(letter):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    if letter.lower() in vowels:
        return "vowel"
    else:
        return "consonant"


user_input = input("Enter a letter: ").strip()

if len(user_input) == 1 and user_input.isalpha():
    result = check_vowel_or_consonant(user_input)
    print(f"The letter '{user_input}' is a {result}.")
else:
    print("Please enter a single alphabetical character.")

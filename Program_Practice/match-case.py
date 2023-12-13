def match_vowels(vowels):
    match vowels:
        case "a" : return ("it's a vowel")
        case "e" : return ("it's a vowel")
        case "i" : return ("it's a vowel")
        case "o" : return ("it's a vowel")
        case "u" : return ("it's a vowel")
        case  _: return ("it's not a vowel")

print(match_vowels("a"))
print(match_vowels("k"))
print(match_vowels("kaka"))

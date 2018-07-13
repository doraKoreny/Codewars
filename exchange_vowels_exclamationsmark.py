def replace_exclamation(s):
    for char in s:
        if char in "aeiouAEIOU":
            s = s.replace(char, "!")
    print(s)


replace_exclamation("Hi!")

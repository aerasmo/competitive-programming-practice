def get_count(input_str):
    num_vowels = 0
    for c in input_str:
        if c in "aeiou":
            num_vowels += 1
    return num_vowels
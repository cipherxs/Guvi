def most_frequent_character(input_string):
    char_count = {}
    for char in input_string:
        if char.isalpha():  # Only consider alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1

    most_frequent_char = max(char_count, key=char_count.get)
    return most_frequent_char, char_count[most_frequent_char]

def count_unique_characters(input_string):
    unique_chars = set(input_string)
    return len(unique_chars)

# Example usage
input_string = "hello"
unique_char_count = count_unique_characters(input_string)
print(unique_char_count)

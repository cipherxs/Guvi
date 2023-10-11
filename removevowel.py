def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result

# Example usage
input_string = "Hello, how are you?"
result_string = remove_vowels(input_string)
print(result_string)

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    individual_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in input_string:
        if char in vowels:
            vowel_count += 1
            char = char.lower()
            individual_counts[char] += 1

    return vowel_count, individual_counts

input_string = "Hello, how are you?"
total_vowels, individual_counts = count_vowels(input_string)

print(f"Total vowels: {total_vowels}")
print(f"Individual counts:")
for vowel, count in individual_counts.items():
    print(f"{vowel}: {count}")

def vowel_counter(array: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for letter in list(array):
        if letter in vowels:
            counter += 1
            return print(counter)
vowel_counter("heellow asd")
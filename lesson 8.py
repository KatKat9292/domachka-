"""def vowel_counter(array: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for letter in list(array):
        if letter in vowels:
            counter += 1
            return print(counter)
vowel_counter("heellow asd")"""

def remove_vowel(array: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    for element in array:
        if element in vowels:
            array = array.replace(element, '')
    return array
print(remove_vowel("heellow asd"))



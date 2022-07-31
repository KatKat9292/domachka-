"""def vowel_counter(array: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for letter in list(array):
        if letter in vowels:
            counter += 1
            return print(counter)
vowel_counter("heellow asd")"""

""""def remove_vowel(array: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    for element in array:
        if element in vowels:
            array = array.replace(element, '')
    return array
print(remove_vowel("heellow asd"))"""

"""def digits_counter(nums: str) -> list:
    new_nums = nums.split()
    numbers = [int(i) for i in new_nums]
    return [sorted(numbers)[0], sorted(numbers)[-1]]
print(digits_counter("1 2 -5 3 12"))"""


def centre(array: str) -> str:
    if len(array) % 2 == 0:
        array = array[int(len(array)/2 - 1 ): int(len(array)/2 + 1)]
    else:
        array = array[len(array) // 2]
    return array
print(centre("testt"))



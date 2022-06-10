def count_vowels(text: str):
    count = 0
    for c in text:
        if c in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


def count_consonents(text: str):
    return len(text) - count_vowels(text)


def has_common_factor(x, y):
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            return True

    return False

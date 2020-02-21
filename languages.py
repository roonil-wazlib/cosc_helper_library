import math

def concatenate_strings(a, b):
    """get ab"""
    result = ""
    for s in a:
        if s != "$":
            result += s
    for s in b:
        if s != "$":
            result += s
    return "$" if result == "" else result


def concatenate_languages(a, b):
    """Get list of all strings in ab"""
    ab = set()
    for i in a:
        for j in b:
            ab.add(concatenate_strings(i, j))
    return list(ab)


def get_size(a):
    """Return  |a|"""
    return len(list(set(a)))


def get_number_string_of_size(alphabet, size):
    """Return number of strings of size"""
    length_alphabet = get_size(alphabet)
    return length_alphabet ** size


def get_number_string_upto_size(alphabet, size):
    """Return number of strings less than or equal to size"""
    total = 0
    length_alphabet = get_size(alphabet)
    for i in range(1, size + 1):
        total += length_alphabet ** i

    return total + 1 #add one for epsilon


def all_strings(alphabet, size):
    """Return all strings of a given size over the alphabet"""

    def get_next_iteration():
        new_strings = []
        for symbol in alphabet:
            this_symbol_strings = [str(symbol) + str(x) for x in current_strings]
            new_strings.extend(this_symbol_strings)

        return new_strings

    current_strings = alphabet.copy()
    for _ in range(size - 1):
        current_strings = get_next_iteration()

    if size == 0 or len(alphabet) == 0:
        return ['']
    else:
        return current_strings
    
    
print(sorted(all_strings({}, 1)))

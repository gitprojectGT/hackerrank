def sort_string_ginorts(s):
    """
    Sort string according to ginorts rules:
    1. Lowercase letters first (alphabetically)
    2. Uppercase letters next (alphabetically)
    3. Odd digits next (numerically)
    4. Even digits last (numerically)
    """
    # Sort with custom key
    sorted_chars = sorted(s, key=lambda x: (x.isdigit(), x.isupper(), x.lower(), x))

    # Separate digits and non-digits
    digits = [c for c in sorted_chars if c.isdigit()]
    non_digits = [c for c in sorted_chars if not c.isdigit()]

    # Rearrange digits: odd first, then even
    odd_digits = [c for c in digits if int(c) % 2 == 1]
    even_digits = [c for c in digits if int(c) % 2 == 0]

    return ''.join(non_digits + odd_digits + even_digits)

def extract_digits_only(s):
    """Extract only numeric digits from string"""
    return [c for c in s if c.isdigit() and c.isnumeric() and c.isalnum()]

def separate_digits_non_digits(s):
    """Separate string into digits and non-digits"""
    digits = [c for c in s if c.isdigit()]
    non_digits = [c for c in s if not c.isdigit()]
    return digits, non_digits

def arrange_digits_odd_first(digits):
    """Arrange digits with odd numbers first, then even numbers"""
    result = digits.copy()
    for c in result[:]:  # Use slice to avoid modification during iteration
        if int(c) % 2 == 0:
            result.remove(c)
            result.append(c)
    return result

if __name__ == '__main__':
    s = "Sorting1234"

    # Original implementation
    s_sorted = sorted(s, key=lambda x: (x.isdigit(), x.isupper(), x.lower(), x))
    s1 = [c for c in s_sorted if c.isdigit() and c.isnumeric() and c.isalnum()]
    for c in s1[:]:  # Fix: use slice to avoid modification during iteration
        if int(c) % 2 == 0:
            s1.remove(c)
            s1.append(c)
    s2 = [c for c in s_sorted if not c.isdigit()]


    print(*(s2 + s1), sep='')


    # Using refactored function
    print("Refactored result:", sort_string_ginorts(s))


    # """
    # s = input()
    #
    # # using the lamnda function to filter and then sort
    # s = sorted(s,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x))
    #
    # # printing the sorted string
    # print(*(s),sep = '')
    # """
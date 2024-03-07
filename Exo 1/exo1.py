def count_upper_lower_case(source):
    upper = 0
    lower = 0
    for char in source:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower
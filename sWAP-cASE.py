def swap_case(s):
    updated_string = ""
    for char in s:
        if (char.islower() == True):
            updated_string += char.upper()
        elif (char.isupper() == True):
            updated_string += char.lower()
        else:
            updated_string += char
    return updated_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

def count_substring(string, sub_string):
    if (sub_string not in string):
        return 0
    index = string.find(sub_string)
    count = 1
    while True:
        n_index = string.find(sub_string, index+1)
        if (n_index == -1):
            break
        count += 1
        index = n_index
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

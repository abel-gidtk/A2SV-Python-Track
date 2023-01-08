def split_and_join(line):
    updated_line = line.split(" ")
    return "-".join(updated_line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

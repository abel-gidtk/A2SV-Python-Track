if __name__ == '__main__':
    li = list()
    N = int(input())
    for i in range(N):
        command = str(input())
        if ("insert" in command):
            new_c = command.split(" ");
            li.insert(int(new_c[1]), int(new_c[2]))
        elif("print" in command):
            print(li)
        elif("sort" in command):
            li.sort()
        elif("pop" in command):
            li.pop()
        elif("append" in command):
            new_c = command.split(" ")
            li.append(int(new_c[1]))
        elif("reverse" in command):
            li.reverse()
        elif("remove" in command):
            new_c = command.split(" ")
            li.remove(int(new_c[1]))

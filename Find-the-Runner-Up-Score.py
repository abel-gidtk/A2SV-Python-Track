if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    li = list()
    for num in arr:
        li.append(num)
    li.sort()
    for i in range(n-1, -1, -1):
        if (li[i] < max(li)):
            print(li[i])
            break

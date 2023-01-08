if __name__ == '__main__':
    li = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.extend([[name, score]])
    
    names = list()
    scores = set()
    for i in li:
        scores.add(i[1])
    scores = list(scores)
    scores.sort()
    
    for i in li:
        if (i[1] == scores[1]):
            names.append(i[0])
    
    names.sort()
    for name in names:
        print(name)

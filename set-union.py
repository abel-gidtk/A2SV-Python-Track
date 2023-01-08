# Enter your code here. Read input from STDIN. Print output to STDOUT
num_eng = int(input())
roll_eng = input().split()
num_frn = int(input())
roll_frn = input().split()

total = set(roll_eng).union(set(roll_frn))
print(len(total))

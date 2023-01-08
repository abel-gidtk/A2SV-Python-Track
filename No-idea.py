# Enter your code here. Read input from STDIN. Print output to STDOUT
sizes = input().split()
size_a = int(sizes[0])
size_b = int(sizes[1])
arr = input().split()
list_a = input().split()
list_b = input().split()
set_a = set()
set_b = set()

for num in list_a:
    set_a.add(num)
    
for num in list_b:
    set_b.add(num)

happiness = 0

for i in arr:
    if (i in set_a):
        happiness += 1
    elif (i in set_b):
        happiness -= 1

print(happiness)

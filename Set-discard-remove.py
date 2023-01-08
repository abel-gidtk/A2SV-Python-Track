# Enter your code here. Read input from STDIN. Print output to STDOUT
nums = set()
set_size = int(input())
elem_list = input().split()
elem_list.reverse()

for i in elem_list:
    nums.add(i)

comm_size = int(input())
for i in range(comm_size):
    command = str(input())
    if ("remove" in command):
        comm = command.split()
        if (comm[1] in nums):
            nums.remove(comm[1])
            
    elif ("discard" in command):
        comm = command.split()
        nums.discard(comm[1])
        
    elif ("pop" in command):
        nums.pop()
        

sum = 0
for num in nums:
    sum += int(num)

print(sum)

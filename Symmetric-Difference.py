# Enter your code here. Read input from STDIN. Print output to STDOUT
num_m = int(input())
list_m = str(input())
num_n = int(input())
list_n = str(input())

set_m = set(list_m.split())
set_n = set(list_n.split())

sym_diff = set_m.difference(set_n).union(set_n.difference(set_m))
sym_diff_list = list(sym_diff)
for num in range(0, len(sym_diff_list)):
    sym_diff_list[num] = int(sym_diff_list[num])
    
sym_diff_list.sort()
for i in sym_diff_list:
    print(i)

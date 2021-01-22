import sys

nums = sys.stdin.readline()

x = nums.split()
new_list = []
for i in range(int(x[0]), int(x[-1])+1):
    if(len(set(str(i)))) ==1:
        new_list.append(str(i))
print(len(new_list))

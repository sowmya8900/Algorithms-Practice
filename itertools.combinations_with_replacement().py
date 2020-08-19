from itertools import combinations_with_replacement
string = str(input()).split()
lst = []
ls = []
sl = (list(combinations_with_replacement(string[0], int(string[1]))))
for i in sl:
    ls.append(sorted(i))
for i in ls:
    lst.append(''.join(i))
lst.sort()
for j in lst:
    print(j)

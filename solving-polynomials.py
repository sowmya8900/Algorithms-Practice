def calculate(x, string, k):
    for i in string:
        if (i == 'x'):
            i = x
    if (eval(string) == k):
        print("True")
    else: 
        print("False")

num = list(map(int, input().split()))
string = str(input())
calculate(num[0], string, num[1])

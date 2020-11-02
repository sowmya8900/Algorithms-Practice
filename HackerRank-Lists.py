if __name__ == '__main__':
    N = int(input())
    lst = []
    for n in range(N):
        command = input()
        commands = command.split()
        if commands[0] == "print":
            print(lst)
        
        if commands[0] == "append":
            lst.append(int(commands[1]))
        
        if commands[0] == "pop":
            lst.pop(len(lst) - 1)

        if commands[0] == "reverse":
            lst.reverse()
        
        if commands[0] == "sort":
            lst.sort()

        if commands[0] == "remove":
            lst.remove(int(commands[1]))
        
        if commands[0] == "insert":
            lst.insert(int(commands[1]), int(commands[2]))

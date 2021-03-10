import sys

M = int(input())

bit = 0
for _ in range(M):
    cmd = sys.stdin.readline().split()
    num = int(cmd[1]) - 1

    if cmd[0] == 'add': 
        bit |= (1 << num)

    elif cmd[0] == 'remove':
        bit &= ~(1 << num)
    
    elif cmd[0] == 'check':
        if bit & (1 << num) == 0:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'toggle':
        bit ^= (1 << num)

    if cmd[0] == 'all':
        bit = (1 << 20) - 1

    if cmd[0] == 'empty':
        bit = 0
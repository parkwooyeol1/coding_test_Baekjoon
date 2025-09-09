import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    order_list = sys.stdin.readline().strip().split()
    if len(order_list) == 2:
        stack.append(int(order_list[1]))
    else:
        if order_list[0] == 'pop':
            if stack:
                a = stack.pop()
                print(a)
            else:
                print(-1)
        elif order_list[0] == 'size':
            print(len(stack))
        elif order_list[0] == 'empty':
            if not stack:
                print(1)
            else:
                print(0)
        elif order_list[0] == 'top':
            if stack:
                print(stack[len(stack)-1])
            else:
                print(-1)

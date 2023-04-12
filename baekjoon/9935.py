
main_string = input().strip()
pattern = input().strip()
pattern_len = len(pattern)

stack = []
for i in range(len(main_string)):
    stack.append(main_string[i])

    if (''.join(stack[-pattern_len:]) == pattern):
        for _ in range(pattern_len):
            stack.pop()

if (stack):
    print(''.join(stack))
else:
    print("FRULA")
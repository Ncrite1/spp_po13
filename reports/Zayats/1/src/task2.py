s = input("Введите строку: ")

stack = []
flag = True

for c in s:
    if c in ('(', '[', '{'):
        stack.append(c)
    else:
        if not stack:
            flag = False
            break

        last = stack.pop()

        if (c, last) not in {(')', '('), (']', '['), ('}', '{')}:
            flag = False
            break

if stack:
    flag = False

print(flag)

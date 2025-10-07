n = 5

for i in range(n):
    for j in range(i + 1):
        print("*", end=' ')
    print()

print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()

print()

for i in range(n):
    for j in range(n):
        if j < i:
            print("  ", end='')
        else:
            print("* ", end='')
    print()

print()

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print("  ", end='')
        else:
            print("* ", end='')
    print()
print()

for i in range(n):
    for j in range(n-1-i):
        print("  ", end='')
    for j in range(i*2+1):
        print("* ", end='')
    for j in range(n-1-i):
        print("  ", end='')
        
    print()
print()

for i in range(n,0,-1):
    for j in range(n-i):
        print("  ", end='')
    for j in range(i*2-1):
        print("* ", end='')
    for j in range(n-i):
        print("  ", end='')
        
    print()
print()
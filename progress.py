total = 100

print('progress: ', end='')
for i in range(total):
    if (((i/total)*100)%10 == 0):
        print('#', end='')
print()
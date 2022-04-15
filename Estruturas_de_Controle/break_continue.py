for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

print('----------------------------------')

for x in range(1, 11):
    if x == 5:
        break
    print(x)

print(
    'The break left the loop and goes to the next block in the code'
)

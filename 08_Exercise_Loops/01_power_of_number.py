number = int(input())
pow = int(input())

result = 1

for i in range(1, pow + 1):
    result *= number
    i += 1

print(result)
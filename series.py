a: int = 1
b: int = 2
n: int = int(input())

for i in range (1, n+1):
    Un: int = a + b*(i-1)
    print(Un, end=' ')

print()




a: int = 4
r: int = 3
n: int = int(input())

for i in range (1, n+1):
    Un: int = a * r**(i-1)
    print(Un, end=' ')

print()
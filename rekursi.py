n: int = int(input())

def hitung_faktorial(n :int) -> int:
    if n == 0 or n==1:
        return 1
    else:
        return n*hitung_faktorial(n-1)


hasil_hitung_faktorial: int = hitung_faktorial(n)
print(f"{n}! = {hasil_hitung_faktorial}.")



a= "ab"
b=""
c = a-b
print(c)
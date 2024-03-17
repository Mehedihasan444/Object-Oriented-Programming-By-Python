def find_prime_number(a:int):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
n=int(input())
result = find_prime_number(n)
print(result)
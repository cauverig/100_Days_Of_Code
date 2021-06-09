import math
n = int(input("n= "))
numbers = list(map(int, input().split()))

arith_mean = sum(numbers)/n
arith_mean = round(arith_mean, 2)

geom_mean = math.prod(numbers) ** (1/n)
geom_mean = round(geom_mean, 2)

sum1 = 0

for i in numbers:
    sum1 += (1/i)

harmonic_mean = sum1/n
harmonic_mean = round(harmonic_mean, 2)

print(f"Arithmetic mean= {arith_mean}")
print(f"Geometric mean= {geom_mean}")
print(f"Harmonic mean= {harmonic_mean}")
population = 620_000.0
target = 1_500_000
growth_rate = 1.037
year = 2021
print(f"\nНаселение на {year} равно {population} тыс.")
while population <= target:
    population = population * growth_rate
    year += 1
print(f"\nНаселение превысит 1.5 млн человек в {year} году.")
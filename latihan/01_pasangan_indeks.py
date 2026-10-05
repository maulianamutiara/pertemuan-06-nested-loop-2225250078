# Latihan 1 - Pasangan Indeks
# Loop luar mengatur nilai i
# Loop dalam mengatur nilai j
# Counter menghitung banyak pasangan

count = 0

for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")
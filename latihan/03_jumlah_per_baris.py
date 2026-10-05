# Latihan 3 - Jumlah Per Baris
# Loop luar menentukan baris
# total_baris direset setiap baris
# Loop dalam menghitung i * j

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        total_baris += i * j

    print(f"Jumlah baris {i} = {total_baris}")
# Pertemuan 06 Nested Loop Python

Nama: Mauliana Mutiara 

NIM: 2225250078  

Kelas: 3A  


## Tujuan

Pada pertemuan ini saya belajar menggunakan nested loop pada Python. Materi yang dipelajari meliputi pembuatan pola, akumulasi, pencacahan, serta cara melakukan pengujian program.

## Cara Menjalankan

Program Tugas 3 dapat dijalankan melalui terminal VS Code dengan perintah:

    python3 tugas/tabel_perkalian_dan_statistik.py

Setelah program dijalankan, masukkan nilai `n` berupa bilangan positif.

## Algoritma Tugas 3

Program ini digunakan untuk membuat tabel perkalian dan menghitung jumlah setiap baris, jumlah seluruh hasil perkalian, serta banyak hasil perkalian yang genap.

Langkah-langkahnya:

1. Memasukkan nilai `n`.
2. Jika `n` kurang dari atau sama dengan 0, program meminta input kembali.
3. Membuat `total_semua` untuk menyimpan jumlah seluruh hasil perkalian.
4. Membuat `count_genap` untuk menghitung banyak hasil perkalian yang genap.
5. Loop luar digunakan untuk menentukan baris.
6. Pada setiap baris, `total_baris` diatur menjadi 0.
7. Loop dalam digunakan untuk menentukan kolom.
8. Menghitung hasil perkalian `i * j`.
9. Hasil perkalian ditambahkan ke `total_baris` dan `total_semua`.
10. Jika hasil perkalian genap, `count_genap` ditambah 1.
11. Setelah satu baris selesai, jumlah baris ditampilkan.
12. Setelah semua proses selesai, program menampilkan total seluruh hasil dan banyak hasil genap.

## Hasil Pengujian

| Input | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| n = 1 | Total = 1, genap = 0 | Total = 1, genap = 0 | Berhasil |
| n = 2 | Total = 9, genap = 3 | Total = 9, genap = 3 | Berhasil |
| n = 3 | Total = 36, genap = 5 | Total = 36, genap = 5 | Berhasil |

### Pengujian n = 1

    1 | jumlah baris = 1
    Total seluruh hasil = 1
    Banyak hasil genap = 0

### Pengujian n = 2

    1   2 | jumlah baris = 3
    2   4 | jumlah baris = 6
    Total seluruh hasil = 9
    Banyak hasil genap = 3

### Pengujian n = 3

    1   2   3 | jumlah baris = 6
    2   4   6 | jumlah baris = 12
    3   6   9 | jumlah baris = 18
    Total seluruh hasil = 36
    Banyak hasil genap = 5

## Analisis Efisiensi

Program menggunakan dua loop yang bersarang. Loop luar berjalan sebanyak `n` kali dan setiap kali loop dalam juga berjalan sebanyak `n` kali.

Jadi, jumlah perulangan pada bagian dalam adalah:

`n × n = n²`

Contohnya, jika `n = 3`, pernyataan `hasil = i * j` dijalankan sebanyak:

`3 × 3 = 9 kali`

Semakin besar nilai `n`, semakin banyak proses yang dilakukan oleh program.

## Refleksi

1. **Mengapa `total_baris` direset di setiap iterasi loop luar?**

   `total_baris` direset menjadi 0 setiap kali loop luar memulai baris baru karena variabel tersebut digunakan untuk menghitung jumlah hasil perkalian pada satu baris saja. Jika tidak direset, jumlah dari baris sebelumnya akan ikut terbawa ke baris berikutnya.

2. **Mengapa `total_semua` tidak direset di setiap baris?**

   `total_semua` tidak direset karena variabel ini digunakan untuk menghitung jumlah seluruh hasil perkalian dari semua baris. Jadi nilainya harus terus bertambah sampai semua proses selesai.

3. **Untuk `n`, berapa kali pernyataan `hasil = i * j` dieksekusi?**

   Pernyataan `hasil = i * j` dieksekusi sebanyak `n × n` atau `n²` kali. Hal ini karena loop luar berjalan `n` kali dan pada setiap iterasi loop luar, loop dalam juga berjalan `n` kali.

4. **Bagaimana membuktikan `count_genap` benar?**

   `count_genap` bertambah satu hanya ketika hasil perkalian memenuhi kondisi `hasil % 2 == 0`. Jadi setiap hasil perkalian yang genap akan dihitung satu kali. Contohnya pada `n = 2`, hasil perkaliannya adalah 1, 2, 2, dan 4. Hasil yang genap ada 3, sehingga `count_genap = 3`.

5. **Apa bagian program yang akan paling banyak melakukan operasi ketika `n` membesar?**

   Bagian yang paling banyak melakukan operasi adalah loop dalam karena berada di dalam loop luar. Setiap loop luar berjalan, loop dalam akan berjalan sebanyak `n` kali. Oleh karena itu, jumlah eksekusi pada bagian tersebut menjadi `n²`.

Dari latihan ini saya memahami bahwa posisi variabel dalam nested loop perlu diperhatikan. Saya juga memahami perbedaan antara akumulator untuk jumlah per baris dan jumlah keseluruhan, serta counter untuk menghitung banyak kejadian yang memenuhi kondisi. Selain itu, saya perlu memperhatikan indentasi karena pada Python indentasi menentukan bagian dari loop dan kondisi.
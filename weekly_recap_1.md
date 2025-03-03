# Weekly Recap 1

1. Kamu ingin mencatat pengeluaran harian tanpa menggunakan perulangan atau kondisi. Program ini akan:

   - Meminta data pengguna: nama, umur, saldo awal.
   - Menyimpan pengeluaran: hanya bisa mencatat tiga barang.
   - Menghitung total pengeluaran dan sisa saldo.
   - Menampilkan ringkasan pengeluaran.

   Input:

   ```
    Masukkan nama Anda: Budi
    Masukkan umur Anda: 25
    Masukkan saldo awal Anda: 100000
    Masukkan nama barang pertama: Nasi Goreng
    Masukkan harga barang pertama: 25000
    Masukkan nama barang kedua: Es Teh
    Masukkan harga barang kedua: 5000
    Masukkan nama barang ketiga: Buku
    Masukkan harga barang ketiga: 35000
   ```

   Output:

   ```
    === RINGKASAN PENGELUARAN ===
    Nama: Budi
    Umur: 25 tahun

    Daftar Pengeluaran:
    1. Nasi Goreng - Rp25.000
    2. Es Teh - Rp5.000
    3. Buku - Rp35.000

    Total Pengeluaran: Rp65.000
    Sisa Saldo: Rp35.000
   ```

   **Notes**:

   - Tidak boleh menggunakan For/While loop dan If conditional.
   - Plus point jika dapat menerapkan `dictionary` untuk menyimpan informasi barang.
   - Kerjakan di file script python (`.py`).

2. Kamu adalah seorang guru dan ingin membuat program sederhana untuk menghitung nilai rata-rata siswa berdasarkan beberapa mata pelajaran. Program ini akan:

   - Meminta jumlah mata pelajaran yang diikuti siswa.
     - Optional: menerapkan validasi input
   - Meminta input nilai untuk setiap mata pelajaran.
     - Optional: menerapkan validasi input
   - Menghitung rata-rata nilai.
   - Menentukan predikat berdasarkan nilai rata-rata:
     ```
       ≥ 90 → "Sangat Baik"
       ≥ 80 → "Baik"
       ≥ 70 → "Cukup"
       < 70 → "Perlu Perbaikan"
     ```
   - Menampilkan hasil akhir.

   Input:

   ```
    Masukkan jumlah mata pelajaran: 3
    Masukkan nilai mata pelajaran ke-1: 85
    Masukkan nilai mata pelajaran ke-2: 90
    Masukkan nilai mata pelajaran ke-3: 78
   ```

   Output:

   ```
    Rata-rata nilai: 84.3
    Predikat: Baik
   ```

   **Notes**:

   - Tidak boleh menggunakan function `sum()`.
   - Kerjakan di file script python (`.py`).

3. Kamu ingin membuat program untuk menghitung BMI (Body Mass Index) seseorang berdasarkan berat dan tinggi badan mereka. Program ini akan menggunakan function untuk modularisasi kode dan juga menerapkan import package `math` untuk perhitungan kuadrat tinggi badan.

   Yang dilakukan program:

   - Meminta input nama, berat badan (kg), dan tinggi badan (cm).
   - Menggunakan function untuk menghitung BMI dengan rumus:
     ```
     BMI = berat / (tinggi ** 2)
     ```
   - Menggunakan function untuk menentukan kategori BMI:
     ```
     BMI < 18.5 → "Kurus"
     18.5 ≤ BMI < 25 → "Normal"
     25 ≤ BMI < 30 → "Kelebihan Berat Badan"
     BMI ≥ 30 → "Obesitas"
     ```
   - Menampilkan hasil akhir berupa nama, nilai BMI, dan kategorinya

   Input:

   ```
   Masukkan nama Anda: Andi
   Masukkan berat badan Anda (kg): 70
   Masukkan tinggi badan Anda (cm): 175
   ```

   Output:

   ```
   Halo, Andi!
   BMI Anda: 22.9
   Kategori: Normal
   ```

   **Notes**:

   - Tidak boleh menggunakan function `sum()`.
   - Kerjakan di file script python (`.py`).

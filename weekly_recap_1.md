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

# 📝 Pandas - Exercise 

## 📄 Setup
- Dataset [ini](https://raw.githubusercontent.com/yuda-notes/teaching-notes/refs/heads/main/dataset/trending-youtube-videos.csv) berisi informasi tentang 1000 video trending di YouTube. 
- Data sudah dibersihkan, sehingga kamu tidak perlu menangani missing values atau mengubah tipe data.
- Kolom-kolom yang tersedia meliputi:
  - `video`: Judul video  
  - `video_views`: Jumlah penayangan  
  - `likes`: Jumlah suka  
  - `dislikes`: Jumlah tidak suka  
  - `category`: Kategori video  
  - `published`: Tahun publikasi  

> Kerjakan di notebook `.ipynb`

## 1. Data Loading
- Baca file CSV dari URL [berikut](https://raw.githubusercontent.com/yuda-notes/teaching-notes/refs/heads/main/dataset/trending-youtube-videos.csv) ke dalam DataFrame

## 2. Data Exploration
- Tampilkan 5 baris pertama dari data.
- Tampilkan informasi umum dari data dengan `.info()`.
- Tampilkan ringkasan statistik dari kolom numerik dengan `.describe()`.

## 3. Data Manipulation
- Ambil 10 data pertama untuk kategori “Music”.
- Hapus semua baris dengan kategori “Gaming”.
- Ambil semua data dari video yang dipublikasikan sebelum tahun 2021.
- Tambahkan kolom baru bernama `label` yang isinya berupa string gabungan antara `video` dan `category` (contoh: `Funny Cats - Comedy`).

## 4. Data Aggregation and Grouping
- Hitung jumlah video untuk setiap kategori (`category`).
- Tampilkan kategori dengan jumlah video terbanyak.
- Hitung rata-rata `views` berdasarkan tahun publikasi.

## 🚀 Bonus - Optional
- Simpan DataFrame hasil akhir ke file baru bernama `processed_trending_videos.csv`.

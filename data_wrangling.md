# Data Wrangling

## Exercise
1. Buat query untuk mengambil hanya tiga huruf pertama dari subscriber_type dan menggabungkannya dengan bike_type. Hasilnya diberi alias short_info.
2. Tampilkan jumlah perjalanan yang terjadi per bulan. Gunakan fungsi EXTRACT untuk mengambil bulan dari start_time.
3. Tampilkan semua perjalanan yang memiliki durasi lebih dari rata-rata durasi perjalanan dalam dataset. Gunakan subquery untuk menghitung rata-rata durasi.
4. Buat query yang mengkategorikan perjalanan berdasarkan durasi:
    - Jika duration_minutes kurang dari 5 menit, labeli sebagai 'Short'
    - Jika duration_minutes antara 5 dan 30 menit, labeli sebagai 'Medium'
    - Jika lebih dari 30 menit, labeli sebagai 'Long'
    - Hasilnya diberi alias `trip_category`.

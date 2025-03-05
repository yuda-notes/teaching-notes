# Data Wrangling

## Exercise
1. Buat query untuk mengambil hanya tiga huruf pertama dari `subscriber_type` dan menggabungkannya dengan `bike_type`. Hasilnya diberi alias `short_info`.
    - Contoh output:

      <img width="148" alt="image" src="https://github.com/user-attachments/assets/b67e1edc-687d-4893-9872-52a915987c22" />

2. Tampilkan jumlah perjalanan yang terjadi per bulan. Gunakan fungsi `EXTRACT` untuk mengambil bulan dari `start_time`.
    - Contoh output:
    
      <img width="272" alt="image" src="https://github.com/user-attachments/assets/272f7428-1082-465d-9847-df27e287d878" />

3. Tampilkan semua perjalanan yang memiliki durasi lebih dari rata-rata durasi perjalanan dalam dataset. Gunakan subquery untuk menghitung rata-rata durasi.
    - Contoh output:

      <img width="1371" alt="image" src="https://github.com/user-attachments/assets/9c2e310c-17f9-4e5e-a6d7-3c1d41192b70" />

4. Buat query yang mengkategorikan perjalanan berdasarkan durasi:
    - Jika duration_minutes kurang dari 5 menit, labeli sebagai 'Short'
    - Jika duration_minutes antara 5 dan 30 menit, labeli sebagai 'Medium'
    - Jika lebih dari 30 menit, labeli sebagai 'Long'
    - Hasilnya diberi alias `trip_category`.
    - Contoh output:

      <img width="407" alt="image" src="https://github.com/user-attachments/assets/cf4c3e51-d776-4343-b4f5-f5d4e7d19dc8" />


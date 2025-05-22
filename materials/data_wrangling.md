# Data Wrangling

## Exercise
1. Buat query untuk mengambil hanya tiga huruf pertama dari `subscriber_type` dan menggabungkannya dengan `bike_type`. Hasilnya diberi alias `short_info`.
    - Contoh output:

      <img width="148" alt="image" src="https://github.com/user-attachments/assets/b67e1edc-687d-4893-9872-52a915987c22" />

2. Tampilkan jumlah perjalanan yang terjadi per bulan. Gunakan fungsi `EXTRACT` untuk mengambil bulan dari `start_time`.
    - Contoh output:
    
      <img width="272" alt="image" src="https://github.com/user-attachments/assets/272f7428-1082-465d-9847-df27e287d878" />

3. Tampilkan semua perjalanan yang memiliki durasi perjalanan lebih dari rata-rata durasi perjalanan pada `subscriber_type` 'Local31'. Urutkan hasil tersebut berdasarkan duration terlama s/d tercepat. Gunakan subquery untuk menghitung rata-rata durasi.
    - Contoh output:

      <img width="1333" alt="image" src="https://github.com/user-attachments/assets/4ec81e3f-3d96-46bc-bb38-52ef069b3059" />


4. Buat query yang mengkategorikan perjalanan berdasarkan durasi:
    - Jika `duration_minutes` kurang dari 5 menit, diberi label 'Short'
    - Jika `duration_minutes` antara 5 dan 30 menit, diberi label 'Medium'
    - Jika lebih dari 30 menit, diberi label 'Long'
    - Hasilnya diberi alias `trip_category`.
    - Contoh output:

      <img width="407" alt="image" src="https://github.com/user-attachments/assets/cf4c3e51-d776-4343-b4f5-f5d4e7d19dc8" />


# Loop

## Menu App
- Buatlah program yang akan menerima inputan dari user (hint: gunakan `input()`)
- Program ini akan melakukan beberapa proses sesuai dengan menu yang dipilih
    - menu `1`: membuat deret fibonacci
      ```py
        # gunakan code berikut untuk melengkapi proses di menu 1
        n = 10
        num1 = 0
        num2 = 1
        next_number = num2  
        count = 1
        result = [num1, num2]
        
        while count <= n:
            count += 1
            num1, num2 = num2, next_number
            result.append(next_number)
        
            next_number = num1 + num2
        
        print(result)
      ```
    - menu `2`: menentukan tanggal ganjil/genap
      ```py
        # gunakan code berikut untuk melengkapi proses di menu 2
        currentDate = 1 # ganti dengan tanggal hari ini
        
        if currentDate % 2 == 0:
            print("tanggal genap")
        else:
            print("tanggal ganjil")
      ```
    - menu `3` atau `exit`: program berhenti
- Jika user memilih salah satu menu, maka program akan mengarahkan ke proses sesuai dengan menu yang dipilih.
- Namun jika user memilih **selain** menu diatas, maka program akan menampilkan pesan error seperti "menu tidak dikenal!".

**Note**: Program ini akan terus berjalan sampai user memilih menu `3` atau `exit`

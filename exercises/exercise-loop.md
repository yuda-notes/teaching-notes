# Loop

## Menu App
- Buatlah program yang akan menerima inputan dari user
- program ini akan melakukan beberapa operasi sesuai dengan menu yang dipilih
    - menu 1: membuat deret fibonacci
    - menu 2: menentukan tanggal ganjil/genap
    - menu 3 atau "exit": program berhenti
    - selain menu diatas, maka program akan menampilkan output "menu tidak dikenal!"

**notes: gunakan 2 code dibawah ini untuk melengkapi statement di menu 1 atau 2**
```py
# Menu 1
# membuat deret fibonacci
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
```py
# Menu 2
# menentukan tanggal ganjil/genap (berdasarkan hari ini)
import datetime 

currentDate = datetime.datetime.now()

if currentDate.day % 2 == 0:
    print("tanggal genap")
else:
    print("tanggal ganjil")
```

# Normalization 1NF - 3NF

Sebuah toko online menyimpan data transaksi pembelian dalam format berikut:

OrderID |	CustomerName	| CustomerAddress |	Items Purchased |	TotalPrice |
---| --| --| --|--
001	| Andi |	Jl. Mawar No. 1, Jakarta	| Laptop, Mouse	| 12.000.000 | 
002 |	Budi | Jl. Melati No. 2, Bogor |	Keyboard, Monitor, Headset |	4.500.000 |
003 |	Andi |	Jl. Mawar No. 1, Jakarta |	Flashdisk |	150.000 |

Notes:
- Setiap order bisa memiliki lebih dari satu item.
- Customer dengan nama yang sama bisa muncul lebih dari sekali.
- Dalam melakukan normalisasi, bisa gunakan `excel` atau `spreadsheet` agar dapat "visualisasi" nya

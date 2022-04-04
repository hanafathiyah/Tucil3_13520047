# Tucil3_13520047
Penyelesaian Persoalan 15-Puzzle dengan Algoritma Branch and Bound

## Deskripsi Singkat Program yang Dibuat
Permainan 15-Puzzle dapat diselesaikan menggunakan algoritma branch and bound. Ide pengerjaannya adalah sebagai berikut.
1. Pengecekan apakah solusi dapat dicapai atau tidak. Dalam hal ini digunakan fungsi-fungsi dalam file reachablechecker.py. Apabila total nilai kurang i ditambah dengan X bernilai genap, solusi dapat ditemukan. Apabila total nilai kurang i ditambah dengan X bernilai ganjil, solusi tidak dapat ditemukan dan menampilkan pesan kesalahan.
2. Melakukan iterasi secara bertahap hingga tidak terdapat elemen di dalam simpul hidup. Selain itu, apabila ditemukan node berupa solusi, iterasi dihentikan.
3. Iterasi dilakukan dalam file bnb.py dengan move up, right, down, left dan menambahkan simpul-simpul tersebut ke dalam simpul hidup sesuai dengan urutannya.
4. Simpul expand didapatkan dari indeks pertama simpul hidup
5. Pengecekan apakah simpul expand merupakan solusi? Jika iya hentikan pencarian. Jika tidak lanjutkan sampai ditemukan node berupa goal_state

## Requirement Program dan Instalasi Module/Package yang Diperlukan
### Requirement Program
1. Python (Lakukan instalasi melalui https://www.python.org/ atau sudo apt install python3)

## Cara Menggunakan Program
1. Pastikan Anda telah melakukan instalasi bahasa _Python_ pada _device_ Anda. Jika belum, Anda dapat melakukan instalasi dengan mengunduh _python_ terbaru pada https://www.python.org/ untuk pengguna windows, atau mengetikkan sudo apt install python3 untuk pengguna Linux/Ubuntu
2. Masuk ke dalam direktori src
3. Jalankan perintah python fifteenpuzzlegame.py
4. Masukkan nama file sesuai path, jika file disimpan di folder test, maka tuliskan ../test/namafile.txt
5. Solusi ditampilkan

## Author / Identitas Pembuat
- Nama  : Hana Fathiyah
- NIM   : 13520047
- Kelas : K02
- Email : 13520047@std.stei.itb.ac.id

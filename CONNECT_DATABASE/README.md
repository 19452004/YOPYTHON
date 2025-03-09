**Menghubungkan Python ke MySQL dengan XAMPP**

Tutorial ini menjelaskan langkah-langkah untuk menghubungkan Python ke MySQL menggunakan XAMPP
adapun beberapa syarat untuk mengikuti tutorial ini, pastikan teman-teman sudah menginstall:
1. XAMPP
2. Python
3. modul mysql-connector(jika belum terinstall, jalankan perintah di terminal "pip install mysql-connector)

GASS ke Tutorialnya!!
Langkah 1: Menjalankan MySQL di XAMPP
 1. Buka XAMPP Control Panel.
 2. Start Apache dan MySQL.
 3. Klik tombol Admin di sebelah MySQL untuk membuka phpMyAdmin

Langkah 2: Membuat Database di phpMyAdmin
 1. Buka phpMyAdmin melalui browser (http://localhost/phpmyadmin).
 2. Buat database baru, misalnya data_test.
 3. Buka tab Browser lalu buat data yang dibutuhkan contoh(id, nama_barang, harga_barang, dll).
  atau ke bagian tab SQL buat seperti ini:

        CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
        );

Lagkah 3: Hubungkan python ke sql liat code dan file  yang terupload 
folder services berisi program bagaimana kita mengkoneksikan ke mysql database

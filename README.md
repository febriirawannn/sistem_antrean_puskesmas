Sistem Antrean Puskesmas

Deskripsi

Sistem Antrean Puskesmas adalah aplikasi berbasis web yang dibuat menggunakan Python dan Streamlit untuk membantu pengelolaan antrean pasien. Sistem ini menerapkan struktur data Queue (FIFO) sehingga pasien dilayani sesuai urutan kedatangan, dengan prioritas khusus untuk pasien darurat.

Fitur

• Dashboard informasi antrean
• Tambah pasien normal dan darurat
• Pemanggilan pasien berdasarkan prioritas
• Pencarian pasien berdasarkan nama atau nomor antrean
• Riwayat pasien yang telah dilayani
• Reset seluruh data antrean

Teknologi yang Digunakan

• Python
• Streamlit
• Collections Deque
• Datetime

Struktur Data

Aplikasi menggunakan Queue (First In First Out/FIFO).

Operasi yang digunakan:

• Enqueue (menambah pasien ke antrean)
• Dequeue (memanggil pasien dari antrean)
• Front (menampilkan pasien terdepan)
• Size (menghitung jumlah antrean)
• Is Empty (memeriksa antrean kosong)

Cara Menjalankan Program

Install Streamlit
pip install streamlit
Jalankan aplikasi
streamlit run app.py
Buka browser dan akses alamat yang muncul pada terminal.

Menu Aplikasi

Dashboard
Menampilkan jumlah antrean normal, darurat, dan pasien yang telah dilayani.
Tambah Pasien
Menambahkan pasien baru ke dalam antrean.
Panggil Pasien
Memanggil pasien berdasarkan prioritas antrean.
Cari Pasien
Mencari data pasien berdasarkan nama atau nomor antrean.
Riwayat Pasien
Menampilkan daftar pasien yang sudah dilayani.
Reset Data
Menghapus seluruh data antrean dan mengembalikan sistem ke kondisi awal.

Implementasi Sistem

• Pasien normal masuk ke antrean normal.
• Pasien darurat masuk ke antrean darurat.
• Pasien darurat dipanggil terlebih dahulu.
• Pasien yang selesai dilayani masuk ke riwayat.
• Sistem dapat mencari dan menampilkan data pasien secara cepat.

Tujuan Proyek

Proyek ini dibuat sebagai implementasi Struktur Data Queue pada sistem antrean pelayanan kesehatan menggunakan Python dan Streamlit.

Demo Online

https://sistemantreanpuskesmas-gkpgappblmhdqgboeje3s7b.streamlit.app/

Repository GitHub

https://github.com/username/sistem-antrean-puskesmas

Pengembang

Nama: febri irawan dan muhamad rizki riyadul istihori
Mata Kuliah: Struktur Data
Proyek: Sistem Antrean Puskesmas Berbasis Streamlit dan Queue Python

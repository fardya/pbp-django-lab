# Tugas 2
Katalog

### Requests
![Tugas2PBP](https://user-images.githubusercontent.com/112617861/190300621-eb7b1abb-b8a2-46a3-97e8-669125a0b168.png)
Klien mengirim URL request ke Django, request masuk ke urls.py. Akan dicari apakah ada sumber untuk URL request tersebut. Jika URL tertaut ke isi views.py, view yang sesuai akan dipanggil. View tersebut memiliki template. Kemudian, view membaca dari models.py untuk mendapatkan model yang sesuai dari database. Data tersebut akan ditulis dalam template kemudian dikembalikan ke klien dalam bentuk HTML. Secara singkat, urls.py berisi URL request, views.py mengandung URL pada urls.py dan tertaut ke models.py untuk membaca dan menulis model, dan berkas html merupakan hasil data yang ditulis ke template dari views.py.

### Virtual Environment
Virtual environment merupakan lingkungan baru untuk mengembangkan suatu program tanpa memengaruhi lingkungan asli. Semua library atau package yang dipasang dalam suatu virtual environment hanya akan berkerja pada virtual environment tersebut. Konsep virtual environment mengizinkan pemula membangun project tanpa perlu khawatir lingkungan aslinya rusak. Apabila terjadi sesuatu, pengembang hanya perlu menghancurkan virtual environment tersebut. Selain itu, virtual environment menghindari bentrok antar-dependency dari berbagai project Django dan perbedaan versi-versi Python dengan cara menciptakan lingkungan yang terisolasi. Pengembang tidak perlu mengalihkan versi Python setiap mengerjakan project berbeda.
Virtual environment tidak wajib digunakan ketika membuat aplikasi web berbasis Django. Namun, mengingat manfaat yang disediakan, menggunakan virtual environment untuk tiap project yang berbeda dianggap sebagai praktik terbaik. Praktik ini meminimalisir masalah sekaligus mempermudah pekerjaan pengembang.

### Steps
* Membuat repositori baru bernama tugas2 menggunakan kode yang telah disediakan
* Clone repositori tersebut ke komputer
* Membuat dan menyalakan virtual environment, kemudian memasang dependencies yang diperlukan
* Mengimplementasi views dengan cara membuat fungsi yang menerima parameter request dan mengembalikan render, mengisi berkas katalog.html dengan template, melakukan routing pada urls.py terhadap fungsi views agar halaman HTML dapat ditampilkan, mendaftarkan aplikasi pada project_django, dan runserver untuk melihat apakah sudah terimplementasi
* Menghubungkan models dengan views dan template, caranya yaitu import models ke views.py, menambah kode untuk memanggil fungsi query ke model database dan menyimpannya ke sebuah variable, menambah parameter context pada pengembalian fungsi render sebelumnya, mengedit file HTML pada folder templates agar dapat menampilkan nama, NPM, dan katalognya
* Melakukan deploy ke Heroku, langkahnya adalah membuat aplikasi baru di Heroku, melakukan konfigurasi repositori dengan menambahkan variabel berisi value API key dan nama aplikasi baru tersebut pada bagian Secrets di GitHub, kemudian menyimpan dan menjalankan ulang workflow pada bagian Actions
